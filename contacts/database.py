from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase , QSqlQuery

def createConnection(databasename):
    conncetion = QSqlDatabase.addDatabase("QSQLITE")
    conncetion.setDatabaseName(databasename)

    if not conncetion.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"database Error : {conncetion.lastError().text()}",
        )
        return False
        
    return True

def _createContentstable():
    createtablequery = QSqlQuery()
    return createtablequery.exec(
        """
        CREATE TABLE IF NOT EXIST contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL ,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )

def createConnection(databasename):
    _createContentstable()
    return True