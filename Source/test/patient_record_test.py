from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note

## Trying to create a patient with the following data
class TestPatientRecord(TestCase):
	def setUp(self):
		self.record = PatientRecord()
	
	def test_add_note_record(self):
		note = self.record.add_note("This is a note")
		
		self.assertEqual(note.text, "This is a note", "The note is not the same!")
		self.assertIn(note.code,  self.record.notes, "The note should be added!")
		self.assertEqual(self.record.notes[note.code], note, "Stored note does not match with the created note!")
		
		
	def test_delete_note_record(self):
		
		note = self.record.add_note("This is a note")
		self.assertIn(note.code,  self.record.notes, "The note should be added!")
		
		result = self.record.delete_note(note.code)
		self.assertTrue(result, "Note could not deleted!")
		self.assertNotIn(note.code, self.record.notes, "Note deletion could not recorded!")
		
		result = self.record.delete_note(note.code)
		self.assertFalse(result, "Deleting should not return False!")

	
	def test_boundary_values(self):
		self.assertEqual(self.record.autocounter, 1, "Autocounter should start at 1")

