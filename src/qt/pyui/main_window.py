# Form implementation generated from reading ui file './src/qt/ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(418, 325)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_download_video = QtWidgets.QPushButton(self.centralwidget)
        self.pb_download_video.setEnabled(False)
        self.pb_download_video.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pb_download_video.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pb_download_video.setObjectName("pb_download_video")
        self.horizontalLayout.addWidget(self.pb_download_video)
        self.pb_download_audio = QtWidgets.QPushButton(self.centralwidget)
        self.pb_download_audio.setEnabled(False)
        self.pb_download_audio.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pb_download_audio.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pb_download_audio.setObjectName("pb_download_audio")
        self.horizontalLayout.addWidget(self.pb_download_audio)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.le_youtube_link = QtWidgets.QLineEdit(self.centralwidget)
        self.le_youtube_link.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.le_youtube_link.setText("")
        self.le_youtube_link.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.le_youtube_link.setReadOnly(False)
        self.le_youtube_link.setObjectName("le_youtube_link")
        self.gridLayout.addWidget(self.le_youtube_link, 0, 0, 1, 1)
        self.l_thumbnail = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_thumbnail.sizePolicy().hasHeightForWidth())
        self.l_thumbnail.setSizePolicy(sizePolicy)
        self.l_thumbnail.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.l_thumbnail.setAutoFillBackground(False)
        self.l_thumbnail.setStyleSheet("color: #888;")
        self.l_thumbnail.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.l_thumbnail.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_thumbnail.setObjectName("l_thumbnail")
        self.gridLayout.addWidget(self.l_thumbnail, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "yt-dpl-qt6"))
        self.pb_download_video.setText(_translate("MainWindow", "Download video"))
        self.pb_download_audio.setText(_translate("MainWindow", "Download audio"))
        self.le_youtube_link.setPlaceholderText(_translate("MainWindow", "Copy-paste the youtube video link"))
        self.l_thumbnail.setText(_translate("MainWindow", "(thumbnail)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
