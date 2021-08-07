from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout ,
    QLineEdit,
    QMainWindow ,
    QMessageBox, 
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from .model import ContactModel
from PyQt5.QtCore import QMetaEnum, Qt

class Window(QMainWindow):

    def __init__(self , parent=None):
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.ContactsModel =ContactModel()  
        self.setupUI()
    
    def setupUI(self):
        self.table = QTableView()
        self.table.setModel(self.ContactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        #buttons
        self.addButton = QPushButton("add")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")

        #layout Gui

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.ContactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()
    
    def deleteContact(self):
        row = self.table.currentIndex().row()
        if row< 0 :
            return
        
        messageBox = QMessageBox.warning(
            self , " Warning!" , "do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.ContactsModel.deletContact(row)


class AddDialog(QDialog):
    def __ini__(self , parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("add contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()
    
    def setupUI(self):
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("job")
        self.emailFiled = QLineEdit()
        self.emailFiled.setObjectName("Email")
        #datafiled Layout
        layout = QFormLayout()
        layout.addRow("name :" , self.nameField)
        layout.addRow("job :" , self.jobField)
        layout.addRow("email :" , self.emailFiled)
        self.layout.addlayout(layout)
        #add buttons
        self.buttonsbox = QDialogButtonBox(self)
        self.buttonsbox.setOrientation(Qt.Horizontal)
        self.buttonsbox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsbox.accepted.connect(self.accept)
        self.buttonsbox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsbox)
    
    def accept(self):
        self.data = []
        for field in (self.nameField , self.jobField , self.emailFiled):
            if not field.text():
                QMessageBox.critical(
                    self , 
                    "Error",
                    f"You must Provide a contat's{field.objectName()}",
                )
                self.data = None
                return
            self.data.append(field.text())
        
        if not self.data:
            return
        
        super().accept()