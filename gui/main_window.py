# gui/main_window.py

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QGroupBox, QFormLayout, QMessageBox, QStatusBar
)
from PyQt5.QtCore import Qt, QRect
from gui.styles import STYLESHEET
from gui.animations import slide_in
from utils.inference_engine import RuleEngine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supply Chain Expert System")
        self.setFixedSize(1000, 700)
        self.setStyleSheet(STYLESHEET)
        self.setup_ui()

    def setup_ui(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout()

        # Title
        title_label = QLabel("Supply Chain Expert System")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(title_label)

        # Input Form Group
        form_group = QGroupBox("Enter Supplier Criteria")
        form_layout = QFormLayout()

        self.cost_input = QLineEdit()
        self.quality_input = QLineEdit()
        self.reliability_input = QLineEdit()
        self.sustainability_input = QLineEdit()
        self.delivery_time_input = QLineEdit()

        form_layout.addRow(QLabel("Cost (low/medium/high):"), self.cost_input)
        form_layout.addRow(
            QLabel("Quality (poor/average/high/excellent):"), self.quality_input)
        form_layout.addRow(
            QLabel("Reliability (poor/average/good/excellent):"), self.reliability_input)
        form_layout.addRow(QLabel(
            "Sustainability (poor/average/good/outstanding):"), self.sustainability_input)
        form_layout.addRow(
            QLabel("Delivery Time (short/medium/long):"), self.delivery_time_input)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Buttons
        button_layout = QHBoxLayout()
        evaluate_button = QPushButton("Evaluate Supplier")
        evaluate_button.clicked.connect(self.evaluate_supplier)

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_fields)

        button_layout.addWidget(evaluate_button)
        button_layout.addWidget(reset_button)

        main_layout.addLayout(button_layout)

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Set Layout
        central_widget.setLayout(main_layout)

        # Animation on Start
        self.start_animation()

    def start_animation(self):
        """
        Animate the main window title sliding into view.
        """
        title_rect = QRect(100, 0, 800, 50)
        target_rect = QRect(100, 100, 800, 50)
        slide_in(self.centralWidget(), title_rect, target_rect)

    def evaluate_supplier(self):
        """
        Evaluate supplier criteria using the RuleEngine.
        """
        criteria = {
            "cost": self.cost_input.text(),
            "quality": self.quality_input.text(),
            "reliability": self.reliability_input.text(),
            "sustainability": self.sustainability_input.text(),
            "delivery_time": self.delivery_time_input.text()
        }

        # Rule Engine
        rule_engine = RuleEngine("knowledge_base/supplier_rules.json")
        result = rule_engine.evaluate(criteria)

        if result["exact_match"]:
            self.show_message("Supplier Recommendation", result["exact_match"])
        else:
            self.show_message(
                "No Exact Match", f"Suggestion: {result['suggestion']} (Score: {result['match_score']})")

    def reset_fields(self):
        """
        Clear all input fields.
        """
        self.cost_input.clear()
        self.quality_input.clear()
        self.reliability_input.clear()
        self.sustainability_input.clear()
        self.delivery_time_input.clear()
        self.status_bar.showMessage("Fields Reset", 2000)

    def show_message(self, title, message):
        """
        Display a message box.
        """
        QMessageBox.information(self, title, message)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
