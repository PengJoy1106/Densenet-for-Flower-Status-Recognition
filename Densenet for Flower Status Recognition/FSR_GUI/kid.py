# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kid.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(981, 794)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        Dialog.setStyleSheet("QDialog{background-color:rgb(    135,206,250);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 721, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 130, 731, 591))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 130, 211, 371))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QPixmap("img/可回收垃圾.jpg"))
        self.label_3.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 111, 51))
        self.pushButton.setMinimumSize(QtCore.QSize(111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet(
            "QPushButton{background:#e6f0fa;border:2px groove gray;border-radius:10px;padding:2px 4px} QPushButton:hover { background-color: rgb(30,144,255); }")
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 111, 51))
        self.pushButton_2.setMinimumSize(QtCore.QSize(111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setStyleSheet(
            "QPushButton{background:#e6f0fa;border:2px groove gray;border-radius:10px;padding:2px 4px} QPushButton:hover { background-color: rgb(30,144,255); }")
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "花卉科普"))
        Dialog.setWindowIcon(QIcon('image/logo.png'))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#428663;\">花卉生长状态介绍</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">花卉状态通常指花卉的健康和生长状态。以下是一些常见的花卉状态：</span></p><br/>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">1. 生长状况：花卉的生长状态可以分为正常、弱势和病态三种状态。生长状况：</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">花卉的生长状态可以分为正常、弱势和病态三种状态。正常状态下，花卉叶片茂</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">盛、花朵艳丽，生长状况良好；弱势状态下，花卉生长缓慢、叶片干枯、花朵不</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">良，需要及时调整生长环境；病态状态下，花卉被病虫害侵袭或生长环境受到严</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">重干扰，需要进行病虫害防治或环境调整。</span></p><br/>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">2. 绿叶状态：花卉的叶片颜色可以分为健康的绿色、黄色和褐色。健康的绿色</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\"表示花卉养分充足，生长健康；黄色则可能表示花卉叶片缺乏养分或遭受病虫害</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">侵袭；褐色则可能表示花卉遭受灼伤或缺水。</span></p><br/>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">3. 开花状况：花卉开花状况可以分为开花期、花期结束、花期延长三种状态。</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">开花期内，花卉花朵开放、色彩鲜艳；花期结束后，花卉花朵凋谢、掉落，进入休</span></p>"
                                                  "<p><span style=\" font-size:12pt; font-weight:600;\">眠期；花期延长时，花卉花朵持续开放，需要进行适当的管理和调整。</span></p>"
                                                  "<p><span font-size:12pt; font-weight:600;\"></span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "花卉养护策略"))
        self.pushButton_2.setText(_translate("Dialog", "花卉生长状态"))
