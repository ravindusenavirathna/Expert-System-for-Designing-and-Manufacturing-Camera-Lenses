import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from inference_engine import LensExpertSystem


class LensDesignApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Lens Design Expert System")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()
        self.expert_system = LensExpertSystem()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input fields
        self.focal_length_input = QLineEdit()
        self.focal_length_input.setPlaceholderText("Enter focal length (mm)")
        layout.addWidget(QLabel("Focal Length:"))
        layout.addWidget(self.focal_length_input)

        self.aperture_input = QLineEdit()
        self.aperture_input.setPlaceholderText("Enter aperture (f-number)")
        layout.addWidget(QLabel("Aperture:"))
        layout.addWidget(self.aperture_input)

        self.material_input = QLineEdit()
        self.material_input.setPlaceholderText(
            "Enter lens material (e.g., BK7)")
        layout.addWidget(QLabel("Lens Material:"))
        layout.addWidget(self.material_input)

        # Submit button
        self.submit_button = QPushButton("Generate Lens Design")
        self.submit_button.clicked.connect(self.generate_lens_design)
        layout.addWidget(self.submit_button)

        # Output display
        self.output_label = QLabel("Output will be displayed here.")
        layout.addWidget(self.output_label)

        # Main widget setup
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_lens_design(self):
        # Gather inputs
        focal_length = self.focal_length_input.text()
        aperture = self.aperture_input.text()
        material = self.material_input.text()

        # Validate inputs
        if not (focal_length and aperture and material):
            QMessageBox.warning(self, "Input Error",
                                "All fields are required!")
            return

        try:
            # Run expert system
            output = self.expert_system.run_expert_system(
                focal_length=float(focal_length),
                aperture=float(aperture),
                material=material
            )
            self.output_label.setText(f"Recommended Design:\n{output}")
        except ValueError:
            QMessageBox.warning(self, "Input Error",
                                "Invalid numerical input.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def run(self):
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
