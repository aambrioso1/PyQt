from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox

app = QApplication([])
app.setStyleSheet("QPushButton { margin: 30ex; }") # Adds a margin
app.setStyle('Fusion') # Windows, WindowsVista
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.blue)
app.setPalette(palette)
button = QPushButton('Hello World! Click the button! ' * 2)

def on_button_clicked():
	alert = QMessageBox()
	alert.setText('Good job! You clicked the button!')
	alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()

