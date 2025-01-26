# file: building.py

from clinic.building_record import BuildingRecord
from .unit import Unit

class Building:
    """
    Represents a building that can contain multiple Unit objects.
    """

    def __init__(self,
                 building_id: str,
                 name: str,
                 autosave=True):
        self.autosave = autosave
        self.building_id = str(building_id)
        self.name = name
        # A Building can contain many Units
        self.units = []
        # If you have a BuildingRecord class, store it here
        self.record = BuildingRecord()

    def __eq__(self, other):
        """
        Two buildings are considered the same if they have the same ID and name.
        """
        if not isinstance(other, Building):
            return False
        return (
            self.building_id == other.building_id
            and self.name == other.name
        )

    def __str__(self):
        """
        Returns a string representation of the Building, including how many Units it has.
        """
        return f"Building(ID: {self.building_id}, Name: {self.name}, Units: {len(self.units)})"
    
    
    def add_unit(self, unit):
        """Adds a unit to the building."""
        self.units.append(unit)