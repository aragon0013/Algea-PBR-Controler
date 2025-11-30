import sys
import pandas as pd
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from signal_handler import signal_manager
import matplotlib
matplotlib.use("QtAgg")  # wichtig für PyQt6
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class pHCalibration(QWidget):
    def __init__(self,parent=None):
        super(pHCalibration,self).__init__(parent)

        #Signale Empfangen
        signal_manager.measurement_started.connect(self.measure_started)
        signal_manager.measure_signal.connect(self.handle_measure_value)

        #Calibration Variables
        self.v_measure_container = None
        self.ph_measure_container = None
        self.ph_cal_p1 = None
        self.ph_cal_p2 = None
        self.ph_cal_slope = None
        self.ph_cal_offset = None
        self.ph_calc_ready = False


        #Parent Initalisieren
        self.parent = parent

        self.MainLayout = QVBoxLayout(self)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.pH_cal_win_title = QLabel()
        self.pH_cal_win_title.setObjectName(u"pH_cal_win_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pH_cal_win_title.sizePolicy().hasHeightForWidth())
        self.pH_cal_win_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.pH_cal_win_title.setFont(font)

        self.MainLayout.addWidget(self.pH_cal_win_title)

        self.hLayout_v_pH = QHBoxLayout()
        self.hLayout_v_pH.setObjectName(u"hLayout_v_pH")
        self.vLayout_v_main = QVBoxLayout()
        self.vLayout_v_main.setObjectName(u"vLayout_v_main")

        #Graphen Initalisieren
        ##V-Graph
        self.figure_v = Figure(figsize=(6,4))
        self.canvas_v = FigureCanvas(self.figure_v)
        self.ax_v = self.figure_v.add_subplot(111)
        (self.line_v,) = self.ax_v.plot([],[])
        self.ax_v.set_title("measured voltage")
        self.ax_v.set_xlabel("no. of measurement")
        self.ax_v.set_ylabel("voltage [V]")
        self.vLayout_v_main.addWidget(self.canvas_v)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_v_relstabw_text = QLabel()
        self.label_v_relstabw_text.setObjectName(u"label_v_relstabw_text")
        self.gridLayout.addWidget(self.label_v_relstabw_text, 2, 0, 1, 1)

        self.label_v_relstabw_value = QLabel()
        self.label_v_relstabw_value.setObjectName(u"label_v_relstabw_value")
        self.gridLayout.addWidget(self.label_v_relstabw_value, 2, 1, 1, 1)

        self.pushButton_set_calp2 = QPushButton()
        self.pushButton_set_calp2.setObjectName(u"pushButton_set_calp2")
        self.gridLayout.addWidget(self.pushButton_set_calp2, 4, 2, 1, 1)

        self.pushButton_set_calp1 = QPushButton()
        self.pushButton_set_calp1.setObjectName(u"pushButton_set_calp1")
        self.gridLayout.addWidget(self.pushButton_set_calp1, 4, 1, 1, 1)

        self.label_v_stabw_text = QLabel()
        self.label_v_stabw_text.setObjectName(u"label_v_stabw_text")
        self.gridLayout.addWidget(self.label_v_stabw_text, 1, 0, 1, 1)

        self.pushButton_reset_calibration = QPushButton()
        self.pushButton_reset_calibration.setObjectName(u"pushButton_reset_calibration")
        self.gridLayout.addWidget(self.pushButton_reset_calibration, 5, 0, 1, 3)

        self.label_v_mean_text = QLabel()
        self.label_v_mean_text.setObjectName(u"label_v_mean_text")
        self.gridLayout.addWidget(self.label_v_mean_text, 0, 0, 1, 1)

        self.label_v_stabw_value = QLabel()
        self.label_v_stabw_value.setObjectName(u"label_v_stabw_value")
        self.gridLayout.addWidget(self.label_v_stabw_value, 1, 1, 1, 1)

        self.lavel_v_mean_value = QLabel()
        self.lavel_v_mean_value.setObjectName(u"lavel_v_mean_value")
        self.gridLayout.addWidget(self.lavel_v_mean_value, 0, 1, 1, 1)

        self.pushButton_reset_measurement = QPushButton()
        self.pushButton_reset_measurement.setObjectName(u"pushButton_reset_measurement")
        self.gridLayout.addWidget(self.pushButton_reset_measurement, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.vLayout_v_main.addLayout(self.gridLayout)
        self.hLayout_v_pH.addLayout(self.vLayout_v_main)
        self.vLayout_pH_main = QVBoxLayout()
        self.vLayout_pH_main.setObjectName(u"vLayout_pH_main")

        #Graphen Initalisieren
        ##V-Graph
        self.figure_ph = Figure(figsize=(6,4))
        self.canvas_ph = FigureCanvas(self.figure_ph)
        self.ax_ph = self.figure_ph.add_subplot(111)
        (self.line_ph,) = self.ax_ph.plot([],[])
        self.ax_ph.set_title("calculated pH level")
        self.ax_ph.set_xlabel("no. of measurement")
        self.ax_ph.set_ylabel("pH")
        self.vLayout_pH_main.addWidget(self.canvas_ph)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_ph_stabw_value = QLabel()
        self.label_ph_stabw_value.setObjectName(u"label_ph_stabw_value")
        self.gridLayout_2.addWidget(self.label_ph_stabw_value, 1, 1, 1, 1)

        self.label_ph_stabw_text = QLabel()
        self.label_ph_stabw_text.setObjectName(u"label_ph_stabw_text")
        self.gridLayout_2.addWidget(self.label_ph_stabw_text, 1, 0, 1, 1)

        self.label_ph_offset_text = QLabel()
        self.label_ph_offset_text.setObjectName(u"label_ph_offset_text")
        self.gridLayout_2.addWidget(self.label_ph_offset_text, 5, 0, 1, 1)

        self.label_ph_relstabw_text = QLabel()
        self.label_ph_relstabw_text.setObjectName(u"label_ph_relstabw_text")
        self.gridLayout_2.addWidget(self.label_ph_relstabw_text, 2, 0, 1, 1)

        self.label_ph_relstabw_value = QLabel()
        self.label_ph_relstabw_value.setObjectName(u"label_ph_relstabw_value")
        self.gridLayout_2.addWidget(self.label_ph_relstabw_value, 2, 1, 1, 1)

        self.label_ph_mean_value = QLabel()
        self.label_ph_mean_value.setObjectName(u"label_ph_mean_value")
        self.gridLayout_2.addWidget(self.label_ph_mean_value, 0, 1, 1, 1)

        self.pushButton_reset_ph = QPushButton()
        self.pushButton_reset_ph.setObjectName(u"pushButton_reset_ph")
        self.gridLayout_2.addWidget(self.pushButton_reset_ph, 7, 0, 1, 1)

        self.label_ph_mean_text = QLabel()
        self.label_ph_mean_text.setObjectName(u"label_ph_mean_text")
        self.gridLayout_2.addWidget(self.label_ph_mean_text, 0, 0, 1, 1)

        self.label_ph_slope_value = QLabel()
        self.label_ph_slope_value.setObjectName(u"label_ph_slope_value")
        self.gridLayout_2.addWidget(self.label_ph_slope_value, 4, 1, 1, 1)

        self.label_ph_slope_text = QLabel()
        self.label_ph_slope_text.setObjectName(u"label_ph_slope_text")
        self.gridLayout_2.addWidget(self.label_ph_slope_text, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)
        self.vLayout_pH_main.addLayout(self.gridLayout_2)

        self.label_ph_offset_value = QLabel()
        self.label_ph_offset_value.setObjectName(u"label_ph_offset_value")
        self.gridLayout_2.addWidget(self.label_ph_offset_value, 5, 1, 1, 1)

        self.line = QFrame()
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 3)

        self.hLayout_v_pH.addLayout(self.vLayout_pH_main)
        self.MainLayout.addLayout(self.hLayout_v_pH)        

        self.retranslateUi(self)

        #connect slots
        self.pushButton_reset_measurement.pressed.connect(self.reset_measurement)
        self.pushButton_set_calp1.pressed.connect(self.set_p1)
        self.pushButton_set_calp2.pressed.connect(self.set_p2)
        self.pushButton_reset_calibration.pressed.connect(self.calibration_reset)
        self.pushButton_reset_ph.pressed.connect(self.reset_ph)

        #Lade Kalibrierungsdaten, falls vorhanden
        try:
            with open("calibration_data.txt","r") as file:
                cal_data = file.read()
                slope, offset = cal_data.split(",")
                self.ph_cal_slope = float(slope)
                self.ph_cal_offset = float(offset)
                self.ph_calc_ready = True
                #Kalibrierungsbuttons disablen
                self.pushButton_set_calp1.setEnabled(False)
                self.pushButton_set_calp2.setEnabled(False)
                #Kalibrierdaten setzen
                self.label_ph_slope_value.setText(str(slope))
                self.label_ph_offset_value.setText(str(offset))
        except FileNotFoundError:
            print("Keine Kalibrierungsdaten vorhane!")
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pH_cal_win_title.setText(QCoreApplication.translate("Form", u"pH Calibration Window", None))
        self.label_v_relstabw_text.setText(QCoreApplication.translate("Form", u"rel. Stabw.:", None))
        self.label_v_relstabw_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.pushButton_set_calp2.setText(QCoreApplication.translate("Form", u"Set P2", None))
        self.pushButton_set_calp1.setText(QCoreApplication.translate("Form", u"Set P1", None))
        self.label_v_stabw_text.setText(QCoreApplication.translate("Form", u"Stabw.:", None))
        self.pushButton_reset_calibration.setText(QCoreApplication.translate("Form", u"Reset Calibration", None))
        self.label_v_mean_text.setText(QCoreApplication.translate("Form", u"Mean:", None))
        self.label_v_stabw_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.lavel_v_mean_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.pushButton_reset_measurement.setText(QCoreApplication.translate("Form", u"Reset Measure", None))
        self.label_ph_relstabw_text.setText(QCoreApplication.translate("Form", u"rel. Stabw.:", None))
        self.label_ph_slope_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.label_ph_slope_text.setText(QCoreApplication.translate("Form", u"Slope:", None))
        self.label_ph_mean_text.setText(QCoreApplication.translate("Form", u"Mean:", None))
        self.label_ph_stabw_text.setText(QCoreApplication.translate("Form", u"Stabw.:", None))
        self.label_ph_offset_text.setText(QCoreApplication.translate("Form", u"TextLabel:", None))
        self.label_ph_mean_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.pushButton_reset_ph.setText(QCoreApplication.translate("Form", u"Reset pH Graph", None))
        self.label_ph_relstabw_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.label_ph_stabw_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.label_ph_offset_value.setText(QCoreApplication.translate("Form", u"NULL", None))
    # retranslateUi
    
    def measure_started(self):
        print("Signal empfangen. Messprozess gestartet!")

    def handle_measure_value(self, data):
        dataset = pd.DataFrame({
                "timestamp":[data[0]],
                "values":[float(data[1])]
            })
        if type(self.v_measure_container) == None:
            self.v_measure_container = dataset
        else:
            self.v_measure_container = pd.concat([self.v_measure_container, dataset], ignore_index=True)

        if self.ph_calc_ready:
            self.calculate_pH(dataset)

        self.update_UI()

    def update_UI(self):
        #Berechne Statistik der Volt Messwerte
        v_mean = 0
        v_stabw = 0
        v_relstabw = 0
        if len(self.v_measure_container["values"]) == 1:
            v_mean = round(self.v_measure_container["values"].iloc[0],4)
        else:
            v_mean = round(self.v_measure_container["values"].mean(),4)
            v_stabw = round(self.v_measure_container["values"].std(ddof=0),4)
            v_relstabw = round(v_stabw/v_mean*100,4)
        self.lavel_v_mean_value.setText(str(v_mean))
        self.label_v_stabw_value.setText(str(v_stabw))
        self.label_v_relstabw_value.setText(str(v_relstabw))

        #update Graphen
        x = self.v_measure_container.index.tolist()
        y = self.v_measure_container["values"].tolist()
        self.line_v.set_data(x,y)
        self.ax_v.relim()
        self.ax_v.autoscale()
        self.canvas_v.draw()

        if self.ph_calc_ready:
            ph_mean = 0
            ph_stabw = 0
            ph_relstabw = 0
            if len(self.ph_measure_container["values"]) == 1:
                ph_mean = round(self.ph_measure_container["values"].iloc[0],4)
            else:
                #Berechne pH und Statistik
                ph_mean = round(self.ph_measure_container["values"].mean(),4)
                ph_stabw = round(self.ph_measure_container["values"].std(ddof=0),4)
                ph_relstabw = round(ph_stabw/ph_mean*100,4)
            self.label_ph_mean_value.setText(str(ph_mean))
            self.label_ph_stabw_value.setText(str(ph_stabw))
            self.label_ph_relstabw_value.setText(str(ph_relstabw))

            #update Graphen
            x = self.ph_measure_container.index.tolist()
            y = self.ph_measure_container["values"].tolist()
            self.line_ph.set_data(x,y)
            self.ax_ph.relim()
            self.ax_ph.autoscale()
            self.canvas_ph.draw()

    def reset_measurement(self):
        print("reset v measurement graph")
        self.v_measure_container = None
        self.line_v.set_data([],[])
        self.canvas_v.draw()

    def reset_ph(self):
        print("reset ph graph")
        self.ph_measure_container = None
        self.line_ph.set_data([],[])
        self.canvas_ph.draw()

    def set_p1(self):
        text, ok = QInputDialog.getText(self, "Calibration Dialog","Which pH Calibration solution was used?")
        if ok:
            try:
                self.ph_cal_p1 = {
                    "pH":float(text),
                    "v":float(self.lavel_v_mean_value.text())
                }
                self.pushButton_set_calp1.setEnabled(False)
            except ValueError:
                QMessageBox.warning(self, "Calibration Error!", "please only pass valid numbers")

    def set_p2(self):
        text, ok = QInputDialog.getText(self, "Calibration Dialog","Which pH Calibration solution was used?")
        if ok:
            try:
                self.ph_cal_p2 = {
                    "pH":float(text),
                    "v":float(self.lavel_v_mean_value.text())
                }
                self.pushButton_set_calp2.setEnabled(False)
                self.calculate_calibration()
            except ValueError:
                QMessageBox.warning(self, "Calibration Error!", "please only pass valid numbers")

    def calculate_calibration(self):
        try:
            slope = (self.ph_cal_p2["pH"]-self.ph_cal_p1["pH"])/(self.ph_cal_p2["v"]-self.ph_cal_p1["v"])
            offset = self.ph_cal_p2["pH"]-(self.ph_cal_p2["v"]*slope)

            self.ph_cal_slope = slope
            self.ph_cal_offset = offset

            self.ph_calc_ready = True
            #Kalibrierdaten setzen
            self.label_ph_slope_value.setText(str(slope))
            self.label_ph_offset_value.setText(str(offset))
            self.save_calibration_data(slope,offset)
        except ZeroDivisionError:
            self.ph_cal_p2 = None
            self.pushButton_set_calp2.setEnabled(True)
            QMessageBox.warning(self, "Calibration Error!", "failure in calibration\n\
                                maybe try to reset measurement and try to set p2 again!") 

    def save_calibration_data(self,slope,offset):
        print("Schreibe Calibration File")
        with open("calibration_data.txt","w") as file:
            file.write(f"{slope},{offset}")

    def calculate_pH(self,data):
        dataset_v = data #Messdaten als dict {"timestamp","values"}
        timestamp = dataset_v["timestamp"]
        voltage = dataset_v["values"][0]
        ph = self.ph_cal_slope*voltage + self.ph_cal_offset
        dataset_ph = pd.DataFrame({
            "timestamp":[timestamp],
            "values":[ph]
        })

        if type(self.ph_measure_container) == None:
            self.ph_measure_container = dataset_ph
        else:
            self.ph_measure_container = pd.concat([self.ph_measure_container, dataset_ph], ignore_index=True)

        #Sende neuen pH-Wert
        print("versuche ph Wert zu senden")
        signal_manager.new_ph_value_calculated.emit(ph)
    
    def calibration_reset(self):
        print("Setze Calibrierung zurück!")
        #Stoppe pH Berechnungen
        self.ph_calc_ready = False

        #Reactivate PushButtons
        self.pushButton_set_calp1.setEnabled(True)
        self.pushButton_set_calp2.setEnabled(True)

        #Lösche Calibration Parameter
        self.ph_cal_slope = None
        self.ph_cal_offset = None

    def initialize_calibration(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = pHCalibration()
    form.show()
    app.exec()