# file: unit.py

from clinic.unit_record import UnitRecord

class Unit:
    """
    Represents a single household or occupant within a building.
    """

    def __init__(self,
                 householdno: str,
                 name: str,
                 sin: str,
                 bday: str,
                 plateno: str,
                 taxno: str,
                 phoneno: str,
                 email: str,
                 address: str,
                 groupno: str,
                 accountno: str,
                 accountnote: str,
                 receiverno: str,
                 receivernote: str,
                 workaddress: str,
                 workphone: str,
                 workemail: str,
                 occupation: str,
                 autosave: bool = True):
        """
        Initialize a new Unit (household) with full occupant details.
        
        :param householdno: A unique number for the occupant/household.
        :param name: Occupant name.
        :param sin: Another identifier.
        :param bday: Date of birth.
        :param plateno: Plate number.
        :param taxno: Tax number.
        :param phoneno: Phone number.
        :param email: Email address.
        :param address: Home address.
        :param groupno: Group number.
        :param accountno: Account number.
        :param accountnote: Any note regarding the account.
        :param receiverno: Receiver number.
        :param receivernote: Note for the receiver info.
        :param workaddress: Work address.
        :param workphone: Work phone.
        :param workemail: Work email.
        :param occupation: Occupation name or description.
        :param autosave: Whether changes should automatically be saved.
        """
        self.autosave = autosave
        self.householdno = str(householdno)
        self.name = name
        self.sin = sin
        self.bday = bday
        self.plateno = plateno
        self.taxno = taxno
        self.phoneno = phoneno
        self.email = email
        self.address = address
        self.groupno = groupno
        self.accountno = accountno
        self.accountnote = accountnote
        self.receiverno = receiverno
        self.receivernote = receivernote
        self.workaddress = workaddress
        self.workphone = workphone
        self.workemail = workemail
        self.occupation = occupation

        # Create a UnitRecord instance if you have UnitRecord defined
        self.record = UnitRecord()
        

    def to_dict(self):
        """Convert Unit object to dictionary."""
        return self.__dict__

    @staticmethod
    def from_dict(data):
        """Convert dictionary to Unit object."""
        return Unit(**data)
    
    def __eq__(self, other):
        """
        Two Units are considered the same if all major occupant details match.
        """
        if not isinstance(other, Unit):
            return False
        return (
            self.householdno == other.householdno and
            self.name == other.name and
            self.sin == other.sin and
            self.bday == other.bday and
            self.plateno == other.plateno and
            self.taxno == other.taxno and
            self.phoneno == other.phoneno and
            self.email == other.email and
            self.address == other.address and
            self.groupno == other.groupno and
            self.accountno == other.accountno and
            self.accountnote == other.accountnote and
            self.receiverno == other.receiverno and
            self.receivernote == other.receivernote and
            self.workaddress == other.workaddress and
            self.workphone == other.workphone and
            self.workemail == other.workemail and
            self.occupation == other.occupation
        )

    def __str__(self):
        """
        Returns a string representation of the occupant details.
        """
        return (
            f"Unit("
            f"Household No: {self.householdno}, "
            f"Name: {self.name}, "
            f"SIN: {self.sin}, "
            f"Birth date: {self.bday}, "
            f"Phone: {self.phoneno}, "
            f"Email: {self.email}, "
            f"Address: {self.address}, "
            f"Plate Number: {self.plateno}, "
            f"Tax Number: {self.taxno}, "
            f"Group Number: {self.groupno}, "
            f"Account Number: {self.accountno}, "
            f"Account Note: {self.accountnote}, "
            f"Receiver Number: {self.receiverno}, "
            f"Receiver Note: {self.receivernote}, "
            f"Work Address: {self.workaddress}, "
            f"Work Phone: {self.workphone}, "
            f"Work Email: {self.workemail}, "
            f"Occupation: {self.occupation}"
            f")"
        )
