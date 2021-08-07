#module provides a model to manage contacts 

from PyQt5.QtCore import Qt 
from PyQt5.QtSql import QSqlTableModel

class ContactModel:
    def __init__(self):
        self.model = self._createModel()

    
    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID" , "Name" , "Job" , "Email")
        for columnIndex , header in enumerate(headers):
            tableModel.setHeaderData(columnIndex , Qt.Horizental , header)
        return tableModel