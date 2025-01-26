import os
import hashlib
from clinic.unit import Unit  # Change from models.unit to clinic.models.unit

from typing import Dict
from datetime import datetime

from clinic.dao.users_dao import UserDAO
from clinic.dao.unit.note_dao_pickle import NoteDAO
from clinic.dao.unit.unit_dao_json import UnitDAO
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException  # (Optional: rename to NoCurrentUnitException)



class UController:
    ## Initializing the default settings 
    def __init__(self, current_building, filepath, autosave=True):
        '''
        Function Name: __init__
        Initializes the Controller for managing units.
        Allows dynamic selection of buildings instead of passing `bu_controller` in the constructor.
        '''
        base = os.path.dirname(os.path.abspath(__file__))
        users_path = os.path.join(base, "users.json")

        if not current_building or not hasattr(current_building, "name"):
            raise ValueError("[ERROR] No valid building selected in UController!")


        self.current_building = current_building # 
        print(f"[DEBUG] UController initialized for building: {self.current_building.name}")
        self.autosave = autosave
        
        self.logged_in = True
        self.user_dao = UserDAO(json_file_path=users_path)
        self.unit_dao = UnitDAO(current_building, filepath=filepath, autosave=autosave)
        self.note_dao = NoteDAO(autosave=autosave, filepath=os.path.join(base, "records"))

        self.current_building = current_building

        self.current_unit = current_building  # Track the currently selected unit
        
        
        



    def create_unit(self, new_unit):
        """
        Creates a new Unit (household) and attaches it to the current building.
        :param householdno: Unique household number for the occupant.
        """
        if not self.current_building:
            raise ValueError("No building selected! Please set_current_building first.")


        # Add the new unit to the building's units list.
        self.current_building.units.append(new_unit)
        

        print(f"[INFO] Added new unit to building '{self.current_building.building_id}': {new_unit}")
        return self.unit_dao.create_unit(new_unit)


    def _ensure_logged_in(self):
        """
        Ensures the user is logged in before performing any operations.
        Raises an IllegalAccessException if the user is not logged in.
        """
        if not self.logged_in:
            print("User is not logged in")  # Debug statement
            raise IllegalAccessException("User must be logged in to perform this action")
        print("User is logged in")  # Debug statement
        return True

    ## Search for a unit by their household number
    def search_unit(self, householdno):
        self._ensure_logged_in()
        self.ensure_building_selected()  # ✅ Ensure a building is selected
        return self.unit_dao.search_unit(householdno)

    ## Retrieve units based on their name
    def retrieve_units(self, name):
        '''
        Function Name: retrieve_units
        Retrieves a list of units whose names match the provided text.
        '''
        self._ensure_logged_in()
        self.ensure_building_selected()
        return self.unit_dao.retrieve_units(name.lower())

    ## Update an existing unit's information
    def update_unit(self, unit_id, householdno, name, sin, bday, plateno, taxno,
                    phoneno, email, address, groupno, accountno, accountnote,
                    receiverno, receivernote, workaddress, workphone, workemail, occupation):
        '''
        Function Name: update_unit

        Function Description:
        (i) Updates the information for an existing unit.
        (ii) Ensures the user is logged in and validates input before making changes.
        (iii) Handles the case where the SIN number is changed and ensures no conflicts in the records.
        '''
        self._ensure_logged_in()
        if self.current_unit:
            raise IllegalOperationException
        return self.unit_dao.update_patient(
            unit_id, householdno, name, sin, bday, plateno, taxno,
            phoneno, email, address, groupno, accountno, accountnote, receiverno,
            receivernote, workaddress, workphone, workemail, occupation
        )

    ## Delete a unit record by their household number
    def delete_unit(self, householdno):
        '''
        Function Name: delete_unit

        Function Description:
        (i) Deletes a unit record based on their household number.
        (ii) Ensures the user is logged in before attempting to delete a record.
        '''
        self._ensure_logged_in()
        if self.current_unit:
            raise IllegalOperationException

        return self.unit_dao.delete_patient(householdno)

    ## Set the current unit based on their household number
    def set_current_unit(self, householdno):
        self._ensure_logged_in()
        found_unit = self.unit_dao.search_patient(householdno)
        if not found_unit:
            raise IllegalOperationException

        self.current_unit = found_unit
        self.note_dao.current_patient = found_unit  # If note DAO still references "patient"
        self._set_current_unit_in_dao()
        self.note_dao.load_notes()

    def _set_current_unit_in_dao(self):
        self.note_dao.current_patient = self.current_unit

    ## get the current unit
    def get_current_unit(self):
        '''
        Function Name: get_current_unit

        Function Description:
        (i) Retrieves the currently set unit, if any.
        (ii) Ensures the user is logged in before accessing the unit data.
        '''
        self._ensure_logged_in()

        if self.current_unit:
            print("Current unit is set to: ", str(self.current_unit))
            return self.current_unit
        else:
            return None

    ## unset the current unit
    def unset_current_unit(self):
        self._ensure_logged_in()
        self.current_unit = None

    ## List all units
    def list_units(self):
        '''
        Function Name: list_units

        Function Description:
        (i) Lists all the units in the system by printing their SIN numbers.
        (ii) Ensures the user is logged in before displaying the unit list.
        '''
        self._ensure_logged_in()
        return self.unit_dao.list_units()

    ## create a note for the current unit
    def create_note(self, text):
        '''
        Function Name: create_note

        Function Description:
        (i) Creates a note for the current unit.
        (ii) Ensures a unit is selected before attempting to add the note.
        '''
        self._ensure_logged_in()
        return self.note_dao.create_note(text)

    ## Search for a note by text
    def search_note(self, text):
        '''
        Function Name: search_note

        Function Description:
        (i) Searches for a note in the current unit's record by matching the provided text.
        (ii) Ensures that the user is logged in before attempting the search.
        '''
        self._ensure_logged_in()
        return self.note_dao.search_note(text)

    ## Retrieve notes by their text
    def retrieve_notes(self, text):
        '''
        Function Name: retrieve_notes

        Function Description:
        (i) Retrieves all notes from the current unit's record that contain the specified text.
        (ii) If no text is provided or the unit is not selected, it will return None or an empty list.
        '''
        self._ensure_logged_in()
        return self.note_dao.retrieve_notes(text)

    ## Update an existing note
    def update_note(self, code, new_text):
        '''
        Function Name: update_note

        Function Description:
        (i) Updates the text of an existing note in the current unit's record.
        (ii) If the note is found, updates the text and the timestamp of the note.
        (iii) Ensures that a current unit is selected before attempting to update the note.
        '''
        self._ensure_logged_in()
        return self.note_dao.update_notes(code, new_text)

    ## Delete a note
    def delete_note(self, code):
        '''
        Function Name: delete_note

        Function Description:
        (i) Deletes a note from the current unit's record by its unique code.
        (ii) Ensures that a current unit is selected before attempting to delete the note.
        '''
        self._ensure_logged_in()
        return self.note_dao.delete_notes(code)

    ## List all notes
    def list_notes(self):
        '''
        Function Name: list_notes

        Function Description:
        (i) Lists all the notes in the current unit's record.
        (ii) If there are no notes, returns an empty list.
        (iii) Ensures that a current unit is selected before attempting to list the notes.
        '''
        self._ensure_logged_in()
        return self.note_dao.list_notes()
