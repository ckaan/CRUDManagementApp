from clinic.turnovers_record import TurnoversRecord

## Initialize a new patient
class Turnovers:
    def __init__(self, group_code, code, company_name, authority, bank_name, taxno, taxplace, iban, address, phonenumber, email, web, autosave=True):
            # Assign attributes
            self.autosave = autosave
            self.group_code = str(group_code)
            self.code = code
            self.company_name = company_name
            self.authority = authority
            self.bank_name = bank_name
            self.taxno = taxno
            self.taxplace = taxplace
            self.iban = iban
            self.address = address
            self.phonenumber = phonenumber
            self.email = email
            self.web = web

            # Initialize a record instance for turnovers
            self.record = TurnoversRecord()

        ## Equality check
    def __eq__(self, other):
            if not isinstance(other, Turnovers):
                return False
            return (
                self.group_code== other.group_code and
                self.code == other.code and
                self.company_name == other.company_name and
                self.authority == other.authority and
                self.bank_name == other.bank_name and
                self.taxno == other.taxno and
                self.taxplace == other.taxplace and
                self.iban == other.iban and
                self.address == other.address and
                self.phonenumber == other.phonenumber and
                self.email == other.email and
                self.web == other.web
            )

        ## toString function
    def __str__(self):
            return (
                "Turnovers(Group Code: " + str(self.group_code) +
                ", Code: " + self.code +
                ", Company Name: " + self.company_name +
                ", Authority: " + self.authority +
                ", Bank Name: " + self.bank_name +
                ", Tax No: " + self.taxno +
                ", Tax Place: " + self.taxplace +
                ", IBAN: " + self.iban +
                ", Address: " + self.address +
                ", Phone: " + self.phonenumber +
                ", Email: " + self.email +
                ", Web: " + self.web + ")"
            )


