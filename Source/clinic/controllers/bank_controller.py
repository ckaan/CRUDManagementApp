import os
import hashlib
from clinic.bank import Bank
from typing import Dict
from datetime import datetime

from clinic.dao.users_dao import UserDAO
from clinic.dao.bank.bnote_dao_pickle import NoteDAO
from clinic.dao.bank.bank_dao_json import BankDAO
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException


class BController:


    




    ## Initializing the default settings 
    def __init__(self, current_building,filepath, autosave=True):
        '''
        Function Name: __init__
        
        Function Description:
        (i) Initializes the Controller object with default login credentials, an empty dictionary for patients, and a list for the current patient.
        (ii) Sets up internal tracking variables such as logged_in, username, password, and a counter for patient IDs.

        Parameters:
        -> None

        Function Return value: None
        '''
        
        base = os.path.dirname(os.path.abspath(__file__))
        self.current_building = current_building
        users_path = os.path.join(base, "users.json")  
        patients_path = os.path.join(base, "bank.json")
        records_path = os.path.join(base, "records")

        self.autosave = autosave
        self.logged_in = True
        self.user_dao = UserDAO(json_file_path = users_path)
        self.patient_dao = BankDAO(autosave=autosave, filepath=patients_path)
        self.note_dao = NoteDAO(autosave=autosave, filepath= records_path)
        self.patient_id=0
        
        self.current_patient = None
        self.current_building = None
        

      



    def get_banks_for_building(self, building_id):
        """
        Retrieves all banks associated with a specific building.
        If no banks exist for the building, an empty list is returned.
        """
        if building_id in self.patient_dao.patients:
            return self.patient_dao.patients[building_id].bank  # ✅ Fetch existing banks
        else:
            return []  # ✅ Create empty list if no banks exist
       
    def authenticate_user(self, username, password):
        # Authenticate using UsersDAO internally
        if self.user_dao.authenticate(username, password):
            self.logged_in_user = username  # Store the logged-in user
            return True
        return False
        
        
    ## To verify the password and username  
    def login(self, username, password):
        '''
        Function Name: login
        
        Function Description:
        (i) Authenticates the user based on a username and password.
        (ii) Sets the `logged_in` status to True if the credentials are correct.

        Parameters:
        -> username: The username input by the user
        -> password: The password input by the user

        Function Return value: 
        -> True if login is successful, False if credentials are incorrect or already logged in.
        '''
        
       
        if self.logged_in:
            raise DuplicateLoginException("User already logged in.")
            
        if not self.user_dao.authenticate(username, password):
            raise InvalidLoginException("Invalid username or password")
        
        self.logged_in = True
        print("User logged in successfully")  # Debug statement
        return True
            
            
            
            
            
            
    ## To log the user out 
    def logout(self):
        '''
        Function Name: logout
        
        Function Description:
        (i) Logs the user out by setting the `logged_in` status to False.
        (ii) Prints a message confirming that the user has logged out.

        Parameters:
        -> None

        Function Return value: 
        -> True if logged out successfully, False if not logged in.
        '''
        if not self.logged_in:
            raise InvalidLogoutException("you cant do that!")
        self.logged_in = False
        print("You logged out successfully!")
        return True





    def _ensure_logged_in(self):
        if not self.logged_in:
            print("User is not logged in")  # Debug statement
            raise IllegalAccessException 
        print("User is logged in")  # Debug statement    
        return True
            
        





    ## Create a new patient record
    def create_patient(self, bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web):
        '''
        Function Name: create_patient
        
        Function Description:
        (i) Creates a new patient record and stores it in the `patients` dictionary.
        (ii) Ensures that the user is logged in before allowing patient creation.
        (iii) Checks if a patient already exists with the same social security number.

        Parameters:
        -> social_security_number: The SIN of the patient
        -> name: The name of the patient
        -> birth_date: The birth date of the patient
        -> phone: The phone number of the patient
        -> email: The email address of the patient
        -> address: The address of the patient

        Function Return value: 
        -> Newly created Patient object if successful, None if the user is not logged in or the patient already exists.
        '''
        # Creating a new patient and adding to the dictionary

        self._ensure_logged_in()
        print("Adding patient: Logged in check passed")  # Debug statement
        patient =self.patient_dao.create_patient(bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web)
        print(f"Patient with SIN {bankno} added: {patient}")
        return patient







    ## Search for a patient by their social security number
    def search_patient(self, bankno):
        self._ensure_logged_in()
        return self.patient_dao.search_patient(bankno) 
        '''
        Function Name: search_patient
        
        Function Description:
        (i) Searches for a patient using their social security number.

        Parameters:
        -> social_security_number: The SIN of the patient to search for

        Function Return value: 
        -> The Patient object if found, None if not found.
        '''








    ## Retrieve patients based on their name
    def retrieve_patients(self, name):
        '''
        Function Name: retrieve_patients
        
        Function Description:
        (i) Retrieves a list of patients whose names match the provided text.
        (ii) Ensures the user is logged in before performing the search.

        Parameters:
        -> name: The name or part of the name to search for

        Function Return value:
        -> A list of matching Patient objects, or None if no matches are found.
        '''
        self._ensure_logged_in()
        return self.patient_dao.retrieve_patients(name.lower())















    ## Update an existing  patient's information    
    def update_patient(self, patient_id, bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web):
        '''
        Function Name: update_patient
        
        Function Description:
        (i) Updates the information for an existing patient.
        (ii) Ensures the user is logged in and validates input before making changes.
        (iii) Handles the case where the SIN number is changed and ensures no conflicts in the records.

        Parameters:
        -> patient_id: The original patient ID (SIN)
        -> social_security_number: The new SIN if updating
        -> name: The new name of the patient
        -> birth_date: The new birth date of the patient
        -> phone: The new phone number of the patient
        -> email: The new email of the patient
        -> address: The new address of the patient

        Function Return value:
        -> True if the update was successful, False if not.
        '''

        self._ensure_logged_in()
        if self.current_patient:
            raise IllegalOperationException
        return self.patient_dao.update_patient(patient_id,bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web)







    ## Delete a patient record by their social security number 
    def delete_patient(self, bankno):
        '''
        Function Name: delete_patient
        
        Function Description:
        (i) Deletes a patient record based on their social security number.
        (ii) Ensures the user is logged in before attempting to delete a record.

        Parameters:
        -> social_security_number: The SIN of the patient to be deleted

        Function Return value: 
        -> True if the patient was deleted, False if patient was not found or user is not logged in.
        '''

        self._ensure_logged_in()
        if self.current_patient:
            raise IllegalOperationException
            
        return self.patient_dao.delete_patient(bankno)








    ## Set the current patient based on their SIN number     
    def set_current_patient(self, bankno):
        self._ensure_logged_in()  # Ensure the user is logged in

        patient = self.patient_dao.search_patient(bankno)
       

        if not patient:
            raise IllegalOperationException

        self.current_patient = patient
        self.note_dao.current_patient = patient
        self.set_current_patient_in_dao()
        self.note_dao.load_notes()


    def set_current_patient_in_dao(self):
        self.note_dao.current_patient = self.current_patient
        




    ## get the current patient 
    def get_current_patient(self):
        '''
        Function Name: get_current_patient
        
        Function Description:
        (i) Retrieves the currently set patient, if any.
        (ii) Ensures the user is logged in before accessing the patient data.

        Parameters:
        -> None

        Function Return value:
        -> The current patient if set, None if no patient is selected.
        '''
        self._ensure_logged_in()

        if self.current_patient:
            print("Current patient is set to: ", str(self.current_patient))
            return self.current_patient
        else:
            return None






    ## unset the current patient 
    def unset_current_patient(self):
        self._ensure_logged_in()
        self.current_patient = None









    ## List all patients         
    def list_patients(self):
        '''
        Function Name: list_patients
        
        Function Description:
        (i) Lists all the patients in the system by printing their SIN numbers.
        (ii) Ensures the user is logged in before displaying the patient list.

        Parameters:
        -> None

        Function Return value:
        -> A list of all patients if available, or an empty list if no patients are found.
        '''
        self._ensure_logged_in()
        return self.patient_dao.list_patients()













    ## create a note for the current patient 
    def create_note(self, text):
        '''
        Function Name: create_note
        
        Function Description:
        (i) Creates a note for the current patient.
        (ii) Ensures a patient is selected before attempting to add the note.

        Parameters:
        -> text: The text content of the note to be added

        Function Return value: 
        -> The newly added note object.
        '''

        self._ensure_logged_in()
        return self.note_dao.create_note(text)









    ## Search for a note by text
    def search_note(self, text):  

        '''
        Function Name: search_note
        
        Function Description:
        (i) Searches for a note in the current patient's record by matching the provided text.
        (ii) Ensures that the user is logged in before attempting the search.

        Parameters:
        -> text: The text content to search for in the patient's notes.

        Function Return value:
        -> The note object if a match is found, None if no note matches the provided text or the user is not logged in.
        '''
        self._ensure_logged_in()
  
        return self.note_dao.search_note(text)











    ## Retrieve notes by their text    
    def retrieve_notes(self, text):
        '''
        Function Name: retrieve_notes
        
        Function Description:
        (i) Retrieves all notes from the current patient's record that contain the specified text.
        (ii) If no text is provided or the patient is not selected, the function will return None or an empty list.

        Parameters:
        -> text: The text content to match within the notes.

        Function Return value:
        -> A list of matching notes, or None if no notes are found or no patient is selected.
        '''
        self._ensure_logged_in()  

        return self.note_dao.retrieve_notes(text)








    ##Update an existing note    
    def update_note(self, code, new_text):
        '''
        Function Name: update_note
        
        Function Description:
        (i) Updates the text of an existing note in the current patient's record.
        (ii) If the note is found, updates the text and the timestamp of the note.
        (iii) Ensures that a current patient is selected before attempting to update the note.

        Parameters: 
        -> code: The unique identifier of the note to be updated.
        -> new_text: The new text content to replace the old text in the note.

        Function Return value:
        -> The updated note object if successful, None if the note cannot be updated.
        '''
        self._ensure_logged_in()
        return self.note_dao.update_notes(code, new_text) 
        
        
        
        
        
        
        

    ## Delete a note       
    def delete_note(self, code):
        '''
        Function Name: delete_note
        
        Function Description:
        (i) Deletes a note from the current patient's record by its unique code.
        (ii) Ensures that a current patient is selected before attempting to delete the note.

        Parameters:
        -> code: The unique identifier of the note to be deleted.

        Function Return value:
        -> The result of the deletion process. If successful, returns the deleted note; otherwise, None.
        '''
        self._ensure_logged_in()
        return self.note_dao.delete_notes(code)   





    ## List all notes
    def list_notes(self):
        '''
        Function Name: list_notes
        
        Function Description:
        (i) Lists all the notes in the current patient's record.
        (ii) If there are no notes, returns an empty list.
        (iii) Ensures that a current patient is selected before attempting to list the notes.

        Parameters:
        -> None

        Function Return value:
        -> A sorted list of all notes for the current patient, or an empty list if no notes exist.
        '''
        
        self._ensure_logged_in()
        return self.note_dao.list_notes()   

