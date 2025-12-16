##################################################################
#
#   This is the main File, where the Main Windows is initilized
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
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import dialogs
from simplePage import SimplePage
from Dashboard import Dashboard
from pH_calibration import pHCalibration
from signal_handler import signal_manager

class PBRMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PBRMainWindow, self).__init__(parent)

        #Subwidget initialization
        #The Subwidget will be initialized later at "Window Initialization"
        self.pages = [
            Dashboard(parent=self),
            pHCalibration(self),
            SimplePage("Platzhalter Sensoren","sdklajföksad")
        ]

        #Placeholder for subprocesses
        self.p = None

        #menu initialization
        pbrOS_menu = self.menuBar().addMenu("PBR OS")
        close_action = self.addAction("&Exit",self.close_app,None,None,None,None)
        pbrOS_menu.addAction(close_action)

        pbrWindow_menu = self.menuBar().addMenu("View")
        dashboard_action = self.addAction("Dashboard",self.dashboard)
        process_action = self.addAction("Process Control",self.processControl)
        light_action = self.addAction("Light Control",self.lightControl)
        sensor_action = self.addAction("Sensor Control",self.sensorControl)
        sensorCal_action = self.addAction("Sensor Calibration",self.sensorCalControl)
        pbrWindow_toAdd = (
            dashboard_action,sensorCal_action#,process_action,light_action,sensor_action
        )
        for action in pbrWindow_toAdd:
            pbrWindow_menu.addAction(action)

        extras_menu = self.menuBar().addMenu("Extras")
        about_action = self.addAction("About",self.about)
        extras_menu.addAction(about_action)

        #window initilization
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        for p in self.pages:
            eff = QGraphicsOpacityEffect(p)
            p.setGraphicsEffect(eff)
            eff.setOpacity(1.0)
            self.stack.addWidget(p)
        
        #Statusbar Initalisierung
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.Shape.StyledPanel|QFrame.Shadow.Sunken)
        self.sizeLabel.setText("PBR OS v.1.0")
        status = self.statusBar()
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready",0)
        ##Statusbar Benachrichtigungen Initalisieren
        signal_manager.measurement_started.connect(self.statusBar().showMessage)
        signal_manager.measurement_stopped.connect(self.statusBar().showMessage)
        signal_manager.measurement_killed.connect(self.statusBar().showMessage)

    #Little helper function to initialize slots, shortcuts, icons, tips, etc.
    #for usage look into the code above and learn how it was used
    def addAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False):
        action = QAction(text,self)
        if icon is not None:
            pass
        if shortcut is not None:
            pass
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        return action
    
    #Actions, here you should add function that have to be executed when you press a button.
    def close_app(self):
        self.close()
    def dashboard(self):
        self.stack.setCurrentIndex(0)
    def processControl(self):
        self.stack.setCurrentIndex(2)
    def lightControl(self):
        pass
    def sensorControl(self):
        pass
    def sensorCalControl(self):
        self.stack.setCurrentIndex(1)
    def about(self):
        message = dialogs.AboutBox()
        message.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = PBRMainWindow()
    form.show()
    app.exec()