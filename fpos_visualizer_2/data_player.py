# This Python file uses the following encoding: utf-8
import sys
import csv

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from PySide6.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui_form import Ui_Widget

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.data_rows = self.load_csv_data()
        self.data_index = 0

        # Timer for updating labels
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_labels_from_data)
        self.timer.start(10)  # Update every 10 milliseconds

    def load_csv_data(self):
        # Load the CSV data into a list for later use
        data = []
        if len(sys.argv) > 1:
            csv_file = sys.argv[1]
            try:
                with open(csv_file, newline='') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    data = [row for row in reader if len(row) >= 11]
            except Exception as e:
                print(f"Error loading CSV file: {e}")
        return data

    def update_labels_from_data(self):
        if self.data_index < len(self.data_rows):
            row = self.data_rows[self.data_index]
            self.update_labels(row)
            self.data_index += 1
        else:
            self.timer.stop()  # Stop the timer if we've exhausted the data

    def update_labels(self, data):
        # Update GUI labels based on data from the CSV row
        for i in range(8):
            label = getattr(self.ui, f'label_{i+1}')
            value = int(float(data[i+3]))
            if value > 3700:
                label.setStyleSheet("QLabel { background-color: red; }")
            else:
                label.setStyleSheet("QLabel { background-color: none; }")

class PlotWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)
        self.plot = self.figure.add_subplot(111)
        self.plot.set_title('Time of Flight (ToF) Data')
        self.plot.set_xlabel('Sample Index')
        self.plot.set_ylabel('ToF Value (mm)')
        self.tof_values = []
        self.sample_count = 0  # Initialize sample count

        # Timer for updating the plot
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(10)  # Update every 10 milliseconds

    def update_graph(self):
        # Check for shared data availability and update the plot
        if main_window.data_index < len(main_window.data_rows):
            row = main_window.data_rows[main_window.data_index]
            tof_value = float(row[-1])
            self.tof_values.append(tof_value)
            self.sample_count += 1  # Increment sample count

            # Only keep the last 50 samples for plotting
            if len(self.tof_values) > 50:
                self.tof_values.pop(0)  # Remove the oldest element

            # Update the graph
            self.plot.clear()
            self.plot.plot(self.tof_values, label='ToF', color='blue')
            self.plot.set_title('Compression depth (mm)')
            self.plot.set_xlabel('Sample num')
            self.plot.set_ylabel('Depth (mm)')
            self.plot.set_xlim(0, 50)  # Fix the x-axis to display exactly 50 samples
            self.canvas.draw()
        else:
            self.timer.stop()  # Stop the timer if we've exhausted the data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    plot_window = PlotWindow()
    main_window.show()
    plot_window.show()
    sys.exit(app.exec())

