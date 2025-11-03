import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import dialogs
from simplePage import SimplePage

class PBRMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PBRMainWindow, self).__init__(parent)

        #Menü initalisierung
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
            dashboard_action,process_action,light_action,sensor_action,sensorCal_action
        )
        for action in pbrWindow_toAdd:
            pbrWindow_menu.addAction(action)

        extras_menu = self.menuBar().addMenu("Extras")
        about_action = self.addAction("About",self.about)
        extras_menu.addAction(about_action)

        #Fenster Initialisierung
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.pages = [
            SimplePage("Platzhalter Dasbhoard","das ist ein Test"),
            SimplePage("Platzhalter Sensoren","sdklajföksad")
        ]
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

    def addAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False):
        action = QAction(text,self)
        if icon is not None:
            pass
        if shortcut is not None:
            pass
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        #action.setCheckable(checkable) #Ist noch von von ChatGPT übrig geblieben
        if slot is not None:
            action.triggered.connect(slot)
        return action
    
    #Action Actionen
    def close_app(self):
        self.close()
    def dashboard(self):
        self.stack.setCurrentIndex(0)
    def processControl(self):
        self.stack.setCurrentIndex(1)
    def lightControl(self):
        pass
    def sensorControl(self):
        pass
    def sensorCalControl(self):
        pass
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