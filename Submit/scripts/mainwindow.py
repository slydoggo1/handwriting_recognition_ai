from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HomePg = QtWidgets.QWidget(self.centralwidget)
        self.HomePg.setGeometry(QtCore.QRect(-10, -10, 821, 621))
        self.HomePg.setStyleSheet("QWidget#HomePg{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(151, 219, 255, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.HomePg.setObjectName("HomePg")
        self.TrainButton = QtWidgets.QPushButton(self.HomePg)
        self.TrainButton.setGeometry(QtCore.QRect(40, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TrainButton.setFont(font)
        self.TrainButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.TrainButton.setObjectName("TrainButton")
        self.Exit_Button = QtWidgets.QPushButton(self.HomePg)
        self.Exit_Button.setGeometry(QtCore.QRect(700, 490, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Exit_Button.setObjectName("Exit_Button")
        self.label = QtWidgets.QLabel(self.HomePg)
        self.label.setGeometry(QtCore.QRect(240, 10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.HomePg)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.HomePg)
        self.label_3.setGeometry(QtCore.QRect(200, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.DownloadBar = QtWidgets.QProgressBar(self.HomePg)
        self.DownloadBar.setGeometry(QtCore.QRect(40, 200, 311, 23))
        self.DownloadBar.setStyleSheet("")
        self.DownloadBar.setProperty("value", 24)
        self.DownloadBar.setObjectName("DownloadBar")
        self.cancel_button = QtWidgets.QPushButton(self.HomePg)
        self.cancel_button.setGeometry(QtCore.QRect(220, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.cancel_button.setObjectName("cancel_button")
        self.epoch = QtWidgets.QSpinBox(self.HomePg)
        self.epoch.setGeometry(QtCore.QRect(50, 120, 61, 22))
        self.epoch.setObjectName("epoch")
        self.batch_size = QtWidgets.QSpinBox(self.HomePg)
        self.batch_size.setGeometry(QtCore.QRect(210, 120, 61, 22))
        self.batch_size.setObjectName("batch_size")
        self.TrainingBar = QtWidgets.QProgressBar(self.HomePg)
        self.TrainingBar.setGeometry(QtCore.QRect(40, 300, 311, 23))
        self.TrainingBar.setProperty("value", 24)
        self.TrainingBar.setObjectName("TrainingBar")
        self.label_5 = QtWidgets.QLabel(self.HomePg)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.HomePg)
        self.label_6.setGeometry(QtCore.QRect(40, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalSlider = QtWidgets.QSlider(self.HomePg)
        self.horizontalSlider.setGeometry(QtCore.QRect(520, 130, 191, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_7 = QtWidgets.QLabel(self.HomePg)
        self.label_7.setGeometry(QtCore.QRect(500, 100, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.HomePg)
        self.label_8.setGeometry(QtCore.QRect(670, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.HomePg)
        self.label_9.setGeometry(QtCore.QRect(450, 320, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.HomePg)
        self.comboBox.setGeometry(QtCore.QRect(500, 230, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.HomePg)
        self.label_10.setGeometry(QtCore.QRect(500, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.HomePg)
        self.label_11.setGeometry(QtCore.QRect(130, 170, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.Download_button = QtWidgets.QPushButton(self.HomePg)
        self.Download_button.setGeometry(QtCore.QRect(40, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Download_button.setFont(font)
        self.Download_button.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Download_button.setObjectName("Download_button")
        self.cancel_button_2 = QtWidgets.QPushButton(self.HomePg)
        self.cancel_button_2.setGeometry(QtCore.QRect(220, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancel_button_2.setFont(font)
        self.cancel_button_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.cancel_button_2.setObjectName("cancel_button_2")
        self.label_12 = QtWidgets.QLabel(self.HomePg)
        self.label_12.setGeometry(QtCore.QRect(500, 160, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTrain_Model = QtWidgets.QAction(MainWindow)
        self.actionTrain_Model.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionTrain_Model.setObjectName("actionTrain_Model")
        self.actionQuite = QtWidgets.QAction(MainWindow)
        self.actionQuite.setObjectName("actionQuite")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TrainButton.setText(_translate("MainWindow", "Train Model"))
        self.Exit_Button.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Handwritten Digit Recognizer"))
        self.label_2.setText(_translate("MainWindow", "# of Epochs"))
        self.label_3.setText(_translate("MainWindow", "Batch Size"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.label_5.setText(_translate("MainWindow", "Download"))
        self.label_6.setText(_translate("MainWindow", "Training"))
        self.label_7.setText(_translate("MainWindow", "Train"))
        self.label_8.setText(_translate("MainWindow", "Validation"))
        self.label_9.setText(_translate("MainWindow", "Accuracy:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Lenet5 CNN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "EMNIST DNN"))
        self.label_10.setText(_translate("MainWindow", "Select NN:"))
        self.label_11.setText(_translate("MainWindow", "Est. Download Time:"))
        self.Download_button.setText(_translate("MainWindow", "Download Model"))
        self.cancel_button_2.setText(_translate("MainWindow", "Cancel"))
        self.label_12.setText(_translate("MainWindow", "Train/Validation Ratio:"))
        self.actionTrain_Model.setText(_translate("MainWindow", "Train Model"))
        self.actionTrain_Model.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionQuite.setText(_translate("MainWindow", "Exit"))
        self.actionQuite.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
