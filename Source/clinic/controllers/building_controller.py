import os
import hashlib
from clinic.building import Building

from typing import Dict
from datetime import datetime

from clinic.dao.users_dao import UserDAO
from clinic.dao.building.bunote_dao_pickle import NoteDAO
from clinic.dao.building.building_dao_json import BuildingDAO


from clinic.controllers.bank_controller import BController
from clinic.controllers.turnovers_controller import TController
from clinic.controllers.unit_controller import UController


from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException


class BuController:

    def __init__(self, filepath, autosave=True):
        """
        Initializes the BuildingController and loads necessary data.
        """
        self.current_building = None
        self.autosave = autosave
        self.logged_in = True  # Default to logged in (update if needed)

        # ✅ Dynamically determine paths
        base = os.path.dirname(os.path.abspath(__file__))
        users_path = os.path.join(base, "users.json")
        records_path = os.path.join(base, "records")

        # ✅ Initialize DAOs
        self.user_dao = UserDAO(json_file_path=users_path)
        self.building_dao = BuildingDAO(current_building=None, filepath=filepath, autosave=autosave)
        self.note_dao = NoteDAO(autosave=autosave, filepath=records_path)

        print(f"[INFO] BuildingController initialized successfully.")
        

    def set_current_building(self, building_id):
        """
        Sets the current building in BuildingController.
        """
        if not building_id:
            raise IllegalOperationException("Building ID cannot be empty!")

        key = str(building_id)  # Ensure we compare strings

        building_obj = self.building_dao.search_building(key)
        if not building_obj:
            raise IllegalOperationException(f"Building with ID '{key}' not found!")

        self.current_building = building_obj
        print(f"[BuildingController] Current building set to: {self.current_building.name} (ID: {self.current_building.building_id})")



    def authenticate_user(self, username, password):
        # Authenticate using UsersDAO internally
        if self.user_dao.authenticate(username, password):
            self.logged_in = True  # Update login status
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
            raise InvalidLogoutException("You can't do that!")
        self.logged_in = False
        print("You logged out successfully!")
        return True

    def _ensure_logged_in(self): 
        """
        Ensures the user is logged in before performing any operations.
        🔹 Now checks `self.logged_in` instead of `master_controller.is_logged_in()`.
        """
        if not self.logged_in:
            raise IllegalAccessException("User is not logged in.")



    ## Create a new building record
    def create_building(self, building_id, name):
        '''
        Function Name: create_patient

        Function Description:
        (i) Creates a new building record and stores it in the `patients` dictionary.
        (ii) Ensures that the user is logged in before allowing building creation.
        (iii) Checks if a building already exists with the same ID.

        Parameters:
        -> social_security_number: The ID of the building
        -> name: The name of the building

        Function Return value: 
        -> Newly created Building object if successful, None if the user is not logged in or the building already exists.
        '''
        self._ensure_logged_in()
        building = self.building_dao.create_building(building_id, name)
        print(f"Building with ID {building_id} added: {building}")
        return building


    def _ensure_logged_in(self):
        if not self.logged_in:
            print("User is not logged in")  # Debug statement
            raise IllegalAccessException 
        print("User is logged in")  # Debug statement    
        return True
    
    ## Search for a building by its ID
    def search_building(self, building_id):
        self._ensure_logged_in()
        return self.building_dao.search_building(building_id)

    ## Retrieve buildings based on their name
    def retrieve_buildings(self, name):
        '''
        Function Name: retrieve_patients

        Function Description:
        (i) Retrieves a list of buildings whose names match the provided text.

        Parameters:
        -> name: The name or part of the name to search for

        Function Return value:
        -> A list of matching Building objects, or None if no matches are found.
        '''
        self._ensure_logged_in()
        return self.building_dao.retrieve_building(name.lower())

    ## Update an existing building's information    
    def update_building(self, patient_id, building_id, name):
        '''
        Function Name: update_patient

        Function Description:
        (i) Updates the information for an existing building.

        Parameters:
        -> patient_id: The original building ID
        -> social_security_number: The new ID if updating
        -> name: The new name of the building

        Function Return value:
        -> True if the update was successful, False if not.
        '''
        self._ensure_logged_in()
        return self.building_dao.update_building(patient_id, building_id, name)

    ## Delete a building record by its ID
    def delete_building(self, building_id):
        '''
        Function Name: delete_patient

        Function Description:
        (i) Deletes a building record based on its ID.

        Parameters:
        -> social_security_number: The ID of the building to be deleted

        Function Return value: 
        -> True if the building was deleted, False if building was not found.
        '''
        self._ensure_logged_in()
        return self.building_dao.delete_building(building_id)

    ## Set the current building based on its ID
    def set_current_building(self, building_id):
        '''
        Function Name: set_current_patient

        Function Description:
        (i) Sets the currently selected building.

        Parameters:
        -> building_id: The ID of the building to be set as current.

        Function Return value:
        -> None
        '''
        self._ensure_logged_in()
        building = self.building_dao.search_building(building_id)

        if not building:
            raise IllegalOperationException("Building not found")

        self.current_building = building
        print(f"Current building set to: {building.name} (ID: {building.building_id})")

    ## List all buildings         
    def list_buildings(self):
        '''
        Function Name: list_patients

        Function Description:
        (i) Lists all the buildings in the system.

        Function Return value:
        -> A list of all buildings if available, or an empty list if none are found.
        '''
        self._ensure_logged_in()
        return self.building_dao.list_buildings()
