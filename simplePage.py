from PyQt6.QtWidgets import *

class SimplePage(QWidget):
    def __init__(self, title, text):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.addWidget(QLabel(f"<h1>{title}</h1>"))
        layout.addWidget(QLabel(text))
        layout.addStretch()