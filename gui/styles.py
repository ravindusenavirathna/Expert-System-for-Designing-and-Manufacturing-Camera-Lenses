# gui/styles.py

STYLESHEET = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1a73e8, stop:1 #4285f4);
    color: #f5f5f5;
}

QLabel {
    font-family: 'Ubuntu';
    font-size: 16px;
    font-weight: bold;
    color: white;
    padding: 5px;
}

QLineEdit {
    background-color: #ffffff;
    border: 2px solid #d1d5db;
    border-radius: 8px;
    padding: 10px;
    font-size: 14px;
    color: #333333;
    font-family: 'Ubuntu';
}

QLineEdit:focus {
    border-color: #1a73e8;
    outline: none;
}

QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4caf50, stop:1 #2e7d32);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    font-family: 'Ubuntu';
    transition: background-color 0.3s ease;
}

QPushButton:hover {
    background-color: #388e3c;
}

QPushButton:pressed {
    background-color: #1b5e20;
}

QGroupBox {
    border: 2px solid #d1d5db;
    border-radius: 8px;
    margin-top: 20px;
    font-family: 'Ubuntu';
    font-size: 14px;
    color: white;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 5px 10px;
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
}

QStatusBar {
    background-color: #333333;
    color: white;
    font-family: 'Ubuntu';
    font-size: 12px;
}
"""
