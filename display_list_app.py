
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel

app = QApplication([])
model = QStringListModel([
    "Date", "Rocket Type", "OtherStuff", "Will the window grow automatically if the text string is long?"
])
view = QListView()
view.setModel(model)
view.show()
app.exec_()