import sys
from PyQt6.QtWidgets import QApplication
from clinic.controllers.master_controller import MasterController
from clinic.gui.clinic_gui import ClinicGUI

def main():
    app = QApplication(sys.argv)  # ✅ Initialize the GUI application

    # ✅ Pass MasterController to GUI
    autosave =True
    gui = ClinicGUI(autosave=True)
    gui.show()

    sys.exit(app.exec())  # ✅ Start the event loop

if __name__ == "__main__":
    main()




