from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note


class TestPatient(TestCase):
## Trying to create a patient with the following data
	def setUp(self):
		self.controller = Controller()
		self.controller.login("user", "clinic2024")
		
		self.patient1 = Patient(123456789, "Test Patient", "2003-07-17", "2265074749", "balseven22@gmail.com", "1616 Dougall Ave")
		self.patient2 =  Patient(987654321, "Test2 Patient", "2023-07-17", "2235074749", "balsev33n22@gmail.com", "1626 Dougall Ave")
		
	def test_patient_initialization(self):
		self.assertEqual(self.patient1.social_security_number, 123456789, "SIN did not initialize")
		self.assertEqual(self.patient1.name, "Test Patient", "name did not initialize")
		self.assertEqual(self.patient1.birth_date, "2003-07-17","birth date did not initialize")
		self.assertEqual(self.patient1.phone, "2265074749","phone did not initialize")
		self.assertEqual(self.patient1.email, "balseven22@gmail.com","email did not initialize")
		self.assertEqual(self.patient1.address, "1616 Dougall Ave","address did not initialize")
		
	def test_boundary_values(self):
		large_value_patient = Patient(9999999999999999999999999999, "Test Patient", "2003-07-17", "2265074749", "balseven22@gmail.com", "1616 Dougall Ave")
		self.assertEqual(large_value_patient.social_security_number, 9999999999999999999999999999)
		
	def test_patient_equality(self):
		same_patient = Patient(123456789, "Test Patient", "2003-07-17", "2265074749", "balseven22@gmail.com", "1616 Dougall Ave")
		different_patient = Patient(123456789, "Test2 Patient", "2003-07-17", "2265074749", "balseven22@gmail.com", "1616 Dougall Ave")
		
		self.assertEqual(self.patient1, same_patient, "Patient is the same")
		self.assertNotEqual(self.patient1, different_patient, "Patient is not the same")
	
	
		
		 

