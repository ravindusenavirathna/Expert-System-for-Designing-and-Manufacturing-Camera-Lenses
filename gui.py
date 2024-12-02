from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QIcon, QPixmap


class LensExpertUI(QWidget):
    def __init__(self):
        super().__init__()
        self.is_maximized = False
        self.init_ui()
        self.offset = QPoint()

    def init_ui(self):
        # Set the window size and remove the default title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 600, 400)

        # Set custom app title icon
        self.setWindowIcon(QIcon("icon.png"))

        # Apply dark theme and font
        self.setStyleSheet("""
            QWidget {
                background-color: #1f1f1f;
                color: #ffffff;
                font-family: 'Ubuntu';
                font-size: 14px;
            }
            QLineEdit {
                background-color: #333;
                border: 2px solid #555;
                border-radius: 8px;
                padding: 8px;
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #00adb5;
            }
            QPushButton {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #00adb5, stop:1 #007c91);
                color: #ffffff;
                font-size: 14px;
                border: none;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #007c91, stop:1 #005f6b);
            }
            QLabel#resultLabel {
                font-size: 16px;
                color: #ffffff;
                padding: 10px;
                background-color: #2b2b2b;
                border: 2px solid #444;
                border-radius: 8px;
                font-weight: bold;
            }
        """)

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Create custom title bar
        title_bar = QFrame()
        title_bar.setStyleSheet("background-color: #1f1f1f;")
        title_bar.setFixedHeight(40)

        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(10, 0, 10, 0)

        # Add title icon to the custom title bar
        title_icon = QLabel()
        title_icon.setPixmap(QIcon("icon.png").pixmap(
            20, 20))  # Scaled to 20x20 pixels
        title_layout.addWidget(title_icon)

        title_label = QLabel("Lens Designer")
        title_label.setStyleSheet(
            "color: #ffffff; font-size: 16px; font-weight: bold;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        # Add minimize button with custom icon
        minimize_button = QPushButton()
        minimize_button.setFixedSize(30, 30)
        minimize_button.setIcon(QIcon("minimize.png"))
        minimize_button.clicked.connect(self.showMinimized)
        title_layout.addWidget(minimize_button)

        # Add maximize/restore button with custom icons
        self.maximize_button = QPushButton()
        self.maximize_button.setFixedSize(30, 30)
        self.maximize_button.setIcon(QIcon("maximize.png"))
        self.maximize_button.clicked.connect(self.toggle_maximize_restore)
        title_layout.addWidget(self.maximize_button)

        # Add close button with custom icon
        close_button = QPushButton()
        close_button.setFixedSize(30, 30)
        close_button.setIcon(QIcon("close.png"))
        close_button.clicked.connect(self.close)
        title_layout.addWidget(close_button)

        title_bar.setLayout(title_layout)

        # Add widgets below the custom title bar
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        self.focal_label = QLabel("Focal Length (mm):")
        self.focal_input = QLineEdit()
        self.design_button = QPushButton("Design Lens")
        self.result_label = QLabel("Result: ")
        self.result_label.setObjectName("resultLabel")

        content_layout.addWidget(self.focal_label)
        content_layout.addWidget(self.focal_input)
        content_layout.addWidget(self.design_button)
        content_layout.addWidget(self.result_label)

        # Combine layouts
        main_layout.addWidget(title_bar)
        main_layout.addLayout(content_layout)

        # Set layout to the main window
        self.setLayout(main_layout)

        # Connect button functionality
        self.design_button.clicked.connect(self.design_lens)

    def design_lens(self):
        try:
            focal_length = int(self.focal_input.text())
            if focal_length < 50:
                self.result_label.setText("Use plastic molding for lenses.")
            else:
                self.result_label.setText("Use glass for precision.")
        except ValueError:
            self.result_label.setText("Please enter a valid number.")

    def toggle_maximize_restore(self):
        # Toggle between maximized and normal window state
        if self.is_maximized:
            self.showNormal()
        else:
            self.showMaximized()
        self.is_maximized = not self.is_maximized

    # Implement dragging functionality for frameless window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None


# Create the application and run the window
app = QApplication([])
app.setFont(QFont("Ubuntu", 10))
window = LensExpertUI()
window.show()
app.exec_()
