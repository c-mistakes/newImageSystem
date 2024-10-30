# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shiyan.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_shiyan(object):
    def setupUi(self, shiyan):
        if not shiyan.objectName():
            shiyan.setObjectName(u"shiyan")
        shiyan.resize(719, 451)
        self.nameLineEdit = QLineEdit(shiyan)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(150, 65, 231, 23))
        self.imageName = QLabel(shiyan)
        self.imageName.setObjectName(u"imageName")
        self.imageName.setGeometry(QRect(80, 70, 68, 15))
        self.imageButton = QPushButton(shiyan)
        self.imageButton.setObjectName(u"imageButton")
        self.imageButton.setGeometry(QRect(420, 65, 84, 24))
        self.label = QLabel(shiyan)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 20, 171, 16))
        self.showLabel = QLabel(shiyan)
        self.showLabel.setObjectName(u"showLabel")
        self.showLabel
        self.showLabel.setGeometry(QRect(60, 140, 601, 271))

        self.retranslateUi(shiyan)

        QMetaObject.connectSlotsByName(shiyan)
    # setupUi

    def retranslateUi(self, shiyan):
        shiyan.setWindowTitle(QCoreApplication.translate("shiyan", u"Form", None))
        self.imageName.setText(QCoreApplication.translate("shiyan", u"\u56fe\u7247\u540d\u79f0\uff1a", None))
        self.imageButton.setText(QCoreApplication.translate("shiyan", u"\u63d0\u53d6\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("shiyan", u"\u83b7\u53d6\u670d\u52a1\u5668\u56fe\u7247\u6d4b\u8bd5\u9875\u9762", None))
        self.showLabel.setText("")
    # retranslateUi

