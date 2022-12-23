import numpy as np
import epics
import time

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

channel = 'x'

t0 = 0.0
ns = []
data = []

def set_bpms_on_off(on, name, bpm_set):
    for bpm in bpm_set:
        epics.PV(name+':'+bpm+':connect-Cmd').put(on)

def onChanged(pvname=None, nanoseconds=None, value=None, char_value=None, **kw):
    global t0, ns, data
    if len(ns) > 0 and ns[-1] > t0 + nanoseconds / 1000000000:
        t0 += 1
    ns.append(t0 + nanoseconds / 1000000000)
    data.append(value)


for bpm_vepp_3 in vepp3_bpms:
    set_bpms_on_off(0, 'VEPP3', vepp3_bpms)
    print('off')
for bpm_vepp_4 in vepp4_bpms:
    set_bpms_on_off(0, 'VEPP4', vepp4_bpms)
for bpm in vepp4_bpms:
    epics.PV('VEPP4:' + bpm + ':connect-Cmd').put(1)
    pv_mode_lowfreq = epics.PV('VEPP4:' + bpm + ':mode_lowfreq-Cmd')
    pv_lowfreq_raw = epics.PV('VEPP4:' + bpm + ':lowfreq_raw-Cmd')
    pv_cur_channel = epics.PV('VEPP4:' + bpm + ':lowfreq_fofb_' + channel + '-I')

    pv_lowfreq_raw.put(1)
    pv_mode_lowfreq.put(30)
    pv_cur_channel.add_callback(onChanged)

    time.sleep(1)
    print('ready')

    pv_cur_channel.clear_callbacks()
    pv_mode_lowfreq.put(0)
    pv_lowfreq_raw.put(0)
    epics.PV('VEPP4:' + bpm + ':connect-Cmd').put(0)

    zipped = zip(ns, data)
    np.savetxt(bpm + '_' + channel + '.log', zipped, fmt='%i, %i')
    t0 = 0
    t0 = []
    data = [0]
