import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class AboutBox(QMessageBox):
    def __init__(self, parent=None):
        super(AboutBox, self).__init__(parent)
        self.setTextFormat(Qt.TextFormat.RichText)
        self.setText("<h1>Photobioreactor Operation System</h1>\
                    Versionnumber: v.0.1<br>\
                    Published:     23.10.2025<br>\
                    2025 Algea PBR 1.0 Team<br><br>\
                    <u>Team:</u>\
                    <table>\
                    <tr><td>Project Manager & Software</td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>Andreas Müller</td></tr>\
                    <tr><td>Lead of Laboratory & Algea</td><td></td><td>Emilia Ruan Sardi</td></tr>\
                    <tr><td>Lead of Electronics</td><td></td><td>Malik Bosnic</td></tr>\
                    <tr><td>Lead of Meachanic</td><td></td><td>Matthew Niccol</td></tr>\
                    </table>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = AboutBox()
    form.show()
    app.exec()