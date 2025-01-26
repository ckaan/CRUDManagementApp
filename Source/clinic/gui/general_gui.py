# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QMessageBox)

from clinic.controllers.unit_controller import UController
from clinic.controllers.bank_controller import BController
from clinic.controllers.turnovers_controller import TController

from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_building_exception import NoCurrentPatientException
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox


from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox,QGridLayout,QInputDialog



 
class UpdateTurnoversDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Turnover")
        self.setGeometry(200, 200, 500, 600)

        # Create the grid layout
        self.layout = QGridLayout(self)

        # Define input fields
        self.fields = {}
        self.add_input_field("l_groupcode", "SIN", 0, 0)
        self.add_input_field("l_code", "Turnover Code", 1, 0)
        self.add_input_field("l_companyname", "Company Name", 2, 0)
        self.add_input_field("l_authority_2", "Authority", 3, 0)
        self.add_input_field("l_bankname_2", "Bank Name", 4, 0)
        self.add_input_field("l_bankname_3", "Tax Number", 5, 0)
        self.add_input_field("l_bankname_4", "Tax Place", 6, 0)
        self.add_input_field("l_bankname_6", "IBAN", 7, 0)
        self.add_input_field("l_bankname_5", "Address", 8, 0)
        self.add_input_field("l_bankname_7", "Phone Number", 9, 0)
        self.add_input_field("l_bankname_8", "Email", 0, 2)
        self.add_input_field("l_email_2", "Website", 1, 2)

        # Buttons
        self.update_button = QPushButton("Update")
        self.cancel_button = QPushButton("Cancel")

        # Add buttons to the layout
        self.layout.addWidget(self.update_button, 10, 1)
        self.layout.addWidget(self.cancel_button, 10, 2)

        # Connect buttons
        self.update_button.clicked.connect(self.accept)  # Closes dialog and returns success
        self.cancel_button.clicked.connect(self.reject)  # Closes dialog without success

        # Clear all fields
        self.clear_fields()

    def add_input_field(self, field_name, label_text, row, col):
        """Helper method to add labeled input fields to the grid layout."""
        label = QLabel(label_text, self)
        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("")  # Ensure no placeholder text
        self.layout.addWidget(label, row, col)
        self.layout.addWidget(line_edit, row, col + 1)
        self.fields[field_name] = line_edit
        print(f"[DEBUG] Field {field_name} initialized with placeholder text: '{line_edit.placeholderText()}'")

    def get_input_data(self):
        """Retrieve data from all input fields."""
        return {field: line_edit.text() for field, line_edit in self.fields.items()}

    def clear_fields(self):
        """Clear the text in all input fields without recreating them."""
        for field_name, line_edit in self.fields.items():
            line_edit.clear()  # Clear any existing text
            print(f"[DEBUG] Cleared field: {field_name}, current text: '{line_edit.text()}'")














class UpdateBankDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Bank")
        self.setGeometry(200, 200, 500, 600)

        # Create the grid layout
        self.layout = QGridLayout(self)

        # Define input fields
        self.fields = {}
        self.add_input_field("l_bankno", "bankno", 0, 0)            # Matches l_bankno
        self.add_input_field("l_bankname", "Bank Name", 1, 0)   # Matches l_bankname
        self.add_input_field("l_branch", "Branch", 2, 0)       # Matches l_branch
        self.add_input_field("l_accountno_2", "Account Number", 3, 0)  # Matches l_accountno_2
        self.add_input_field("l_accountname", "Account Name", 4, 0)  # Matches l_accountname
        self.add_input_field("l_authority", "Authority", 5, 0)  # Matches l_authority
        self.add_input_field("l_phonenumber_2", "Phone Number", 6, 0)  # Matches l_phonenumber_2
        self.add_input_field("l_faxno", "Fax Number", 7, 0)    # Matches l_faxno
        self.add_input_field("l_ibanno", "IBAN Number", 8, 0)  # Matches l_ibanno
        self.add_input_field("l_web", "Website", 9, 0)         # Matches l_web


        # Buttons
        self.update_button = QPushButton("Update")
        self.cancel_button = QPushButton("Cancel")

        # Add buttons to the layout
        self.layout.addWidget(self.update_button, 10, 1)
        self.layout.addWidget(self.cancel_button, 10, 2)

        # Connect buttons
        self.update_button.clicked.connect(self.accept)  # Closes dialog and returns success
        self.cancel_button.clicked.connect(self.reject)  # Closes dialog without success

        # Clear all fields
        self.clear_fields()

    def add_input_field(self, field_name, label_text, row, col):
        """Helper method to add labeled input fields to the grid layout."""
        label = QLabel(label_text, self)
        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("")  # Ensure no placeholder text
        self.layout.addWidget(label, row, col)
        self.layout.addWidget(line_edit, row, col + 1)
        self.fields[field_name] = line_edit
        print(f"[DEBUG] Field {field_name} initialized with placeholder text: '{line_edit.placeholderText()}'")

    def get_input_data(self):
        """Retrieve data from all input fields."""
        return {field: line_edit.text() for field, line_edit in self.fields.items()}

    def clear_fields(self):
        """Clear the text in all input fields without recreating them."""
        for field_name, line_edit in self.fields.items():
            line_edit.clear()  # Clear any existing text
            print(f"[DEBUG] Cleared field: {field_name}, current text: '{line_edit.text()}'")


class UpdateUnitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Unit")
        self.setGeometry(200, 200, 500, 600)

        # Create the grid layout
        self.layout = QGridLayout(self)

        # Define input fields
        self.fields = {}
        self.add_input_field("household_no", "Household No", 0, 0)
        self.add_input_field("name", "Name", 1, 0)
        self.add_input_field("sin", "SIN", 2, 0)
        self.add_input_field("birth_date", "Birth Date", 3, 0)
        self.add_input_field("plate_no", "Number Plate", 4, 0)
        self.add_input_field("tax_no", "Tax Number", 5, 0)
        self.add_input_field("phone_number", "Phone Number", 6, 0)
        self.add_input_field("email", "Email", 7, 0)
        self.add_input_field("address", "Address", 8, 0)
        self.add_input_field("group_no", "Group No", 9, 0)
        self.add_input_field("account_no", "Account Number", 0, 2)
        self.add_input_field("account_note", "Account Note", 1, 2)
        self.add_input_field("receiver_no", "Receiver Account No", 2, 2)
        self.add_input_field("receiver_note", "Receiver Account Note", 3, 2)
        self.add_input_field("work_address", "Work Address", 4, 2)
        self.add_input_field("work_phone", "Work Phone Number", 5, 2)
        self.add_input_field("work_email", "Work Email", 6, 2)
        self.add_input_field("occupation", "Occupation", 7, 2)

        # Buttons
        self.update_button = QPushButton("Update")
        self.cancel_button = QPushButton("Cancel")

        # Add buttons to the layout
        self.layout.addWidget(self.update_button, 10, 1)
        self.layout.addWidget(self.cancel_button, 10, 2)

        # Connect buttons
        self.update_button.clicked.connect(self.accept)  # Closes dialog and returns success
        self.cancel_button.clicked.connect(self.reject)  # Closes dialog without success

        # Clear all fields
        self.clear_fields()

    def add_input_field(self, field_name, label_text, row, col):
        """Helper method to add labeled input fields to the grid layout."""
        label = QLabel(label_text, self)
        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("")  # Ensure no placeholder text
        self.layout.addWidget(label, row, col)
        self.layout.addWidget(line_edit, row, col + 1)
        self.fields[field_name] = line_edit
        print(f"[DEBUG] Field {field_name} placeholder text: '{line_edit.placeholderText()}'")

    def get_input_data(self):
        """Retrieve data from all input fields."""
        return {field: line_edit.text() for field, line_edit in self.fields.items()}

    def clear_fields(self):
        """Clear the text in all input fields without recreating them."""
        for field_name, line_edit in self.fields.items():
            line_edit.clear()  # Clear any existing text
            print(f"[DEBUG] Cleared field: {field_name}, current text: '{line_edit.text()}'")



class DeleteTurnoversDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete Turnover")
        self.setGeometry(200, 200, 300, 100)

        # Group Code input field
        self.group_code_input = QLineEdit(self)
        self.group_code_input.setPlaceholderText("Enter Turnover Group Code")
        self.group_code_input.setGeometry(50, 20, 200, 30)

        # Buttons
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setGeometry(50, 60, 100, 30)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setGeometry(160, 60, 100, 30)

        # Connect buttons
        self.delete_button.clicked.connect(self.accept)  # Closes dialog and returns success
        self.cancel_button.clicked.connect(self.reject)  # Closes dialog without success

    @property
    def group_code(self):
        """Retrieve the Group Code entered in the dialog."""
        return self.group_code_input.text().strip()


class DeleteBankDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Ensure no recursive calls
        self.setWindowTitle("Delete Bank")
        self.setGeometry(200, 200, 300, 100)

        # SIN input field
        self.social_security_number_input = QLineEdit(self)
        self.social_security_number_input.setPlaceholderText("Enter Bank SIN")
        self.social_security_number_input.setGeometry(50, 20, 200, 30)

        # Buttons
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setGeometry(50, 60, 100, 30)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setGeometry(160, 60, 100, 30)

        # Connect buttons
        self.delete_button.clicked.connect(self.accept)  # Closes dialog and returns success
        self.cancel_button.clicked.connect(self.reject)  # Closes dialog without success

    @property
    def sin(self):
        """Retrieve the SIN entered in the dialog."""
        return self.social_security_number_input.text().strip()




class DeleteUnitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Make sure this does not call itself recursively
        self.setWindowTitle("Delete Unit")
        self.setGeometry(200, 200, 300, 100)

        # SIN input field
        self.social_security_number_input = QLineEdit(self)
        self.social_security_number_input.setPlaceholderText("Enter SIN")
        self.social_security_number_input.setGeometry(50, 20, 200, 30)

        # Buttons
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setGeometry(50, 60, 100, 30)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setGeometry(160, 60, 100, 30)

        # Connect buttons
        self.delete_button.clicked.connect(self.accept)  # Closes dialog and returns success
        self.cancel_button.clicked.connect(self.reject)  # Closes dialog without success

    @property
    def sin(self):
        return self.social_security_number_input.text()






class Ui_MainWindow(object):
    
    def __init__(self, master_controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master_controller = master_controller
    
    def prompt_for_household_no(self):
        """Prompt the user to enter the Household No (unit_id)."""
        household_no, ok = QInputDialog.getText(self.centralwidget, "Enter Household No", "Household No:")
        if ok and household_no.strip():
            return household_no.strip()
        return None
    
    def prompt_for_bank_no(self):
        """Prompt the user to enter the Household No (patient_id)."""
        household_no, ok = QInputDialog.getText(self.centralwidget, "Enter Bank No", "Bank No:")
        if ok and household_no.strip():
            return household_no.strip()
        return None
   
    def prompt_for_turnover_no(self):
        """Prompt the user to enter the Turnover Number."""
        turnover_no, ok = QInputDialog.getText(self.centralwidget, "Enter Turnover Number", "Turnover Number:")
        if ok and turnover_no.strip():
            return turnover_no.strip()
        return None
    
    def handle_add_turnover(self):
        # Retrieve data from UI
        gruop_code = self.l_groupcode.text()       # Group Code (l_groupcode)
        turnover = self.l_turnoverno.text()                  # Turnover Code (l_code)
        company_name = self.l_companyname.text()   # Company Name (l_companyname)
        authority = self.l_authority_2.text()      # Authority (l_authority_2)
        bank_name = self.l_bankname_2.text()       # Bank Name (l_bankname_2)
        taxno = self.l_bankname_3.text()           # Tax Number (l_bankname_3)
        taxplace = self.l_bankname_4.text()        # Tax Place (l_bankname_4)
        iban = self.l_bankname_6.text()            # IBAN (l_bankname_6)
        address = self.l_bankname_5.text()         # Address (l_bankname_5)
        phonenumber = self.l_bankname_7.text()     # Phone Number (l_bankname_7)
        email = self.l_bankname_8.text()           # Email (l_bankname_8)
        web = self.l_email_2.text()                # Website (l_email_2)

        print(f"[DEBUG] Adding Turnover with the following details:")
        print(f"  Group Code: {gruop_code}")
        print(f"  Turnover Code: {turnover}")
        print(f"  Company Name: {company_name}")
        print(f"  Authority: {authority}")
        print(f"  Bank Name: {bank_name}")
        print(f"  Tax Number: {taxno}")
        print(f"  Tax Place: {taxplace}")
        print(f"  IBAN: {iban}")
        print(f"  Address: {address}")
        print(f"  Phone Number: {phonenumber}")
        print(f"  Email: {email}")
        print(f"  Website: {web}")

        # Validation
        if not gruop_code or not company_name or not turnover:
            QMessageBox.warning(None, "Input Error", "SIN, Company Name, and Code are required.")
            return

        try:
            # Call the controller's create_turnover method
            self.turnovers_controller.turnover_dao.create_patient(
                gruop_code, turnover, company_name, authority, bank_name,
                taxno, taxplace, iban, address, phonenumber, email, web
            )
            QMessageBox.information(None, "Success", f"Turnover '{company_name}' added successfully!")
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to add turnover: {str(e)}")
            
            
    
    def handle_add_bank(self):
        # Retrieve data from UI
        social_security_number = self.l_bankno.text()
        bank_name = self.l_bankname.text()
        branch = self.l_branch.text()
        account_no = self.l_accountno_2.text()
        account_name = self.l_accountname.text()
        authority = self.l_authority.text()
        phonenumber = self.l_phonenumber_2.text()
        faxno = self.l_faxno.text()
        ibanno = self.l_ibanno.text()
        web = self.l_web.text()

        print(f"Adding Bank: SIN={social_security_number}, Bank Name={bank_name}, Branch={branch}, Account No={account_no}, Phone={phonenumber}")

        # Validation
        if not social_security_number or not bank_name or not account_no:
            QMessageBox.warning(None, "Input Error", "SIN, Bank Name, and Account Number are required.")
            return

        try:
            # Call the controller's create_bank method
            self.bank_controller.create_patient(
                social_security_number, bank_name, branch, account_no, account_name, authority,
                phonenumber, faxno, ibanno, web
            )
            QMessageBox.information(None, "Success", f"Bank '{bank_name}' added successfully!")
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to add bank: {str(e)}")

        
    def handle_add_unit(self):
        household_no = self.l_householdno.text()
        name = self.l_name.text()
        sin = self.l_sin.text()
        birth_date = self.l_bday.text()
        plate_no = self.l_plateno.text()
        tax_no = self.l_taxno.text()
        phone_number = self.l_phonenumber.text()
        email = self.l_email.text()
        address = self.l_address.text()
        group_no = self.l_groupno.text()
        account_no = self.l_accountno.text()
        account_note = self.l_accountnote.text()
        receiver_no = self.l_receiverno.text()
        receiver_note = self.l_receivernote.text()
        work_address = self.l_workaddress.text()
        work_phone_number = self.l_workphonenumber.text()
        work_email = self.l_workemail.text()
        occupation = self.l_occupation.text()

        if not household_no or not name or not sin:
            QMessageBox.warning(None, "Input Error", "Household No, Name, and SIN are required.")
            return

        try:
            self.master_controller.unit_controller.unit_dao.create_unit(
                household_no, name, sin, birth_date, plate_no, tax_no,
                phone_number, email, address, group_no, account_no,
                account_note, receiver_no, receiver_note, work_address,
                work_phone_number, work_email, occupation
            )
            QMessageBox.information(None, "Success", f"Unit '{name}' added successfully!")
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to add unit: {str(e)}")





    def open_delete_bank_dialog(self):
        """Open a dialog to confirm and delete a bank by SIN."""
        dialog = DeleteBankDialog(self.centralwidget)  # Use the central widget or any valid QWidget as the parent
        if dialog.exec():  # Shows the dialog as a modal and waits for user interaction
            sin = dialog.sin.strip()  # Get and clean SIN input
            print(f"[DEBUG] SIN entered for deletion: {sin}")
            if not sin:
                QMessageBox.warning(self.centralwidget, "Input Error", "SIN cannot be empty.")
                return

            try:
                # Attempt to delete the bank
                success = self.bank_controller.delete_patient(sin)
                if success:
                    QMessageBox.information(self.centralwidget, "Success", f"Bank with SIN {sin} deleted successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Delete Failed", f"No bank found with SIN {sin}.")
                    print(f"[DEBUG] SIN {sin} could not be found.")
            except Exception as e:
                QMessageBox.critical(self.centralwidget, "Error", f"Failed to delete bank: {str(e)}")
                print(f"[DEBUG] Exception during deletion: {e}")

                    
                    
                    

    def open_delete_unit_dialog(self):
        """Open a dialog to confirm and delete a unit by SIN."""
        dialog = DeleteUnitDialog(self.centralwidget)  # Use central widget as the parent
        if dialog.exec():  # Show modal dialog
            sin = dialog.sin.strip()  # Get and clean SIN input
            print(f"[DEBUG] SIN entered for deletion: {sin}")
            
            if not sin:
                QMessageBox.warning(self.centralwidget, "Input Error", "SIN cannot be empty.")
                return

            try:
                # Attempt to delete the unit via MasterController
                success = self.master_controller.delete_unit(sin)
                if success:
                    QMessageBox.information(self.centralwidget, "Success", f"Unit with SIN {sin} deleted successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Delete Failed", f"No unit found with SIN {sin}.")
                    print(f"[DEBUG] SIN {sin} could not be found.")
            except Exception as e:
                QMessageBox.critical(self.centralwidget, "Error", f"Failed to delete unit: {str(e)}")
                print(f"[DEBUG] Exception during deletion: {e}")
                
                
    def open_delete_turnovers_dialog(self):
            """Open a dialog to confirm and delete a unit by SIN."""
            dialog = DeleteTurnoversDialog(self.centralwidget)  # Use the central widget or any valid QWidget as the parent
            if dialog.exec():  # Shows the dialog as a modal and waits for user interaction
                sin = dialog.sin.strip()  # Get and clean SIN input
                print(f"[DEBUG] SIN entered for deletion: {sin}")
                if not sin:
                    QMessageBox.warning(self.centralwidget, "Input Error", "SIN cannot be empty.")
                    return

                try:
                    # Attempt to delete the unit
                    success = self.turnovers_controller.delete_patient(sin)
                    if success:
                        QMessageBox.information(self.centralwidget, "Success", f"Unit with SIN {sin} deleted successfully!")
                    else:
                        QMessageBox.warning(self.centralwidget, "Delete Failed", f"No unit found with SIN {sin}.")
                        print(f"[DEBUG] SIN {sin} could not be found.")
                except Exception as e:
                    QMessageBox.critical(self.centralwidget, "Error", f"Failed to delete unit: {str(e)}")
                    print(f"[DEBUG] Exception during deletion: {e}")

    def handle_update_turnover(self):
        try:
            # Step 1: Prompt for Turnover Group Code
            group_code = self.prompt_for_turnover_no()
            if not group_code:
                QMessageBox.warning(self.centralwidget, "Input Error", "Turnover Group Code is required to update.")
                return

            # Step 2: Search for the turnover
            turnover = self.turnovers_controller.search_patient(group_code)
            if not turnover:
                QMessageBox.warning(self.centralwidget, "Not Found", f"No turnover found with Group Code: {group_code}.")
                return

            # Step 3: Create and Show Update Dialog
            dialog = UpdateTurnoversDialog(self.centralwidget)  # Use self.centralwidget as parent
            dialog.clear_fields()  # Ensure fields are cleared

            # Step 5: Handle User Input
            if dialog.exec():  # User clicked "Update"
                updated_data = dialog.get_input_data()
                print("[DEBUG] Updated Data from Dialog:", updated_data)

                # Map updated data to match the expected GUI field names
                mapped_data = {
                    "group_code": updated_data.get("l_groupcode"),  # GUI name: l_groupcode
                    "code": updated_data.get("l_code"),            # GUI name: l_code
                    "company_name": updated_data.get("l_companyname"),  # GUI name: l_companyname
                    "authority": updated_data.get("l_authority_2"),    # GUI name: l_authority_2
                    "bank_name": updated_data.get("l_bankname_2"),    # GUI name: l_bankname_2
                    "taxno": updated_data.get("l_bankname_3"),        # GUI name: l_bankname_3
                    "taxplace": updated_data.get("l_bankname_4"),     # GUI name: l_bankname_4
                    "iban": updated_data.get("l_bankname_6"),         # GUI name: l_bankname_6
                    "address": updated_data.get("l_bankname_5"),      # GUI name: l_bankname_5
                    "phonenumber": updated_data.get("l_bankname_7"),  # GUI name: l_bankname_7
                    "email": updated_data.get("l_bankname_8"),            # GUI name: l_emaill
                    "web": updated_data.get("l_email_2"),                # GUI name: l_webb
                }
                print("[DEBUG] Mapped Data for Update:", mapped_data)

                # Step 6: Call the DAO's update method
                success = self.turnovers_controller.update_patient(patient_id=group_code, **mapped_data)

                if success:
                    QMessageBox.information(self.centralwidget, "Success", "Turnover updated successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Update Failed", "Failed to update turnover.")
        except Exception as e:
            QMessageBox.critical(self.centralwidget, "Error", f"Failed to update turnover: {str(e)}")


    def handle_update_bank(self):
        try:
            # Step 1: Prompt for Bank SIN
            bank_no = self.prompt_for_bank_no()
            if not bank_no:
                QMessageBox.warning(self.centralwidget, "Input Error", "Bank SIN is required to update a bank.")
                return

            # Step 2: Search for the bank
            bank = self.bank_controller.search_patient(bank_no)
            if not bank:
                QMessageBox.warning(self.centralwidget, "Not Found", f"No bank found with SIN: {bank_no}.")
                return

            # Step 3: Create and Show Update Dialog
            dialog = UpdateBankDialog(self.centralwidget)  # Use self.centralwidget as parent
            dialog.clear_fields()  # Ensure fields are cleared

            # Step 4: Handle User Input
            if dialog.exec():  # User clicked "Update"
                updated_data = dialog.get_input_data()
                print("[DEBUG] Updated Data:", updated_data)

                # Map updated data to match the expected field names
                mapped_data = {
                    "bankno": updated_data.get("l_bankno"),
                    "bank_name": updated_data.get("l_bankname"),
                    "branch": updated_data.get("l_branch"),
                    "account_no": updated_data.get("l_accountno_2"),
                    "account_name": updated_data.get("l_accountname"),
                    "authority": updated_data.get("l_authority"),
                    "phonenumber": updated_data.get("l_phonenumber_2"),
                    "faxno": updated_data.get("l_faxno"),
                    "ibanno": updated_data.get("l_ibanno"),
                    "web": updated_data.get("l_web"),
                }
                print("[DEBUG] Mapped Data for Update:", mapped_data)

                # Call the DAO's update method
                success = self.bank_controller.update_patient(patient_id=bank_no, **mapped_data)

                if success:
                    QMessageBox.information(self.centralwidget, "Success", "Bank updated successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Update Failed", "Failed to update bank.")
        except Exception as e:
            QMessageBox.critical(self.centralwidget, "Error", f"Failed to update bank: {str(e)}")




    def handle_update_unit(self):
        """Handles updating an existing unit."""
        try:
            # Step 1: Prompt for Household No
            household_no = self.prompt_for_household_no()
            if not household_no:
                QMessageBox.warning(self.centralwidget, "Input Error", "Household No is required to update a unit.")
                return

            # Step 2: Search for the unit using MasterController
            unit = self.master_controller.search_unit(household_no)
            if not unit:
                QMessageBox.warning(self.centralwidget, "Not Found", f"No unit found with Household No: {household_no}.")
                return

            # Step 3: Create and Show Update Dialog
            dialog = UpdateUnitDialog(self.centralwidget)  # Use self.centralwidget as parent
            dialog.clear_fields()  # Ensure fields are cleared

            # Pre-fill fields with current data (optional)
            for field, line_edit in dialog.fields.items():
                if hasattr(unit, field) and getattr(unit, field):
                    line_edit.setText(str(getattr(unit, field)))  # Populate only if the attribute exists

            # Step 4: Handle User Input
            if dialog.exec():  # User clicked "Update"
                updated_data = dialog.get_input_data()
                print("[DEBUG] Updated Data:", updated_data)

                # Call MasterController's update method
                success = self.master_controller.update_unit(
                    unit_id=household_no,
                    social_security_number=updated_data["sin"],
                    name=updated_data["name"],
                    sin=updated_data["sin"],
                    birth_date=updated_data["birth_date"],
                    plate_no=updated_data["plate_no"],
                    tax_no=updated_data["tax_no"],
                    phone_number=updated_data["phone_number"],
                    email=updated_data["email"],
                    address=updated_data["address"],
                    group_no=updated_data["group_no"],
                    account_no=updated_data["account_no"],
                    account_note=updated_data["account_note"],
                    receiver_no=updated_data["receiver_no"],
                    receiver_note=updated_data["receiver_note"],
                    work_address=updated_data["work_address"],
                    work_phone_number=updated_data["work_phone_number"],
                    work_email=updated_data["work_email"],
                    occupation=updated_data["occupation"],
                )

                if success:
                    QMessageBox.information(self.centralwidget, "Success", "Unit updated successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Update Failed", "Failed to update unit.")
        except Exception as e:
            QMessageBox.critical(self.centralwidget, "Error", f"Failed to update unit: {str(e)}")

    def open_update_bank_dialog(self):
        dialog = UpdateUnitDialog(self.centralwidget)
        if dialog.exec():
            updated_data = dialog.get_input_data()
            print("[DEBUG] Updated Data:", updated_data)

            try:
                # Call the update method in your controller/DAO
                success = self.bank_controller.update_patient(**updated_data)
                if success:
                    QMessageBox.information(self, "Success", "Unit updated successfully!")
                else:
                    QMessageBox.warning(self, "Update Failed", "Failed to update bank.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update bank: {str(e)}")
            
    def open_update_unit_dialog(self):
        """Opens the update dialog and updates unit data via MasterController."""
        dialog = UpdateUnitDialog(self.centralwidget)  
        if dialog.exec():
            updated_data = dialog.get_input_data()
            print("[DEBUG] Updated Data:", updated_data)

            try:
                # Call MasterController's update method
                success = self.master_controller.update_unit(**updated_data)
                if success:
                    QMessageBox.information(self, "Success", "Unit updated successfully!")
                else:
                    QMessageBox.warning(self, "Update Failed", "Failed to update unit.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update unit: {str(e)}")

                
                
            
    
    
    def open_delete_turnover_dialog(self):
        """Open a dialog to confirm and delete a turnover by SIN."""
        dialog = DeleteTurnoversDialog(self.centralwidget)  # Use the central widget or any valid QWidget as the parent
        if dialog.exec():  # Shows the dialog as a modal and waits for user interaction
            group_code = dialog.group_code.strip()  # Get and clean SIN input
            print(f"[DEBUG] SIN entered for deletion: {group_code}")
            if not group_code:
                QMessageBox.warning(self.centralwidget, "Input Error", "SIN cannot be empty.")
                return

            try:
                # Attempt to delete the turnover
                success = self.turnovers_controller.delete_patient(group_code)
                if success:
                    QMessageBox.information(self.centralwidget, "Success", f"Turnover with SIN {group_code} deleted successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Delete Failed", f"No turnover found with SIN {group_code}.")
                    print(f"[DEBUG] SIN {group_code} could not be found.")
            except Exception as e:
                QMessageBox.critical(self.centralwidget, "Error", f"Failed to delete turnover: {str(e)}")
                print(f"[DEBUG] Exception during deletion: {e}")






    def handle_delete_bank(self):
        try:
            social_security_number = self.l_sin.text()

            # Validate required field
            if not social_security_number:
                QMessageBox.warning(self, "Input Error", "SIN is required to delete a bank.")
                return

            # Confirm deletion
            reply = QMessageBox.question(
                self,
                "Confirm Deletion",
                f"Are you sure you want to delete the bank with SIN {social_security_number}?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                success = self.bank_controller.delete_patient(social_security_number)
                if success:
                    QMessageBox.information(self, "Success", "Bank deleted successfully!")
                    self.clear_form()  # Optionally clear the form after deletion
                else:
                    QMessageBox.warning(self, "Delete Failed", "Failed to delete bank.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete bank: {str(e)}")

    
            
    def handle_delete_unit(self):
        """Deletes a unit by SIN using MasterController."""
        try:
            social_security_number = self.l_sin.text()

            # Validate required field
            if not social_security_number:
                QMessageBox.warning(self, "Input Error", "SIN is required to delete a unit.")
                return

            # Confirm deletion
            reply = QMessageBox.question(
                self,
                "Confirm Deletion",
                f"Are you sure you want to delete the unit with SIN {social_security_number}?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                success = self.master_controller.delete_unit(social_security_number)
                if success:
                    QMessageBox.information(self, "Success", "Unit deleted successfully!")
                    self.clear_form()  # Optionally clear the form after deletion
                else:
                    QMessageBox.warning(self, "Delete Failed", "Failed to delete unit.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete unit: {str(e)}")


    def clear_form(self):
        # Clear all input fields for Unit
        self.l_householdno.clear()
        self.l_name.clear()
        self.l_sin.clear()
        self.l_bday.clear()
        self.l_plateno.clear()
        self.l_taxno.clear()
        self.l_phonenumber.clear()
        self.l_email.clear()
        self.l_address.clear()
        self.l_groupno.clear()
        self.l_accountno.clear()
        self.l_accountnote.clear()
        self.l_receiverno.clear()
        self.l_receivernote.clear()
        self.l_workaddress.clear()
        self.l_workphonenumber.clear()
        self.l_workemail.clear()
        self.l_occupation.clear()

        # Clear all input fields for Bank
        self.l_bankno.clear()
        self.l_bankname.clear()
        self.l_branch.clear()
        self.l_accountno_2.clear()
        self.l_accountname.clear()
        self.l_authority.clear()
        self.l_phonenumber_2.clear()
        self.l_faxno.clear()
        self.l_ibanno.clear()
        self.l_web.clear()

        # Clear all input fields for Turnover
        self.l_turnoverno.clear()
        self.l_code.clear()
        self.l_company_name.clear()
        self.l_turnover_authority.clear()
        self.l_turnover_bank_name.clear()
        self.l_turnover_taxno.clear()
        self.l_turnover_taxplace.clear()
        self.l_turnover_iban.clear()
        self.l_turnover_address.clear()
        self.l_turnover_phonenumber.clear()
        self.l_turnover_email.clear()
        self.l_turnover_web.clear()

        


        
      
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 596)
        self.actionRegistration = QAction(MainWindow)
        self.actionRegistration.setObjectName(u"actionRegistration")
        self.actionList = QAction(MainWindow)
        self.actionList.setObjectName(u"actionList")
        self.actionBulk_Loan = QAction(MainWindow)
        self.actionBulk_Loan.setObjectName(u"actionBulk_Loan")
        self.actionLoan_By_Square_Meter = QAction(MainWindow)
        self.actionLoan_By_Square_Meter.setObjectName(u"actionLoan_By_Square_Meter")
        self.actionLoan_By_Meters = QAction(MainWindow)
        self.actionLoan_By_Meters.setObjectName(u"actionLoan_By_Meters")
        self.actionLoan_Updating = QAction(MainWindow)
        self.actionLoan_Updating.setObjectName(u"actionLoan_Updating")
        self.actionFast_Pay = QAction(MainWindow)
        self.actionFast_Pay.setObjectName(u"actionFast_Pay")
        self.actionBulk_Pay = QAction(MainWindow)
        self.actionBulk_Pay.setObjectName(u"actionBulk_Pay")
        self.actionTemporary_Account = QAction(MainWindow)
        self.actionTemporary_Account.setObjectName(u"actionTemporary_Account")
        self.actionBulk_Collection_Update = QAction(MainWindow)
        self.actionBulk_Collection_Update.setObjectName(u"actionBulk_Collection_Update")
        self.actionTurnovers = QAction(MainWindow)
        self.actionTurnovers.setObjectName(u"actionTurnovers")
        self.actionFollow_Turnovers = QAction(MainWindow)
        self.actionFollow_Turnovers.setObjectName(u"actionFollow_Turnovers")
        self.actionTransactions = QAction(MainWindow)
        self.actionTransactions.setObjectName(u"actionTransactions")
        self.actionExtract = QAction(MainWindow)
        self.actionExtract.setObjectName(u"actionExtract")
        self.actionCollection_System = QAction(MainWindow)
        self.actionCollection_System.setObjectName(u"actionCollection_System")
        self.actionR1 = QAction(MainWindow)
        self.actionR1.setObjectName(u"actionR1")
        self.actionR2 = QAction(MainWindow)
        self.actionR2.setObjectName(u"actionR2")
        self.actionR3 = QAction(MainWindow)
        self.actionR3.setObjectName(u"actionR3")
        self.actionR4 = QAction(MainWindow)
        self.actionR4.setObjectName(u"actionR4")
        self.actionR5 = QAction(MainWindow)
        self.actionR5.setObjectName(u"actionR5")
        self.actionR6 = QAction(MainWindow)
        self.actionR6.setObjectName(u"actionR6")
        self.actionR7 = QAction(MainWindow)
        self.actionR7.setObjectName(u"actionR7")
        self.actionR8 = QAction(MainWindow)
        self.actionR8.setObjectName(u"actionR8")
        self.actionR9 = QAction(MainWindow)
        self.actionR9.setObjectName(u"actionR9")
        self.actionR10 = QAction(MainWindow)
        self.actionR10.setObjectName(u"actionR10")
        self.actionR11 = QAction(MainWindow)
        self.actionR11.setObjectName(u"actionR11")
        self.actionR12 = QAction(MainWindow)
        self.actionR12.setObjectName(u"actionR12")
        self.actionR13 = QAction(MainWindow)
        self.actionR13.setObjectName(u"actionR13")
        self.actionR14 = QAction(MainWindow)
        self.actionR14.setObjectName(u"actionR14")
        self.actionR15 = QAction(MainWindow)
        self.actionR15.setObjectName(u"actionR15")
        self.actionR16 = QAction(MainWindow)
        self.actionR16.setObjectName(u"actionR16")
        self.actionR17 = QAction(MainWindow)
        self.actionR17.setObjectName(u"actionR17")
        self.actionR18 = QAction(MainWindow)
        self.actionR18.setObjectName(u"actionR18")
        self.actionLogs = QAction(MainWindow)
        self.actionLogs.setObjectName(u"actionLogs")
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(u"actionRemove")
        self.actionHousehold_Update = QAction(MainWindow)
        self.actionHousehold_Update.setObjectName(u"actionHousehold_Update")
        self.actionLandlord_Tenant_Match = QAction(MainWindow)
        self.actionLandlord_Tenant_Match.setObjectName(u"actionLandlord_Tenant_Match")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_pages = QFrame(self.centralwidget)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setGeometry(QRect(160, 90, 781, 431))
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 781, 431))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayoutWidget_2 = QWidget(self.page1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 0, 121, 371))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        
        self.householdno = QLineEdit(self.verticalLayoutWidget_2)
        self.householdno.setObjectName(u"householdno")
        self.householdno.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.householdno)

        self.name = QLineEdit(self.verticalLayoutWidget_2)
        self.name.setObjectName(u"name")
        self.name.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.name)

        self.sin = QLineEdit(self.verticalLayoutWidget_2)
        self.sin.setObjectName(u"sin")
        self.sin.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.sin)

        self.bday = QLineEdit(self.verticalLayoutWidget_2)
        self.bday.setObjectName(u"bday")
        self.bday.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.bday)

        self.plateno = QLineEdit(self.verticalLayoutWidget_2)
        self.plateno.setObjectName(u"plateno")
        self.plateno.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plateno)

        self.taxno = QLineEdit(self.verticalLayoutWidget_2)
        self.taxno.setObjectName(u"taxno")
        self.taxno.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.taxno)

        self.phonenumber = QLineEdit(self.verticalLayoutWidget_2)
        self.phonenumber.setObjectName(u"phonenumber")
        self.phonenumber.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.phonenumber)

        self.email = QLineEdit(self.verticalLayoutWidget_2)
        self.email.setObjectName(u"email")
        self.email.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.email)

        self.address = QLineEdit(self.verticalLayoutWidget_2)
        self.address.setObjectName(u"address")
        self.address.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.address)

        self.groupno = QLineEdit(self.verticalLayoutWidget_2)
        self.groupno.setObjectName(u"groupno")
        self.groupno.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.groupno)

        self.verticalLayoutWidget_3 = QWidget(self.page1)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(150, 0, 221, 371))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.l_householdno = QLineEdit(self.verticalLayoutWidget_3)
        self.l_householdno.setObjectName(u"l_householdno")

        self.verticalLayout_3.addWidget(self.l_householdno)

        self.l_name = QLineEdit(self.verticalLayoutWidget_3)
        self.l_name.setObjectName(u"l_name")

        self.verticalLayout_3.addWidget(self.l_name)

        self.l_sin = QLineEdit(self.verticalLayoutWidget_3)
        self.l_sin.setObjectName(u"l_sin")

        self.verticalLayout_3.addWidget(self.l_sin)

        self.l_bday = QLineEdit(self.verticalLayoutWidget_3)
        self.l_bday.setObjectName(u"l_bday")

        self.verticalLayout_3.addWidget(self.l_bday)

        self.l_plateno = QLineEdit(self.verticalLayoutWidget_3)
        self.l_plateno.setObjectName(u"l_plateno")

        self.verticalLayout_3.addWidget(self.l_plateno)

        self.l_taxno = QLineEdit(self.verticalLayoutWidget_3)
        self.l_taxno.setObjectName(u"l_taxno")

        self.verticalLayout_3.addWidget(self.l_taxno)

        self.l_phonenumber = QLineEdit(self.verticalLayoutWidget_3)
        self.l_phonenumber.setObjectName(u"l_phonenumber")

        self.verticalLayout_3.addWidget(self.l_phonenumber)

        self.l_email = QLineEdit(self.verticalLayoutWidget_3)
        self.l_email.setObjectName(u"l_email")

        self.verticalLayout_3.addWidget(self.l_email)

        self.l_address = QLineEdit(self.verticalLayoutWidget_3)
        self.l_address.setObjectName(u"l_address")

        self.verticalLayout_3.addWidget(self.l_address)

        self.l_groupno = QLineEdit(self.verticalLayoutWidget_3)
        self.l_groupno.setObjectName(u"l_groupno")

        self.verticalLayout_3.addWidget(self.l_groupno)

        self.verticalLayoutWidget_4 = QWidget(self.page1)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(430, 0, 131, 371))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.accountno = QLineEdit(self.verticalLayoutWidget_4)
        self.accountno.setObjectName(u"accountno")
        self.accountno.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.accountno)

        self.accountnote = QLineEdit(self.verticalLayoutWidget_4)
        self.accountnote.setObjectName(u"accountnote")
        self.accountnote.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.accountnote)

        self.receiverno = QLineEdit(self.verticalLayoutWidget_4)
        self.receiverno.setObjectName(u"receiverno")
        self.receiverno.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.receiverno)

        self.receivernote = QLineEdit(self.verticalLayoutWidget_4)
        self.receivernote.setObjectName(u"receivernote")
        self.receivernote.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.receivernote)

        self.workaddress = QLineEdit(self.verticalLayoutWidget_4)
        self.workaddress.setObjectName(u"workaddress")
        self.workaddress.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.workaddress)

        self.workphonenumber = QLineEdit(self.verticalLayoutWidget_4)
        self.workphonenumber.setObjectName(u"workphonenumber")
        self.workphonenumber.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.workphonenumber)

        self.workemail = QLineEdit(self.verticalLayoutWidget_4)
        self.workemail.setObjectName(u"workemail")
        self.workemail.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.workemail)

        self.occupation = QLineEdit(self.verticalLayoutWidget_4)
        self.occupation.setObjectName(u"occupation")
        self.occupation.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.occupation)

        self.verticalLayoutWidget_5 = QWidget(self.page1)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(570, 0, 191, 371))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.l_accountno = QLineEdit(self.verticalLayoutWidget_5)
        self.l_accountno.setObjectName(u"l_accountno")

        self.verticalLayout_8.addWidget(self.l_accountno)

        self.l_accountnote = QLineEdit(self.verticalLayoutWidget_5)
        self.l_accountnote.setObjectName(u"l_accountnote")

        self.verticalLayout_8.addWidget(self.l_accountnote)

        self.l_receiverno = QLineEdit(self.verticalLayoutWidget_5)
        self.l_receiverno.setObjectName(u"l_receiverno")

        self.verticalLayout_8.addWidget(self.l_receiverno)

        self.l_receivernote = QLineEdit(self.verticalLayoutWidget_5)
        self.l_receivernote.setObjectName(u"l_receivernote")

        self.verticalLayout_8.addWidget(self.l_receivernote)

        self.l_workaddress = QLineEdit(self.verticalLayoutWidget_5)
        self.l_workaddress.setObjectName(u"l_workaddress")

        self.verticalLayout_8.addWidget(self.l_workaddress)

        self.l_workphonenumber = QLineEdit(self.verticalLayoutWidget_5)
        self.l_workphonenumber.setObjectName(u"l_workphonenumber")

        self.verticalLayout_8.addWidget(self.l_workphonenumber)

        self.l_workemail = QLineEdit(self.verticalLayoutWidget_5)
        self.l_workemail.setObjectName(u"l_workemail")

        self.verticalLayout_8.addWidget(self.l_workemail)

        self.l_occupation = QLineEdit(self.verticalLayoutWidget_5)
        self.l_occupation.setObjectName(u"l_occupation")

        self.verticalLayout_8.addWidget(self.l_occupation)

        self.horizontalLayoutWidget_2 = QWidget(self.page1)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(140, 380, 631, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add = QPushButton(self.horizontalLayoutWidget_2)
        self.add.setObjectName(u"add")

        self.horizontalLayout_2.addWidget(self.add)

        self.clear_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.clear_2.setObjectName(u"clear_2")

        self.horizontalLayout_2.addWidget(self.clear_2)

        self.update = QPushButton(self.horizontalLayoutWidget_2)
        self.update.setObjectName(u"update")

        self.horizontalLayout_2.addWidget(self.update)

        self.delete_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.delete_2.setObjectName(u"delete_2")

        self.horizontalLayout_2.addWidget(self.delete_2)
        
        self.add.clicked.connect(self.handle_add_unit)
        self.clear_2.clicked.connect(self.clear_form)
        self.update.clicked.connect(self.handle_update_unit)
        self.delete_2.clicked.connect(self.open_delete_unit_dialog)

        
        self.stackedWidget.addWidget(self.page1)



## Page 2 [Bank Register]

        
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayoutWidget_6 = QWidget(self.page2)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 101, 311))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bankno = QLineEdit(self.verticalLayoutWidget_6)
        self.bankno.setObjectName(u"bankno")
        self.bankno.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.bankno)

        self.bankname = QLineEdit(self.verticalLayoutWidget_6)
        self.bankname.setObjectName(u"bankname")
        self.bankname.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.bankname)

        self.branch = QLineEdit(self.verticalLayoutWidget_6)
        self.branch.setObjectName(u"branch")
        self.branch.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.branch)

        self.accountno_2 = QLineEdit(self.verticalLayoutWidget_6)
        self.accountno_2.setObjectName(u"accountno_2")
        self.accountno_2.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.accountno_2)

        self.accountname = QLineEdit(self.verticalLayoutWidget_6)
        self.accountname.setObjectName(u"accountname")
        self.accountname.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.accountname)

        self.authority = QLineEdit(self.verticalLayoutWidget_6)
        self.authority.setObjectName(u"authority")
        self.authority.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.authority)

        self.phonenumber_2 = QLineEdit(self.verticalLayoutWidget_6)
        self.phonenumber_2.setObjectName(u"phonenumber_2")
        self.phonenumber_2.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.phonenumber_2)

        self.faxno = QLineEdit(self.verticalLayoutWidget_6)
        self.faxno.setObjectName(u"faxno")
        self.faxno.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.faxno)

        self.ibanno = QLineEdit(self.verticalLayoutWidget_6)
        self.ibanno.setObjectName(u"ibanno")
        self.ibanno.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.ibanno)

        self.web = QLineEdit(self.verticalLayoutWidget_6)
        self.web.setObjectName(u"web")
        self.web.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.web)

        self.verticalLayoutWidget_7 = QWidget(self.page2)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(120, 10, 160, 311))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.l_bankno = QLineEdit(self.verticalLayoutWidget_7)
        self.l_bankno.setObjectName(u"l_bankno")

        self.verticalLayout_10.addWidget(self.l_bankno)

        self.l_bankname = QLineEdit(self.verticalLayoutWidget_7)
        self.l_bankname.setObjectName(u"l_bankname")

        self.verticalLayout_10.addWidget(self.l_bankname)

        self.l_branch = QLineEdit(self.verticalLayoutWidget_7)
        self.l_branch.setObjectName(u"l_branch")

        self.verticalLayout_10.addWidget(self.l_branch)

        self.l_accountno_2 = QLineEdit(self.verticalLayoutWidget_7)
        self.l_accountno_2.setObjectName(u"l_accountno_2")

        self.verticalLayout_10.addWidget(self.l_accountno_2)

        self.l_accountname = QLineEdit(self.verticalLayoutWidget_7)
        self.l_accountname.setObjectName(u"l_accountname")

        self.verticalLayout_10.addWidget(self.l_accountname)

        self.l_authority = QLineEdit(self.verticalLayoutWidget_7)
        self.l_authority.setObjectName(u"l_authority")

        self.verticalLayout_10.addWidget(self.l_authority)

        self.l_phonenumber_2 = QLineEdit(self.verticalLayoutWidget_7)
        self.l_phonenumber_2.setObjectName(u"l_phonenumber_2")

        self.verticalLayout_10.addWidget(self.l_phonenumber_2)

        self.l_faxno = QLineEdit(self.verticalLayoutWidget_7)
        self.l_faxno.setObjectName(u"l_faxno")

        self.verticalLayout_10.addWidget(self.l_faxno)

        self.l_ibanno = QLineEdit(self.verticalLayoutWidget_7)
        self.l_ibanno.setObjectName(u"l_ibanno")

        self.verticalLayout_10.addWidget(self.l_ibanno)

        self.l_web = QLineEdit(self.verticalLayoutWidget_7)
        self.l_web.setObjectName(u"l_web")

        self.verticalLayout_10.addWidget(self.l_web)

        self.gridLayoutWidget = QWidget(self.page2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(390, 330, 361, 82))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.balance = QLineEdit(self.gridLayoutWidget)
        self.balance.setObjectName(u"balance")
        self.balance.setReadOnly(True)

        self.gridLayout.addWidget(self.balance, 2, 0, 1, 1)

        self.income = QLineEdit(self.gridLayoutWidget)
        self.income.setObjectName(u"income")
        self.income.setReadOnly(True)

        self.gridLayout.addWidget(self.income, 0, 0, 1, 1)

        self.expense = QLineEdit(self.gridLayoutWidget)
        self.expense.setObjectName(u"expense")
        self.expense.setReadOnly(True)

        self.gridLayout.addWidget(self.expense, 1, 0, 1, 1)

        self.o_balance = QLineEdit(self.gridLayoutWidget)
        self.o_balance.setObjectName(u"o_balance")
        self.o_balance.setReadOnly(True)

        self.gridLayout.addWidget(self.o_balance, 2, 1, 1, 1)

        self.o_expense = QLineEdit(self.gridLayoutWidget)
        self.o_expense.setObjectName(u"o_expense")
        self.o_expense.setReadOnly(True)

        self.gridLayout.addWidget(self.o_expense, 1, 1, 1, 1)

        self.o_income = QLineEdit(self.gridLayoutWidget)
        self.o_income.setObjectName(u"o_income")
        self.o_income.setReadOnly(True)

        self.gridLayout.addWidget(self.o_income, 0, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.page2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(40, 340, 241, 100))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.transactions = QPushButton(self.gridLayoutWidget_2)
        self.transactions.setObjectName(u"transactions")

        self.gridLayout_2.addWidget(self.transactions, 2, 0, 1, 1)

        self.add_2 = QPushButton(self.gridLayoutWidget_2)
        self.add_2.setObjectName(u"add_2")

        self.gridLayout_2.addWidget(self.add_2, 0, 0, 1, 1)

        self.update_2 = QPushButton(self.gridLayoutWidget_2)
        self.update_2.setObjectName(u"update_2")

        self.gridLayout_2.addWidget(self.update_2, 1, 0, 1, 1)

        self.clear = QPushButton(self.gridLayoutWidget_2)
        self.clear.setObjectName(u"clear")

        self.gridLayout_2.addWidget(self.clear, 0, 1, 1, 1)

        self.delete_3 = QPushButton(self.gridLayoutWidget_2)
        self.delete_3.setObjectName(u"delete_3")

        self.gridLayout_2.addWidget(self.delete_3, 1, 1, 1, 1)

        self.extract = QPushButton(self.gridLayoutWidget_2)
        self.extract.setObjectName(u"extract")

        self.gridLayout_2.addWidget(self.extract, 2, 1, 1, 1)

        self.tableWidget_4 = QTableWidget(self.page2)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(350, 10, 411, 311))
        
        self.add_2.clicked.connect(self.handle_add_bank)
        self.clear.clicked.connect(self.clear_form)
        self.update_2.clicked.connect(self.handle_update_bank)
        self.delete_3.clicked.connect(self.open_delete_bank_dialog)
        
        
        
        self.stackedWidget.addWidget(self.page2)
        
        
        
        
        
        ## Page 3 [Income]
        
        
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.horizontalLayoutWidget_3 = QWidget(self.page3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 360, 804, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_3 = QPushButton(self.horizontalLayoutWidget_3)
        self.add_3.setObjectName(u"add_3")

        self.horizontalLayout_3.addWidget(self.add_3)

        self.delete_4 = QPushButton(self.horizontalLayoutWidget_3)
        self.delete_4.setObjectName(u"delete_4")

        self.horizontalLayout_3.addWidget(self.delete_4)

        self.filter = QPushButton(self.horizontalLayoutWidget_3)
        self.filter.setObjectName(u"filter")

        self.horizontalLayout_3.addWidget(self.filter)

        self.update_3 = QPushButton(self.horizontalLayoutWidget_3)
        self.update_3.setObjectName(u"update_3")

        self.horizontalLayout_3.addWidget(self.update_3)

        self.sort = QPushButton(self.horizontalLayoutWidget_3)
        self.sort.setObjectName(u"sort")

        self.horizontalLayout_3.addWidget(self.sort)

        self.import_2 = QPushButton(self.horizontalLayoutWidget_3)
        self.import_2.setObjectName(u"import_2")

        self.horizontalLayout_3.addWidget(self.import_2)

        self.transactions_2 = QPushButton(self.horizontalLayoutWidget_3)
        self.transactions_2.setObjectName(u"transactions_2")

        self.horizontalLayout_3.addWidget(self.transactions_2)

        self.print = QPushButton(self.horizontalLayoutWidget_3)
        self.print.setObjectName(u"print")

        self.horizontalLayout_3.addWidget(self.print)

        self.tableWidget_2 = QTableWidget(self.page3)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 30, 751, 311))
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.horizontalLayoutWidget_4 = QWidget(self.page4)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 360, 804, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.add_4 = QPushButton(self.horizontalLayoutWidget_4)
        self.add_4.setObjectName(u"add_4")

        self.horizontalLayout_4.addWidget(self.add_4)

        self.delete_5 = QPushButton(self.horizontalLayoutWidget_4)
        self.delete_5.setObjectName(u"delete_5")

        self.horizontalLayout_4.addWidget(self.delete_5)

        self.filter_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.filter_2.setObjectName(u"filter_2")

        self.horizontalLayout_4.addWidget(self.filter_2)

        self.update_4 = QPushButton(self.horizontalLayoutWidget_4)
        self.update_4.setObjectName(u"update_4")

        self.horizontalLayout_4.addWidget(self.update_4)

        self.sort_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.sort_2.setObjectName(u"sort_2")

        self.horizontalLayout_4.addWidget(self.sort_2)

        self.import_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.import_3.setObjectName(u"import_3")

        self.horizontalLayout_4.addWidget(self.import_3)

        self.transactions_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.transactions_3.setObjectName(u"transactions_3")

        self.horizontalLayout_4.addWidget(self.transactions_3)

        self.print_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.print_2.setObjectName(u"print_2")

        self.horizontalLayout_4.addWidget(self.print_2)

        self.tableWidget_3 = QTableWidget(self.page4)
        if (self.tableWidget_3.columnCount() < 9):
            self.tableWidget_3.setColumnCount(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 30, 751, 311))
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QWidget()
        
        
        
        
        ## Page 5 [Turnovers]
        self.page5.setObjectName(u"page5")
        self.verticalLayoutWidget_8 = QWidget(self.page5)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(20, 50, 91, 351))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.turnoverno = QLineEdit(self.verticalLayoutWidget_8)
        self.turnoverno.setObjectName(u"turnoverno")
        self.turnoverno.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.turnoverno)

        self.companyname = QLineEdit(self.verticalLayoutWidget_8)
        self.companyname.setObjectName(u"companyname")
        self.companyname.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.companyname)

        self.authority_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.authority_2.setObjectName(u"authority_2")
        self.authority_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.authority_2)

        self.bankname_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.bankname_2.setObjectName(u"bankname_2")
        self.bankname_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.bankname_2)

        self.taxno_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.taxno_2.setObjectName(u"taxno_2")
        self.taxno_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.taxno_2)

        self.taxplace = QLineEdit(self.verticalLayoutWidget_8)
        self.taxplace.setObjectName(u"taxplace")
        self.taxplace.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.taxplace)

        self.ibanno_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.ibanno_2.setObjectName(u"ibanno_2")
        self.ibanno_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.ibanno_2)

        self.address_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.address_2.setObjectName(u"address_2")
        self.address_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.address_2)

        self.phonenumber_3 = QLineEdit(self.verticalLayoutWidget_8)
        self.phonenumber_3.setObjectName(u"phonenumber_3")
        self.phonenumber_3.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.phonenumber_3)

        self.email_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.email_2)

        self.web_2 = QLineEdit(self.verticalLayoutWidget_8)
        self.web_2.setObjectName(u"web_2")
        self.web_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.web_2)

        self.verticalLayoutWidget_9 = QWidget(self.page5)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(120, 50, 206, 351))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.l_turnoverno = QLineEdit(self.verticalLayoutWidget_9)
        self.l_turnoverno.setObjectName(u"l_turnoverno")
        self.l_turnoverno.setReadOnly(False)
        
        self.verticalLayout_12.addWidget(self.l_turnoverno)

        self.l_companyname = QLineEdit(self.verticalLayoutWidget_9)
        self.l_companyname.setObjectName(u"l_companyname")

        self.verticalLayout_12.addWidget(self.l_companyname)

        self.l_authority_2 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_authority_2.setObjectName(u"l_authority_2")

        self.verticalLayout_12.addWidget(self.l_authority_2)

        self.l_bankname_2 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_2.setObjectName(u"l_bankname_2")

        self.verticalLayout_12.addWidget(self.l_bankname_2)

        self.l_bankname_3 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_3.setObjectName(u"l_bankname_3")

        self.verticalLayout_12.addWidget(self.l_bankname_3)

        self.l_bankname_4 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_4.setObjectName(u"l_bankname_4")

        self.verticalLayout_12.addWidget(self.l_bankname_4)

        self.l_bankname_6 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_6.setObjectName(u"l_bankname_6")

        self.verticalLayout_12.addWidget(self.l_bankname_6)

        self.l_bankname_5 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_5.setObjectName(u"l_bankname_5")

        self.verticalLayout_12.addWidget(self.l_bankname_5)

        self.l_bankname_7 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_7.setObjectName(u"l_bankname_7")

        self.verticalLayout_12.addWidget(self.l_bankname_7)

        self.l_bankname_8 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_bankname_8.setObjectName(u"l_bankname_8")
        self.l_bankname_8.setReadOnly(False)

        self.verticalLayout_12.addWidget(self.l_bankname_8)

        self.l_email_2 = QLineEdit(self.verticalLayoutWidget_9)
        self.l_email_2.setObjectName(u"l_email_2")

        self.verticalLayout_12.addWidget(self.l_email_2)

        self.groupcode = QLineEdit(self.page5)
        self.groupcode.setObjectName(u"groupcode")
        self.groupcode.setGeometry(QRect(20, 10, 89, 20))
        self.groupcode.setReadOnly(True)
        self.l_groupcode = QLineEdit(self.page5)
        self.l_groupcode.setObjectName(u"l_groupcode")
        self.l_groupcode.setGeometry(QRect(120, 10, 161, 22))
        self.gridLayoutWidget_3 = QWidget(self.page5)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(440, 210, 311, 82))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.balance_2 = QLineEdit(self.gridLayoutWidget_3)
        self.balance_2.setObjectName(u"balance_2")
        self.balance_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.balance_2, 2, 0, 1, 1)

        self.debt = QLineEdit(self.gridLayoutWidget_3)
        self.debt.setObjectName(u"debt")
        self.debt.setReadOnly(True)

        self.gridLayout_3.addWidget(self.debt, 0, 0, 1, 1)

        self.income_2 = QLineEdit(self.gridLayoutWidget_3)
        self.income_2.setObjectName(u"income_2")
        self.income_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.income_2, 1, 0, 1, 1)

        self.o_debt = QLineEdit(self.gridLayoutWidget_3)
        self.o_debt.setObjectName(u"o_debt")
        self.o_debt.setReadOnly(True)

        self.gridLayout_3.addWidget(self.o_debt, 0, 1, 1, 1)

        self.o_income_2 = QLineEdit(self.gridLayoutWidget_3)
        self.o_income_2.setObjectName(u"o_income_2")
        self.o_income_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.o_income_2, 1, 1, 1, 1)

        self.o_balance_2 = QLineEdit(self.gridLayoutWidget_3)
        self.o_balance_2.setObjectName(u"o_balance_2")
        self.o_balance_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.o_balance_2, 2, 1, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.page5)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(430, 300, 331, 135))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.add_5 = QPushButton(self.gridLayoutWidget_4)
        self.add_5.setObjectName(u"add_5")

        self.gridLayout_4.addWidget(self.add_5, 0, 0, 1, 1)

        self.update_5 = QPushButton(self.gridLayoutWidget_4)
        self.update_5.setObjectName(u"update_5")

        self.gridLayout_4.addWidget(self.update_5, 1, 0, 1, 1)

        self.delete_6 = QPushButton(self.gridLayoutWidget_4)
        self.delete_6.setObjectName(u"delete_6")

        self.gridLayout_4.addWidget(self.delete_6, 1, 1, 1, 1)

        self.clear_3 = QPushButton(self.gridLayoutWidget_4)
        self.clear_3.setObjectName(u"clear_3")

        self.gridLayout_4.addWidget(self.clear_3, 0, 1, 1, 1)

        self.search = QPushButton(self.gridLayoutWidget_4)
        self.search.setObjectName(u"search")

        self.gridLayout_4.addWidget(self.search, 2, 0, 1, 1)

        self.extract_2 = QPushButton(self.gridLayoutWidget_4)
        self.extract_2.setObjectName(u"extract_2")

        self.gridLayout_4.addWidget(self.extract_2, 2, 1, 1, 1)

        self.transactions_4 = QPushButton(self.gridLayoutWidget_4)
        self.transactions_4.setObjectName(u"transactions_4")

        self.gridLayout_4.addWidget(self.transactions_4, 3, 1, 1, 1)

        self.tableWidget = QTableWidget(self.page5)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(350, 10, 421, 192))
        
        
        
        
        
           
        self.add_5.clicked.connect(self.handle_add_turnover)
        self.clear_3.clicked.connect(self.clear_form)
        self.update_5.clicked.connect(self.handle_update_turnover)
        self.delete_6.clicked.connect(self.open_delete_turnover_dialog)
        
        
        
        
        
        
        self.stackedWidget.addWidget(self.page5)
        
        
            ## Page 6
        self.page6 = QWidget()
    
        self.page6.setObjectName(u"page6")
        self.search_2 = QPushButton(self.page6)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setGeometry(QRect(580, 390, 93, 28))
        self.listall = QPushButton(self.page6)
        self.listall.setObjectName(u"listall")
        self.listall.setGeometry(QRect(680, 390, 93, 28))
        self.tableWidget_5 = QTableWidget(self.page6)
        if (self.tableWidget_5.columnCount() < 6):
            self.tableWidget_5.setColumnCount(6)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(10, 20, 761, 351))
        self.stackedWidget.addWidget(self.page6)
        self.building_choose = QFrame(self.centralwidget)
        self.building_choose.setObjectName(u"building_choose")
        self.building_choose.setGeometry(QRect(30, 10, 361, 61))
        self.building_choose.setFrameShape(QFrame.StyledPanel)
        self.building_choose.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.building_choose)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 341, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.choosebuilding = QLineEdit(self.horizontalLayoutWidget)
        self.choosebuilding.setObjectName(u"choosebuilding")
        self.choosebuilding.setReadOnly(True)

        self.horizontalLayout.addWidget(self.choosebuilding)

        self.l_choosebuilding = QComboBox(self.horizontalLayoutWidget)
        self.l_choosebuilding.setObjectName(u"l_choosebuilding")

        self.horizontalLayout.addWidget(self.l_choosebuilding)

        self.left_navigator = QFrame(self.centralwidget)
        self.left_navigator.setObjectName(u"left_navigator")
        self.left_navigator.setGeometry(QRect(10, 90, 141, 411))
        self.left_navigator.setFrameShape(QFrame.StyledPanel)
        self.left_navigator.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.left_navigator)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 121, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.n_householdregister = QPushButton(self.verticalLayoutWidget)
        self.n_householdregister.setObjectName(u"n_householdregister")

        self.verticalLayout.addWidget(self.n_householdregister)

        self.n_bankregister = QPushButton(self.verticalLayoutWidget)
        self.n_bankregister.setObjectName(u"n_bankregister")

        self.verticalLayout.addWidget(self.n_bankregister)

        self.n_income = QPushButton(self.verticalLayoutWidget)
        self.n_income.setObjectName(u"n_income")

        self.verticalLayout.addWidget(self.n_income)

        self.n_expenses = QPushButton(self.verticalLayoutWidget)
        self.n_expenses.setObjectName(u"n_expenses")

        self.verticalLayout.addWidget(self.n_expenses)

        self.n_turnovers = QPushButton(self.verticalLayoutWidget)
        self.n_turnovers.setObjectName(u"n_turnovers")

        self.verticalLayout.addWidget(self.n_turnovers)

        self.n_search = QPushButton(self.verticalLayoutWidget)
        self.n_search.setObjectName(u"n_search")

        self.verticalLayout.addWidget(self.n_search)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 952, 26))
        self.menuDebit_Transactions = QMenu(self.menubar)
        self.menuDebit_Transactions.setObjectName(u"menuDebit_Transactions")
        self.action3 = QMenu(self.menubar)
        self.action3.setObjectName(u"action3")
        self.action4 = QMenu(self.menubar)
        self.action4.setObjectName(u"action4")
        self.action5 = QMenu(self.menubar)
        self.action5.setObjectName(u"action5")
        self.action6 = QMenu(self.menubar)
        self.action6.setObjectName(u"action6")
        self.action7 = QMenu(self.menubar)
        self.action7.setObjectName(u"action7")
        self.action8 = QMenu(self.menubar)
        self.action8.setObjectName(u"action8")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDebit_Transactions.menuAction())
        self.menubar.addAction(self.action3.menuAction())
        self.menubar.addAction(self.action4.menuAction())
        self.menubar.addAction(self.action5.menuAction())
        self.menubar.addAction(self.action6.menuAction())
        self.menubar.addAction(self.action7.menuAction())
        self.menubar.addAction(self.action8.menuAction())
        self.menuDebit_Transactions.addSeparator()
        self.menuDebit_Transactions.addAction(self.actionBulk_Loan)
        self.menuDebit_Transactions.addAction(self.actionLoan_By_Square_Meter)
        self.menuDebit_Transactions.addAction(self.actionLoan_By_Meters)
        self.menuDebit_Transactions.addAction(self.actionLoan_Updating)
        self.action3.addAction(self.actionFast_Pay)
        self.action3.addAction(self.actionBulk_Pay)
        self.action3.addAction(self.actionTemporary_Account)
        self.action3.addAction(self.actionBulk_Collection_Update)
        self.action4.addAction(self.actionTurnovers)
        self.action4.addAction(self.actionFollow_Turnovers)
        self.action5.addAction(self.actionTransactions)
        self.action5.addAction(self.actionExtract)
        self.action5.addSeparator()
        self.action5.addAction(self.actionCollection_System)
        self.action6.addAction(self.actionR1)
        self.action6.addAction(self.actionR2)
        self.action6.addAction(self.actionR3)
        self.action6.addAction(self.actionR4)
        self.action6.addAction(self.actionR5)
        self.action6.addAction(self.actionR6)
        self.action6.addAction(self.actionR7)
        self.action6.addAction(self.actionR8)
        self.action6.addAction(self.actionR9)
        self.action6.addAction(self.actionR10)
        self.action6.addAction(self.actionR11)
        self.action6.addAction(self.actionR12)
        self.action6.addAction(self.actionR13)
        self.action6.addAction(self.actionR14)
        self.action6.addAction(self.actionR15)
        self.action6.addAction(self.actionR16)
        self.action6.addAction(self.actionR17)
        self.action6.addAction(self.actionR18)
        self.action7.addAction(self.actionLogs)
        self.action7.addAction(self.actionRemove)
        self.action8.addAction(self.actionHousehold_Update)
        self.action8.addAction(self.actionLandlord_Tenant_Match)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        
         # Connect Buttons to Page Switch
        self.n_householdregister.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.n_bankregister.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.n_income.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.n_expenses.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.n_turnovers.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.n_search.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRegistration.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.actionList.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.actionBulk_Loan.setText(QCoreApplication.translate("MainWindow", u"Bulk Loan", None))
        self.actionLoan_By_Square_Meter.setText(QCoreApplication.translate("MainWindow", u"Loan By Square Meter", None))
        self.actionLoan_By_Meters.setText(QCoreApplication.translate("MainWindow", u"Loan By Meters", None))
        self.actionLoan_Updating.setText(QCoreApplication.translate("MainWindow", u"Loan Updating", None))
        self.actionFast_Pay.setText(QCoreApplication.translate("MainWindow", u"Fast Pay", None))
        self.actionBulk_Pay.setText(QCoreApplication.translate("MainWindow", u"Bulk Pay", None))
        self.actionTemporary_Account.setText(QCoreApplication.translate("MainWindow", u"Temporary Account", None))
        self.actionBulk_Collection_Update.setText(QCoreApplication.translate("MainWindow", u"Bulk Collection Update", None))
        self.actionTurnovers.setText(QCoreApplication.translate("MainWindow", u"Turnovers", None))
        self.actionFollow_Turnovers.setText(QCoreApplication.translate("MainWindow", u"Follow Turnovers", None))
        self.actionTransactions.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.actionExtract.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.actionCollection_System.setText(QCoreApplication.translate("MainWindow", u"Collection System", None))
        self.actionR1.setText(QCoreApplication.translate("MainWindow", u"R1", None))
        self.actionR2.setText(QCoreApplication.translate("MainWindow", u"R2", None))
        self.actionR3.setText(QCoreApplication.translate("MainWindow", u"R3", None))
        self.actionR4.setText(QCoreApplication.translate("MainWindow", u"R4", None))
        self.actionR5.setText(QCoreApplication.translate("MainWindow", u"R5", None))
        self.actionR6.setText(QCoreApplication.translate("MainWindow", u"R6", None))
        self.actionR7.setText(QCoreApplication.translate("MainWindow", u"R7", None))
        self.actionR8.setText(QCoreApplication.translate("MainWindow", u"R8", None))
        self.actionR9.setText(QCoreApplication.translate("MainWindow", u"R9", None))
        self.actionR10.setText(QCoreApplication.translate("MainWindow", u"R10", None))
        self.actionR11.setText(QCoreApplication.translate("MainWindow", u"R11", None))
        self.actionR12.setText(QCoreApplication.translate("MainWindow", u"R12", None))
        self.actionR13.setText(QCoreApplication.translate("MainWindow", u"R13", None))
        self.actionR14.setText(QCoreApplication.translate("MainWindow", u"R14", None))
        self.actionR15.setText(QCoreApplication.translate("MainWindow", u"R15", None))
        self.actionR16.setText(QCoreApplication.translate("MainWindow", u"R16", None))
        self.actionR17.setText(QCoreApplication.translate("MainWindow", u"R17", None))
        self.actionR18.setText(QCoreApplication.translate("MainWindow", u"R18", None))
        self.actionLogs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.actionRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.actionHousehold_Update.setText(QCoreApplication.translate("MainWindow", u"Household Update", None))
        self.actionLandlord_Tenant_Match.setText(QCoreApplication.translate("MainWindow", u"Landlord - Tenant Match", None))
        self.householdno.setText(QCoreApplication.translate("MainWindow", u"Household Number", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.sin.setText(QCoreApplication.translate("MainWindow", u"SIN", None))
        self.bday.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.plateno.setText(QCoreApplication.translate("MainWindow", u"Number Plate", None))
        self.taxno.setText(QCoreApplication.translate("MainWindow", u"Tax Number", None))
        self.phonenumber.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.address.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.groupno.setText(QCoreApplication.translate("MainWindow", u"Group No", None))
        self.accountno.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.accountnote.setText(QCoreApplication.translate("MainWindow", u"Account Note", None))
        self.receiverno.setText(QCoreApplication.translate("MainWindow", u"Receiver No", None))
        self.receivernote.setText(QCoreApplication.translate("MainWindow", u"Account Note", None))
        self.workaddress.setText(QCoreApplication.translate("MainWindow", u"Work Address", None))
        self.workphonenumber.setText(QCoreApplication.translate("MainWindow", u"Work Phone Number", None))
        self.workemail.setText(QCoreApplication.translate("MainWindow", u"Work Email", None))
        self.occupation.setText(QCoreApplication.translate("MainWindow", u"Occupation", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.clear_2.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.bankno.setText(QCoreApplication.translate("MainWindow", u"Bank No", None))
        self.bankname.setText(QCoreApplication.translate("MainWindow", u"Bank Name", None))
        self.branch.setText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.accountno_2.setText(QCoreApplication.translate("MainWindow", u"Account No", None))
        self.accountname.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.authority.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.phonenumber_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.faxno.setText(QCoreApplication.translate("MainWindow", u"Fax No", None))
        self.ibanno.setText(QCoreApplication.translate("MainWindow", u"IBAN No", None))
        self.web.setText(QCoreApplication.translate("MainWindow", u"Web", None))
        self.balance.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.expense.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.transactions.setText(QCoreApplication.translate("MainWindow", u"TRANSACTIONS", None))
        self.add_2.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.update_2.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.delete_3.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.extract.setText(QCoreApplication.translate("MainWindow", u"EXTRACT", None))
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Bank No", None));
        ___qtablewidgetitem1 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Bank Name", None));
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Branch", None));
        self.add_3.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.delete_4.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.filter.setText(QCoreApplication.translate("MainWindow", u"FILTER", None))
        self.update_3.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.sort.setText(QCoreApplication.translate("MainWindow", u"SORT", None))
        self.import_2.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.transactions_2.setText(QCoreApplication.translate("MainWindow", u"TRANSACTIONS", None))
        self.print.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"No", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Document No", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Account No", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Account Note", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Note", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Total ", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Expense Code", None));
        self.add_4.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.delete_5.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.filter_2.setText(QCoreApplication.translate("MainWindow", u"FILTRE", None))
        self.update_4.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.sort_2.setText(QCoreApplication.translate("MainWindow", u"SORT", None))
        self.import_3.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.transactions_3.setText(QCoreApplication.translate("MainWindow", u"TRANSACTIONS", None))
        self.print_2.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"No", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Document No", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Account Code", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Account Note", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Note", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Payment Place", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Expense Code", None));
        self.turnoverno.setText(QCoreApplication.translate("MainWindow", u"Turnover No", None))
        self.companyname.setText(QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.authority_2.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.bankname_2.setText(QCoreApplication.translate("MainWindow", u"Bank Name", None))
        self.taxno_2.setText(QCoreApplication.translate("MainWindow", u"Tax No", None))
        self.taxplace.setText(QCoreApplication.translate("MainWindow", u"Tax Place", None))
        self.ibanno_2.setText(QCoreApplication.translate("MainWindow", u"IBAN", None))
        self.address_2.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.phonenumber_3.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.email_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.web_2.setText(QCoreApplication.translate("MainWindow", u"Web", None))
        self.groupcode.setText(QCoreApplication.translate("MainWindow", u"Grup Code", None))
        self.balance_2.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.debt.setText(QCoreApplication.translate("MainWindow", u"Debt", None))
        self.income_2.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.o_debt.setText("")
        self.o_income_2.setText("")
        self.o_balance_2.setText("")
        self.add_5.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.update_5.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.delete_6.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.clear_3.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.extract_2.setText(QCoreApplication.translate("MainWindow", u"EXTRACT", None))
        self.transactions_4.setText(QCoreApplication.translate("MainWindow", u"TRANSACTIONS", None))
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Group Code", None));
        self.search_2.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.listall.setText(QCoreApplication.translate("MainWindow", u"LIST ALL", None))
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Household No", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"SIN", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        self.choosebuilding.setText(QCoreApplication.translate("MainWindow", u"Choose The Building", None))
        self.n_householdregister.setText(QCoreApplication.translate("MainWindow", u"Household Register", None))
        self.n_bankregister.setText(QCoreApplication.translate("MainWindow", u"Bank Register", None))
        self.n_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.n_expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.n_turnovers.setText(QCoreApplication.translate("MainWindow", u"Turnovers", None))
        self.n_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.menuDebit_Transactions.setTitle(QCoreApplication.translate("MainWindow", u"Debit Transactions", None))
        self.action3.setTitle(QCoreApplication.translate("MainWindow", u"Collections", None))
        self.action4.setTitle(QCoreApplication.translate("MainWindow", u"Enforcements", None))
        self.action5.setTitle(QCoreApplication.translate("MainWindow", u"Banks", None))
        self.action6.setTitle(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.action7.setTitle(QCoreApplication.translate("MainWindow", u"Residential Transfer", None))
        self.action8.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
  
  
   
if __name__ == "__main__":
    import sys
    from clinic.controllers.master_controller import MasterController

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    master_controller = MasterController(autosave=True)  # ✅ Correct Initialization
    ui = Ui_MainWindow(master_controller)  # ✅ Pass Initialized MasterController
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())

