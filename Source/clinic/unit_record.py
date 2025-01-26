import os

from clinic.note import Note

class UnitRecord:
    def __init__(self, autocounter=1, autosave= True):
        self.autosave= autosave
        self.autocounter = autocounter
        self.notes = {}
        
            
    

    ## Add notes
    def add_note(self, text):
        new_note = Note(self.autocounter, text)
        self.notes[self.autocounter] = new_note
        print("\nAdded note with code -> " + str(self.autocounter) + " : " + str(new_note))
        self.autocounter += 1

       
        return new_note

    ## Delete notes
    def delete_note(self, code):
        print("Notes before deletion: ", self.notes.keys())
        if code in self.notes:
            del self.notes[code]
            print("The note is deleted!", code)
            print("Notes after deletion: ", self.notes.keys())

            
            return True
        else:
            print("The note could not be deleted!")
            print("Notes at failure: ", self.notes.keys())
            return False
            
    #toString function
    def __str__(self):
        return "The number of patients at the moment: " + str(self.autocounter)

