# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # from epics import caget, camonitor
#
# # def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# # camonitor('VEPP4:orbit:e1_x-I')
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
#     # print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# import epics
# import time
# import pyqtgraph as pg
# import numpy as np
#
# win = pg.GraphicsLayoutWidget(show=True)
# p1 = win.addPlot()
# plot_data = p1.plot([1, 2, 3])
# # win.show()
#


import pyepics
import time
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np




#
# fofb_x = pyepics.PV('VEPP4:NEP3:lowfreq_fofb_x-I')
# fofb_x.add_callback(onChanges())


from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        mode_lowfreq_pv = pyepics.PV('VEPP4:NEP3:mode_lowfreq-Cmd')
        mode_lowfreq_pv.put(10)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = []  # 100 time points
        self.y = []  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        self.fofb_x = pyepics.PV('VEPP4:NEP3:lowfreq_fofb_x-I')
        self.fofb_x.add_callback(self.onChanges)
        self.t0 = time.time()
        self.mean = 0.


    def onChanges(self, pvname=None, value=None, char_value=None, **kw):
        if len(self.x) > 500:
            self.x = self.x[1:]  # Remove the first y element.
            self.y = self.y[1:]  # Remove the first

        self.x.append(time.time() - self.t0)  # Add a new value 1 higher than the last.
        self.y.append(self.fofb_x.value)  # Add a new random value.
        self.mean = np.mean(self.y)
        temp = []
        for i in range(len(self.y)):
            temp.append(self.y[i] - self.mean)
        self.data_line.setData(self.x, temp)  # Update the data.


def onChanges(pvname=None, nanoseconds=None, value=None, char_value=None, **kw):
    f.write(str(nanoseconds))
    f.write(' ')
    f.write(str(value))
    f.write('\n')

mode_lowfreq_pv = epics.PV('VEPP4:SEP0:mode_lowfreq-Cmd')
mode_lowfreq_pv.put(10)
lowfreq_pv_raw = epics.PV('VEPP4:SEP0:lowfreq_raw-Cmd')
lowfreq_pv_raw.put(1)
f = open('data_x_pv_time_30_SEP0_24_10_22_4.log', 'w')
fofb_x = epics.PV('VEPP4:SEP0:lowfreq_fofb_x-I')
fofb_x.add_callback(onChanges)
time.sleep(10)
fofb_x.clear_callbacks()
f.close()

#
# app = QtWidgets.QApplication(sys.argv)
# w = MainWindow()
# w.show()
# sys.exit(app.exec_())