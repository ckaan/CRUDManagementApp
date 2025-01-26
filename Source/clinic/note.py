from datetime import datetime
class Note:		
	## Initiliazing 
	def __init__(self, code, text, autosave= False):
		self.code = code
		self.autosave=autosave
		self.text= text
		self.timestamp= datetime.now()
		
	## Checks equality
	def __eq__(self, other):
		if not isinstance(other, Note):
			return False
		return self.code == other.code and self.text == other.text and int(self.timestamp.timestamp()) == int(other.timestamp.timestamp())

	## toString function 
	def __str__(self):
		return f"Note(Code: {self.code}, Text: {self.text}, Time: {self.timestamp})"
