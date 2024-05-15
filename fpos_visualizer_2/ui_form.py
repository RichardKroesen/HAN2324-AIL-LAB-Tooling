# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_cont = QWidget(Widget)
        self.label_cont.setObjectName(u"label_cont")
        self.label = QLabel(self.label_cont)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 791, 581))
        self.label.setPixmap(QPixmap(u"2024-05-15-12-35-56-838.jpg"))
        self.label.setScaledContents(True)
        self.label_8 = QLabel(self.label_cont)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 130, 61, 51))
        self.label_8.setAutoFillBackground(True)
        self.label_3 = QLabel(self.label_cont)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 170, 61, 51))
        self.label_3.setAutoFillBackground(True)
        self.label_6 = QLabel(self.label_cont)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(440, 130, 61, 51))
        self.label_6.setAutoFillBackground(True)
        self.label_4 = QLabel(self.label_cont)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 70, 61, 51))
        self.label_4.setAutoFillBackground(True)
        self.label_2 = QLabel(self.label_cont)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 270, 61, 51))
        self.label_2.setAutoFillBackground(True)
        self.label_5 = QLabel(self.label_cont)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 210, 61, 51))
        self.label_5.setAutoFillBackground(True)
        self.label_7 = QLabel(self.label_cont)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 210, 61, 51))
        self.label_7.setAutoFillBackground(True)
        self.label_1 = QLabel(self.label_cont)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(340, 370, 61, 51))
        self.label_1.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.label_cont, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText("")
        self.label_8.setText("")
        self.label_3.setText("")
        self.label_6.setText("")
    # retranslateUi

