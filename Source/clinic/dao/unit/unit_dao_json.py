import json
import os
from abc import ABC, abstractmethod
import sys

from clinic.unit import Unit
from .unit_decoder import UnitDecoder
from .unit_encoder import UnitEncoder
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException


class UnitDAO(ABC):
    def __init__(self, current_building, filepath, autosave=True):
        """
        Function Name: __init__
        (i) Initializes the UnitDAO with the current building context.
        (ii) Ensures that units are stored per building.

        Parameters:
        -> autosave: Boolean flag to enable autosave.
        -> filepath: The file path where unit data is stored.
        """

        self.autosave = autosave
        self.current_building = current_building  

       
        self.filepath = filepath 

        self.units: dict[int, Unit] = {}  # Dictionary to store unit data (renamed from 'patients')
        self.current_unit = None  # Track the selected unit (renamed from 'current_patient')

        if self.autosave:
            self.load_units()  # Renamed from load_patients()

    # Saving units if autosave is true
    def save_units(self):
        if self.autosave:
            with open(self.filepath, "w") as file:
                json.dump({"units": list(self.units.values())}, file, indent=4, cls=UnitEncoder)

    # Loading units from a JSON file
    def load_units(self):
        try:
            with open(self.filepath, "r") as file:
                content = file.read().strip()
                if not content:
                    print("[DEBUG] JSON file is empty!")
                    return None

                data = json.loads(content)
                print("[DEBUG] Loaded JSON keys:", data.keys())

                if "units" in data and isinstance(data["units"], list):
                    updated_units = []  # Create a new list with fixed keys

                    for unit_data in data["units"]:
                        print("[DEBUG] Unit keys before fix:", unit_data.keys())

                        # Convert 'household_no' to 'householdno' if needed
                        if "household_no" in unit_data:
                            unit_data["householdno"] = unit_data.pop("household_no")

                        print("[DEBUG] Unit keys after fix:", unit_data.keys())
                        updated_units.append(unit_data)  # Add to new list

                    # Save the fixed JSON back to file
                    with open(self.filepath, "w") as file:
                        json.dump({"units": updated_units}, file, indent=4)

                    # Now process the updated JSON
                    for unit_data in updated_units:
                        unit = Unit(
                            householdno=unit_data["householdno"],
                            name=unit_data["name"],
                            sin=unit_data["sin"],
                            bday=unit_data["bday"],
                            plateno=unit_data["plateno"],
                            taxno=unit_data["taxno"],
                            phoneno=unit_data["phoneno"],
                            email=unit_data["email"],
                            address=unit_data["address"],
                            groupno=unit_data["groupno"],
                            accountno=unit_data["accountno"],
                            accountnote=unit_data["accountnote"],
                            receiverno=unit_data["receiverno"],
                            receivernote=unit_data["receivernote"],
                            workaddress=unit_data["workaddress"],
                            workphone=unit_data["workphone"],
                            workemail=unit_data["workemail"],
                            occupation=unit_data["occupation"],
                        )
                        self.units[str(unit.householdno)] = unit
                else:
                    print("[ERROR] Unexpected JSON format:", data)
        except FileNotFoundError:
            print("[ERROR] File not found:", self.filepath)
        except json.JSONDecodeError:
            print("[ERROR] JSON Decoding Error!")



    def search_unit(self, householdno):
        key = str(householdno)
        return self.units.get(key, None)

    def create_unit(self, householdno, name, sin, bday, plateno, taxno, phoneno, email, address,
                    groupno, accountno, accountnote, receiverno, receivernote, workaddress, workphone,
                    workemail, occupation):
        key = str(householdno)
        if key in self.units:
            raise IllegalOperationException("Unit already exists.")
        unit = Unit(householdno, name, sin, bday, plateno, taxno, phoneno, email, address, groupno,
                    accountno, accountnote, receiverno, receivernote, workaddress, workphone, workemail, occupation)
        self.units[key] = unit

        if self.autosave:
            self.save_units()
        return unit

    def delete_unit(self, householdno):
        key = str(householdno)
        if key not in self.units:
            raise IllegalOperationException("Unit not found.")

        del self.units[key]

        if self.autosave:
            self.save_units()
        return True

    def list_units(self):
        if not self.units:
            print("No units available!")
            return []
        return list(self.units.values())

