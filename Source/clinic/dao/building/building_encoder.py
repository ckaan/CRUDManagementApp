# file: dao/building/building_encoder.py

import json
from clinic.building import Building

class BuildingEncoder(json.JSONEncoder):
    """Encodes Building objects to JSON format."""
    def default(self, obj):
        if isinstance(obj, Building):
            # You may also include 'units' serialization here if you want 
            # them saved in the same file:
            return {
                "building_id": obj.building_id,
                "name": obj.name,
                # Example:
                "units": [self._encode_unit(u) for u in obj.units]
            }
        return super().default(obj)

    def _encode_unit(self, unit_obj):
        # Return a dict of the Unit's data
        return {
            "social_security_number": unit_obj.social_security_number,
            "name": unit_obj.name,
            "sin": unit_obj.sin,
            "bday": unit_obj.bday,
            "plateno": unit_obj.plateno,
            "taxno": unit_obj.taxno,
            "phoneno": unit_obj.phoneno,
            "email": unit_obj.email,
            "address": unit_obj.address,
            "groupno": unit_obj.groupno,
            "accountno": unit_obj.accountno,
            "accountnote": unit_obj.accountnote,
            "receiverno": unit_obj.receiverno,
            "receivernote": unit_obj.receivernote,
            "workaddress": unit_obj.workaddress,
            "workphone": unit_obj.workphone,
            "workemail": unit_obj.workemail,
            "occupation": unit_obj.occupation
        }
