import json
from abc import ABC, abstractmethod
import sys

from clinic.turnovers import Turnovers
from .turnovers_decoder import PatientDecoder
from .turnovers_encoder import PatientEncoder
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException


class TurnoversDAO(ABC):
    def __init__(self, autosave =True, filepath="turnovers.json"):
        self.patients: Dict[int, Turnovers] = {}  # Using a dictionary to store patients
        self.autosave=autosave
        self.filepath = filepath
        self.current_patient = []
        
        if self.autosave:
            self.load_patients()
    
    
    # Saving patients if autosave is true 
    def save_patients(self):
        if self.autosave:
            with open(self.filepath, "w") as file:
                json.dump({"turnovers": list(self.patients.values())}, file, indent=4, cls=PatientEncoder)
 
      
        
    # Loading patients from a json file that is list of dictionaries
    def load_patients(self):
        try:
            with open(self.filepath, "r") as file:
                content = file.read().strip()
                if not content:
                    return None

                # Load JSON data
                data = json.loads(content, cls=PatientDecoder)

                # Handle the "turnovers" key containing a list of turnovers
                if "turnovers" in data and isinstance(data["turnovers"], list):
                    for turnover_data in data["turnovers"]:
                        turnover = Turnovers(
                            group_code=turnover_data["group_code"],
                            code=turnover_data["code"],
                            company_name=turnover_data["company_name"],
                            authority=turnover_data["authority"],
                            bank_name=turnover_data["bank_name"],
                            taxno=turnover_data["taxno"],
                            taxplace=turnover_data["taxplace"],
                            iban=turnover_data["iban"],
                            address=turnover_data["address"],
                            phonenumber=turnover_data["phonenumber"],
                            email=turnover_data["email"],
                            web=turnover_data["web"]
                        )
                        self.patients[str(turnover.group_code)] = turnover
                else:
                    print("Unexpected JSON format")
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError as e:
            print("JSON Decoding Error!")




            
     ## Searching patient by social_security_number
    def search_patient(self, group_code): 
        '''
        Function Name: search_patient
        
        Function Description:
        (i) Searches for a patient using their social security number.

        Parameters:
        -> social_security_number: The SIN of the patient to search for

        Function Return value: 
        -> The Patient object if found, None if not found.
        '''
    
        key =str(group_code)
        patient = self.patients.get(key)
        
        if patient == None:
            return None
        return patient
    
    
    
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
    
    
    ## Creating patient and saving if autosave is enabled
    def create_patient(self, group_code, code, company_name, authority, bank_name, taxno, taxplace, iban, address, phonenumber, email, web):
        key =str(group_code)
        if key in self.patients:
            raise IllegalOperationException
        patient = Turnovers(group_code, code, company_name, authority, bank_name, taxno, taxplace, iban, address, phonenumber, email, web)
        self.patients[key] = patient

        if self.autosave:
            self.save_patients()
        return patient
    
    # Retrieving patients by their name
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
    
        retrieved = []
        for patient in self.patients.values():  # Iterate over patient objects
            print(patient)
            if name in patient.name.lower():
                retrieved.append(patient)
        return retrieved
    
    
    
    
    
    def update_patient(self, patient_id, group_code, code, company_name, authority, bank_name, taxno, taxplace, iban, address, phonenumber, email, web):
        """
        Updates the information for an existing turnover.
        Parameters:
        -> patient_id: The original ID (group_code) of the turnover
        -> group_code: The new Group Code if updating
        -> Other parameters: Fields to update
        """
        key = str(patient_id)
        turnover = self.patients.get(key)

        if turnover is None:
            raise IllegalOperationException("Turnover not found.")

        # Handle case where group_code is updated
        if group_code != key and group_code is not None and group_code != "":
            if group_code in self.patients:
                raise IllegalOperationException("Group Code conflict with an existing turnover.")
            del self.patients[key]
            self.patients[group_code] = turnover
            turnover.group_code = group_code
            key = group_code

        # Update fields only if new value is not None or empty string
        if code:
            turnover.code = code
        if company_name:
            turnover.company_name = company_name
        if authority:
            turnover.authority = authority
        if bank_name:
            turnover.bank_name = bank_name
        if taxno:
            turnover.taxno = taxno
        if taxplace:
            turnover.taxplace = taxplace
        if iban:
            turnover.iban = iban
        if address:
            turnover.address = address
        if phonenumber:
            turnover.phonenumber = phonenumber
        if email:
            turnover.email = email
        if web:
            turnover.web = web

        # Save changes if autosave is enabled
        if self.autosave:
            self.save_patients()

        return True

    
    
    
    
    def delete_patient(self, group_code):
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

        group_code = str(group_code) 

    # Check if the patient exists
        if group_code not in self.patients:
            raise IllegalOperationException("Patient not found.")

    # Remove the patient
        del self.patients[group_code]

    # Autosave if it is true
        if self.autosave:
            self.save_patients()
        return True
 
 
 
 
 
 
   
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
    
    
         if not self.patients:
            print("No patients available!")
            return []

         for patient in self.patients.values():  # Accessing patient objects
            print("The SIN Number of patient:"+str(patient.group_code)+"\n")
         return list(self.patients.values())






