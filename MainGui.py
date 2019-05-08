# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIByHaies.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EncryptOrDecryptFilesHaies(object):
    def setupUi(self, EncryptOrDecryptFilesHaies):
        EncryptOrDecryptFilesHaies.setObjectName("EncryptOrDecryptFilesHaies")
        EncryptOrDecryptFilesHaies.resize(379, 632)
        EncryptOrDecryptFilesHaies.setMinimumSize(QtCore.QSize(379, 632))
        EncryptOrDecryptFilesHaies.setMaximumSize(QtCore.QSize(379, 632))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EncryptOrDecryptFilesHaies.setWindowIcon(icon)
        EncryptOrDecryptFilesHaies.setStyleSheet("QWidget{\n"
"background-image: url(:/img/backcool3.png);\n"
"}\n"
"")
        EncryptOrDecryptFilesHaies.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.centralwidget = QtWidgets.QWidget(EncryptOrDecryptFilesHaies)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 270, 357, 322))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditSelected = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditSelected.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditSelected.setFont(font)
        self.lineEditSelected.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditSelected.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.lineEditSelected.setObjectName("lineEditSelected")
        self.verticalLayout.addWidget(self.lineEditSelected)
        self.progressBarForCountFile = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBarForCountFile.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBarForCountFile.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.progressBarForCountFile.setProperty("value", 0)
        self.progressBarForCountFile.setTextVisible(False)
        self.progressBarForCountFile.setObjectName("progressBarForCountFile")
        self.verticalLayout.addWidget(self.progressBarForCountFile)
        self.progressBarForEncOrDec = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBarForEncOrDec.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBarForEncOrDec.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.progressBarForEncOrDec.setProperty("value", 0)
        self.progressBarForEncOrDec.setTextVisible(False)
        self.progressBarForEncOrDec.setObjectName("progressBarForEncOrDec")
        self.verticalLayout.addWidget(self.progressBarForEncOrDec)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButtonSelectFolder = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButtonSelectFolder.setFont(font)
        self.toolButtonSelectFolder.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolButtonSelectFolder.setStyleSheet("/*\n"
".QToolButton {\n"
"    position: relative;\n"
"    display: inline-block;\n"
"    font-weight: bold;\n"
"    padding: 0.25em 0.5em;\n"
"    text-decoration: none;\n"
"    color: #00BCD4;\n"
"    background: #ECECEC;\n"
"    border-radius: 0 15px 15px 0;\n"
"    transition: .4s;\n"
"  }\n"
"\n"
".QToolButton:hover {\n"
"    background: #636363;\n"
"}\n"
"*/\n"
".QToolButton {\n"
"color: #20bf6b !important;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"background: #ffffff;\n"
"padding: 5px 5px;\n"
"border: 2px solid #20bf6b !important;\n"
"border-radius: 10px;\n"
"display: inline-block;\n"
"}\n"
".QToolButton:hover {\n"
"color: #494949 !important;\n"
"border-radius: 40px;\n"
"border-color: #494949 !important;\n"
"transition: all 0.3s ease 0s;\n"
"}")
        self.toolButtonSelectFolder.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.toolButtonSelectFolder.setObjectName("toolButtonSelectFolder")
        self.horizontalLayout_2.addWidget(self.toolButtonSelectFolder)
        self.toolButtonSelectFile = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolButtonSelectFile.setFont(font)
        self.toolButtonSelectFile.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolButtonSelectFile.setStyleSheet("/*\n"
".QToolButton {\n"
"    position: relative;\n"
"    display: inline-block;\n"
"    font-weight: bold;\n"
"    padding: 0.25em 0.5em;\n"
"    text-decoration: none;\n"
"    color: #00BCD4;\n"
"    background: #ECECEC;\n"
"    border-radius: 0 15px 15px 0;\n"
"    transition: .4s;\n"
"  }\n"
"\n"
".QToolButton:hover {\n"
"    background: #636363;\n"
"}\n"
"*/\n"
".QToolButton {\n"
"color: #20bf6b !important;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"background: #ffffff;\n"
"padding: 5px 5px;\n"
"border: 2px solid #20bf6b !important;\n"
"border-radius: 10px;\n"
"display: inline-block;\n"
"}\n"
".QToolButton:hover {\n"
"color: #494949 !important;\n"
"border-radius: 40px;\n"
"border-color: #494949 !important;\n"
"transition: all 0.3s ease 0s;\n"
"}")
        self.toolButtonSelectFile.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.toolButtonSelectFile.setCheckable(False)
        self.toolButtonSelectFile.setAutoRaise(False)
        self.toolButtonSelectFile.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonSelectFile.setObjectName("toolButtonSelectFile")
        self.horizontalLayout_2.addWidget(self.toolButtonSelectFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("")
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonDecrypt = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonDecrypt.setFont(font)
        self.radioButtonDecrypt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButtonDecrypt.setObjectName("radioButtonDecrypt")
        self.horizontalLayout.addWidget(self.radioButtonDecrypt)
        self.radioButtonEncrypt = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonEncrypt.setFont(font)
        self.radioButtonEncrypt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButtonEncrypt.setChecked(True)
        self.radioButtonEncrypt.setObjectName("radioButtonEncrypt")
        self.horizontalLayout.addWidget(self.radioButtonEncrypt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditConfPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditConfPassword.setFont(font)
        self.lineEditConfPassword.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditConfPassword.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.lineEditConfPassword.setMaxLength(16)
        self.lineEditConfPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditConfPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditConfPassword.setDragEnabled(True)
        self.lineEditConfPassword.setClearButtonEnabled(True)
        self.lineEditConfPassword.setObjectName("lineEditConfPassword")
        self.gridLayout.addWidget(self.lineEditConfPassword, 1, 1, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditPassword.setStyleSheet("")
        self.lineEditPassword.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.lineEditPassword.setMaxLength(16)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditPassword.setDragEnabled(False)
        self.lineEditPassword.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditPassword.setClearButtonEnabled(True)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonOk = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtonOk.setStyleSheet("/*\n"
".QPushButton {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"border-radius: 6px;\n"
"display: inline-block;\n"
"}\n"
"*/\n"
".QPushButton {\n"
"color: #ff0000 !important;\n"
"text-transform: uppercase;\n"
"background: #484848;\n"
"padding: 10px;\n"
"border: 2px solid #494949 !important;\n"
"border-radius: 10px;\n"
"display: inline-block;\n"
"}\n"
".QPushButton:active {\n"
"color: #ffffff !important;\n"
"background:#67ce00;\n"
"border-color: #67ce00 !important;\n"
"\n"
"text-transform: uppercase;\n"
"padding: 10px;\n"
"border: 2px solid #494949 !important;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
".QPushButton:pressed {\n"
"color: #7bbe0e !important;\n"
"background: #ffffff;\n"
"border-color: #67ce00 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
".QPushButton:hover {\n"
"border-radius: 40px;\n"
"border-color: #494949 !important;\n"
"transition: all 0.3s ease 0s;\n"
"}")
        self.pushButtonOk.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout_3.addWidget(self.pushButtonOk)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 169, 251))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_11.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_13.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_13.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13.setOpenExternalLinks(True)
        self.label_13.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 20, 181, 211))
        self.label_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/img/icon.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        EncryptOrDecryptFilesHaies.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EncryptOrDecryptFilesHaies)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 34))
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.menubar.setObjectName("menubar")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuSystem.setFont(font)
        self.menuSystem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuSystem.setAutoFillBackground(False)
        self.menuSystem.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.menuSystem.setObjectName("menuSystem")
        EncryptOrDecryptFilesHaies.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(EncryptOrDecryptFilesHaies)
        self.actionHelp.setCheckable(False)
        self.actionHelp.setChecked(False)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(EncryptOrDecryptFilesHaies)
        font = QtGui.QFont()
        font.setFamily("Harmattan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.menuSystem.addAction(self.actionHelp)
        self.menuSystem.addAction(self.actionExit)
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(EncryptOrDecryptFilesHaies)
        QtCore.QMetaObject.connectSlotsByName(EncryptOrDecryptFilesHaies)

    def retranslateUi(self, EncryptOrDecryptFilesHaies):
        _translate = QtCore.QCoreApplication.translate
        EncryptOrDecryptFilesHaies.setWindowTitle(_translate("EncryptOrDecryptFilesHaies", "EncryptOrDecryptFilesByHaies"))
        self.toolButtonSelectFolder.setText(_translate("EncryptOrDecryptFilesHaies", "تحديد مجلد"))
        self.toolButtonSelectFile.setText(_translate("EncryptOrDecryptFilesHaies", "تحديد ملف"))
        self.label.setText(_translate("EncryptOrDecryptFilesHaies", "حدد الملفات :"))
        self.radioButtonDecrypt.setText(_translate("EncryptOrDecryptFilesHaies", "فك التشفير"))
        self.radioButtonEncrypt.setText(_translate("EncryptOrDecryptFilesHaies", "تشفير"))
        self.label_2.setText(_translate("EncryptOrDecryptFilesHaies", "حدد النوع :"))
        self.lineEditConfPassword.setPlaceholderText(_translate("EncryptOrDecryptFilesHaies", "أعد كتابة كلمة السر"))
        self.lineEditPassword.setPlaceholderText(_translate("EncryptOrDecryptFilesHaies", "أكتب كلمة السر"))
        self.label_3.setText(_translate("EncryptOrDecryptFilesHaies", "كلمة السر :"))
        self.label_4.setText(_translate("EncryptOrDecryptFilesHaies", "أعد كلمة السر :"))
        self.pushButtonOk.setText(_translate("EncryptOrDecryptFilesHaies", "موافق"))
        self.label_5.setText(_translate("EncryptOrDecryptFilesHaies", "هذا البرنامج يسمح لك"))
        self.label_6.setText(_translate("EncryptOrDecryptFilesHaies", "بتشفير بياناتك وحمايتها"))
        self.label_7.setText(_translate("EncryptOrDecryptFilesHaies", "وفك تشفيرها مرة أخرى"))
        self.label_8.setText(_translate("EncryptOrDecryptFilesHaies", "بإستخدام خوارزمية متطورة"))
        self.label_9.setText(_translate("EncryptOrDecryptFilesHaies", "برنامج سهل الإستخدام"))
        self.label_10.setText(_translate("EncryptOrDecryptFilesHaies", "تمت برمجته بواسطة :"))
        self.label_11.setText(_translate("EncryptOrDecryptFilesHaies", "أحمد حايس"))
        self.label_12.setText(_translate("EncryptOrDecryptFilesHaies", "فيس بوك :"))
        self.label_13.setText(_translate("EncryptOrDecryptFilesHaies", "<a href=\"https://fb.com/ahmed.haies\">ahmed.haies</a>"))
        self.menuSystem.setTitle(_translate("EncryptOrDecryptFilesHaies", "النظام"))
        self.actionHelp.setText(_translate("EncryptOrDecryptFilesHaies", "مساعدة"))
        self.actionExit.setText(_translate("EncryptOrDecryptFilesHaies", "خروج"))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EncryptOrDecryptFilesHaies = QtWidgets.QMainWindow()
    ui = Ui_EncryptOrDecryptFilesHaies()
    ui.setupUi(EncryptOrDecryptFilesHaies)
    EncryptOrDecryptFilesHaies.show()
    sys.exit(app.exec_())

