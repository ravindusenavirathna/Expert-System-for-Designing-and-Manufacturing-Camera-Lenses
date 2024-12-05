# gui/styles.py

STYLESHEET = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0e0e0e, stop:1 #363636);
    color: #f0f0f0;
}

QLabel {
    font-family: 'Ubuntu';
    font-size: 16px;
    font-weight: bold;
    color: #f5f5f5;
    padding: 5px;
}

QLineEdit {
    background-color: #1e1e1e;
    border: 2px solid #333333;
    border-radius: 8px;
    padding: 10px;
    font-size: 14px;
    color: #f0f0f0;
    font-family: 'Ubuntu';
    transition: border-color 1s ease-in-out;
}

QLineEdit:focus {
    border-color: #505050;
    outline: none;
    transition: border-color 1s ease-in-out;
}

QPushButton {
    border: 2px solid;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    font-family: 'Ubuntu';
    padding: 10px 20px;
    transition: all 0.3s ease;
}

QPushButton#resetButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff4081, stop:1 #f50057);
    color: white;
    border-color: #f50057;
}

QPushButton#resetButton:hover {
    background-color: #d81b60;
}

QPushButton#resetButton:pressed {
    background-color: #c2185b;
}

QPushButton#evaluateButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3481bf, stop:1 #1166b1);
    color: white;
    border-color: #1166b1;
}

QPushButton#evaluateButton:hover {
    background-color: #1976d2;
}

QPushButton#evaluateButton:pressed {
    background-color: #1565c0;
}

QGroupBox {
    border: 2px solid #333333;
    border-radius: 8px;
    margin-top: 0px;
    padding-top: 30px;
    font-family: 'Ubuntu';
    font-size: 14px;
    color: white;
    background-color: #21212180;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 5px 10px;
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    background-color: #333333;
    border-top-left-radius: 5px;
    border-bottom-right-radius: 5px;
    padding: 2px 8px;
}

QMessageBox {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #121212, stop:1 #1a1a1a);
    border: 2px solid #333333;
    color: #f5f5f5;
    font-family: 'Ubuntu';
    font-size: 14px;
}

QMessageBox QLabel {
    color: #f5f5f5;
}

QMessageBox QPushButton {
    background-color: #424242;
    border: 1px solid #555555;
    color: #ffffff;
    padding: 5px 10px;
    border-radius: 5px;
    font-family: 'Ubuntu';
    font-size: 14px;
}

QMessageBox QPushButton:hover {
    background-color: #555555;
}

QMessageBox QPushButton:pressed {
    background-color: #333333;
}

QComboBox {
    background-color: #1e1e1e;
    color: #f5f5f5;
    border: 2px solid #333333;
    border-radius: 12px;
    padding: 5px 10px;
    font-size: 14px;
    font-family: 'Ubuntu';
}

QComboBox:focus {
    background-color: #333333; 
}

QComboBox:selected {
    background-color: #444444;
    color: #ffffff;
}

QComboBox QAbstractItemView {
    background-color: #1e1e1e;
    color: #f5f5f5;
    border-radius: 12px;
    selection-background-color: #444444; 
    selection-color: #ffffff;
    padding: 5px;
    font-size: 14px;
    font-family: 'Ubuntu';
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: url(gui/resources/down_arrow_icon.png);
    width: 14px;
    height: 14px;
}

QComboBox::down-arrow:hover {
    image: url(gui/resources/down_arrow_hover_icon.png);
}

QComboBox::down-arrow:on {
    image: url(gui/resources/down_arrow_selected_icon.png);
}

QComboBox QAbstractItemView::item {
    border-radius: 8px;
    margin: 3px;
    padding: 5px;
}

QComboBox QAbstractItemView::item:selected {
    background-color: #555555; 
    color: #ffffff;
}


"""
