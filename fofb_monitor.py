# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.V_BPM = QtWidgets.QComboBox(self.centralwidget)
        self.V_BPM.setGeometry(QtCore.QRect(130, 120, 80, 22))
        self.V_BPM.setObjectName("V_BPM")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.V_BPM.addItem("")
        self.F_REC = QtWidgets.QPushButton(self.centralwidget)
        self.F_REC.setEnabled(True)
        self.F_REC.setGeometry(QtCore.QRect(130, 520, 93, 28))
        self.F_REC.setObjectName("F_REC")
        self.F_X = QtWidgets.QCheckBox(self.centralwidget)
        self.F_X.setGeometry(QtCore.QRect(130, 430, 81, 20))
        self.F_X.setObjectName("F_X")
        self.F_Z = QtWidgets.QCheckBox(self.centralwidget)
        self.F_Z.setGeometry(QtCore.QRect(130, 460, 81, 20))
        self.F_Z.setObjectName("F_Z")
        self.F_SIZE = QtWidgets.QLineEdit(self.centralwidget)
        self.F_SIZE.setGeometry(QtCore.QRect(130, 360, 80, 22))
        self.F_SIZE.setObjectName("F_SIZE")
        self.F_I = QtWidgets.QCheckBox(self.centralwidget)
        self.F_I.setGeometry(QtCore.QRect(130, 490, 81, 20))
        self.F_I.setObjectName("F_I")
        self.F_LABEL_SIZE = QtWidgets.QLabel(self.centralwidget)
        self.F_LABEL_SIZE.setGeometry(QtCore.QRect(50, 360, 55, 20))
        self.F_LABEL_SIZE.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.F_LABEL_SIZE.setObjectName("F_LABEL_SIZE")
        self.GRAPH = PlotWidget(self.centralwidget)
        self.GRAPH.setGeometry(QtCore.QRect(310, 20, 780, 290))
        self.GRAPH.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.GRAPH.setObjectName("GRAPH")
        self.FOURIER = PlotWidget(self.centralwidget)
        self.FOURIER.setGeometry(QtCore.QRect(310, 330, 780, 290))
        self.FOURIER.setObjectName("FOURIER")
        self.LABEL_GRAPH_OPTIONS = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_GRAPH_OPTIONS.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.LABEL_GRAPH_OPTIONS.setObjectName("LABEL_GRAPH_OPTIONS")
        self.V_RAD_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.V_RAD_4.setGeometry(QtCore.QRect(90, 50, 120, 20))
        self.V_RAD_4.setChecked(True)
        self.V_RAD_4.setAutoExclusive(False)
        self.V_RAD_4.setObjectName("V_RAD_4")
        self.V_LABEL_BPM = QtWidgets.QLabel(self.centralwidget)
        self.V_LABEL_BPM.setGeometry(QtCore.QRect(60, 120, 55, 20))
        self.V_LABEL_BPM.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.V_LABEL_BPM.setObjectName("V_LABEL_BPM")
        self.V_LABEL_CHANNEL = QtWidgets.QLabel(self.centralwidget)
        self.V_LABEL_CHANNEL.setGeometry(QtCore.QRect(60, 150, 55, 20))
        self.V_LABEL_CHANNEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.V_LABEL_CHANNEL.setObjectName("V_LABEL_CHANNEL")
        self.V_CHANNEL = QtWidgets.QComboBox(self.centralwidget)
        self.V_CHANNEL.setGeometry(QtCore.QRect(130, 150, 80, 22))
        self.V_CHANNEL.setObjectName("V_CHANNEL")
        self.V_CHANNEL.addItem("")
        self.V_CHANNEL.addItem("")
        self.V_CHANNEL.addItem("")
        self.LABEL_FILE_RECORDING = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_FILE_RECORDING.setGeometry(QtCore.QRect(20, 330, 101, 21))
        self.LABEL_FILE_RECORDING.setObjectName("LABEL_FILE_RECORDING")
        self.V_RAD_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.V_RAD_3.setGeometry(QtCore.QRect(90, 80, 120, 20))
        self.V_RAD_3.setChecked(True)
        self.V_RAD_3.setAutoExclusive(False)
        self.V_RAD_3.setObjectName("V_RAD_3")
        self.V_ON_OFF = QtWidgets.QRadioButton(self.centralwidget)
        self.V_ON_OFF.setGeometry(QtCore.QRect(90, 210, 151, 20))
        self.V_ON_OFF.setObjectName("V_ON_OFF")
        self.F_LABEL_BPM = QtWidgets.QLabel(self.centralwidget)
        self.F_LABEL_BPM.setGeometry(QtCore.QRect(50, 390, 55, 20))
        self.F_LABEL_BPM.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.F_LABEL_BPM.setObjectName("F_LABEL_BPM")
        self.F_BPM = QtWidgets.QComboBox(self.centralwidget)
        self.F_BPM.setGeometry(QtCore.QRect(130, 390, 80, 22))
        self.F_BPM.setObjectName("F_BPM")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_BPM.addItem("")
        self.F_3D_REC = QtWidgets.QPushButton(self.centralwidget)
        self.F_3D_REC.setGeometry(QtCore.QRect(130, 560, 93, 28))
        self.F_3D_REC.setObjectName("F_3D_REC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOFB Monitor"))
        self.V_BPM.setItemText(0, _translate("MainWindow", "STP0"))
        self.V_BPM.setItemText(1, _translate("MainWindow", "STP2"))
        self.V_BPM.setItemText(2, _translate("MainWindow", "STP4"))
        self.V_BPM.setItemText(3, _translate("MainWindow", "SRP1"))
        self.V_BPM.setItemText(4, _translate("MainWindow", "SRP2"))
        self.V_BPM.setItemText(5, _translate("MainWindow", "SRP3"))
        self.V_BPM.setItemText(6, _translate("MainWindow", "SRP4"))
        self.V_BPM.setItemText(7, _translate("MainWindow", "SRP5"))
        self.V_BPM.setItemText(8, _translate("MainWindow", "SRP6"))
        self.V_BPM.setItemText(9, _translate("MainWindow", "SRP7"))
        self.V_BPM.setItemText(10, _translate("MainWindow", "SRP8"))
        self.V_BPM.setItemText(11, _translate("MainWindow", "SRP9"))
        self.V_BPM.setItemText(12, _translate("MainWindow", "SIP1"))
        self.V_BPM.setItemText(13, _translate("MainWindow", "SIP2"))
        self.V_BPM.setItemText(14, _translate("MainWindow", "SRP10"))
        self.V_BPM.setItemText(15, _translate("MainWindow", "SRP11"))
        self.V_BPM.setItemText(16, _translate("MainWindow", "SRP12"))
        self.V_BPM.setItemText(17, _translate("MainWindow", "SRP13"))
        self.V_BPM.setItemText(18, _translate("MainWindow", "SRP14"))
        self.V_BPM.setItemText(19, _translate("MainWindow", "SRP15"))
        self.V_BPM.setItemText(20, _translate("MainWindow", "SRP16"))
        self.V_BPM.setItemText(21, _translate("MainWindow", "SRP17"))
        self.V_BPM.setItemText(22, _translate("MainWindow", "SEP5"))
        self.V_BPM.setItemText(23, _translate("MainWindow", "SEP4"))
        self.V_BPM.setItemText(24, _translate("MainWindow", "SEP3"))
        self.V_BPM.setItemText(25, _translate("MainWindow", "SEP1"))
        self.V_BPM.setItemText(26, _translate("MainWindow", "SEP0"))
        self.V_BPM.setItemText(27, _translate("MainWindow", "NEP0"))
        self.V_BPM.setItemText(28, _translate("MainWindow", "NEP1"))
        self.V_BPM.setItemText(29, _translate("MainWindow", "NEP3"))
        self.V_BPM.setItemText(30, _translate("MainWindow", "NEP4"))
        self.V_BPM.setItemText(31, _translate("MainWindow", "NEP5"))
        self.V_BPM.setItemText(32, _translate("MainWindow", "NRP17"))
        self.V_BPM.setItemText(33, _translate("MainWindow", "NRP16"))
        self.V_BPM.setItemText(34, _translate("MainWindow", "NRP15"))
        self.V_BPM.setItemText(35, _translate("MainWindow", "NRP14"))
        self.V_BPM.setItemText(36, _translate("MainWindow", "NRP13"))
        self.V_BPM.setItemText(37, _translate("MainWindow", "NRP12"))
        self.V_BPM.setItemText(38, _translate("MainWindow", "NRP11"))
        self.V_BPM.setItemText(39, _translate("MainWindow", "NRP10"))
        self.V_BPM.setItemText(40, _translate("MainWindow", "NIP3"))
        self.V_BPM.setItemText(41, _translate("MainWindow", "NIP1"))
        self.V_BPM.setItemText(42, _translate("MainWindow", "NRP9"))
        self.V_BPM.setItemText(43, _translate("MainWindow", "NRP8"))
        self.V_BPM.setItemText(44, _translate("MainWindow", "NRP7"))
        self.V_BPM.setItemText(45, _translate("MainWindow", "NRP6"))
        self.V_BPM.setItemText(46, _translate("MainWindow", "NRP5"))
        self.V_BPM.setItemText(47, _translate("MainWindow", "NRP4"))
        self.V_BPM.setItemText(48, _translate("MainWindow", "NRP3"))
        self.V_BPM.setItemText(49, _translate("MainWindow", "NRP2"))
        self.V_BPM.setItemText(50, _translate("MainWindow", "NRP1"))
        self.V_BPM.setItemText(51, _translate("MainWindow", "NTP4"))
        self.V_BPM.setItemText(52, _translate("MainWindow", "NTP2"))
        self.V_BPM.setItemText(53, _translate("MainWindow", "NTP0"))
        self.F_REC.setText(_translate("MainWindow", "Save to Files"))
        self.F_X.setText(_translate("MainWindow", "x"))
        self.F_Z.setText(_translate("MainWindow", "z"))
        self.F_I.setText(_translate("MainWindow", "I"))
        self.F_LABEL_SIZE.setText(_translate("MainWindow", "Size:"))
        self.LABEL_GRAPH_OPTIONS.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Graph Options</span></p></body></html>"))
        self.V_RAD_4.setText(_translate("MainWindow", "VEPP-4M BPMs"))
        self.V_LABEL_BPM.setText(_translate("MainWindow", "BPM:"))
        self.V_LABEL_CHANNEL.setText(_translate("MainWindow", "channel:"))
        self.V_CHANNEL.setItemText(0, _translate("MainWindow", "x"))
        self.V_CHANNEL.setItemText(1, _translate("MainWindow", "z"))
        self.V_CHANNEL.setItemText(2, _translate("MainWindow", "I"))
        self.LABEL_FILE_RECORDING.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">File Recording</span></p></body></html>"))
        self.V_RAD_3.setText(_translate("MainWindow", "VEPP-3 BPMs"))
        self.V_ON_OFF.setText(_translate("MainWindow", "Graph Visualization"))
        self.F_LABEL_BPM.setText(_translate("MainWindow", "BPM:"))
        self.F_BPM.setItemText(0, _translate("MainWindow", "STP0"))
        self.F_BPM.setItemText(1, _translate("MainWindow", "STP2"))
        self.F_BPM.setItemText(2, _translate("MainWindow", "STP4"))
        self.F_BPM.setItemText(3, _translate("MainWindow", "SRP1"))
        self.F_BPM.setItemText(4, _translate("MainWindow", "SRP2"))
        self.F_BPM.setItemText(5, _translate("MainWindow", "SRP3"))
        self.F_BPM.setItemText(6, _translate("MainWindow", "SRP4"))
        self.F_BPM.setItemText(7, _translate("MainWindow", "SRP5"))
        self.F_BPM.setItemText(8, _translate("MainWindow", "SRP6"))
        self.F_BPM.setItemText(9, _translate("MainWindow", "SRP7"))
        self.F_BPM.setItemText(10, _translate("MainWindow", "SRP8"))
        self.F_BPM.setItemText(11, _translate("MainWindow", "SRP9"))
        self.F_BPM.setItemText(12, _translate("MainWindow", "SIP1"))
        self.F_BPM.setItemText(13, _translate("MainWindow", "SIP2"))
        self.F_BPM.setItemText(14, _translate("MainWindow", "SRP10"))
        self.F_BPM.setItemText(15, _translate("MainWindow", "SRP11"))
        self.F_BPM.setItemText(16, _translate("MainWindow", "SRP12"))
        self.F_BPM.setItemText(17, _translate("MainWindow", "SRP13"))
        self.F_BPM.setItemText(18, _translate("MainWindow", "SRP14"))
        self.F_BPM.setItemText(19, _translate("MainWindow", "SRP15"))
        self.F_BPM.setItemText(20, _translate("MainWindow", "SRP16"))
        self.F_BPM.setItemText(21, _translate("MainWindow", "SRP17"))
        self.F_BPM.setItemText(22, _translate("MainWindow", "SEP5"))
        self.F_BPM.setItemText(23, _translate("MainWindow", "SEP4"))
        self.F_BPM.setItemText(24, _translate("MainWindow", "SEP3"))
        self.F_BPM.setItemText(25, _translate("MainWindow", "SEP1"))
        self.F_BPM.setItemText(26, _translate("MainWindow", "SEP0"))
        self.F_BPM.setItemText(27, _translate("MainWindow", "NEP0"))
        self.F_BPM.setItemText(28, _translate("MainWindow", "NEP1"))
        self.F_BPM.setItemText(29, _translate("MainWindow", "NEP3"))
        self.F_BPM.setItemText(30, _translate("MainWindow", "NEP4"))
        self.F_BPM.setItemText(31, _translate("MainWindow", "NEP5"))
        self.F_BPM.setItemText(32, _translate("MainWindow", "NRP17"))
        self.F_BPM.setItemText(33, _translate("MainWindow", "NRP16"))
        self.F_BPM.setItemText(34, _translate("MainWindow", "NRP15"))
        self.F_BPM.setItemText(35, _translate("MainWindow", "NRP14"))
        self.F_BPM.setItemText(36, _translate("MainWindow", "NRP13"))
        self.F_BPM.setItemText(37, _translate("MainWindow", "NRP12"))
        self.F_BPM.setItemText(38, _translate("MainWindow", "NRP11"))
        self.F_BPM.setItemText(39, _translate("MainWindow", "NRP10"))
        self.F_BPM.setItemText(40, _translate("MainWindow", "NIP3"))
        self.F_BPM.setItemText(41, _translate("MainWindow", "NIP1"))
        self.F_BPM.setItemText(42, _translate("MainWindow", "NRP9"))
        self.F_BPM.setItemText(43, _translate("MainWindow", "NRP8"))
        self.F_BPM.setItemText(44, _translate("MainWindow", "NRP7"))
        self.F_BPM.setItemText(45, _translate("MainWindow", "NRP6"))
        self.F_BPM.setItemText(46, _translate("MainWindow", "NRP5"))
        self.F_BPM.setItemText(47, _translate("MainWindow", "NRP4"))
        self.F_BPM.setItemText(48, _translate("MainWindow", "NRP3"))
        self.F_BPM.setItemText(49, _translate("MainWindow", "NRP2"))
        self.F_BPM.setItemText(50, _translate("MainWindow", "NRP1"))
        self.F_BPM.setItemText(51, _translate("MainWindow", "NTP4"))
        self.F_BPM.setItemText(52, _translate("MainWindow", "NTP2"))
        self.F_BPM.setItemText(53, _translate("MainWindow", "NTP0"))
        self.F_3D_REC.setText(_translate("MainWindow", "3D"))
from pyqtgraph import PlotWidget