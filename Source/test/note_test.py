from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note


class TestNote(TestCase):
	## Trying to create a patient with the following data
	def setUp(self):
		self.note = Note(1, "Test note!")
	
	def test_note_initialization(self):
		self.assertEqual(self.note.code, 1, "Code does not match")
		self.assertEqual(self.note.text, "Test note!", "Text does not match")
		self.assertIsNotNone(self.note.timestamp, "The note do not have a timestamp!")

	
	def test_note_equality(self):
		same_note = Note(1, "Test note!")
		different_note = Note(2, "Test2 note!")
		self.assertEqual(self.note, same_note, "Note is not the same")
		self.assertNotEqual(self.note, different_note, "Note is the same")
	
	
