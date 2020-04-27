# -*- coding: utf-8 -*-

# I've imported QtWebEngineWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    # My Section

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.url_bar.text())
        if url.isValid():
            self.view.load(url)
        else:
            self.statusbar.showMessage('Invalid URL')

    def url_changed(self, url):
        self.url_bar.setText(url.toString())

    def open_help(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.information(MainWindow, 'About HSWB', 
    '''\
    This is a Simple Web Browser created by H.A.R.K.

    and, HSWB stands for "H.A.R.K. Simple Web Browser"

    My Website: https://hussainark.github.io
    Short Link: https://bit.ly/hark-official
    ''')

    # End of my Section

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        MainWindow.setBaseSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hswb.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.setGeometry(QtCore.QRect(1150, 10, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.go_button.setFont(font)
        self.go_button.setObjectName("go_button")
        self.url_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.url_bar.setGeometry(QtCore.QRect(10, 10, 1131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.url_bar.setFont(font)
        self.url_bar.setObjectName("url_bar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_exit.setFont(font)
        self.action_exit.setObjectName("action_exit")
        self.action_about = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_about.setFont(font)
        self.action_about.setObjectName("action_about")
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        # My Section

        self.action_exit.setShortcut('Ctrl+Q')
        self.go_button.clicked.connect(self.load)
        self.url_bar.returnPressed.connect(self.load)
        self.action_about.triggered.connect(self.open_help)
        self.action_exit.triggered.connect(MainWindow.close)
        self.view = QtWebEngineWidgets.QWebEngineView(MainWindow)
        self.view.setUrl(QtCore.QUrl('https://hussainark.github.io'))
        self.view.setGeometry(0, 80, 1200, 700)
        self.view.urlChanged.connect(self.url_changed)
        self.view.show()

        # End of My Section


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HSWB"))
        self.go_button.setText(_translate("MainWindow", "Go"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_about.setText(_translate("MainWindow", "About HSWB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
