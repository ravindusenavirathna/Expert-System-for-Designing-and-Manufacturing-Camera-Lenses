# gui/main_window.py

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QPushButton, QGroupBox, QFormLayout, QMessageBox, QStatusBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from gui.styles import STYLESHEET
from utils.inference_engine import RuleEngine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SC-Xpert")
        self.setFixedSize(1000, 700)
        self.setStyleSheet(STYLESHEET)

        # Set application icon
        self.setWindowIcon(QIcon("gui/resources/icon.png"))

        # Initialize Rule Engines
        self.rule_engines = {
            "Supplier": RuleEngine("knowledge_base/supplier_rules.json"),
            "Inventory": RuleEngine("knowledge_base/inventory_rules.json"),
            "Logistics": RuleEngine("knowledge_base/logistic_rules.json"),
            "Diagnostics": RuleEngine("knowledge_base/diagnostic_rules.json"),
        }
        self.current_engine = None

        self.setup_ui()

    def setup_ui(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout()

        # Title with Icon
        title_layout = QHBoxLayout()
        self.title_icon = QLabel()
        self.title_icon.setPixmap(
            QIcon("gui/resources/title_icon.png").pixmap(120, 120))
        self.title_icon.setAlignment(Qt.AlignCenter)
        self.title_icon.setStyleSheet(
            "padding-left: 180px;"
        )

        self.title_label = QLabel("Supply Chain Expert System")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet(
            "font-size: 32px; font-weight: bold; color: #f5f5f5; padding-right: 180px;"
        )

        title_layout.addWidget(self.title_icon)
        title_layout.addWidget(self.title_label)

        main_layout.addLayout(title_layout)

        # Context Selection
        context_layout = QHBoxLayout()
        context_label = QLabel("Select Context:")
        context_label.setStyleSheet("font-size: 16px; color: #f5f5f5;")
        self.context_selector = QComboBox()
        self.context_selector.addItems(
            ["Select", "Supplier", "Inventory", "Logistics", "Diagnostics"])
        self.context_selector.currentTextChanged.connect(self.update_context)
        self.context_selector.setStyleSheet(
            """
            QComboBox {
                background-color: #1e1e1e;
                color: #f5f5f5;
                border: 2px solid #333333;
                border-radius: 8px;
                padding: 5px 10px;
                font-size: 14px;
            }
            QComboBox:focus {
                background-color: #333333;
            }
            """
        )
        context_layout.addWidget(context_label)
        context_layout.addWidget(self.context_selector)

        main_layout.addLayout(context_layout)

        # Input Form Group
        self.form_group = QGroupBox("Enter Criteria")
        self.form_layout = QFormLayout()
        self.input_fields = {}  # To store dynamically generated input fields
        self.form_group.setLayout(self.form_layout)
        main_layout.addWidget(self.form_group)

        # Buttons
        button_layout = QHBoxLayout()
        evaluate_button = QPushButton("Evaluate")
        evaluate_button.setObjectName("evaluateButton")
        evaluate_button.clicked.connect(self.evaluate)

        reset_button = QPushButton("Reset")
        reset_button.setObjectName("resetButton")
        reset_button.clicked.connect(self.reset_fields)

        button_layout.addWidget(evaluate_button)
        button_layout.addWidget(reset_button)

        main_layout.addLayout(button_layout)

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Set Layout
        central_widget.setLayout(main_layout)

    def update_context(self, context):
        """
        Update input fields based on the selected context.
        """

        print(context)
        # Clear all widgets from the form layout
        while self.form_layout.count():
            item = self.form_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.input_fields.clear()  # Clear stored input fields
        self.current_engine = self.rule_engines.get(context, None)

        if not self.current_engine:
            self.status_bar.showMessage("Please select a valid context.", 3000)
            return

        # Dynamically update fields based on context
        context_fields = {
            "Supplier": {
                "Cost": ["Select", "Low", "Medium", "High"],
                "Quality": ["Select", "Poor", "Average", "High", "Excellent"],
                "Reliability": ["Select", "Poor", "Average", "Good", "Excellent"],
                "Sustainability": ["Select", "Poor", "Average", "Good", "Outstanding"],
                "Delivery Time": ["Select", "Short", "Medium", "Long"],
            },
            "Inventory": {
                "Demand Forecast": ["Select", "Low", "Medium", "High"],
                "Stock Level": ["Select", "Low", "Medium", "High"],
                "Lead Time": ["Select", "Short", "Medium", "Long"],
            },
            "Logistics": {
                "Distance": ["Select", "Short", "Medium", "Long"],
                "Load": ["Select", "Light", "Medium", "Heavy"],
                "Carrier Availability": ["Select", "Low", "Medium", "High"],
                "Cost": ["Select", "Low", "Medium", "High"],
            },
            "Diagnostics": {
                "Issue": ["Select", "Inventory Shortage", "Transportation Delay", "Quality Issue", "Other"],
                "Cause": ["Select", "Unexpected Demand", "Supplier Failure", "Process Issue", "Unknown"],
                "Response Time": ["Select", "Immediate", "Moderate", "Slow"],
            },
        }

        fields = context_fields.get(context, {})

        for field, options in fields.items():
            dropdown = QComboBox()
            dropdown.addItems(options)
            self.input_fields[field] = dropdown
            self.form_layout.addRow(QLabel(f"{field}:"), dropdown)

    # def evaluate(self):
    #     """
    #     Evaluate criteria using the selected rule engine.
    #     Handle missing or incomplete user inputs by predicting values.
    #     """
    #     if not self.current_engine:
    #         self.status_bar.showMessage("No context selected.", 3000)
    #         return

    #     # Retrieve user inputs

    #     criteria = {
    #         field.lower(): dropdown.currentText().strip().lower()
    #         for field, dropdown in self.input_fields.items()
    #     }

    #     print(f"Evaluating with criteria: {criteria}")

    #     # Validate inputs and predict missing values
    #     predicted_criteria = self.predict_missing_values(criteria)

    #     # Evaluate using the current rule engine
    #     result = self.current_engine.evaluate(predicted_criteria)

    #     # Display the result
    #     msg_box = QMessageBox(self)
    #     msg_box.setStyleSheet(STYLESHEET)
    #     msg_box.setWindowTitle("Evaluation Result")

    #     if result["exact_match"]:
    #         msg_box.setText(f"""
    #             <div style="font-size: 14px; font-weight: bold; color: #4CAF50;">
    #                 <p><strong>Recommendation:</strong> {result['exact_match']}</p>
    #                 <p style="font-size: 12px; color: #555555;">
    #                     The recommendation exactly matches the criteria based on the provided information.
    #                 </p>
    #             </div>
    #         """)
    #     else:
    #         msg_box.setText(f"""
    #             <div style="font-size: 14px; font-weight: bold; color: #FF9800;">
    #                 <p><strong>Suggestion:</strong> {result['suggestion']}</p>
    #                 <p style="font-size: 12px; color: #555555;">
    #                     Based on your criteria, the best match is a suggestion.
    #                     Match Score: <strong>{result['match_score']}</strong>.
    #                 </p>
    #             </div>
    #         """)

    #     msg_box.exec_()

    def evaluate(self):
        """
        Evaluate criteria using the selected rule engine.
        Display results dynamically based on the knowledge base type with appropriate colors.
        """
        if not self.current_engine:
            self.status_bar.showMessage("No context selected.", 3000)
            return

        # Retrieve user inputs
        criteria = {
            field.lower(): dropdown.currentText().strip().lower()
            for field, dropdown in self.input_fields.items()
        }

        # Validate inputs and predict missing values
        predicted_criteria = self.predict_missing_values(criteria)

        # Evaluate using the current rule engine
        result = self.current_engine.evaluate(predicted_criteria)

        # Determine context and process results accordingly
        context = self.context_selector.currentText()
        msg_box = QMessageBox(self)
        msg_box.setStyleSheet(STYLESHEET)
        msg_box.setWindowTitle("Evaluation Result")

        # Process results based on match levels
        if result.get("exact_match"):
            color = "#4CAF50"  # Green for exact match
            message = self.format_message(
                context, result["exact_match"], color)
        else:
            color = "#FFC107"  # Yellow for suggestion
            message = self.format_message(
                context, result["suggestion"], color, match_score=result.get("match_score"))

        # Set and display the message in the message box
        msg_box.setText(message)
        msg_box.exec_()

    def format_message(self, context, data, color, match_score=None):
        """
        Format the result message dynamically based on the knowledge base context.
        """
        if context == "Supplier":
            return f"""
                <div style="font-size: 16px; font-weight: bold; color: {color};">
                    <p><strong>Recommendation:</strong> {data}</p>
                </div>
            """
        elif context == "Inventory":
            action = data.get("action", "N/A")
            recommended_stock = data.get("recommended stock", "N/A")
            return f"""
                <div style="font-size: 16px; font-weight: bold; color: {color};">
                    <p><strong>Action:</strong> {action}</p>
                    <p><strong>Recommended Stock:</strong> {recommended_stock}</p>
                    {f"<p><strong>Match Score:</strong> {match_score}</p>" if match_score else ""}
                </div>
            """
        elif context == "Diagnostics":
            diagnosis = data.get("diagnosis", "N/A")
            recommendation = data.get("recommendation", "N/A")
            return f"""
                <div style="font-size: 16px; font-weight: bold; color: {color};">
                    <p><strong>Diagnosis:</strong> {diagnosis}</p>
                    <p><strong>Recommendation:</strong> {recommendation}</p>
                    {f"<p><strong>Match Score:</strong> {match_score}</p>" if match_score else ""}
                </div>
            """
        elif context == "Logistics":
            mode_of_transport = data.get("mode of transport", "N/A")
            priority = data.get("priority", "N/A")
            return f"""
                <div style="font-size: 16px; font-weight: bold; color: {color};">
                    <p><strong>Mode of Transport:</strong> {mode_of_transport}</p>
                    <p><strong>Priority:</strong> {priority}</p>
                    {f"<p><strong>Match Score:</strong> {match_score}</p>" if match_score else ""}
                </div>
            """
        else:
            return f"""
                <div style="font-size: 16px; font-weight: bold; color: {color};">
                    <p>No valid recommendation available for the selected context.</p>
                </div>
            """

    def predict_missing_values(self, criteria):
        """
        Predict missing values in the user's input based on similar rules in the knowledge base.
        """
        rules = self.current_engine.rules

        for field, value in criteria.items():
            if value == "select":  # Missing field
                # Predict value by finding the most common value in the rules
                possible_values = [rule["if"][field]
                                   for rule in rules if field in rule["if"]]
                if possible_values:
                    criteria[field] = max(
                        set(possible_values), key=possible_values.count)

        return criteria

    def reset_fields(self):
        """
        Reset all input fields.
        """
        for dropdown in self.input_fields.values():
            dropdown.setCurrentIndex(0)
        self.status_bar.showMessage("Fields reset.", 2000)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
