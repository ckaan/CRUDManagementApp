import json
from clinic.bank import Bank

class PatientEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Bank):
            return {
                "bankno": obj.bankno,
                "bank_name": obj.bank_name,
                "branch": obj.branch,
                "account_no": obj.account_no,
                "account_name": obj.account_name,
                "authority": obj.authority,
                "phonenumber": obj.phonenumber,
                "faxno": obj.faxno,
                "ibanno": obj.ibanno,
                "web": obj.web,
            }
        return super().default(obj)


