##################################################################
#
#   This is the About File.
#
#   Note: Future contribution should be added here
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


import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class AboutBox(QMessageBox):
    def __init__(self, parent=None):
        super(AboutBox, self).__init__(parent)
        self.setTextFormat(Qt.TextFormat.RichText)
        self.setText("<h1>Photobioreactor Operation System</h1>\
                    Versionnumber: v.1.0<br>\
                    Published:     23.10.2025<br>\
                    2025 Algea PBR 1.0 Team<br><br>\
                    <u>Team:</u>\
                    <table>\
                    <tr><td>Project Manager & Software</td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>Andreas Müller</td></tr>\
                    <tr><td>Lead of Laboratory & Algea</td><td></td><td>Emilia Ruan Sardi</td></tr>\
                    <tr><td>Lead of Electronics</td><td></td><td>Malik Bosnic</td></tr>\
                    <tr><td>Lead of Meachanic</td><td></td><td>Matthew Niccol</td></tr>\
                    </table>\
                     <br><br>\
                     GUI was created with Qt Designer<br>\
                     <img src=EN_Co-fundedbytheEU_RGB_POS.png width=300>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = AboutBox()
    form.show()
    app.exec()