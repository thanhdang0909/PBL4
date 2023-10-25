# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(800, 625)
        SignUp.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(SignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.lblSignUp = QtWidgets.QLabel(self.centralwidget)
        self.lblSignUp.setGeometry(QtCore.QRect(280, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblSignUp.setFont(font)
        self.lblSignUp.setObjectName("lblSignUp")
        self.lblUserID = QtWidgets.QLabel(self.centralwidget)
        self.lblUserID.setGeometry(QtCore.QRect(120, 150, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblUserID.setFont(font)
        self.lblUserID.setObjectName("lblUserID")
        self.lblPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword.setGeometry(QtCore.QRect(120, 210, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.lblConfirmPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblConfirmPassword.setGeometry(QtCore.QRect(120, 280, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblConfirmPassword.setFont(font)
        self.lblConfirmPassword.setObjectName("lblConfirmPassword")
        self.txtUserID = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtUserID.setGeometry(QtCore.QRect(370, 140, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtUserID.setFont(font)
        self.txtUserID.setObjectName("txtUserID")
        self.txtPassword = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(370, 200, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        self.txtConfirmPassword = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtConfirmPassword.setGeometry(QtCore.QRect(370, 270, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtConfirmPassword.setFont(font)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(430, 370, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnForgotPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnForgotPassword.setGeometry(QtCore.QRect(190, 370, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btnForgotPassword.setFont(font)
        self.btnForgotPassword.setObjectName("btnForgotPassword")
        self.lblOr = QtWidgets.QLabel(self.centralwidget)
        self.lblOr.setGeometry(QtCore.QRect(370, 430, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.lblOr.setFont(font)
        self.lblOr.setObjectName("lblOr")
        self.btnCreateAccount = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateAccount.setGeometry(QtCore.QRect(250, 470, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCreateAccount.setFont(font)
        self.btnCreateAccount.setObjectName("btnCreateAccount")
        self.btnSigninGoogle = QtWidgets.QPushButton(self.centralwidget)
        self.btnSigninGoogle.setGeometry(QtCore.QRect(250, 520, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnSigninGoogle.setFont(font)
        self.btnSigninGoogle.setObjectName("btnSigninGoogle")
        SignUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SignUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignUp)
        self.statusbar.setObjectName("statusbar")
        SignUp.setStatusBar(self.statusbar)

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "MainWindow"))
        self.lblSignUp.setText(_translate("SignUp", "SIGN UP"))
        self.lblUserID.setText(_translate("SignUp", "User ID"))
        self.lblPassword.setText(_translate("SignUp", "Password"))
        self.lblConfirmPassword.setText(_translate("SignUp", "Confirm Password"))
        self.btnLogin.setText(_translate("SignUp", "Login"))
        self.btnForgotPassword.setText(_translate("SignUp", "Forgot Password"))
        self.lblOr.setText(_translate("SignUp", "or"))
        self.btnCreateAccount.setText(_translate("SignUp", "Craete an Account"))
        self.btnSigninGoogle.setText(_translate("SignUp", "Sign in with Google"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QMainWindow()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())
