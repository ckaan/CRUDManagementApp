from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QApplication
import sys
from .building_gui import PatientGUI

class LoginGUI(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller= controller
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)
        print(f"Controller instance in LoginGUI: {id(self.controller)}")
        
        # UI Elements
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit(self)
        
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.handle_exit)

        # Layouts
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.exit_button)

        # Combine layouts
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def handle_login(self):
        # Get input values
        username = self.username_input.text()
        password = self.password_input.text()

        try: # Authenticate using the Controller
            if self.controller.login(username, password):
            # Login successful, close this window and proceed
                print("User is successfully logged in")  # Debugging statement
                self.accept()  # This will close the dialog
                self.open_next_window(username)
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
        
        except InvalidLoginException:
        # Login failed, show an error message
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
        except DuplicateLoginException:
        # Handle the case where the user is already logged in
            QMessageBox.warning(self, "Login Failed", "User already logged in. Please log out first.")
          

    def handle_exit(self):
        # Exit the application
        QApplication.quit()
    
    def show_error_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.exec()
        
    def open_next_window(self, username):
        # Open the main window after successful login
        self.main_window = PatientGUI(self.controller, username)
        self.main_window.show()
        self.close()  # Close the login window  


# For testing purposes only:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    from clinic.controller import Controller  # Adjust the path as needed
    controller = Controller()
    login_gui = LoginGUI(controller)
    login_gui.show()
    sys.exit(app.exec())


