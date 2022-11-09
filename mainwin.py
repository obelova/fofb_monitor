# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import epics
import numpy as np

class Ui_MainWindow(object):
    bpms = ["STP0", "STP2", "STP4", "SRP1", "SRP2", "SRP3", "SRP4", "SRP5", "SRP6", "SRP7",
            "SRP8", "SRP9", "SIP1", "SIP2", "SRP10", "SRP11", "SRP12", "SRP13", "SRP14",
            "SRP15", "SRP16", "SRP17", "SEP5", "SEP4", "SEP3", "SEP1", "SEP0", "NEP0", "NEP1",
            "NEP3", "NEP4", "NEP5", "NRP17", "NRP16", "NRP15", "NRP14", "NRP13", "NRP12",
            "NRP11", "NRP10", "NIP3", "NIP1", "NRP9", "NRP8", "NRP7", "NRP6", "NRP5",
            "NRP4", "NRP3", "NRP2", "NRP1", "NTP4", "NTP2", "NTP0"]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 616)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bmp_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.bmp_combobox.setGeometry(QtCore.QRect(90, 150, 61, 22))
        self.bmp_combobox.setObjectName("bmp_combobox")
        self.bmp_combobox.addItems(self.bpms)
        self.cur_bpm = ''

        self.write_to_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.write_to_file_button.setGeometry(QtCore.QRect(40, 440, 93, 28))
        self.write_to_file_button.setObjectName("write_to_file_button")

        self.x_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.x_checkbox.setGeometry(QtCore.QRect(20, 330, 81, 20))
        self.x_checkbox.setObjectName("x_checkbox")

        self.z_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.z_checkbox.setGeometry(QtCore.QRect(20, 360, 81, 20))
        self.z_checkbox.setObjectName("z_checkbox")

        self.total_time_line = QtWidgets.QLineEdit(self.centralwidget)
        self.total_time_line.setGeometry(QtCore.QRect(90, 360, 61, 22))
        self.total_time_line.setObjectName("total_time_line")

        self.seconds_label = QtWidgets.QLabel(self.centralwidget)
        self.seconds_label.setGeometry(QtCore.QRect(160, 360, 21, 16))
        self.seconds_label.setObjectName("seconds_label")

        self.I_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.I_checkbox.setGeometry(QtCore.QRect(20, 390, 81, 20))
        self.I_checkbox.setObjectName("I_checkbox")

        self.recording_time_label = QtWidgets.QLabel(self.centralwidget)
        self.recording_time_label.setGeometry(QtCore.QRect(90, 320, 91, 41))
        self.recording_time_label.setObjectName("recording_time_label")

        self.t = []
        self.cur_time_in_sec = 0
        self.ch = []
        self.mean = 0.

        self.graph = PlotWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(200, 20, 781, 251))
        self.graph.setObjectName("graph")
        self.graph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_graph =  self.graph.plot(self.t, self.ch, pen=pen)

        self.fourier = PlotWidget(self.centralwidget)
        self.fourier.setGeometry(QtCore.QRect(200, 290, 781, 251))
        self.fourier.setObjectName("fourier")
        self.fourier.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_fourier = self.fourier.plot([0, 1, 2, 3], [0, 1, 4, 9], pen=pen)

        self.graph_options_label = QtWidgets.QLabel(self.centralwidget)
        self.graph_options_label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.graph_options_label.setObjectName("graph_options_label")

        self.on_button = QtWidgets.QRadioButton(self.centralwidget)
        self.on_button.setGeometry(QtCore.QRect(20, 50, 95, 20))
        self.on_button.setChecked(True)
        self.on_button.setObjectName("on_button")
        self.on_button.toggled.connect(self.radio_onClicked)

        self.bpm_label = QtWidgets.QLabel(self.centralwidget)
        self.bpm_label.setGeometry(QtCore.QRect(50, 150, 55, 21))
        self.bpm_label.setObjectName("bpm_label")

        self.channel_label = QtWidgets.QLabel(self.centralwidget)
        self.channel_label.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.channel_label.setObjectName("channel_label")
        self.channel_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.channel_combobox.setGeometry(QtCore.QRect(90, 180, 61, 22))
        self.channel_combobox.setObjectName("channel_combobox")
        self.channel_combobox.addItems(["x", "z", "i"])
        self.cur_channel = self.channel_combobox.currentText()

        self.show_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_button.setGeometry(QtCore.QRect(20, 220, 61, 31))
        self.show_button.setObjectName("show_button")
        self.show_button.clicked.connect(self.show_onClicked)

        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(90, 220, 61, 31))
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setStyleSheet('background-color: grey;')
        self.stop_button.clicked.connect(self.stop_onClicked)

        self.file_rec_label = QtWidgets.QLabel(self.centralwidget)
        self.file_rec_label.setGeometry(QtCore.QRect(20, 290, 101, 21))
        self.file_rec_label.setObjectName("file_rec_label")

        self.note_label = QtWidgets.QLabel(self.centralwidget)
        self.note_label.setGeometry(QtCore.QRect(20, 80, 181, 51))
        self.note_label.setObjectName("note_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mode_lowfreq = epics.PV('VEPP4:'+self.cur_bpm+':mode_lowfreq-Cmd')
        self.fofb_ch = epics.PV('VEPP4:' + self.cur_bpm + ':lowfreq_fofb_' + self.cur_channel + '-I')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def radio_onClicked(self):
        on = self.on_button.isChecked()
        for bpm in self.bpms:
            epics.PV('VEPP4:'+bpm+':connect-Cmd').put(on)

    def fofb_pv_onChanges(self, pvname=None, nanoseconds=None, value=None, char_value=None, **kw):
        if len(self.t) > 500:
            self.t = self.t[1:]  # Remove the first y element.
            self.ch = self.ch[1:]  # Remove the first

        print(value)

        self.t.append(self.cur_time_in_sec + nanoseconds / 1000000000)  # Add a new value 1 higher than the last.
        if len(self.t) > 1 and self.t[-2] > self.t[-1]:
            self.t[-1] += 1.
            self.cur_time_in_sec += 1
        self.ch.append(value)  # Add a new random value.
        self.mean = np.mean(self.ch)
        temp = []
        for i in range(len(self.ch)):
            temp.append(self.ch[i] - self.mean)
        self.data_line_graph.setData(self.t, self.ch)  # or temp for mean

    def show_onClicked(self):
        self.show_button.setStyleSheet('background-color: grey;')
        self.stop_button.setStyleSheet('background-color: light grey;')

        self.cur_bpm = self.bmp_combobox.currentText()
        epics.PV('VEPP4:' + self.cur_bpm + ':connect-Cmd').put(1)

        self.mode_lowfreq = epics.PV('VEPP4:' + self.cur_bpm + ':mode_lowfreq-Cmd')
        self.mode_lowfreq.put(10)
        self.mode_lowfreq.add_callback(self.mode_lowfreq_onChanges)

        epics.PV('VEPP4:' + self.cur_bpm + ':lowfreq_raw-Cmd').put(1)

        self.cur_channel = self.channel_combobox.currentText()
        self.fofb_ch = epics.PV('VEPP4:' + self.cur_bpm + ':lowfreq_fofb_' + self.cur_channel + '-I')
        self.fofb_ch.add_callback(self.fofb_pv_onChanges)

    def mode_lowfreq_onChanges(self, pvname=None, value=None, char_value=None, **kw):
        if value == 1:
            self.mode_lowfreq.put(10)

    def stop_onClicked(self):
        self.show_button.setStyleSheet('background-color: light grey;')
        self.stop_button.setStyleSheet('background-color: grey;')

        self.mode_lowfreq.put(0)
        self.mode_lowfreq.clear_callbacks()

        self.fofb_ch.clear_callbacks()

        epics.PV('VEPP4:' + self.cur_bpm + ':lowfreq_raw-Cmd').put(0)

        self.t = []
        self.ch = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOFB Monitor"))
        self.bmp_combobox.setItemText(0, _translate("MainWindow", "STP0"))
        self.bmp_combobox.setItemText(1, _translate("MainWindow", "STP2"))
        self.bmp_combobox.setItemText(2, _translate("MainWindow", "STP4"))
        self.bmp_combobox.setItemText(3, _translate("MainWindow", "SRP1"))
        self.bmp_combobox.setItemText(4, _translate("MainWindow", "SRP2"))
        self.bmp_combobox.setItemText(5, _translate("MainWindow", "SRP3"))
        self.bmp_combobox.setItemText(6, _translate("MainWindow", "SRP4"))
        self.bmp_combobox.setItemText(7, _translate("MainWindow", "SRP5"))
        self.bmp_combobox.setItemText(8, _translate("MainWindow", "SRP6"))
        self.bmp_combobox.setItemText(9, _translate("MainWindow", "SRP7"))
        self.bmp_combobox.setItemText(10, _translate("MainWindow", "SRP8"))
        self.bmp_combobox.setItemText(11, _translate("MainWindow", "SRP9"))
        self.bmp_combobox.setItemText(12, _translate("MainWindow", "SIP1"))
        self.bmp_combobox.setItemText(13, _translate("MainWindow", "SIP2"))
        self.bmp_combobox.setItemText(14, _translate("MainWindow", "SRP10"))
        self.bmp_combobox.setItemText(15, _translate("MainWindow", "SRP11"))
        self.bmp_combobox.setItemText(16, _translate("MainWindow", "SRP12"))
        self.bmp_combobox.setItemText(17, _translate("MainWindow", "SRP13"))
        self.bmp_combobox.setItemText(18, _translate("MainWindow", "SRP14"))
        self.bmp_combobox.setItemText(19, _translate("MainWindow", "SRP15"))
        self.bmp_combobox.setItemText(20, _translate("MainWindow", "SRP16"))
        self.bmp_combobox.setItemText(21, _translate("MainWindow", "SRP17"))
        self.bmp_combobox.setItemText(22, _translate("MainWindow", "SEP5"))
        self.bmp_combobox.setItemText(23, _translate("MainWindow", "SEP4"))
        self.bmp_combobox.setItemText(24, _translate("MainWindow", "SEP3"))
        self.bmp_combobox.setItemText(25, _translate("MainWindow", "SEP1"))
        self.bmp_combobox.setItemText(26, _translate("MainWindow", "SEP0"))
        self.bmp_combobox.setItemText(27, _translate("MainWindow", "NEP0"))
        self.bmp_combobox.setItemText(28, _translate("MainWindow", "NEP1"))
        self.bmp_combobox.setItemText(29, _translate("MainWindow", "NEP3"))
        self.bmp_combobox.setItemText(30, _translate("MainWindow", "NEP4"))
        self.bmp_combobox.setItemText(31, _translate("MainWindow", "NEP5"))
        self.bmp_combobox.setItemText(32, _translate("MainWindow", "NRP17"))
        self.bmp_combobox.setItemText(33, _translate("MainWindow", "NRP16"))
        self.bmp_combobox.setItemText(34, _translate("MainWindow", "NRP15"))
        self.bmp_combobox.setItemText(35, _translate("MainWindow", "NRP14"))
        self.bmp_combobox.setItemText(36, _translate("MainWindow", "NRP13"))
        self.bmp_combobox.setItemText(37, _translate("MainWindow", "NRP12"))
        self.bmp_combobox.setItemText(38, _translate("MainWindow", "NRP11"))
        self.bmp_combobox.setItemText(39, _translate("MainWindow", "NRP10"))
        self.bmp_combobox.setItemText(40, _translate("MainWindow", "NIP3"))
        self.bmp_combobox.setItemText(41, _translate("MainWindow", "NIP1"))
        self.bmp_combobox.setItemText(42, _translate("MainWindow", "NRP9"))
        self.bmp_combobox.setItemText(43, _translate("MainWindow", "NRP8"))
        self.bmp_combobox.setItemText(44, _translate("MainWindow", "NRP7"))
        self.bmp_combobox.setItemText(45, _translate("MainWindow", "NRP6"))
        self.bmp_combobox.setItemText(46, _translate("MainWindow", "NRP5"))
        self.bmp_combobox.setItemText(47, _translate("MainWindow", "NRP4"))
        self.bmp_combobox.setItemText(48, _translate("MainWindow", "NRP3"))
        self.bmp_combobox.setItemText(49, _translate("MainWindow", "NRP2"))
        self.bmp_combobox.setItemText(50, _translate("MainWindow", "NRP1"))
        self.bmp_combobox.setItemText(51, _translate("MainWindow", "NTP4"))
        self.bmp_combobox.setItemText(52, _translate("MainWindow", "NTP2"))
        self.bmp_combobox.setItemText(53, _translate("MainWindow", "NTP0"))
        self.write_to_file_button.setText(_translate("MainWindow", "Save to Files"))
        self.x_checkbox.setText(_translate("MainWindow", "x"))
        self.z_checkbox.setText(_translate("MainWindow", "z"))
        self.seconds_label.setText(_translate("MainWindow", "s"))
        self.I_checkbox.setText(_translate("MainWindow", "i"))
        self.recording_time_label.setText(_translate("MainWindow", "Recording time:"))
        self.graph_options_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Graph Options</span></p></body></html>"))
        self.on_button.setText(_translate("MainWindow", "All pv on"))
        self.bpm_label.setText(_translate("MainWindow", "BPM:"))
        self.channel_label.setText(_translate("MainWindow", "channel:"))
        self.channel_combobox.setItemText(0, _translate("MainWindow", "x"))
        self.channel_combobox.setItemText(1, _translate("MainWindow", "z"))
        self.channel_combobox.setItemText(2, _translate("MainWindow", "I"))
        self.show_button.setText(_translate("MainWindow", "Show"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.file_rec_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">File Recording</span></p></body></html>"))
        self.note_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">note</span>: don\'t forget to turn off <br/>all pvs before viewing <br/>the graphs and recording files</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())