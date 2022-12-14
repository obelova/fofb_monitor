# -*- coding: utf-8 -*-
import time

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.interpolate import interp1d
import epics

vepp4_bpms = ["STP0", "STP2", "STP4",
              "SRP1", "SRP2", "SRP3", "SRP4", "SRP5", "SRP6", "SRP7", "SRP8", "SRP9",
              "SIP1", "SIP2",
              "SRP10", "SRP11", "SRP12", "SRP13", "SRP14", "SRP15", "SRP16", "SRP17",
              "SEP5", "SEP4", "SEP3", "SEP1", "SEP0",
              "NEP0", "NEP1", "NEP3", "NEP4", "NEP5",
              "NRP17", "NRP16", "NRP15", "NRP14", "NRP13", "NRP12", "NRP11", "NRP10",
              "NIP3", "NIP1",
              "NRP9", "NRP8", "NRP7", "NRP6", "NRP5", "NRP4", "NRP3", "NRP2", "NRP1",
              "NTP4", "NTP2", "NTP0"]

vepp3_bpms = ["1P1", "1P2", "1P3", "1P5", "1P6", "1P7", "2P3", "2P4", "2P5", "2P6", "3P1",
              "3P2", "3P3", "3P5", "3P6", "3P8", "4P2", "4P4", "4P5", "4P6"]


def calc_step(x):
    steps = x[1:] - x[:-1]
    return np.percentile(steps, 50)


def calc_fft(t, x, spline_kind='linear'):
    # t, x - input data
    # N - number of sample points
    step = calc_step(np.array(t))
    N = int((t[-1] - t[0]) // step)
    x_sample, step = np.linspace(t[0], t[-1], N, retstep=True)

    if spline_kind == 'None':
        y_sample = x
    else:
        f = interp1d(t, x, kind=spline_kind)
        y_sample = f(x_sample)

    yf = 2.0 * np.abs(fft(y_sample, norm="forward"))[:N // 2]
    xf = fftfreq(N, step)[:N // 2]
    return xf, yf


def set_bpms_on_off(on, name, bpm_set):
    for bpm in bpm_set:
        epics.PV(name+':'+bpm+':connect-Cmd').put(on)


def update_graph(graph, x, y):
    graph.setData(x, y)


def cut_data(x, y, num):
    return x[num:], y[num:]


class Ui_MainWindow(object):

    pen = pg.mkPen(color=(255, 0, 0))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 680)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LABEL_GRAPH_OPTIONS = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_GRAPH_OPTIONS.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.LABEL_GRAPH_OPTIONS.setObjectName("LABEL_GRAPH_OPTIONS")

        self.V_RAD_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.V_RAD_4.setGeometry(QtCore.QRect(90, 50, 120, 20))
        self.V_RAD_4.setChecked(True)
        self.V_RAD_4.setAutoExclusive(False)
        self.V_RAD_4.setObjectName("V_RAD_4")
        self.V_RAD_4.toggled.connect(self.v_rad_4_onClicked)

        self.V_RAD_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.V_RAD_3.setGeometry(QtCore.QRect(90, 80, 120, 20))
        self.V_RAD_3.setChecked(True)
        self.V_RAD_3.setAutoExclusive(False)
        self.V_RAD_3.setObjectName("V_RAD_3")
        self.V_RAD_3.toggled.connect(self.v_rad_3_onClicked)

        self.V_LABEL_BPM = QtWidgets.QLabel(self.centralwidget)
        self.V_LABEL_BPM.setGeometry(QtCore.QRect(60, 120, 55, 20))
        self.V_LABEL_BPM.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.V_LABEL_BPM.setObjectName("V_LABEL_BPM")

        self.V_BPM = QtWidgets.QComboBox(self.centralwidget)
        self.V_BPM.setGeometry(QtCore.QRect(130, 120, 80, 22))
        self.V_BPM.setObjectName("V_BPM")
        self.V_BPM.addItems(vepp4_bpms)

        self.V_LABEL_CHANNEL = QtWidgets.QLabel(self.centralwidget)
        self.V_LABEL_CHANNEL.setGeometry(QtCore.QRect(60, 150, 55, 20))
        self.V_LABEL_CHANNEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.V_LABEL_CHANNEL.setObjectName("V_LABEL_CHANNEL")

        self.V_CHANNEL = QtWidgets.QComboBox(self.centralwidget)
        self.V_CHANNEL.setGeometry(QtCore.QRect(130, 150, 80, 22))
        self.V_CHANNEL.setObjectName("V_CHANNEL")
        self.V_CHANNEL.addItems(vepp3_bpms)

        self.V_ON_OFF = QtWidgets.QRadioButton(self.centralwidget)
        self.V_ON_OFF.setGeometry(QtCore.QRect(90, 210, 151, 20))
        self.V_ON_OFF.setObjectName("V_ON_OFF")
        self.V_ON_OFF.toggled.connect(self.v_on_off_onClicked)

        self.cur_time_in_sec = 0
        self.t = []
        self.sig = []

        self.GRAPH = PlotWidget(self.centralwidget)
        self.GRAPH.setGeometry(QtCore.QRect(310, 20, 780, 290))
        self.GRAPH.setObjectName("GRAPH")
        self.GRAPH.setBackground('w')
        self.GRAPH.setLabel("bottom", "Time (s)")
        self.GRAPH.setLabel("left", "(mm)")
        self.GRAPH.showGrid(x=True, y=True)
        self.GRAPH_PLOT = self.GRAPH.plot(self.t, self.sig, pen=self.pen)

        self.f = []
        self.ampl = []

        self.FOURIER = PlotWidget(self.centralwidget)
        self.FOURIER.setGeometry(QtCore.QRect(310, 330, 780, 290))
        self.FOURIER.setObjectName("FOURIER")
        self.FOURIER.setBackground('w')
        self.FOURIER.setLabel("bottom", "Frequency (Hz)")
        self.FOURIER.setLabel("left", "Amplitude (mm)")
        self.FOURIER.showGrid(x=True, y=True)
        self.FOURIER_PLOT = self.FOURIER.plot(self.f, self.ampl, pen=self.pen)

        #### RECORDING FILES

        self.LABEL_FILE_RECORDING = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_FILE_RECORDING.setGeometry(QtCore.QRect(20, 330, 101, 21))
        self.LABEL_FILE_RECORDING.setObjectName("LABEL_FILE_RECORDING")

        self.F_LABEL_SIZE = QtWidgets.QLabel(self.centralwidget)
        self.F_LABEL_SIZE.setGeometry(QtCore.QRect(50, 360, 55, 20))
        self.F_LABEL_SIZE.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.F_LABEL_SIZE.setObjectName("F_LABEL_SIZE")

        self.F_SIZE = QtWidgets.QLineEdit(self.centralwidget)
        self.F_SIZE.setGeometry(QtCore.QRect(130, 360, 80, 22))
        self.F_SIZE.setObjectName("F_SIZE")

        #self.F_LABEL_BPM = QtWidgets.QLabel(self.centralwidget)
        #self.F_LABEL_BPM.setGeometry(QtCore.QRect(50, 390, 55, 20))
        #self.F_LABEL_BPM.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #self.F_LABEL_BPM.setObjectName("F_LABEL_BPM")

        #self.F_BPM = QtWidgets.QComboBox(self.centralwidget)
        #self.F_BPM.setGeometry(QtCore.QRect(130, 390, 80, 22))
        #self.F_BPM.setObjectName("F_BPM")
        #self.F_BPM.addItems(vepp4_bpms)

        self.F_X = QtWidgets.QCheckBox(self.centralwidget)
        self.F_X.setGeometry(QtCore.QRect(130, 430, 81, 20))
        self.F_X.setObjectName("F_X")

        self.F_Z = QtWidgets.QCheckBox(self.centralwidget)
        self.F_Z.setGeometry(QtCore.QRect(130, 460, 81, 20))
        self.F_Z.setObjectName("F_Z")

        self.F_I = QtWidgets.QCheckBox(self.centralwidget)
        self.F_I.setGeometry(QtCore.QRect(130, 490, 81, 20))
        self.F_I.setObjectName("F_I")

        self.F_REC = QtWidgets.QPushButton(self.centralwidget)
        self.F_REC.setEnabled(True)
        self.F_REC.setGeometry(QtCore.QRect(130, 520, 93, 28))
        self.F_REC.setObjectName("F_REC")

        self.files = dict(x=None, z=None, I=None)

        #self.F_3D_REC = QtWidgets.QPushButton(self.centralwidget)
        #self.F_3D_REC.setGeometry(QtCore.QRect(130, 560, 93, 28))
        #self.F_3D_REC.setObjectName("F_3D_REC")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def v_rad_4_onClicked(self):
        set_bpms_on_off(self.V_RAD_4.isChecked(), 'VEPP4', vepp4_bpms)

    def v_rad_3_onClicked(self):
        set_bpms_on_off(self.V_RAD_3.isChecked(), 'VEPP3', vepp3_bpms)

    def v_on_off_onClicked(self):
        cur_bpm = self.V_BPM.currentText()
        cur_channel = self.V_CHANNEL.currentText()
        epics.PV('VEPP4:' + cur_bpm + ':connect-Cmd').put(1)

        pv_mode_lowfreq = epics.PV('VEPP4:' + cur_bpm + ':mode_lowfreq-Cmd')
        pv_lowfreq_raw = epics.PV('VEPP4:' + cur_bpm + ':lowfreq_raw-Cmd')
        pv_cur_channel = epics.PV('VEPP4:' + cur_bpm + ':lowfreq_fofb_' + cur_channel + '-I')

        if self.V_ON_OFF.isChecked():
            self.V_BPM.setDisabled(1)
            self.V_CHANNEL.setDisabled(1)

            pv_lowfreq_raw.put(1)
            pv_mode_lowfreq.put(30)
            pv_cur_channel.add_callback(self.v_pv_onChanged)
        else:
            pv_cur_channel.clear_callbacks()
            pv_mode_lowfreq.put(0)
            pv_lowfreq_raw.put(0)

            self.V_RAD_4.setChecked(True)
            self.V_RAD_3.setChecked(True)
            self.cur_time_in_sec = 0.0

            self.t = []
            self.sig = []

            self.V_BPM.setDisabled(0)
            self.V_CHANNEL.setDisabled(0)

    def v_pv_onChanged(self, pvname=None, nanoseconds=None, value=None, char_value=None, **kw):
        self.v_append_data(nanoseconds, value)
        if len(self.t) == 500:
            self.v_update_plots(self.t, self.sig)
            self.t, self.sig = cut_data(self.t, self.sig, 50)

    def v_update_plots(self, x, y):
        update_graph(self.GRAPH_PLOT, x, y)
        f, ampl = calc_fft(x, y)
        update_graph(self.FOURIER_PLOT, f[1:], ampl[1:])

    def v_append_data(self, nanoseconds, value):
        if len(self.t) > 0 and self.t[-1] > self.cur_time_in_sec + nanoseconds / 1000000000:
            self.cur_time_in_sec += 1
        self.t.append(self.cur_time_in_sec + nanoseconds / 1000000000)
        self.sig.append(value)

    def f_pv_onChanges(self, pvname=None, nanoseconds=None, value=None, char_value=None, **kw):
        cur_channel = pvname[-3]

    def f_rec_onClicked(self):
        time_in_sec = float(self.F_SIZE.text())
        cur_bpm = self.V_BPM.currentText()

        isChecked = dict([('x', self.F_X.isChecked()), ('z', self.F_Z.isChecked()), ('I', self.F_I.isChecked())])
        pvs = []

        pv_mode_lowfreq = epics.PV('VEPP4:' + cur_bpm + ':mode_lowfreq-Cmd')
        pv_lowfreq_raw = epics.PV('VEPP4:' + cur_bpm + ':lowfreq_raw-Cmd')
        pv_nturns = epics.PV('VEPP4:' + cur_bpm + ':nturns_lowfreq-SP')

        pv_lowfreq_raw.put(1)
        pv_mode_lowfreq.put(30)
        pv_nturns.put(800)

        i = 0
        for key, value in isChecked.items():
            if value:
                pvs[i] = epics.PV('VEPP4:' + cur_bpm + ':lowfreq_fofb_' + key + '-I')
                ++i
                filename = cur_bpm + '_' + key + '.log'
                self.files[key] = open(filename, 'w')
                pvs[i].add_callback(self.f_pv_onChanges)

        time.sleep(time_in_sec)
        for pv in pvs:
            pv.clear_callbacks()
        for k, v in self.files.items():
            if v is not None:
                v.close()

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
        # self.F_LABEL_BPM.setText(_translate("MainWindow", "BPM:"))
        # self.F_BPM.setItemText(0, _translate("MainWindow", "STP0"))
        # self.F_BPM.setItemText(1, _translate("MainWindow", "STP2"))
        # self.F_BPM.setItemText(2, _translate("MainWindow", "STP4"))
        # self.F_BPM.setItemText(3, _translate("MainWindow", "SRP1"))
        # self.F_BPM.setItemText(4, _translate("MainWindow", "SRP2"))
        # self.F_BPM.setItemText(5, _translate("MainWindow", "SRP3"))
        # self.F_BPM.setItemText(6, _translate("MainWindow", "SRP4"))
        # self.F_BPM.setItemText(7, _translate("MainWindow", "SRP5"))
        # self.F_BPM.setItemText(8, _translate("MainWindow", "SRP6"))
        # self.F_BPM.setItemText(9, _translate("MainWindow", "SRP7"))
        # self.F_BPM.setItemText(10, _translate("MainWindow", "SRP8"))
        # self.F_BPM.setItemText(11, _translate("MainWindow", "SRP9"))
        # self.F_BPM.setItemText(12, _translate("MainWindow", "SIP1"))
        # self.F_BPM.setItemText(13, _translate("MainWindow", "SIP2"))
        # self.F_BPM.setItemText(14, _translate("MainWindow", "SRP10"))
        # self.F_BPM.setItemText(15, _translate("MainWindow", "SRP11"))
        # self.F_BPM.setItemText(16, _translate("MainWindow", "SRP12"))
        # self.F_BPM.setItemText(17, _translate("MainWindow", "SRP13"))
        # self.F_BPM.setItemText(18, _translate("MainWindow", "SRP14"))
        # self.F_BPM.setItemText(19, _translate("MainWindow", "SRP15"))
        # self.F_BPM.setItemText(20, _translate("MainWindow", "SRP16"))
        # self.F_BPM.setItemText(21, _translate("MainWindow", "SRP17"))
        # self.F_BPM.setItemText(22, _translate("MainWindow", "SEP5"))
        # self.F_BPM.setItemText(23, _translate("MainWindow", "SEP4"))
        # self.F_BPM.setItemText(24, _translate("MainWindow", "SEP3"))
        # self.F_BPM.setItemText(25, _translate("MainWindow", "SEP1"))
        # self.F_BPM.setItemText(26, _translate("MainWindow", "SEP0"))
        # self.F_BPM.setItemText(27, _translate("MainWindow", "NEP0"))
        # self.F_BPM.setItemText(28, _translate("MainWindow", "NEP1"))
        # self.F_BPM.setItemText(29, _translate("MainWindow", "NEP3"))
        # self.F_BPM.setItemText(30, _translate("MainWindow", "NEP4"))
        # self.F_BPM.setItemText(31, _translate("MainWindow", "NEP5"))
        # self.F_BPM.setItemText(32, _translate("MainWindow", "NRP17"))
        # self.F_BPM.setItemText(33, _translate("MainWindow", "NRP16"))
        # self.F_BPM.setItemText(34, _translate("MainWindow", "NRP15"))
        # self.F_BPM.setItemText(35, _translate("MainWindow", "NRP14"))
        # self.F_BPM.setItemText(36, _translate("MainWindow", "NRP13"))
        # self.F_BPM.setItemText(37, _translate("MainWindow", "NRP12"))
        # self.F_BPM.setItemText(38, _translate("MainWindow", "NRP11"))
        # self.F_BPM.setItemText(39, _translate("MainWindow", "NRP10"))
        # self.F_BPM.setItemText(40, _translate("MainWindow", "NIP3"))
        # self.F_BPM.setItemText(41, _translate("MainWindow", "NIP1"))
        # self.F_BPM.setItemText(42, _translate("MainWindow", "NRP9"))
        # self.F_BPM.setItemText(43, _translate("MainWindow", "NRP8"))
        # self.F_BPM.setItemText(44, _translate("MainWindow", "NRP7"))
        # self.F_BPM.setItemText(45, _translate("MainWindow", "NRP6"))
        # self.F_BPM.setItemText(46, _translate("MainWindow", "NRP5"))
        # self.F_BPM.setItemText(47, _translate("MainWindow", "NRP4"))
        # self.F_BPM.setItemText(48, _translate("MainWindow", "NRP3"))
        # self.F_BPM.setItemText(49, _translate("MainWindow", "NRP2"))
        # self.F_BPM.setItemText(50, _translate("MainWindow", "NRP1"))
        # self.F_BPM.setItemText(51, _translate("MainWindow", "NTP4"))
        # self.F_BPM.setItemText(52, _translate("MainWindow", "NTP2"))
        # self.F_BPM.setItemText(53, _translate("MainWindow", "NTP0"))
        #self.F_3D_REC.setText(_translate("MainWindow", "3D"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
