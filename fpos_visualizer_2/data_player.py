# This Python file uses the following encoding: utf-8
import sys
import csv

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer

from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.data_rows = self.load_csv_data()
        self.data_index = 0
        self.init_timer()

    def load_csv_data(self):
        # Load the CSV data into a list for later use
        data = []
        if len(sys.argv) > 1:
            csv_file = sys.argv[1]
            try:
                with open(csv_file, newline='') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    data = [row for row in reader if len(row) >= 11]  # Ensure rows have sufficient columns
            except Exception as e:
                print(f"Error loading CSV file: {e}")
        return data

    def init_timer(self):
        # Timer to periodically update the labels from CSV data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_labels_from_data)
        self.timer.start(10)  # Trigger every 10 milliseconds

    def update_labels_from_data(self):
        if self.data_index < len(self.data_rows):
            self.update_labels(self.data_rows[self.data_index])
            self.data_index += 1
        else:
            self.timer.stop()  # Stop the timer if we've exhausted the data

    def update_labels(self, data):
        # Update GUI labels based on data from the CSV row
        for i in range(8):  # Update 8 labels
            label = getattr(self.ui, f'label_{i+1}')
            value = int(float(data[i+3]))  # Convert string to float then to int
            if value > 3400:
                label.setStyleSheet("QLabel { background-color: red; }")
            else:
                label.setStyleSheet("QLabel { background-color: none; }")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

