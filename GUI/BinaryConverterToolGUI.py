# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BinaryConverterToolGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BinaryConverterToolGUI(object):
    def setupUi(self, BinaryConverterToolGUI):
        BinaryConverterToolGUI.setObjectName("BinaryConverterToolGUI")
        BinaryConverterToolGUI.setWindowModality(QtCore.Qt.NonModal)
        BinaryConverterToolGUI.setEnabled(True)
        BinaryConverterToolGUI.resize(800, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BinaryConverterToolGUI.sizePolicy().hasHeightForWidth())
        BinaryConverterToolGUI.setSizePolicy(sizePolicy)
        BinaryConverterToolGUI.setMinimumSize(QtCore.QSize(800, 430))
        BinaryConverterToolGUI.setMaximumSize(QtCore.QSize(800, 430))
        BinaryConverterToolGUI.setAutoFillBackground(False)
        BinaryConverterToolGUI.setStyleSheet("")
        self.menubar = QtWidgets.QMenuBar(BinaryConverterToolGUI)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 25))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.lbObjFileName = QtWidgets.QLabel(BinaryConverterToolGUI)
        self.lbObjFileName.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.lbObjFileName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbObjFileName.setObjectName("lbObjFileName")
        self.lbDstFileName = QtWidgets.QLabel(BinaryConverterToolGUI)
        self.lbDstFileName.setGeometry(QtCore.QRect(9, 290, 101, 20))
        self.lbDstFileName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbDstFileName.setObjectName("lbDstFileName")
        self.txObjFileName = QtWidgets.QTextEdit(BinaryConverterToolGUI)
        self.txObjFileName.setGeometry(QtCore.QRect(120, 40, 480, 50))
        self.txObjFileName.setDocumentTitle("")
        self.txObjFileName.setObjectName("txObjFileName")
        self.txDstFileName = QtWidgets.QTextEdit(BinaryConverterToolGUI)
        self.txDstFileName.setEnabled(False)
        self.txDstFileName.setGeometry(QtCore.QRect(120, 290, 480, 30))
        self.txDstFileName.setObjectName("txDstFileName")
        self.btObjFileName = QtWidgets.QPushButton(BinaryConverterToolGUI)
        self.btObjFileName.setGeometry(QtCore.QRect(610, 40, 50, 25))
        self.btObjFileName.setObjectName("btObjFileName")
        self.cbDstFileName = QtWidgets.QCheckBox(BinaryConverterToolGUI)
        self.cbDstFileName.setGeometry(QtCore.QRect(610, 290, 101, 16))
        self.cbDstFileName.setObjectName("cbDstFileName")
        self.lbDstFilePath = QtWidgets.QLabel(BinaryConverterToolGUI)
        self.lbDstFilePath.setGeometry(QtCore.QRect(10, 220, 101, 20))
        self.lbDstFilePath.setTextFormat(QtCore.Qt.AutoText)
        self.lbDstFilePath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbDstFilePath.setObjectName("lbDstFilePath")
        self.txDstFilePath = QtWidgets.QTextEdit(BinaryConverterToolGUI)
        self.txDstFilePath.setEnabled(False)
        self.txDstFilePath.setGeometry(QtCore.QRect(120, 220, 480, 50))
        self.txDstFilePath.setObjectName("txDstFilePath")
        self.cbDstFilePath = QtWidgets.QCheckBox(BinaryConverterToolGUI)
        self.cbDstFilePath.setEnabled(True)
        self.cbDstFilePath.setGeometry(QtCore.QRect(610, 220, 91, 16))
        self.cbDstFilePath.setChecked(False)
        self.cbDstFilePath.setObjectName("cbDstFilePath")
        self.btDstFilePath = QtWidgets.QPushButton(BinaryConverterToolGUI)
        self.btDstFilePath.setEnabled(False)
        self.btDstFilePath.setGeometry(QtCore.QRect(610, 240, 50, 25))
        self.btDstFilePath.setObjectName("btDstFilePath")
        self.lbDstFileNote = QtWidgets.QLabel(BinaryConverterToolGUI)
        self.lbDstFileNote.setGeometry(QtCore.QRect(120, 330, 251, 20))
        self.lbDstFileNote.setObjectName("lbDstFileNote")
        self.btDstFileProcess = QtWidgets.QPushButton(BinaryConverterToolGUI)
        self.btDstFileProcess.setGeometry(QtCore.QRect(220, 370, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btDstFileProcess.setFont(font)
        self.btDstFileProcess.setObjectName("btDstFileProcess")
        self.cbDstFileOverWrite = QtWidgets.QCheckBox(BinaryConverterToolGUI)
        self.cbDstFileOverWrite.setGeometry(QtCore.QRect(370, 330, 121, 16))
        self.cbDstFileOverWrite.setChecked(True)
        self.cbDstFileOverWrite.setObjectName("cbDstFileOverWrite")
        self.cb2ExcelFile = QtWidgets.QCheckBox(BinaryConverterToolGUI)
        self.cb2ExcelFile.setEnabled(True)
        self.cb2ExcelFile.setGeometry(QtCore.QRect(500, 330, 121, 16))
        self.cb2ExcelFile.setChecked(False)
        self.cb2ExcelFile.setObjectName("cb2ExcelFile")
        self.gbSpecMemRange = QtWidgets.QGroupBox(BinaryConverterToolGUI)
        self.gbSpecMemRange.setGeometry(QtCore.QRect(360, 100, 241, 91))
        self.gbSpecMemRange.setObjectName("gbSpecMemRange")
        self.txStartAddr = QtWidgets.QTextEdit(self.gbSpecMemRange)
        self.txStartAddr.setEnabled(False)
        self.txStartAddr.setGeometry(QtCore.QRect(110, 20, 91, 25))
        self.txStartAddr.setDocumentTitle("")
        self.txStartAddr.setObjectName("txStartAddr")
        self.txMemorySize = QtWidgets.QTextEdit(self.gbSpecMemRange)
        self.txMemorySize.setEnabled(False)
        self.txMemorySize.setGeometry(QtCore.QRect(110, 50, 91, 25))
        self.txMemorySize.setDocumentTitle("")
        self.txMemorySize.setObjectName("txMemorySize")
        self.lbStartAddr = QtWidgets.QLabel(self.gbSpecMemRange)
        self.lbStartAddr.setGeometry(QtCore.QRect(20, 20, 81, 25))
        self.lbStartAddr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbStartAddr.setObjectName("lbStartAddr")
        self.lbMemorySize = QtWidgets.QLabel(self.gbSpecMemRange)
        self.lbMemorySize.setGeometry(QtCore.QRect(10, 50, 91, 25))
        self.lbMemorySize.setTextFormat(QtCore.Qt.AutoText)
        self.lbMemorySize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbMemorySize.setObjectName("lbMemorySize")
        self.cbSpecMemRange = QtWidgets.QCheckBox(BinaryConverterToolGUI)
        self.cbSpecMemRange.setEnabled(True)
        self.cbSpecMemRange.setGeometry(QtCore.QRect(610, 110, 151, 16))
        self.cbSpecMemRange.setChecked(False)
        self.cbSpecMemRange.setObjectName("cbSpecMemRange")
        self.gbSpecMemType = QtWidgets.QGroupBox(BinaryConverterToolGUI)
        self.gbSpecMemType.setGeometry(QtCore.QRect(120, 100, 211, 91))
        self.gbSpecMemType.setObjectName("gbSpecMemType")
        self.rbSpecMemSize = QtWidgets.QRadioButton(self.gbSpecMemType)
        self.rbSpecMemSize.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.rbSpecMemSize.setChecked(True)
        self.rbSpecMemSize.setObjectName("rbSpecMemSize")
        self.rbSpecEndAddr = QtWidgets.QRadioButton(self.gbSpecMemType)
        self.rbSpecEndAddr.setGeometry(QtCore.QRect(10, 50, 191, 16))
        self.rbSpecEndAddr.setChecked(False)
        self.rbSpecEndAddr.setObjectName("rbSpecEndAddr")
        self.actionOther = QtWidgets.QAction(BinaryConverterToolGUI)
        self.actionOther.setObjectName("actionOther")
        self.actionAboutDstDecodeTool = QtWidgets.QAction(BinaryConverterToolGUI)
        self.actionAboutDstDecodeTool.setObjectName("actionAboutDstDecodeTool")
        self.menubar.raise_()
        self.btObjFileName.raise_()
        self.lbObjFileName.raise_()
        self.lbDstFileName.raise_()
        self.txObjFileName.raise_()
        self.txDstFileName.raise_()
        self.cbDstFileName.raise_()
        self.lbDstFilePath.raise_()
        self.txDstFilePath.raise_()
        self.cbDstFilePath.raise_()
        self.btDstFilePath.raise_()
        self.lbDstFileNote.raise_()
        self.btDstFileProcess.raise_()
        self.cbDstFileOverWrite.raise_()
        self.cb2ExcelFile.raise_()
        self.gbSpecMemRange.raise_()
        self.cbSpecMemRange.raise_()
        self.gbSpecMemType.raise_()
        self.menuSetting.addAction(self.actionOther)
        self.menuHelp.addAction(self.actionAboutDstDecodeTool)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(BinaryConverterToolGUI)
        QtCore.QMetaObject.connectSlotsByName(BinaryConverterToolGUI)

    def retranslateUi(self, BinaryConverterToolGUI):
        _translate = QtCore.QCoreApplication.translate
        BinaryConverterToolGUI.setWindowTitle(_translate("BinaryConverterToolGUI", "BinaryConverterToolGUI"))
        self.menuSetting.setTitle(_translate("BinaryConverterToolGUI", "menuSetting"))
        self.menuHelp.setTitle(_translate("BinaryConverterToolGUI", "Help"))
        self.lbObjFileName.setText(_translate("BinaryConverterToolGUI", "ObjectFileAddress"))
        self.lbDstFileName.setText(_translate("BinaryConverterToolGUI", "DstFileName"))
        self.txObjFileName.setHtml(_translate("BinaryConverterToolGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btObjFileName.setText(_translate("BinaryConverterToolGUI", "select"))
        self.cbDstFileName.setText(_translate("BinaryConverterToolGUI", "Handwritting"))
        self.lbDstFilePath.setText(_translate("BinaryConverterToolGUI", "DstFilePath"))
        self.cbDstFilePath.setText(_translate("BinaryConverterToolGUI", "Handwritting"))
        self.btDstFilePath.setText(_translate("BinaryConverterToolGUI", "select"))
        self.lbDstFileNote.setText(_translate("BinaryConverterToolGUI", "※ 👆 Don\'t input the extension name please."))
        self.btDstFileProcess.setText(_translate("BinaryConverterToolGUI", "DstFileProcess"))
        self.cbDstFileOverWrite.setText(_translate("BinaryConverterToolGUI", "overwrite saving"))
        self.cb2ExcelFile.setText(_translate("BinaryConverterToolGUI", "outputExcelFile"))
        self.gbSpecMemRange.setTitle(_translate("BinaryConverterToolGUI", "Specify memory range(Hex)"))
        self.txStartAddr.setHtml(_translate("BinaryConverterToolGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.txMemorySize.setHtml(_translate("BinaryConverterToolGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lbStartAddr.setText(_translate("BinaryConverterToolGUI", "StartAddress"))
        self.lbMemorySize.setText(_translate("BinaryConverterToolGUI", "MemorySize"))
        self.cbSpecMemRange.setText(_translate("BinaryConverterToolGUI", "Specify memory range"))
        self.gbSpecMemType.setTitle(_translate("BinaryConverterToolGUI", "Specify Memory Type"))
        self.rbSpecMemSize.setText(_translate("BinaryConverterToolGUI", "StartAddress/MemorySize"))
        self.rbSpecEndAddr.setText(_translate("BinaryConverterToolGUI", "StartAddress/EndAddress"))
        self.actionOther.setText(_translate("BinaryConverterToolGUI", "actionOther(NoUse)"))
        self.actionAboutDstDecodeTool.setText(_translate("BinaryConverterToolGUI", "AboutDstDecodeTool"))
