# -*- coding: utf-8 -*-

## @file calc_gui.py
# @author Martin Talajka
# @date 19.4.2021
# @brief The main graphical interface of the calculator

# Form implementation generated from reading ui file 'calc_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set MainWindow name and size
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(300, 440))
        MainWindow.setMaximumSize(QtCore.QSize(300, 440))

        # Set icon for MainWindow
        srcDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setWindowIcon(QtGui.QIcon(srcDir + os.path.sep + 'Calc_icon.ico'))
        
        # Set frame name, size and style
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Set calculator UI to dark (by default)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 410))
        self.frame.setMinimumSize(QtCore.QSize(300, 410))
        self.frame.setMaximumSize(QtCore.QSize(300, 410))
        self.frame.setStyleSheet("QFrame { background-color: rgb(49, 54, 59) }"
                                "QLineEdit { background-color: rgb(68, 68, 68); border-style: outset; border-width: 0px; color: rgb(255, 255, 255)}"
                                "QPushButton { border-style: outset;border-color: rgb(0, 0, 0); border-width: 1px; border-radius: 10px; color: white }"
                                "QPushButton[objectName^=\"n\"] { background-color: rgb(35, 35, 35) }"
                                "QPushButton[objectName^=\"e\"] { background-color: rgb(96, 96, 96); font: 30pt \"Noto Mono\" }"
                                "QPushButton[objectName^=\"b\"] { background-color: rgb(68, 68, 68) }"
                                "QPushButton#button_delete{ font: 30pt \"Noto Mono\" }"
                                "QPushButton:hover { background-color: rgb(122, 122, 122) }"
                                "QPushButton:pressed { background-color: rgb(135, 135, 135) }"
                                )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        
        # Set same font for all buttons
        font = QtGui.QFont("Noto Mono", 20)

        # Set all buttons attributes - position, font, cursor change, name
        self.n_button_sign = QtWidgets.QPushButton(self.frame)
        self.n_button_sign.setGeometry(QtCore.QRect(4, 356, 70, 50))
        self.n_button_sign.setFont(font)
        self.n_button_sign.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_sign.setObjectName("n_button_sign")

        self.n_button_0 = QtWidgets.QPushButton(self.frame)
        self.n_button_0.setGeometry(QtCore.QRect(76, 356, 70, 50))
        self.n_button_0.setFont(font)
        self.n_button_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_0.setObjectName("n_button_0")

        self.n_button_comma = QtWidgets.QPushButton(self.frame)
        self.n_button_comma.setGeometry(QtCore.QRect(148, 356, 70, 50))
        self.n_button_comma.setFont(font)
        self.n_button_comma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_comma.setObjectName("n_button_comma")
        
        self.n_button_7 = QtWidgets.QPushButton(self.frame)
        self.n_button_7.setGeometry(QtCore.QRect(4, 200, 70, 50))
        self.n_button_7.setFont(font)
        self.n_button_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_7.setObjectName("n_button_7")

        self.n_button_9 = QtWidgets.QPushButton(self.frame)
        self.n_button_9.setGeometry(QtCore.QRect(148, 200, 70, 50))
        self.n_button_9.setFont(font)
        self.n_button_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_9.setObjectName("n_button_9")

        self.n_button_8 = QtWidgets.QPushButton(self.frame)
        self.n_button_8.setGeometry(QtCore.QRect(76, 200, 70, 50))
        self.n_button_8.setFont(font)
        self.n_button_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_8.setObjectName("n_button_8")

        self.button_multiply = QtWidgets.QPushButton(self.frame)
        self.button_multiply.setGeometry(QtCore.QRect(224, 200, 70, 50))
        self.button_multiply.setFont(font)
        self.button_multiply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_multiply.setObjectName("button_multiply")

        self.n_button_4 = QtWidgets.QPushButton(self.frame)
        self.n_button_4.setGeometry(QtCore.QRect(4, 252, 70, 50))
        self.n_button_4.setFont(font)
        self.n_button_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_4.setObjectName("n_button_4")

        self.n_button_6 = QtWidgets.QPushButton(self.frame)
        self.n_button_6.setGeometry(QtCore.QRect(148, 252, 70, 50))
        self.n_button_6.setFont(font)
        self.n_button_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_6.setObjectName("n_button_6")

        self.n_button_5 = QtWidgets.QPushButton(self.frame)
        self.n_button_5.setGeometry(QtCore.QRect(76, 252, 70, 50))
        self.n_button_5.setFont(font)
        self.n_button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_5.setObjectName("n_button_5")

        self.button_minus = QtWidgets.QPushButton(self.frame)
        self.button_minus.setGeometry(QtCore.QRect(224, 252, 70, 50))
        self.button_minus.setFont(font)
        self.button_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_minus.setObjectName("button_minus")

        self.n_button_1 = QtWidgets.QPushButton(self.frame)
        self.n_button_1.setGeometry(QtCore.QRect(4, 304, 70, 50))
        self.n_button_1.setFont(font)
        self.n_button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_1.setObjectName("n_button_1")

        self.n_button_3 = QtWidgets.QPushButton(self.frame)
        self.n_button_3.setGeometry(QtCore.QRect(148, 304, 70, 50))
        self.n_button_3.setFont(font)
        self.n_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_3.setObjectName("n_button_3")

        self.n_button_2 = QtWidgets.QPushButton(self.frame)
        self.n_button_2.setGeometry(QtCore.QRect(76, 304, 70, 50))
        self.n_button_2.setFont(font)
        self.n_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.n_button_2.setObjectName("n_button_2")

        self.button_plus = QtWidgets.QPushButton(self.frame)
        self.button_plus.setGeometry(QtCore.QRect(224, 304, 70, 50))
        self.button_plus.setFont(font)
        self.button_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_plus.setObjectName("button_plus")

        self.button_fact = QtWidgets.QPushButton(self.frame)
        self.button_fact.setGeometry(QtCore.QRect(4, 144, 70, 50))
        self.button_fact.setFont(font)
        self.button_fact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_fact.setObjectName("button_fact")

        self.button_sroot = QtWidgets.QPushButton(self.frame)
        self.button_sroot.setGeometry(QtCore.QRect(148, 144, 70, 50))
        self.button_sroot.setFont(font)
        self.button_sroot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sroot.setObjectName("button_sroot")

        self.button_root = QtWidgets.QPushButton(self.frame)
        self.button_root.setGeometry(QtCore.QRect(76, 144, 70, 50))
        self.button_root.setFont(font)
        self.button_root.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_root.setObjectName("button_root")

        self.button_divide = QtWidgets.QPushButton(self.frame)
        self.button_divide.setGeometry(QtCore.QRect(224, 144, 70, 50))
        self.button_divide.setFont(font)
        self.button_divide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_divide.setObjectName("button_divide")

        self.button_ce = QtWidgets.QPushButton(self.frame)
        self.button_ce.setGeometry(QtCore.QRect(4, 92, 70, 50))
        self.button_ce.setFont(font)
        self.button_ce.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ce.setObjectName("button_ce")

        self.button_parent = QtWidgets.QPushButton(self.frame)
        self.button_parent.setGeometry(QtCore.QRect(148, 92, 70, 50))
        self.button_parent.setFont(font)
        self.button_parent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_parent.setObjectName("button_parent")

        self.button_random = QtWidgets.QPushButton(self.frame)
        self.button_random.setGeometry(QtCore.QRect(76, 92, 70, 50))
        self.button_random.setFont(font)
        self.button_random.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_random.setObjectName("button_random")

        self.button_delete = QtWidgets.QPushButton(self.frame)
        self.button_delete.setGeometry(QtCore.QRect(224, 92, 70, 50))
        font.setPointSize(30)
        self.button_delete.setFont(font)
        self.button_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_delete.setObjectName("button_delete")

        self.equal_button = QtWidgets.QPushButton(self.frame)
        self.equal_button.setGeometry(QtCore.QRect(224, 356, 70, 50))
        font.setPointSize(30)
        self.equal_button.setFont(font)
        self.equal_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equal_button.setObjectName("equal_button")

        # Create main display with all atributes
        self.main_display = QtWidgets.QLineEdit(self.frame)
        self.main_display.setGeometry(QtCore.QRect(4, 24, 290, 50))
        self.main_display.setMinimumSize(QtCore.QSize(290, 50))
        self.main_display.setMaximumSize(QtCore.QSize(290, 50))
        self.main_display.setObjectName("main_display")
        self.main_display.setAlignment(QtCore.Qt.AlignRight)
        self.main_display.setReadOnly(True)
        font = QtGui.QFont("Noto Sans", 22)
        self.main_display.setFont(font)

        # Create 2nd display with all atributes
        self.h_display = QtWidgets.QLineEdit(self.frame)
        self.h_display.setGeometry(QtCore.QRect(4, 4, 290, 20))
        self.h_display.setMinimumSize(QtCore.QSize(290, 20))
        self.h_display.setMaximumSize(QtCore.QSize(290, 20))
        self.h_display.setObjectName("h_display")
        self.h_display.setAlignment(QtCore.Qt.AlignRight)
        self.h_display.setReadOnly(True)
        font = QtGui.QFont("Noto Sans", 9)
        self.h_display.setFont(font)

        # Create line under display
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(6, 74, 285, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Create line in display, under main numbers
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(8, 62, 280, 1))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 30))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)

        # Menu entry - dark mode
        self.actionDark_mode = QtWidgets.QAction(MainWindow)
        self.actionDark_mode.setCheckable(True)
        self.actionDark_mode.setChecked(True)
        self.actionDark_mode.setObjectName("actionDark_mode")

        # Change color to white/dark if button in menu is checked
        self.actionDark_mode.toggled.connect(lambda c = self.actionDark_mode.toggle : self.sColor(c))

        # Menu entry - Help
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        # Open help pdf     # TODO

        # Menu entry - Information
        self.actionInformation = QtWidgets.QAction(MainWindow)
        self.actionInformation.setObjectName("actionInformation")

        self.menuMenu.addAction(self.actionDark_mode)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionHelp)
        self.menuMenu.addAction(self.actionInformation)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "F11 Calculator"))
        
        # Set buttons names and keyboard shortcuts
        self.n_button_0.setText(_translate("MainWindow", "0"))
        self.n_button_0.setShortcut(_translate("MainWindow", "0"))
        self.n_button_1.setText(_translate("MainWindow", "1"))
        self.n_button_1.setShortcut(_translate("MainWindow", "1"))
        self.n_button_2.setText(_translate("MainWindow", "2"))
        self.n_button_2.setShortcut(_translate("MainWindow", "2"))
        self.n_button_3.setText(_translate("MainWindow", "3"))
        self.n_button_3.setShortcut(_translate("MainWindow", "3"))
        self.n_button_4.setText(_translate("MainWindow", "4"))
        self.n_button_4.setShortcut(_translate("MainWindow", "4"))
        self.n_button_5.setText(_translate("MainWindow", "5"))
        self.n_button_5.setShortcut(_translate("MainWindow", "5"))
        self.n_button_6.setText(_translate("MainWindow", "6"))
        self.n_button_6.setShortcut(_translate("MainWindow", "6"))
        self.n_button_7.setText(_translate("MainWindow", "7"))
        self.n_button_7.setShortcut(_translate("MainWindow", "7"))
        self.n_button_8.setText(_translate("MainWindow", "8"))
        self.n_button_8.setShortcut(_translate("MainWindow", "8"))
        self.n_button_9.setText(_translate("MainWindow", "9"))
        self.n_button_9.setShortcut(_translate("MainWindow", "9"))
        
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_plus.setShortcut(_translate("MainWindow", "+"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_minus.setShortcut(_translate("MainWindow", "-"))
        self.button_multiply.setText(_translate("MainWindow", "×"))
        self.button_multiply.setShortcut(_translate("MainWindow", "*"))
        self.button_divide.setText(_translate("MainWindow", "÷"))
        self.button_divide.setShortcut(_translate("MainWindow", "/"))

        self.button_fact.setText(_translate("MainWindow", "!"))
        self.button_fact.setShortcut(_translate("MainWindow", "!"))
        self.button_root.setText(_translate("MainWindow", "x^n"))
        self.button_root.setShortcut(_translate("MainWindow", "^"))
        self.button_sroot.setText(_translate("MainWindow", "n√x"))
        self.button_sroot.setShortcut(_translate("MainWindow", "q"))
        
        self.n_button_sign.setText(_translate("MainWindow", "±"))
        self.n_button_sign.setShortcut(_translate("MainWindow", "s"))
        self.n_button_comma.setText(_translate("MainWindow", "."))
        self.n_button_comma.setShortcut(_translate("MainWindow", "."))      # TODO vymyslieť aby fungovalo . aj ,
        self.button_parent.setText(_translate("MainWindow", "()"))
        self.button_parent.setShortcut(_translate("MainWindow", "("))       # TODO vymyslieť aby fungovalo ( aj )
        self.button_random.setText(_translate("MainWindow", "RND"))
        self.button_random.setShortcut(_translate("MainWindow", "r"))

        self.button_delete.setText(_translate("MainWindow", "⇚"))
        self.button_delete.setShortcut(_translate("MainWindow", "Backspace"))
        self.button_ce.setText(_translate("MainWindow", "CE"))
        self.button_ce.setShortcut(_translate("MainWindow", "c"))

        self.equal_button.setText(_translate("MainWindow", "="))
        self.equal_button.setShortcut(_translate("MainWindow", "Enter"))

        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionDark_mode.setText(_translate("MainWindow", "Dark mode"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionInformation.setText(_translate("MainWindow", "Information"))

# End of file calc_gui.py