import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class pHCalibration(QWidget):
    def __init__(self,parent=None):
        super(pHCalibration,self).__init__(parent)
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
        self.w_placeh_v_graph = QWidget()
        self.w_placeh_v_graph.setObjectName(u"w_placeh_v_graph")
        self.vLayout_v_main.addWidget(self.w_placeh_v_graph)

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

        self.w_placeh_pH_graph = QWidget()
        self.w_placeh_pH_graph.setObjectName(u"w_placeh_pH_graph")
        self.vLayout_pH_main.addWidget(self.w_placeh_pH_graph)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_ph_stabw_value = QLabel()
        self.label_ph_stabw_value.setObjectName(u"label_ph_stabw_value")
        self.gridLayout_2.addWidget(self.label_ph_stabw_value, 1, 1, 1, 1)

        self.label_ph_stabw_text = QLabel()
        self.label_ph_stabw_text.setObjectName(u"label_ph_stabw_text")
        self.gridLayout_2.addWidget(self.label_ph_stabw_text, 1, 0, 1, 1)

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
        self.gridLayout_2.addWidget(self.pushButton_reset_ph, 4, 0, 1, 1)

        self.label_ph_mean_text = QLabel()
        self.label_ph_mean_text.setObjectName(u"label_ph_mean_text")
        self.gridLayout_2.addWidget(self.label_ph_mean_text, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)
        self.vLayout_pH_main.addLayout(self.gridLayout_2)

        self.hLayout_v_pH.addLayout(self.vLayout_pH_main)
        self.MainLayout.addLayout(self.hLayout_v_pH)


        self.retranslateUi(self)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pH_cal_win_title.setText(QCoreApplication.translate("Form", u"pH Calibration Window", None))
        self.label_v_relstabw_text.setText(QCoreApplication.translate("Form", u"rel. Stabw", None))
        self.label_v_relstabw_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.pushButton_set_calp2.setText(QCoreApplication.translate("Form", u"Set P2", None))
        self.pushButton_set_calp1.setText(QCoreApplication.translate("Form", u"Set P1", None))
        self.label_v_stabw_text.setText(QCoreApplication.translate("Form", u"Stabw", None))
        self.pushButton_reset_calibration.setText(QCoreApplication.translate("Form", u"Reset Calibration", None))
        self.label_v_mean_text.setText(QCoreApplication.translate("Form", u"Mean", None))
        self.label_v_stabw_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.lavel_v_mean_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.pushButton_reset_measurement.setText(QCoreApplication.translate("Form", u"Reset Measure", None))
        self.label_ph_stabw_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_ph_stabw_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_ph_relstabw_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_ph_relstabw_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_ph_mean_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_reset_ph.setText(QCoreApplication.translate("Form", u"Reset pH Graph", None))
        self.label_ph_mean_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = pHCalibration()
    form.show()
    app.exec()