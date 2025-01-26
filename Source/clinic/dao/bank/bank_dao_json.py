import json
from abc import ABC, abstractmethod
import sys

from clinic.bank import Bank
from .bank_decoder import PatientDecoder
from .bank_encoder import PatientEncoder
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException


class BankDAO(ABC):
    def __init__(self, autosave =True, filepath="bank.json"):
        self.patients: Dict[int, Bank] = {}  # Using a dictionary to store patients
        self.autosave=autosave
        self.filepath = filepath
        self.current_patient = []
        
        if self.autosave:
            self.load_patients()
    
    
    # Saving patients if autosave is true 
    def save_patients(self):
        try:
            if self.autosave:
                with open(self.filepath, "w") as file:
                    json.dump({"bank": list(self.patients.values())}, file, indent=4, cls=PatientEncoder)
                print("[DEBUG] Banks saved successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to save bank: {e}")

 
      
        
    # Loading patients from a json file that is list of dictionaries
    def load_patients(self):
        try:
            with open(self.filepath, "r") as file:
                content = file.read().strip()
                if not content:
                    return None
               
                # Load JSON data
                data = json.loads(content, cls=PatientDecoder)

                # Handle the "patients" key containing a list of patients
                if "bank" in data and isinstance(data["bank"], list):
                    for patient_data in data["bank"]:
                        patient = Bank(
                        bankno=patient_data["bankno"],
                        bank_name=patient_data["bank_name"],
                        branch=patient_data["branch"],
                        account_no=patient_data["account_no"],
                        account_name=patient_data["account_name"],
                        authority=patient_data["authority"],
                        phonenumber=patient_data["phonenumber"],
                        faxno=patient_data["faxno"],
                        ibanno=patient_data["ibanno"],
                        web=patient_data["web"]
                        )
                        self.patients[str(patient.bankno)] = patient
                       
                else:
                     print("Unexpected JSON format")
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError as e:
            print("Json Decoding Error!")



            
     ## Searching patient by social_security_number
    def search_patient(self, bankno): 
        '''
        Function Name: search_patient
        
        Function Description:
        (i) Searches for a patient using their social security number.

        Parameters:
        -> social_security_number: The SIN of the patient to search for

        Function Return value: 
        -> The Patient object if found, None if not found.
        '''
    
        key =str(bankno)
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
    def create_patient(self, bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web):
        key =str(bankno)
        if key in self.patients:
            raise IllegalOperationException
        patient = Bank(bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web)
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
    
    
    
    
    
    
   
    def update_patient(self, patient_id, bankno=None, bank_name=None, branch=None, account_no=None, account_name=None, authority=None, phonenumber=None, faxno=None, ibanno=None, web=None):
        try:
            key = str(patient_id)
            bankno = str(bankno) if bankno else key
            patient = self.patients.get(key)

            if patient is None:
                print(f"[ERROR] Patient with ID {key} not found.")
                raise IllegalOperationException("Patient not found.")

            # Handle SIN update
            if bankno != key:
                if bankno in self.patients:
                    print(f"[ERROR] Patient with SIN {bankno} already exists.")
                    raise IllegalOperationException("Conflict with existing patient.")
                del self.patients[key]
                self.patients[bankno] = patient
                patient.bankno = bankno
                key = bankno

            # Update fields
            patient.bank_name = bank_name or patient.bank_name
            patient.branch = branch or patient.branch
            patient.account_no = account_no or patient.account_no
            patient.account_name = account_name or patient.account_name
            patient.authority = authority or patient.authority
            patient.phonenumber = phonenumber or patient.phonenumber
            patient.faxno = faxno or patient.faxno
            patient.ibanno = ibanno or patient.ibanno
            patient.web = web or patient.web

            # Debug updated patient
            print(f"[DEBUG] Updated patient: {vars(patient)}")

            # Autosave
            if self.autosave:
                self.save_patients()

            return True
        except Exception as e:
            print(f"[ERROR] Failed to update patient: {e}")
            raise

    
    
    
    def delete_patient(self, bankno):
        '''
        Function Name: delete_patient
        
        Function Description:
        (i) Deletes a patient record based on their bankno.
        (ii) Ensures the user is logged in before attempting to delete a record.

        Parameters:
        -> bankno: The SIN of the patient to be deleted

        Function Return value: 
        -> True if the patient was deleted, False if patient was not found or user is not logged in.
        '''

        bankno = str(bankno) 

    # Check if the patient exists
        if bankno not in self.patients:
            raise IllegalOperationException("Patient not found.")

    # Remove the patient
        del self.patients[bankno]

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
            print("The SIN Number of patient:"+str(patient.bankno)+"\n")
         return list(self.patients.values())






