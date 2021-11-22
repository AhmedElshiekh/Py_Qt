
import sys
from PyQt4 import QtCore, QtGui

from untitled import Ui_Form
from collections import OrderedDict

class GetInfo():
    def __init__(self):
        self.info = OrderedDict([('userName', None),
            ('passWord', ' ')])

    def login_name(self):
        name = raw_input("Enter Login Name: ")
        self.login_info["login_name"] = name

    def password(self):
        name = raw_input("Enter Password: ")
        self.login_info["password"] = name


class TextLineModel(QtCore.QAbstractListModel):
        def __init__(self, text, parent = none):
             QtCore.QAbstractListModel.__init__(self, parent)
             self._text = text

         def data(self, index, roll):
                if roll == QtCore.Qt.DisplayRole:
                    value = self._text
                    return value


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    x = GetInfo()
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())