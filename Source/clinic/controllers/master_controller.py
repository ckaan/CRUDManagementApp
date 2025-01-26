from datetime import datetime
import sys
import os
import json
# Import your specialized controllers
from clinic.controllers.building_controller import BuController
from clinic.controllers.unit_controller import UController
from clinic.controllers.turnovers_controller import TController
from clinic.controllers.bank_controller import BController


from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException


class MasterController:
    """
        Acts as the single orchestrator for all domain controllers:
        - BuildingController (BuController)
        - UnitController (UController)
        - TurnoverController (TController)
        - BankController (BController)

        The GUI (or any other front-end) should interact ONLY with this class.
    """

    def __init__(self, autosave=True):  
         """
        Initializes MasterController but delays UnitController initialization until a building is selected.
         """
         self.current_building = None
         self.autosave = autosave  

         self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
         self.data_dir = os.path.join(self.base_dir, "data")
         os.makedirs(self.data_dir, exist_ok=True)

         self.buildings_path = os.path.join(self.data_dir, "buildings.json")
         self.units_path = None  # ✅ Will be set dynamically after selecting a building

         try:
            # ✅ Ensure controllers are initialized
            print("[INFO] Initializing BuildingController...")  # Debug
            self.building_controller = BuController(filepath=self.buildings_path, autosave=self.autosave)
            print("[INFO] BuildingController initialized.")  # Debug
                
            self.unit_controller = None  # ❌ Do not initialize yet

         except Exception as e:
            print(f"[ERROR] Failed to initialize MasterController: {e}")  # Debug
            raise

         print(f"[INFO] MasterController initialized with autosave={self.autosave}")


        
    def _ensure_logged_in(self):
        if not self.logged_in:
            print("User is not logged in")  # Debug statement
            raise IllegalAccessException 
        print("User is logged in")  # Debug statement    
        return True


    
    def is_logged_in(self):
        """Returns True if the user is logged in."""
        return self.logged_in
    # ---------------------------------------------
    # BUILDING-RELATED METHODS
    # ---------------------------------------------
    def create_building(self, building_id, name):
        """
        Creates a new building via `BuildingController` and saves it.
        """
        self.building_controller.create_building(building_id, name)
        self.building_controller.building_dao.save_buildings()

    def list_buildings(self):
        """
        Returns a list of all buildings from BuildingController.
        """
        return self.building_controller.list_buildings()

    def search_building(self, building_id):
        """
        Searches for a building in BuildingController by its ID (or 'social_security_number' if not renamed).
        Returns the Building object if found, else None.
        """
        return self.building_controller.search_building(building_id)

   
   
    def set_current_building(self, building_id):
        """
        Sets the current building and initializes the UnitController.
        """
        if not building_id:
            raise IllegalOperationException("Building ID cannot be empty.")

        key = str(building_id)
        building_obj = self.building_controller.search_building(key)
        if not building_obj:
            raise IllegalOperationException(f"Building with ID '{key}' not found!")

        # ✅ Store full Building object
        self.current_building = building_obj
        
        # ✅ Keep BuildingController in sync
        self.building_controller.current_building = building_obj


        # ✅ Set correct units file path
        self.units_path = os.path.join(self.data_dir, f"{self.current_building.name}_units.json")

        # 🔹 If the file doesn't exist, create an empty JSON file
        if not os.path.exists(self.units_path):
            print(f"[INFO] Creating new units file: {self.units_path}")
            with open(self.units_path, "w") as file:
                json.dump({"units": []}, file, indent=4)

        # ✅ Initialize UnitController with correct building object
        self.unit_controller = UController(self.current_building, filepath=self.units_path, autosave=self.autosave)

        print(f"[INFO] MasterController: Current building set to '{self.current_building.name}'")



    def create_unit(self, household_no, name, sin, birth_date, plate_no, tax_no, phone_number,
                email, address, group_no, account_no, account_note, receiver_no, receiver_note,
                work_address, work_phone_number, work_email, occupation):
        """
        Creates a new unit and assigns it to the selected building via UnitController.
        """
        if not self.current_building:
            raise ValueError("[ERROR] No building is selected. Cannot add a unit!")

        if not self.unit_controller:
            raise ValueError("[ERROR] UnitController is not initialized! Did you set a building first?")

        # ✅ Construct the unit dictionary
        new_unit = {
            "household_no": household_no,
            "name": name,
            "sin": sin,
            "birth_date": birth_date,
            "plate_no": plate_no,
            "tax_no": tax_no,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "group_no": group_no,
            "account_no": account_no,
            "account_note": account_note,
            "receiver_no": receiver_no,
            "receiver_note": receiver_note,
            "work_address": work_address,
            "work_phone_number": work_phone_number,
            "work_email": work_email,
            "occupation": occupation
        }

        # 🔴 FIX: Ensure UnitController exists before accessing `unit_dao`
        if not hasattr(self.unit_controller, "unit_dao") or self.unit_controller.unit_dao is None:
            raise ValueError("[ERROR] UnitController is missing `unit_dao`. Building might not be properly set!")

        # ✅ Call UnitController to create the unit
        try:
            created_unit = self.unit_controller.unit_dao.create_unit(new_unit)
            self.unit_controller.unit_dao.save_units()
            print("[SUCCESS] Unit added successfully!")
            return created_unit
        except Exception as e:
            print(f"[ERROR] Failed to add unit: {e}")
            raise

     



