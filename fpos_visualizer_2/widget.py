# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QTimer, QIODeviceBase
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtSerialPort import QSerialPort
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.init_serial()
        self.init_timer()

    def init_serial(self):
        self.ser = QSerialPort()
        self.ser.setBaudRate(QSerialPort.BaudRate.Baud115200)
        self.ser.setPortName('/dev/ttyACM0')  # Adjust this as per your serial port
        if not self.ser.open(QIODeviceBase.OpenModeFlag.ReadWrite):
            print(f"Could not open serial port: {self.ser.errorString()}")

    def init_timer(self):
        # Timer to periodically check the serial port
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_serial_data)
        self.timer.start(1)  # Check every 100 milliseconds

    def read_serial_data(self):
       if self.ser.isOpen() and self.ser.canReadLine():
            try:
                line = self.ser.readLine()  # This reads the line as a QByteArray
                line = bytes(line).decode('utf-8').strip()  # Decode the QByteArray to string
                if line:
                    self.update_labels(line)
            except Exception as e:
                print(f"Error reading serial data: {e}")

    def update_labels(self, data):
        values = data.split(',')
        if len(values) >= 8:  # Expecting at least 8 values
            for i in range(8):
               label = getattr(self.ui,f'label_{i+1}')
               value = int(values[i+2])
               if value > 3700:
                    label.setStyleSheet("QLabel { background-color: red; }")
               else:
                    label.setStyleSheet("QLabel { background-color: none; }")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
