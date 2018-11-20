import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QScrollArea,
                             QFileDialog, QHBoxLayout, QTableWidget, QTableWidgetItem,
                             QLineEdit, QGridLayout, QLCDNumber, QSlider, QVBoxLayout, QInputDialog, QSizePolicy, QDialog)
from PyQt5.QtGui import QFont, QIcon, QColor, QPixmap, QScreen
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5 import QtWidgets, QtCore, QtGui
import pandas as pd
import numpy as np


class MetroMap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        load_btn = QPushButton('Load data', self)
        predict_btn = QPushButton('Predict', self)
        present_btn = QPushButton('Present', self)
        quit_btn = QPushButton('Quit', self)
        vbox = QVBoxLayout()
        vbox.addWidget(load_btn)
        vbox.addWidget(predict_btn)
        vbox.addWidget(present_btn)
        vbox.addWidget(quit_btn)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 400, 400)
        self.center()
        self.setWindowTitle('Talk back classifier')

        load_btn.clicked.connect(self.load_button_clicked)
        predict_btn.clicked.connect(self.predict_button_clicked)
        present_btn.clicked.connect(self.present_btn_clicked)
        quit_btn.clicked.connect(QApplication.instance().quit)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def predict_button_clicked(self):
        """ Model prediction here"""
        try:
            self.data['Prediction'] = pd.Series(np.random.randn(len(self.data['ARTICLE_ID'])))
            print("Prediction completed")
        except Exception as e:
            print(e)
        return

    def present_btn_clicked(self):
        try:
            sorted_data = self.data.sort_values(by=['Prediction'], ascending=False)
            print(sorted_data[0:10])
            # win = QWidget()
            # scroll = QScrollArea()
            # layout = QVBoxLayout()
            # view = QtWidgets.QTableWidget(parent=self)
            # scroll.setWidget(view)
            # layout.addWidget(view)
            # win.setLayout(layout)
            # view.setColumnCount(len(self.data[0:10].columns))
            # view.setRowCount(len(self.data[0:10].index))
            # for i in range(len(self.data[0:10].index)):
            #     for j in range(len(self.data[0:10].columns)):
            #         view.setItem(i, j, QTableWidgetItem(str(self.data[0:10].iloc[i, j])))
            # win.show()
            # for i in range (19999999):
            #     time.sleep(10)
        except Exception as e:
            print(e)


    def load_button_clicked(self):
        """ Loads a csv file with raw data and returns
            a pandas dataframe """
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        self.data = pd.read_csv(fname[0])

class PandasModel(QtCore.QAbstractTableModel):
    def _init_(self, data, parent=None):
        QtCore.QAbstractTableModel._init_(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    TalkBack_UI = MetroMap()
    TalkBack_UI.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())


