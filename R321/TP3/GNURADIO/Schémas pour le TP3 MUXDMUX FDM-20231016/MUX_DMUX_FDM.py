#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Multiplexeur démultiplexeur FDM
# Author: Philippe PUJAS
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class MUX_DMUX_FDM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multiplexeur démultiplexeur FDM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multiplexeur démultiplexeur FDM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "MUX_DMUX_FDM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1920000/2
        self.num_canal_C = num_canal_C = 3.4
        self.num_canal_B = num_canal_B = 3
        self.num_canal_A = num_canal_A = 0
        self.chsp = chsp = 20000
        self.ch0 = ch0 = 50000
        self.canal_sel = canal_sel = 0
        self.audio_rate = audio_rate = 48000
        self.BP = BP = 18000

        ##################################################
        # Blocks
        ##################################################
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 1

        _canal_sel_dial_control = qtgui.GrDialControl('Canal', self, 0,5,0,"default",self.set_canal_sel,isFloat, scaleFactor, 100, True, "'value'")
        self.canal_sel = _canal_sel_dial_control

        self.top_layout.addWidget(_canal_sel_dial_control)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=int(samp_rate/audio_rate),
                taps=[],
                fractional_bw=0)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_f(
            4096, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-150, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['Programme A', 'Programme B', 'Programme C', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            4096, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-150, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['Programme démultiplexé', 'trc1', 'v1', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            4096, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-150, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Multiplex des programmes A,B,C', 'trc1', 'v1', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                samp_rate,
                BP/2,
                300,
                window.WIN_HAMMING,
                6.76))
        self.blocks_wavfile_source_0_0_0 = blocks.wavfile_source('/home/lucky/Desktop/IUT-cours/R321/TP3/GNURADIO/Fichiers Wav échantillonnées à 960 kHz pour le TP3-20231016/09-960k.wav', True)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/home/lucky/Desktop/IUT-cours/R321/TP3/GNURADIO/12-large-960k.wav', True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/lucky/Desktop/IUT-cours/R321/TP3/GNURADIO/Fichiers Wav échantillonnées à 960 kHz pour le TP3-20231016/01-960k.wav', True)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                canal_sel*chsp+ch0-BP/2,
                canal_sel*chsp+ch0+BP/2,
                200,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(audio_rate, '', True)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, canal_sel*chsp+ch0, 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, ch0+num_canal_C*chsp, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, ch0+num_canal_B*chsp, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, ch0+num_canal_A*chsp, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.qtgui_freq_sink_x_0_1, 1))
        self.connect((self.blocks_wavfile_source_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_wavfile_source_0_0_0, 0), (self.qtgui_freq_sink_x_0_1, 2))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MUX_DMUX_FDM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.canal_sel*self.chsp+self.ch0-self.BP/2, self.canal_sel*self.chsp+self.ch0+self.BP/2, 200, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(2, self.samp_rate, self.BP/2, 300, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)

    def get_num_canal_C(self):
        return self.num_canal_C

    def set_num_canal_C(self, num_canal_C):
        self.num_canal_C = num_canal_C
        self.analog_sig_source_x_0_0_0.set_frequency(self.ch0+self.num_canal_C*self.chsp)

    def get_num_canal_B(self):
        return self.num_canal_B

    def set_num_canal_B(self, num_canal_B):
        self.num_canal_B = num_canal_B
        self.analog_sig_source_x_0_0.set_frequency(self.ch0+self.num_canal_B*self.chsp)

    def get_num_canal_A(self):
        return self.num_canal_A

    def set_num_canal_A(self, num_canal_A):
        self.num_canal_A = num_canal_A
        self.analog_sig_source_x_0.set_frequency(self.ch0+self.num_canal_A*self.chsp)

    def get_chsp(self):
        return self.chsp

    def set_chsp(self, chsp):
        self.chsp = chsp
        self.analog_sig_source_x_0.set_frequency(self.ch0+self.num_canal_A*self.chsp)
        self.analog_sig_source_x_0_0.set_frequency(self.ch0+self.num_canal_B*self.chsp)
        self.analog_sig_source_x_0_0_0.set_frequency(self.ch0+self.num_canal_C*self.chsp)
        self.analog_sig_source_x_0_1.set_frequency(self.canal_sel*self.chsp+self.ch0)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.canal_sel*self.chsp+self.ch0-self.BP/2, self.canal_sel*self.chsp+self.ch0+self.BP/2, 200, window.WIN_HAMMING, 6.76))

    def get_ch0(self):
        return self.ch0

    def set_ch0(self, ch0):
        self.ch0 = ch0
        self.analog_sig_source_x_0.set_frequency(self.ch0+self.num_canal_A*self.chsp)
        self.analog_sig_source_x_0_0.set_frequency(self.ch0+self.num_canal_B*self.chsp)
        self.analog_sig_source_x_0_0_0.set_frequency(self.ch0+self.num_canal_C*self.chsp)
        self.analog_sig_source_x_0_1.set_frequency(self.canal_sel*self.chsp+self.ch0)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.canal_sel*self.chsp+self.ch0-self.BP/2, self.canal_sel*self.chsp+self.ch0+self.BP/2, 200, window.WIN_HAMMING, 6.76))

    def get_canal_sel(self):
        return self.canal_sel

    def set_canal_sel(self, canal_sel):
        self.canal_sel = canal_sel
        self.analog_sig_source_x_0_1.set_frequency(self.canal_sel*self.chsp+self.ch0)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.canal_sel*self.chsp+self.ch0-self.BP/2, self.canal_sel*self.chsp+self.ch0+self.BP/2, 200, window.WIN_HAMMING, 6.76))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

    def get_BP(self):
        return self.BP

    def set_BP(self, BP):
        self.BP = BP
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.canal_sel*self.chsp+self.ch0-self.BP/2, self.canal_sel*self.chsp+self.ch0+self.BP/2, 200, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(2, self.samp_rate, self.BP/2, 300, window.WIN_HAMMING, 6.76))




def main(top_block_cls=MUX_DMUX_FDM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
