from clinic.bank_record import BankRecord

class Bank:
## Initialize a new patient
    def __init__(self, bankno, bank_name, branch, account_no, account_name, authority, phonenumber, faxno, ibanno, web, autosave = True): 
    ## Assign their attributes 
        self.autosave = autosave
        self.bankno = str(bankno) # Bank No
        
        self.bank_name = bank_name
        self.branch = branch
        self.account_no = account_no
        self.account_name = account_name
        self.authority=authority
        self.phonenumber = phonenumber
        self.faxno = faxno
        self.ibanno = ibanno
        self.web = web
        
        
        ## Creating a patient record instance
        self.record = BankRecord()
        
        
        ## Equality check
    def __eq__(self, other):
        if not isinstance(other, Bank):
            return False
        return (
            self.bankno == other.bankno and
            self.bank_name == other.bank_name and self.branch == other.branch and
            self.account_no == other.account_no and self.account_name == other.account_name and
            self.authority == other.authority and self.phonenumber == other.phonenumber and 
            self.faxno == other.faxno and self.ibanno == other.ibanno and self.web == other.web
    )

               
    ## toString function
    def __str__(self):
        return (f"Bank(SIN: {self.bankno}, "
                f"Bank Name: {self.bank_name}, "
                f"Branch: {self.branch}, "
                f"Account No: {self.account_no}, "
                f"Account Name: {self.account_name}, "
                f"Authority: {self.authority}, "
                f"Phone Number: {self.phonenumber}, "
                f"Fax Number: {self.faxno}, "
                f"IBAN No: {self.ibanno}, "
                f"Web: {self.web})")



