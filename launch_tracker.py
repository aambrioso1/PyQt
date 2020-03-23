"""
Launch Tracker

The data retrieval code was written by my daughter Erika Ambrioso.
The GUI was written by me (Alex Ambrioso)


Based on example code for PyQt5:  https://github.com/pyqt/examples/blob/_/src/14%20QAbstractTableModel%20example/main.py

"""

# These are the libraries used by the program.
import json, requests, sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant

# print("Welcome to my launch tracker\n")

url = "https://fdo.rocketlaunch.live/json/launches/next/5"

response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)
d = data['result']

"""
# This code was used to study the JSON information.

for i in range(4):
	print('First flight ', data['result'][i])
	print('*' * 50)
	print('First flight name', data['result'][i]['name'])
	print('First flight vehicle name', data['result'][i]['vehicle']['name'])
	print('First flight provider name', data['result'][i]['provider']['name'])
	# print('First flight lcoation', data['result'][i]['location'])
	print('First flight pad location', data['result'][i]['pad']['location']['name'])
	# print('First flight description', data['result'][i]['launch_description'])
	print('First flight date', data['result'][i]['date_str'])
	print('First flight win_open', data['result'][i]['win_open'][11:16])


	first_flight = data['result'][0]['launch_description']
	second_flight = data['result'][1]['launch_description']
	third_flight = data['result'][2]['launch_description']
	print('*' * 50)
	print('*' * 50)
"""

rows = []
for i in range(5):
	flight = d[i]['name']
	vehicle = d[i]['vehicle']['name']
	provider = d[i]['provider']['name']
	pad = d[i]['pad']['location']['name']
	location = d[i]['pad']['location']['name']
	date = d[i]['date_str']
	time = d[i]['win_open'][11:16]
	rows.append((flight, vehicle, provider, pad, date, time))

headers = ['Flight', 'Vehicle', 'Provider', 'Pad', 'Date', 'Time']


class TableModel(QAbstractTableModel):
	def rowCount(self, parent):
		return len(rows)
	def columnCount(self, parent):
		return len(headers)
	def data(self, index, role):
		if role != Qt.DisplayRole:
			return QVariant()
		return rows[index.row()][index.column()]
	def headerData(self, section, orientation, role):
		if role != Qt.DisplayRole or orientation != Qt.Horizontal:
			return QVariant()
		return headers[section]

app = QApplication([])
app.setStyle('Fusia')
app.setStyleSheet("QTableView, QTableView * { background: lightblue}")

model = TableModel()
view = QTableView()

view.setGeometry(500, 600, 1500, 400)
view.setWindowTitle('Erika\'s Launch Schedule App')


view.setModel(model)
view.resizeColumnsToContents()

view.show()
app.exec_()