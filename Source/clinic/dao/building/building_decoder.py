# file: dao/building/building_decoder.py

import json
from clinic.building import Building
from clinic.unit import Unit

class BuildingDecoder(json.JSONDecoder):
    """Decodes JSON data into Building objects."""
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        """
        If the JSON object has 'building_id', we treat it as a Building. 
        Also handle 'units' if present.
        """
        if "building_id" in obj:
            # Create a Building object
            building = Building(
                building_id=obj["building_id"],
                name=obj.get("name", ""),
            )
            # If you store 'units' in JSON, you can deserialize them:
            if "units" in obj and isinstance(obj["units"], list):
                for unit_data in obj["units"]:
                    # Suppose each 'unit_data' has the fields needed for Unit(...)
                    unit = Unit(
                        social_security_number=unit_data.get("social_security_number", ""),
                        name=unit_data.get("name", ""),
                        sin=unit_data.get("sin", ""),
                        bday=unit_data.get("bday", ""),
                        plateno=unit_data.get("plateno", ""),
                        taxno=unit_data.get("taxno", ""),
                        phoneno=unit_data.get("phoneno", ""),
                        email=unit_data.get("email", ""),
                        address=unit_data.get("address", ""),
                        groupno=unit_data.get("groupno", ""),
                        accountno=unit_data.get("accountno", ""),
                        accountnote=unit_data.get("accountnote", ""),
                        receiverno=unit_data.get("receiverno", ""),
                        receivernote=unit_data.get("receivernote", ""),
                        workaddress=unit_data.get("workaddress", ""),
                        workphone=unit_data.get("workphone", ""),
                        workemail=unit_data.get("workemail", ""),
                        occupation=unit_data.get("occupation", "")
                    )
                    building.units.append(unit)
            return building
        return obj  # If it's not a Building dict, return as-is.
