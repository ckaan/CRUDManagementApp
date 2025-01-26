import sys
sys.path.append(r"C:\Users\User\Documents\Projects\Building Management")
from clinic.turnovers import Turnovers

import json

class PatientDecoder(json.JSONDecoder):
    def object_hook(self, obj):
        # Check if the object represents a single patient
        if "group_code" in obj:
            return Turnovers(
                group_code=obj["group_code"],
                code=obj["code"],
                company_name=obj["company_name"],
                authority=obj["authority"],
                bank_name=obj["bank_name"],
                taxno=obj["taxno"],
                taxplace=obj["taxplace"],
                iban=obj["iban"],
                address=obj["address"],
                phonenumber=obj["phonenumber"],
                email=obj["email"],
                web=obj["web"]
            )
        # Return the object unchanged if it doesn't match a Patient
        return obj

