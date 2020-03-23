from PyQt5.QtWidgets import *
"""
A simple label

This and similar examples can be found here.

https://github.com/pyqt/examples
"""

app = QApplication([])
label = QLabel('Hello World!')
app.setStyleSheet("QLabel { margin: 30ex; }")
label.show()
app.exec_()