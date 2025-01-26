import json
import os
from abc import ABC, abstractmethod
import sys

from clinic.building import Building
from .building_decoder import BuildingDecoder  # Kept original import name
from .building_encoder import BuildingEncoder  # Kept original import name
from clinic.exception.illegal_operation_exception import IllegalOperationException


class BuildingDAO(ABC):
    def __init__(self, current_building, filepath, autosave=True):
        """
        Initializes the BuildingDAO and ensures buildings are stored in a JSON file.
        """
        self.filepath = filepath
        self.autosave = autosave
        self.buildings: dict[int, Building] = {}  # Stores buildings
        self.current_building = current_building  # ✅ Correctly assigned without recursion

        if self.autosave:
            self.load_buildings()  # ✅ Load existing data only once


    def save_buildings(self):
        """
        Saves all buildings, including their associated units, to a JSON file.
        """
        if self.autosave:
            try:
                with open(self.filepath, "w") as file:
                    json.dump({"buildings": list(self.buildings.values())}, file, indent=4, cls=BuildingEncoder)
                    print(f"[INFO] Buildings successfully saved to {self.filepath}")
            except Exception as e:
                print(f"[ERROR] Could not save buildings: {str(e)}")

    def load_buildings(self):
        print(f"[DEBUG] Loading buildings from: {self.filepath}")  # ✅ Print file path
        
        try:
            if not os.path.exists(self.filepath):
                print("[ERROR] Buildings file does not exist!")
                return

            with open(self.filepath, "r") as file:
                content = file.read().strip()
                if not content:
                    print("[WARNING] Buildings file is empty.")
                    return

                data = json.loads(content, cls=BuildingDecoder)
                if "buildings" in data:
                    for building in data["buildings"]:
                        self.buildings[str(building.building_id)] = Building(
                            building_id=str(building.building_id),  # Ensure string ID
                            name=building.name
                        )

                        print(f"[INFO] Loaded Building: {building.name} (ID: {building.building_id})")
                else:
                    print("[ERROR] JSON format incorrect.")

        except FileNotFoundError:
            print("[ERROR] File not found")
        except json.JSONDecodeError:
            print("[ERROR] JSON Decoding Error!")



    def search_building(self, building_id):
        """
        Function Name: search_patient

        Function Description:
        (i) Searches for a building using its social security number.

        Parameters:
        -> social_security_number: The ID of the building to search for.

        Function Return value:
        -> The Building object if found, None if not found.
        """

        key = str(building_id)
        print(f"[DEBUG] Searching for building with ID: {key}")
        print(f"[DEBUG] Available Buildings: {self.buildings}")
        return self.buildings.get(key)

    def create_building(self, building_id, name):
        """
        Function Name: create_building

        Function Description:
        (i) Creates a new building and assigns it empty lists for units, turnovers, and banks.

        Parameters:
        -> social_security_number: The ID of the building.
        -> name: The name of the building.

        Function Return value:
        -> Newly created Building object.
        """

        key = str(building_id)
        # CHANGE: replaced self.patients -> self.buildings
        if key in self.buildings:
            raise IllegalOperationException("Building already exists!")

        # The Building constructor doesn't have a 'unit' parameter originally;
        # so after creation, we can set building.units = []
        building = Building(building_id, name)
        building.units = []  # Minimal fix

        self.buildings[key] = building

        if self.autosave:
            self.save_buildings()
        return building

    def retrieve_buildings(self, name):
        """
        Function Name: retrieve_patients

        Function Description:
        (i) Retrieves a list of buildings whose names match the provided text.

        Parameters:
        -> name: The name or part of the name to search for.

        Function Return value:
        -> A list of matching Building objects, or an empty list if no matches are found.
        """

        return [building for building in self.buildings.values() if name.lower() in building.name.lower()]

    def update_building(self, patient_id, building_id, name):
        """
        Function Name: update_patient

        Function Description:
        (i) Updates the information for an existing building.
        (ii) Ensures the ID number is changed properly without conflicts.

        Parameters:
        -> patient_id: The original building ID.
        -> social_security_number: The new ID if updating.
        -> name: The new name of the building.

        Function Return value:
        -> True if the update was successful, False otherwise.
        """

        key = str(patient_id)
        building_id = str(building_id)
        building = self.buildings.get(key)

        if building is None:
            raise IllegalOperationException("Building not found.")

        # Handle case where ID is updated
        # CHANGE: replaced 'if building_id in self.patients' -> 'if building_id in self.buildings'
        if building_id != key:
            if building_id in self.buildings:
                raise IllegalOperationException("New ID already exists.")
            del self.buildings[key]
            self.buildings[building_id] = building
            building.building_id = building_id

        if name and building.name != name:
            building.name = name

        if self.autosave:
            self.save_buildings()

        return True

    def delete_building(self, building_id):
        """
        Function Name: delete_patient

        Function Description:
        (i) Deletes a building record based on its ID.
        (ii) Ensures that associated units, turnovers, and banks are also removed.

        Parameters:
        -> social_security_number: The ID of the building to be deleted.

        Function Return value:
        -> True if the building was deleted, False otherwise.
        """

        building_id = str(building_id)

        if building_id not in self.buildings:
            raise IllegalOperationException("Building not found.")

        # Remove the building
        del self.buildings[building_id]

        if self.autosave:
            self.save_buildings()
        return True

    def list_buildings(self):
        """
        Function Name: list_patients

        Function Description:
        (i) Lists all the buildings in the system.

        Parameters:
        -> None

        Function Return value:
        -> A list of all buildings if available, or an empty list if none are found.
        """

        return list(self.buildings.values())
