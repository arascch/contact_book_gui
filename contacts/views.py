from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout ,
    QMainWindow , 
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

class Window(QMainWindow):

    def __init__(self , parent=None):
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()
    
    def setupUI(self):
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        #buttons
        self.addButton = QPushButton("add")
        self.deleteButton = QPushButton("delete")
        self.clearAllButton = QPushButton("Clear All")

        #layout Gui

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)