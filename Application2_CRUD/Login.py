# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(257, 152)
        Form.setMinimumSize(QtCore.QSize(245, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.verticalGroupBox.setFont(font)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(6, 5, 6, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_User = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_User.setMinimumSize(QtCore.QSize(114, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_User.setFont(font)
        self.label_User.setObjectName("label_User")
        self.horizontalLayout.addWidget(self.label_User)
        spacerItem = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_User = QtWidgets.QLineEdit(self.verticalGroupBox)
        self.lineEdit_User.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_User.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_User.setFont(font)
        self.lineEdit_User.setStyleSheet("QLineEdit{\n"
"border: 1px  solid gray;\n"
"    \n"
"}")
        self.lineEdit_User.setObjectName("lineEdit_User")
        self.horizontalLayout.addWidget(self.lineEdit_User)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Pass = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_Pass.setFont(font)
        self.label_Pass.setObjectName("label_Pass")
        self.horizontalLayout_2.addWidget(self.label_Pass)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_Pass = QtWidgets.QLineEdit(self.verticalGroupBox)
        self.lineEdit_Pass.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_Pass.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_Pass.setFont(font)
        self.lineEdit_Pass.setStyleSheet("QLineEdit{\n"
"border: 1px  solid gray;\n"
"    \n"
"}")
        self.lineEdit_Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Pass.setObjectName("lineEdit_Pass")
        self.horizontalLayout_2.addWidget(self.lineEdit_Pass)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_OK = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_OK.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.horizontalLayout_3.addWidget(self.pushButton_OK)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.verticalGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.verticalGroupBox.setTitle(_translate("Form", "Connexion"))
        self.label_User.setText(_translate("Form", "Nom d\'utilisateur :"))
        self.label_Pass.setText(_translate("Form", "Mot de passe :"))
        self.pushButton_OK.setText(_translate("Form", "Connexion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())