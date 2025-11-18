import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Dashboard(QWidget):
    def __init__(self,parent=None):
        super(Dashboard, self).__init__(parent)

        #Metadaten Initialisierung

        #Layout Initalisierung
        self.verticalLayout = QVBoxLayout(parent)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.verticalLayout)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_2)

        #Titel
        self.label = QLabel()
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        #pH-Sektion
        self.horizontalLayout_pH = QHBoxLayout()
        self.horizontalLayout_pH.setObjectName(u"horizontalLayout_pH")
        self.ph_text = QLabel(parent)
        self.ph_text.setObjectName(u"ph_text")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.ph_text.setFont(font1)
        self.horizontalLayout_pH.addWidget(self.ph_text)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_pH.addItem(self.horizontalSpacer)

        self.pH_value = QLabel(parent)
        self.pH_value.setObjectName(u"pH_value")
        self.horizontalLayout_pH.addWidget(self.pH_value)

        self.pH_measure_box = QCheckBox(parent)
        self.pH_measure_box.setObjectName(u"pH_measure_box")
        self.horizontalLayout_pH.addWidget(self.pH_measure_box)

        self.pH_record_box = QCheckBox(parent)
        self.pH_record_box.setObjectName(u"pH_record_box")
        self.horizontalLayout_pH.addWidget(self.pH_record_box)

        self.verticalLayout.addLayout(self.horizontalLayout_pH)

        #conductivity-Sektion
        self.horizontalLayout_conductivity = QHBoxLayout()
        self.horizontalLayout_conductivity.setObjectName(u"horizontalLayout_conductivity")
        self.conductivity_text = QLabel(parent)
        self.conductivity_text.setObjectName(u"conductivity_text")
        self.conductivity_text.setFont(font1)
        self.horizontalLayout_conductivity.addWidget(self.conductivity_text)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_conductivity.addItem(self.horizontalSpacer_2)

        self.conductivity_value = QLabel(parent)
        self.conductivity_value.setObjectName(u"conductivity_value")
        self.horizontalLayout_conductivity.addWidget(self.conductivity_value)

        self.conductivity_measure_box = QCheckBox(parent)
        self.conductivity_measure_box.setObjectName(u"conductivity_measure_box")
        self.horizontalLayout_conductivity.addWidget(self.conductivity_measure_box)

        self.conductivity_record_box = QCheckBox(parent)
        self.conductivity_record_box.setObjectName(u"conductivity_record_box")
        self.horizontalLayout_conductivity.addWidget(self.conductivity_record_box)

        self.verticalLayout.addLayout(self.horizontalLayout_conductivity)

        #temperature-Sektion
        self.horizontalLayout_temperature = QHBoxLayout()
        self.horizontalLayout_temperature.setObjectName(u"horizontalLayout_temperature")
        self.temperature_text = QLabel(parent)
        self.temperature_text.setObjectName(u"temperature_text")
        self.temperature_text.setFont(font1)
        self.horizontalLayout_temperature.addWidget(self.temperature_text)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_temperature.addItem(self.horizontalSpacer_3)

        self.temperature_value = QLabel(parent)
        self.temperature_value.setObjectName(u"temperature_value")
        self.horizontalLayout_temperature.addWidget(self.temperature_value)

        self.temperature_measure_box = QCheckBox(parent)
        self.temperature_measure_box.setObjectName(u"temperature_measure_box")
        self.horizontalLayout_temperature.addWidget(self.temperature_measure_box)

        self.temperature_record_box = QCheckBox(parent)
        self.temperature_record_box.setObjectName(u"temperature_record_box")
        self.horizontalLayout_temperature.addWidget(self.temperature_record_box)

        self.verticalLayout.addLayout(self.horizontalLayout_temperature)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

        self.retranslateUi(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.ph_text.setText(QCoreApplication.translate("Form", u"pH:", None))
        self.pH_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.pH_measure_box.setText(QCoreApplication.translate("Form", u"measure", None))
        self.pH_record_box.setText(QCoreApplication.translate("Form", u"record", None))
        self.conductivity_text.setText(QCoreApplication.translate("Form", u"conductivity:", None))
        self.conductivity_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.conductivity_measure_box.setText(QCoreApplication.translate("Form", u"measure", None))
        self.conductivity_record_box.setText(QCoreApplication.translate("Form", u"record", None))
        self.temperature_text.setText(QCoreApplication.translate("Form", u"temperature:", None))
        self.temperature_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.temperature_measure_box.setText(QCoreApplication.translate("Form", u"measure", None))
        self.temperature_record_box.setText(QCoreApplication.translate("Form", u"record", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Algea PBR Team")
    app.setApplicationName("PBR OS v.1.0")
    form = Dashboard()
    form.show()
    app.exec()