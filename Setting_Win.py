# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setting_Win.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_12 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.layoutWidget_14 = QtWidgets.QWidget(self.groupBox_12)
        self.layoutWidget_14.setGeometry(QtCore.QRect(10, 30, 133, 181))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.l_leftEye_rb = QtWidgets.QRadioButton(self.layoutWidget_14)
        self.l_leftEye_rb.setObjectName("l_leftEye_rb")
        self.verticalLayout_14.addWidget(self.l_leftEye_rb)
        self.l_rightEye_rb = QtWidgets.QRadioButton(self.layoutWidget_14)
        self.l_rightEye_rb.setObjectName("l_rightEye_rb")
        self.verticalLayout_14.addWidget(self.l_rightEye_rb)
        self.l_smile_rb = QtWidgets.QRadioButton(self.layoutWidget_14)
        self.l_smile_rb.setObjectName("l_smile_rb")
        self.verticalLayout_14.addWidget(self.l_smile_rb)
        self.l_eyeBrows_rb = QtWidgets.QRadioButton(self.layoutWidget_14)
        self.l_eyeBrows_rb.setObjectName("l_eyeBrows_rb")
        self.verticalLayout_14.addWidget(self.l_eyeBrows_rb)
        self.horizontalLayout_8.addWidget(self.groupBox_12)
        self.groupBox_13 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.layoutWidget_15 = QtWidgets.QWidget(self.groupBox_13)
        self.layoutWidget_15.setGeometry(QtCore.QRect(10, 30, 133, 181))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.r_leftEye_rb = QtWidgets.QRadioButton(self.layoutWidget_15)
        self.r_leftEye_rb.setObjectName("r_leftEye_rb")
        self.verticalLayout_15.addWidget(self.r_leftEye_rb)
        self.r_rightEye_rb = QtWidgets.QRadioButton(self.layoutWidget_15)
        self.r_rightEye_rb.setObjectName("r_rightEye_rb")
        self.verticalLayout_15.addWidget(self.r_rightEye_rb)
        self.r_smile_rb = QtWidgets.QRadioButton(self.layoutWidget_15)
        self.r_smile_rb.setObjectName("r_smile_rb")
        self.verticalLayout_15.addWidget(self.r_smile_rb)
        self.r_eyeBrows_rb = QtWidgets.QRadioButton(self.layoutWidget_15)
        self.r_eyeBrows_rb.setObjectName("r_eyeBrows_rb")
        self.verticalLayout_15.addWidget(self.r_eyeBrows_rb)
        self.horizontalLayout_8.addWidget(self.groupBox_13)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_11 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.layoutWidget_13 = QtWidgets.QWidget(self.groupBox_11)
        self.layoutWidget_13.setGeometry(QtCore.QRect(10, 30, 133, 181))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.sm_blink_rb = QtWidgets.QRadioButton(self.layoutWidget_13)
        self.sm_blink_rb.setObjectName("sm_blink_rb")
        self.verticalLayout_13.addWidget(self.sm_blink_rb)
        self.sm_smile_rb = QtWidgets.QRadioButton(self.layoutWidget_13)
        self.sm_smile_rb.setObjectName("sm_smile_rb")
        self.verticalLayout_13.addWidget(self.sm_smile_rb)
        self.sm_eyeBrows_rb = QtWidgets.QRadioButton(self.layoutWidget_13)
        self.sm_eyeBrows_rb.setObjectName("sm_eyeBrows_rb")
        self.verticalLayout_13.addWidget(self.sm_eyeBrows_rb)
        self.horizontalLayout_7.addWidget(self.groupBox_11)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mo_speed_slider = QtWidgets.QSlider(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mo_speed_slider.sizePolicy().hasHeightForWidth())
        self.mo_speed_slider.setSizePolicy(sizePolicy)
        self.mo_speed_slider.setMaximum(100)
        self.mo_speed_slider.setProperty("value", 50)
        self.mo_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.mo_speed_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.mo_speed_slider.setObjectName("mo_speed_slider")
        self.horizontalLayout.addWidget(self.mo_speed_slider)
        self.spin_speed = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_speed.sizePolicy().hasHeightForWidth())
        self.spin_speed.setSizePolicy(sizePolicy)
        self.spin_speed.setMaximum(150)
        self.spin_speed.setProperty("value", 50)
        self.spin_speed.setObjectName("spin_speed")
        self.horizontalLayout.addWidget(self.spin_speed)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scroll_speed_slider_2 = QtWidgets.QSlider(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_speed_slider_2.sizePolicy().hasHeightForWidth())
        self.scroll_speed_slider_2.setSizePolicy(sizePolicy)
        self.scroll_speed_slider_2.setMaximum(70)
        self.scroll_speed_slider_2.setProperty("value", 40)
        self.scroll_speed_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_speed_slider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.scroll_speed_slider_2.setObjectName("scroll_speed_slider_2")
        self.horizontalLayout_2.addWidget(self.scroll_speed_slider_2)
        self.spin_speed_2 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_speed_2.sizePolicy().hasHeightForWidth())
        self.spin_speed_2.setSizePolicy(sizePolicy)
        self.spin_speed_2.setMaximum(150)
        self.spin_speed_2.setProperty("value", 40)
        self.spin_speed_2.setObjectName("spin_speed_2")
        self.horizontalLayout_2.addWidget(self.spin_speed_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.on_alarm_rb = QtWidgets.QRadioButton(self.groupBox_3)
        self.on_alarm_rb.setObjectName("on_alarm_rb")
        self.horizontalLayout_3.addWidget(self.on_alarm_rb)
        self.off_alarm_rb = QtWidgets.QRadioButton(self.groupBox_3)
        self.off_alarm_rb.setObjectName("off_alarm_rb")
        self.horizontalLayout_3.addWidget(self.off_alarm_rb)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.apply_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_btn.sizePolicy().hasHeightForWidth())
        self.apply_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.apply_btn.setFont(font)
        self.apply_btn.setObjectName("apply_btn")
        self.verticalLayout_2.addWidget(self.apply_btn)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 21))
        self.menubar.setObjectName("menubar")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings Window"))
        self.label.setText(_translate("MainWindow", "Mouse Mode"))
        self.label_2.setText(_translate("MainWindow", "Select appropriate mode below to choose what Mouse Mode Functions you wish to use."))
        self.groupBox_12.setTitle(_translate("MainWindow", "Left Click"))
        self.l_leftEye_rb.setText(_translate("MainWindow", "Left eye"))
        self.l_rightEye_rb.setText(_translate("MainWindow", "Right eye"))
        self.l_smile_rb.setText(_translate("MainWindow", "Smile"))
        self.l_eyeBrows_rb.setText(_translate("MainWindow", "Eye Brows"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Right Click"))
        self.r_leftEye_rb.setText(_translate("MainWindow", "Left eye"))
        self.r_rightEye_rb.setText(_translate("MainWindow", "Right eye"))
        self.r_smile_rb.setText(_translate("MainWindow", "Smile"))
        self.r_eyeBrows_rb.setText(_translate("MainWindow", "Eye Brows"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Scroll Mode"))
        self.sm_blink_rb.setText(_translate("MainWindow", "Blink"))
        self.sm_smile_rb.setText(_translate("MainWindow", "Smile"))
        self.sm_eyeBrows_rb.setText(_translate("MainWindow", "Eye Browse"))
        self.groupBox.setTitle(_translate("MainWindow", "Mouse Sensetivity (Speed)"))
        self.label_5.setText(_translate("MainWindow", "Change Mouse Sensetivity (Speed) "))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scroll Sensetivity (Speed)"))
        self.label_6.setText(_translate("MainWindow", "Change Scroll Sensetivity (Speed) "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Additional Options"))
        self.label_3.setText(_translate("MainWindow", "Language"))
        self.label_4.setText(_translate("MainWindow", "Enable Alarm"))
        self.on_alarm_rb.setText(_translate("MainWindow", "ON"))
        self.off_alarm_rb.setText(_translate("MainWindow", "OFF"))
        self.apply_btn.setText(_translate("MainWindow", "Apply"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
