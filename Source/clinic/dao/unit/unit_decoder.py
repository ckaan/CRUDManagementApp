import sys

from clinic.unit import Unit
import json

class UnitDecoder(json.JSONDecoder):
    def object_hook(self, obj):
        # Check if the object represents a single unit
        if "household_no" in obj:
            return Unit(
                householdno=obj.get("household_no"),
                name=obj.get("name"),
                sin=obj.get("sin"),
                bday=obj.get("bday"),
                phoneno=obj.get("phoneno"),
                email=obj.get("email"),
                address=obj.get("address"),
                plateno=obj.get("plateno"),
                taxno=obj.get("taxno"),
                groupno=obj.get("groupno"),
                accountno=obj.get("accountno"),
                accountnote=obj.get("accountnote"),
                receiverno=obj.get("receiverno"),
                receivernote=obj.get("receivernote"),
                workaddress=obj.get("workaddress"),
                workphone=obj.get("workphone"),
                workemail=obj.get("workemail"),
                occupation=obj.get("occupation")
            )
        # Return the object unchanged if it doesn't match a Unit
        return obj

