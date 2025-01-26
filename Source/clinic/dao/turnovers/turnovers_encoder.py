import json
from clinic.turnovers import Turnovers

class PatientEncoder(json.JSONEncoder):
    #Standard encoder implementation for json file that is list of dictionaries 
    def default(self, obj):
        if isinstance(obj, Turnovers):
            return {
                "group_code": obj.group_code,
                "code": obj.code,
                "company_name": obj.company_name,
                "authority": obj.authority,
                "bank_name": obj.bank_name,
                "taxno": obj.taxno,
                "taxplace": obj.taxplace,
                "iban": obj.iban,
                "address": obj.address,
                "phonenumber": obj.phonenumber,
                "email": obj.email,
                "web": obj.web
            }
        return super().default(obj)

