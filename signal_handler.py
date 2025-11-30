# Signal Handler
# Funktion: Zentralle Klasse zum Verwalten der Signale
#
from PyQt6.QtCore import QObject, pyqtSignal


class SignalManager(QObject):
    measurement_started = pyqtSignal(str)
    measurement_stopped = pyqtSignal(str)
    measurement_killed = pyqtSignal(str)
    measure_signal = pyqtSignal(list)

    new_ph_value_calculated = pyqtSignal(float)



signal_manager = SignalManager()