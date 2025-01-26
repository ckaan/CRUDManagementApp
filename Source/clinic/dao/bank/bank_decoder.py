import sys

from clinic.bank import Bank

import json

class PatientDecoder(json.JSONDecoder):
    def object_hook(self, obj):
        # Check if the object represents a single patient
        if "bankno" in obj:
            return Bank(
                bankno=obj["bankno"],
                bank_name=obj["bank_name"],
                branch=obj["branch"],
                account_no=obj["account_no"],
                account_name=obj["account_name"],
                authority=obj["authority"],
                phonenumber=obj["phonenumber"],
                faxno=obj["faxno"],
                ibanno=obj["ibanno"],
                web=obj["web"]
            )
        # Return the object unchanged if it doesn't match a Patient
        return obj

