import sys
import mainWindow
from PyQt6.QtWidgets import *


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = mainWindow.PBRMainWindow()
    form.show()
    app.exec()

if __name__ == '__main__':
    main()