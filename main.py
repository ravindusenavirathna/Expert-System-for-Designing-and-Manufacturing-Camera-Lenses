import sys
from PyQt5.QtWidgets import QApplication
from gui import LensDesignApp

if __name__ == "__main__":
    # Create the QApplication instance
    app = QApplication(sys.argv)

    # Create and show the main window
    main_window = LensDesignApp()
    main_window.show()

    # Execute the application
    sys.exit(app.exec_())
