# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created: Sat Jul 23 18:22:33 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
# from kfilemetadatawidget import KFileMetaDataWidget
# from kpixmapregionselectorwidget import KPixmapRegionSelectorWidget

# ---------------------------------------------
# -------------- ENCODING ---------------------
# ---------------------------------------------

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------

class Ui_Frame(object):

    # -------------- CONSTRUTOR ------------------

   # def __init__(self, Frame):

    #    self.setupUI(Frame)

    # --------------------------------------------
    # --------------------------------------------

    def __init__(self, Frame):
    
        # Frame
    
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(640, 480)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)

        # Tabs
        self.tabWidget = QtGui.QTabWidget(Frame)
        self.tabWidget.setGeometry(QtCore.QRect(130, 10, 491, 461))
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        # Tab 1 - Diagrama de Classe
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.picture = QtGui.QLabel(self.tab)
        self.picture.setGeometry(0, 10, 471, 411)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        # Tab 2 - Codigo em python
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 471, 411))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        # Botoes - 1 para cada design pattern

        self.commandLinkButton = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 120, 131, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(lambda: self.file_open('../Singleton/README.md'))
        self.commandLinkButton.clicked.connect(lambda: self.image_open('../etc/Singleton_example.png'))

        self.commandLinkButton_2 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(0, 200, 131, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_2.clicked.connect(lambda: self.file_open('../Adapter/README.md'))
        self.commandLinkButton_2.clicked.connect(lambda: self.image_open('../etc/Adapter_example.png'))

        self.commandLinkButton_3 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(0, 240, 131, 41))
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.commandLinkButton_3.clicked.connect(lambda: self.file_open('../Composite/README.md'))
        self.commandLinkButton_3.clicked.connect(lambda: self.image_open('../etc/Composite_example.png'))

        self.commandLinkButton_4 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(0, 280, 131, 41))
        self.commandLinkButton_4.setObjectName(_fromUtf8("commandLinkButton_4"))
        self.commandLinkButton_4.clicked.connect(lambda: self.file_open('../Facade/README.md'))
        self.commandLinkButton_4.clicked.connect(lambda: self.image_open('../etc/Facade_example.png'))

        self.commandLinkButton_5 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(0, 320, 131, 41))
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        self.commandLinkButton_5.clicked.connect(lambda: self.file_open('../Proxy/README.md'))
        self.commandLinkButton_5.clicked.connect(lambda: self.image_open('../etc/Proxy_example.png'))

        self.commandLinkButton_6 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 390, 131, 41))
        self.commandLinkButton_6.setObjectName(_fromUtf8("commandLinkButton_6"))
        self.commandLinkButton_6.clicked.connect(lambda: self.file_open('../Command/README.md'))
        self.commandLinkButton_6.clicked.connect(lambda: self.image_open('../etc/Command_example.png'))

        self.commandLinkButton_7 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(0, 80, 131, 41))
        self.commandLinkButton_7.setObjectName(_fromUtf8("commandLinkButton_7"))
        self.commandLinkButton_7.clicked.connect(lambda: self.file_open('../FactoryMethod/README.md'))
        self.commandLinkButton_7.clicked.connect(lambda: self.image_open('../etc/Factory_Method_example.png'))

        self.commandLinkButton_8 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_8.setGeometry(QtCore.QRect(0, 430, 131, 41))
        self.commandLinkButton_8.setObjectName(_fromUtf8("commandLinkButton_8"))
        self.commandLinkButton_8.clicked.connect(lambda: self.file_open('../Observer/README.md'))
        self.commandLinkButton_8.clicked.connect(lambda: self.image_open('../etc/Observer_example.png'))

        self.commandLinkButton_9 = QtGui.QCommandLinkButton(Frame)
        self.commandLinkButton_9.setGeometry(QtCore.QRect(0, 40, 131, 41))
        self.commandLinkButton_9.setObjectName(_fromUtf8("commandLinkButton_9"))
        self.commandLinkButton_9.clicked.connect(lambda: self.file_open('../AbstractFactory/README.md'))
        self.commandLinkButton_9.clicked.connect(lambda: self.image_open('../etc/Abstract_Factory_example.png'))

        # Labels - Creational, Structural e Behavioral

        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        # Renomeando os UI
        self.retranslateUi(Frame)

        # Setando tab deafult
        self.tabWidget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(Frame)

        Frame.show()

    # --------------------------------------------
    # --------------------------------------------

    def file_open(self, name):
        file = open(name, 'r')
        with file:
            text = file.read()
            self.plainTextEdit.setPlainText(text)

    # --------------------------------------------
    # --------------------------------------------

    def image_open(self, name):
        self.picture.setPixmap(QtGui.QPixmap(name))


    # --------------------------------------------
    # --------------------------------------------

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Desing Patterns", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Frame", "Diagrama de classe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Frame", "Código em Python", None))
        self.commandLinkButton.setText(_translate("Frame", "Singleton", None))
        self.commandLinkButton_2.setText(_translate("Frame", "Adapter", None))
        self.commandLinkButton_3.setText(_translate("Frame", "Composite", None))
        self.commandLinkButton_4.setText(_translate("Frame", "Facade", None))
        self.commandLinkButton_5.setText(_translate("Frame", "Proxy", None))
        self.commandLinkButton_6.setText(_translate("Frame", "Command", None))
        self.commandLinkButton_7.setText(_translate("Frame", "Factory Method", None))
        self.commandLinkButton_8.setText(_translate("Frame", "Observer", None))
        self.commandLinkButton_9.setText(_translate("Frame", "Abstract Factory", None))
        self.label.setText(_translate("Frame", "Creational", None))
        self.label_2.setText(_translate("Frame", "Structural", None))
        self.label_3.setText(_translate("Frame", "Behavioral", None))


# --------------------------------------------
# -------- MAIN : RODA O PROGRAMA ------------
# --------------------------------------------

def main():
    app = QtGui.QApplication(sys.argv)
    frame = QtGui.QFrame()
    Ui_Frame(frame)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


