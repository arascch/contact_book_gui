from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase

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