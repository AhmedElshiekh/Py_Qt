# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try1.ui'
#
# Created: Mon May 27 04:00:05 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

    class Ui_Form(object):
        def setupUi(self, Form):
            Form.setObjectName(_fromUtf8("Form"))
            Form.resize(640, 480)
            self.label = QtGui.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(100, 30, 71, 16))
            self.label.setObjectName(_fromUtf8("label"))
            self.label_2 = QtGui.QLabel(Form)
            self.label_2.setGeometry(QtCore.QRect(100, 60, 61, 16))
            self.label_2.setObjectName(_fromUtf8("label_2"))
            self.lineEdit = QtGui.QLineEdit(Form)
            self.lineEdit.setGeometry(QtCore.QRect(160, 30, 231, 20))
            self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
            self.lineEdit_2 = QtGui.QLineEdit(Form)
            self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 231, 20))
            self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
            self.verticalLayoutWidget = QtGui.QWidget(Form)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 20, 361, 81))
            self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
            self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout_2.setMargin(0)
            self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
            Form.setWindowTitle(_translate("Form", "Form", None))
            self.label.setText(_translate("Form", "UserName:", None))
            self.label_2.setText(_translate("Form", "Password:", None))

