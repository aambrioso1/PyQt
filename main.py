"""
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel

import sys

if __name__ == '__main__':
    app = QApplication([])
    window = QLabel()
    image = QPixmap('Erikapic.jpg')
    window.setPixmap(image)
    window.show()
    sys.exit(app.exec_())
"""

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = QLabel()
    image = QPixmap(appctxt.get_resource('Erikapic.jpg'))
    window.setPixmap(image)
    window.show()
    sys.exit(appctxt.app.exec_())