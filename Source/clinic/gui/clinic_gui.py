import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox, QComboBox, QHBoxLayout, QLineEdit
)
from PySide6.QtCore import Qt, Signal
from clinic.controllers.building_controller import BuController
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException

from .general_gui import Ui_MainWindow  # Import your next page's UI class


from clinic.controllers.master_controller import MasterController

class BuildingRegistrationWindow(QWidget):
    
    building_registered = Signal()

    def __init__(self, master_controller):
        super().__init__()
        self.controller = master_controller
        self.setWindowTitle("Register a New Building")
        self.setGeometry(150, 150, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.building_id_label = QLabel("Building No:")
        self.building_id_input = QLineEdit()
        layout.addWidget(self.building_id_label)
        layout.addWidget(self.building_id_input)

        self.building_name_label = QLabel("Building Name:")
        self.building_name_input = QLineEdit()
        layout.addWidget(self.building_name_label)
        layout.addWidget(self.building_name_input)

        self.submit_button = QPushButton("Register Building")
        self.submit_button.clicked.connect(self.register_building)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def register_building(self):
        building_id = self.building_id_input.text()
        building_name = self.building_name_input.text()

        if not building_id or not building_name:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            self.controller._ensure_logged_in()
            self.controller.create_building(building_id, building_name)
            self.building_registered.emit()
            QMessageBox.information(self, "Success", f"Building '{building_name}' registered successfully!")
            self.close()
        except IllegalAccessException:
            QMessageBox.critical(self, "Login Error", "Please log in to register a building.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to register building: {str(e)}")

class ClinicGUI(QMainWindow):
    def __init__(self, autosave):
        super().__init__()
        self.autosave = autosave
        self.master_controller = MasterController(autosave)

        # Initialize the UI and pass the Master Controller
        self.ui = Ui_MainWindow(self.master_controller)
        self.ui.setupUi(self)  # Assuming this method exists

        self.setWindowTitle("Building Management System - Main Menu")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to Transparent Pro Management's Management App")
        welcome_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(welcome_label)

        building_selection_layout = QHBoxLayout()
        building_label = QLabel("Choose an Existing Building:")
        self.building_dropdown = QComboBox()
        self.update_building_dropdown()
        building_selection_layout.addWidget(building_label)
        building_selection_layout.addWidget(self.building_dropdown)
        main_layout.addLayout(building_selection_layout)

        self.building_dropdown.currentIndexChanged.connect(self.set_current_building)

        self.continue_building_button = QPushButton("Continue")
        self.continue_building_button.clicked.connect(self.open_next_page)
        main_layout.addWidget(self.continue_building_button)

        self.register_building_button = QPushButton("Register Building")
        self.register_building_button.clicked.connect(self.open_building_registration_window)
        main_layout.addWidget(self.register_building_button)

        self.delete_building_button = QPushButton("Delete")
        self.delete_building_button.clicked.connect(self.delete_selected_building)
        main_layout.addWidget(self.delete_building_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(lambda: exit(1))
        main_layout.addWidget(self.exit_button)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def open_building_registration_window(self):
        self.building_registration_window = BuildingRegistrationWindow(self.master_controller)
        self.building_registration_window.building_registered.connect(self.update_building_dropdown)
        self.building_registration_window.show()

    def update_building_dropdown(self):
        self.building_dropdown.clear()
        buildings = self.master_controller.list_buildings()
        if not buildings:
            QMessageBox.information(self, "Info", "No buildings available to display.")
            return

        self.buildings = buildings
        for building in buildings:
            self.building_dropdown.addItem(f"{building.name} (ID: {building.building_id})", building.building_id)

        if self.buildings:
            self.set_current_building(0) 

    def set_current_building(self, index):
        """Sets the currently selected building based on dropdown selection."""
        
        if self.building_dropdown.count() == 0:
            QMessageBox.warning(self, "Error", "No buildings available to select.")
            return

        # Ensure index is an integer
        if isinstance(index, str):
            index = self.building_dropdown.findText(index)  # Convert string to index
        
        if index == -1:
            QMessageBox.warning(self, "Error", "Invalid building selection.")
            return

        building_id = self.building_dropdown.itemData(index, Qt.UserRole)  # ✅ Correct way to get ID

        if not building_id:
            QMessageBox.warning(self, "Error", "Could not retrieve valid building ID.")
            return

        print(f"[DEBUG] GUI selected building: {building_id}")

        try:
            self.master_controller.set_current_building(building_id)
            QMessageBox.information(self, "Success", f"Building changed to {building_id}")
        except Exception as e:
            print(f"[ERROR] Failed to set current building: {e}")
            QMessageBox.critical(self, "Error", f"Failed to set current building: {str(e)}")


    def delete_selected_building(self):
        if self.building_dropdown.count() == 0:
            QMessageBox.warning(self, "Selection Error", "No buildings available to delete.")
            return

        selected_index = self.building_dropdown.currentIndex()
        if selected_index < 0:
            QMessageBox.warning(self, "Selection Error", "No building selected.")
            return

        building_id = self.building_dropdown.itemData(selected_index)
        if not building_id:
            QMessageBox.warning(self, "Error", "Could not retrieve building ID.")
            return

        try:
            reply = QMessageBox.question(
                self,
                "Delete Building",
                f"Are you sure you want to delete the building with ID: {building_id}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.master_controller.delete_building(building_id)
                QMessageBox.information(self, "Success", f"Building with ID {building_id} deleted successfully.")
                self.update_building_dropdown()
        except IllegalOperationException as e:
            QMessageBox.critical(self, "Error", f"Failed to delete building: {str(e)}")
        except Exception as e:
            print("Error")

    def open_next_page(self):
        try:
            self.next_page = QMainWindow()
            self.ui = Ui_MainWindow(self.master_controller)
            self.ui.setupUi(self.next_page)
            self.next_page.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open the next page: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ClinicGUI(autosave=True)  # ✅ Pass autosave=True
    main_window.show()
    sys.exit(app.exec())
