
# ------------------------------------------------------------

import json
from clinic.unit import Unit

class UnitEncoder(json.JSONEncoder):
    # Standard encoder implementation for JSON file that is a list of dictionaries
    def default(self, obj):
        if isinstance(obj, Unit):
            return {
                "household_no": obj.householdno,
                "name": obj.name,
                "sin": obj.sin,
                "bday": obj.bday,
                "phoneno": obj.phoneno,
                "email": obj.email,
                "address": obj.address,
                "plateno": obj.plateno,
                "taxno": obj.taxno,
                "groupno": obj.groupno,
                "accountno": obj.accountno,
                "accountnote": obj.accountnote,
                "receiverno": obj.receiverno,
                "receivernote": obj.receivernote,
                "workaddress": obj.workaddress,
                "workphone": obj.workphone,
                "workemail": obj.workemail,
                "occupation": obj.occupation
            }
        return super().default(obj)

