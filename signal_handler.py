##################################################################
#
#   This is the file where every signal is defined globally.
#
#   Note:   Signals need to be implemented to work as a communication
#           ...channel between Widget & Windows. But are not designed
#           ...for continous delivery of measure values.
#   
#   Author: Andreas Müller (Github: aragon0013)
#
# Copyright (C) 2025 Andreas Müller

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
##################################################################

from PyQt6.QtCore import QObject, pyqtSignal


class SignalManager(QObject):
    measurement_started = pyqtSignal(str)
    measurement_stopped = pyqtSignal(str)
    measurement_killed = pyqtSignal(str)
    measure_signal = pyqtSignal(list)

    new_ph_value_calculated = pyqtSignal(float)



signal_manager = SignalManager()