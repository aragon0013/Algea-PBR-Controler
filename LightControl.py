import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class LightControl(QWidget):
    def __init__(self, parent=None):
        super(LightControl, self).__init__(parent)

        #Hauptinformationen
        #ZUSATZINFO-GridLayout: Koordinaten 0:vertikal, 1:horizontal, 2:grösse vertikal, 3:grösse horizontal
        ##Linien
        ###Horizontale Linien oberbalb und unterhalb der individuellen Cycles Einstellungen
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.line_2 = QFrame(self)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        ###Vertikale Linie Bei Aktivierungscheckboxen
        self.line_3 = QFrame(self)
        self.line_3.setObjectName(u"lin3_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        ##Restliche Logik
        self.setObjectName(u"gridLayoutWidget")
        self.setGeometry(QRect(80, 60, 344, 230))
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        ###Linien Adden
        self.gridLayout.addWidget(self.line, 8, 0, 1, 5)
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 5)
        self.gridLayout.addWidget(self.line_3, 3, 2, 6, 1)

        ###Label
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)

        self.label_8 = QLabel(self)
        self.label_8.setObjectName(u"label_8")
        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)

        self.label_9 = QLabel(self)
        self.label_9.setObjectName(u"label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 2)

        ####Titel
        self.label_10 = QLabel()
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 0, 211, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_10.setFont(font)

        
        ###LineEdits
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 3, 1, 1)

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 6, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 7, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 4, 1, 1)

        self.lineEdit_7 = QLineEdit(self)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 4, 4, 1, 1)

        self.lineEdit_8 = QLineEdit(self)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 5, 4, 1, 1)

        self.lineEdit_9 = QLineEdit(self)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 6, 4, 1, 1)

        self.lineEdit_10 = QLineEdit(self)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 7, 4, 1, 1)

        self.lineEdit_11 = QLineEdit(self)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 9, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 9, 4, 1, 1)


        ###CheckBoxes
        self.checkBox = QCheckBox(self)
        self.checkBox.setObjectName(u"checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 3, 1, 2)

        self.checkBox_2 = QCheckBox(self)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 3, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 4, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 5, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 6, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 7, 1, 1, 1)
        
        #HauptGrid
        self.main_h_grid = QVBoxLayout()
        self.main_h_grid.addWidget(self.label_10,0)
        self.main_h_grid.addLayout(self.gridLayout,1)
        self.setLayout(self.main_h_grid)

        self.retranslateUi(self)

    #Initialisierung Namen 
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"green (550nm)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"blue (550 nm)", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"day", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"individual D/N Cycles", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"night", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"overall settings", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"white (400nm-750nm)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"yellow (590 nm)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"red (660 nm)", None))
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"activated LEDs", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"LED Light Control", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = LightControl()
    form.show()
    app.exec()