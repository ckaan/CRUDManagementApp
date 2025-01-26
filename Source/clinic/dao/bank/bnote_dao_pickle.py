from abc import ABC, abstractmethod
from datetime import datetime
import pickle
import os

from clinic.note import Note
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException

class NoteDAO(ABC):
    def __init__(self, autosave = True, filepath="clinic/records"):
        self.filepath = filepath
        self.notes = {}
        self.autosave = autosave
        self.current_patient = []
        
        
            
     
     
   
    # Saving notes by pickle class
    def save_notes(self):
        if not self.current_patient:
            raise NoCurrentPatientException("No current patient set in NoteDAO.")
        # Assigning file path to the filepath and the name properties of files to create and save. 
        filepath = os.path.join(self.filepath, f"{self.current_patient.social_security_number}.dat")


        try:
            #Creating file inside of the "directory"
            directory = os.path.dirname(filepath)
            os.makedirs(directory, exist_ok=True)

            # Attempt to write notes to file
            with open(filepath, "wb") as file:
                pickle.dump(self.current_patient.record.notes, file)

        except Exception as e:   
            raise 
            
            
            
            
            
            
            
            
    # Loading notes by pickle class
    def load_notes(self):
        if not self.current_patient:
            raise NoCurrentPatientException
        # Assigning file path to the filepath and the name properties of files to load.
        filepath = os.path.join(self.filepath, f"{self.current_patient.social_security_number}.dat")


        if os.path.exists(filepath):
            try:
            ## Attempt to read notes from a file
                with open(filepath, "rb") as file:
                    notes = pickle.load(file)
                    self.current_patient.record.notes = notes
                    self.notes = notes
                    
                    if notes:
                        self.current_patient.record.autocounter = max(notes.keys()) + 1
                    else:
                        self.current_patient.record.autocounter = 1
            except Exception as e:
                print("Failed to load notes for PHN")
                self.current_patient.record.notes = {}
                self.notes={}
        else:
            print("No file found for PHN. Initializing empty notes.")
            self.current_patient.record.notes = {}
            self.notes={}
 

   
            
    # Searching current patient's note by their code        
    def search_note(self, code): 
    
        '''
        Function Name: search_note
        
        Function Description:
        (i) Searches for a note in the current patient's record by matching the provided text.
        (ii) Ensures that the user is logged in before attempting the search.

        Parameters:
        -> text: The text content to search for in the patient's notes.

        Function Return value:
        -> The note object if a match is found, None if no note matches the provided text or the user is not logged in.
        '''
        
        
        if not self.current_patient:
            raise NoCurrentPatientException
    
        note = self.current_patient.record.notes.get(code)
        return note

    # Creating note for the current patient
    def create_note(self, text):
        if not self.current_patient:
            raise NoCurrentPatientException
                
        new_note = self.current_patient.record.add_note(text)  
        self.save_notes()
        
        return new_note
        
        
        
        
        
        
        
    # Retrieving note for the current patient
    def retrieve_notes(self, text):
        '''
        Function Name: retrieve_notes
        
        Function Description:
        (i) Retrieves all notes from the current patient's record that contain the specified text.
        (ii) If no text is provided or the patient is not selected, the function will return None or an empty list.

        Parameters:
        -> text: The text content to match within the notes.

        Function Return value:
        -> A list of matching notes, or None if no notes are found or no patient is selected.
        '''

    
    
        if not self.current_patient:
            raise NoCurrentPatientException

        if len(text) == 0:
            return []

        matching_notes = []
        for note in self.current_patient.record.notes.values():
            if text.lower() in note.text.lower():
                matching_notes.append(note)

        if matching_notes:
            for note in matching_notes:
                print(note)
        else:
            print("DEBUG: No notes found matching the text.")

        return matching_notes
        
        
        
        
        
        
        

    #Updating note for the current patient 
    def update_notes(self, code, new_text):
    
        '''
        Function Name: update_note
        
        Function Description:
        (i) Updates the text of an existing note in the current patient's record.
        (ii) If the note is found, updates the text and the timestamp of the note.
        (iii) Ensures that a current patient is selected before attempting to update the note.

        Parameters:
        -> code: The unique identifier of the note to be updated.
        -> new_text: The new text content to replace the old text in the note.

        Function Return value:
        -> The updated note object if successful, None if the note cannot be updated.
        '''
        if not self.current_patient:
            raise NoCurrentPatientException

        note = self.current_patient.record.notes.get(code)

        if note:
            if len(new_text) != 0:
                note.text = new_text

            note.timestamp = datetime.now()
            print("Note is updated!")       
        else:
            print("Note could not updated!")
        
        self.save_notes()
        return note 
        
        
        
        
        
        
        
    # Deleting note for the current patient
    def delete_notes(self, code):
    
        '''
        Function Name: delete_note
        
        Function Description:
        (i) Deletes a note from the current patient's record by its unique code.
        (ii) Ensures that a current patient is selected before attempting to delete the note.

        Parameters:
        -> code: The unique identifier of the note to be deleted.

        Function Return value:
        -> The result of the deletion process. If successful, returns the deleted note; otherwise, None.
        '''
        
        if not self.current_patient:
            raise NoCurrentPatientException

        if self.current_patient.record.delete_note(code):
            if self.autosave:
                self.save_notes()
            else:
                self.save_notes()
            return True

        return False

        
        
        
        
        
        
        
        
        
    #Listing all the notes exist for the current patient
    def list_notes(self):
    
        '''
        Function Name: list_notes
        
        Function Description:
        (i) Lists all the notes in the current patient's record.
        (ii) If there are no notes, returns an empty list.
        (iii) Ensures that a current patient is selected before attempting to list the notes.

        Parameters:
        -> None

        Function Return value:
        -> A sorted list of all notes for the current patient, or an empty list if no notes exist.
        '''
        
        
        if not self.current_patient:
            raise NoCurrentPatientException
        if len(self.current_patient.record.notes) == 0:
            return []
        if self.current_patient:
            print(self.current_patient.record)
        else:
            print("No current patient selected!")

        notes_list = list(self.current_patient.record.notes.values())
        n = len(notes_list)
        #Sorting 
        for i in range(n):
            for j in range(0, n-i-1):
                if notes_list[j].code < notes_list[j+1].code:
                    notes_list[j], notes_list[j+1] = notes_list[j+1], notes_list[j]
        return notes_list
