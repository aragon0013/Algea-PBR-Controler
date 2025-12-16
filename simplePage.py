##################################################################
#
#   This is a helper Widget. It was used to have placeholders for 
#   the main Window and to test the possiblity to switch windows
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

from PyQt6.QtWidgets import *

class SimplePage(QWidget):
    def __init__(self, title, text):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.addWidget(QLabel(f"<h1>{title}</h1>"))
        layout.addWidget(QLabel(text))
        layout.addStretch()