# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(779, 650)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 70, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 420, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_plaintext = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_plaintext.setGeometry(QtCore.QRect(130, 190, 381, 71))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_key = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_key.setGeometry(QtCore.QRect(130, 290, 381, 71))
        self.txt_key.setObjectName("txt_key")
        self.txt_ciphertext = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_ciphertext.setGeometry(QtCore.QRect(130, 410, 381, 71))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.btn_encrypt = QtWidgets.QPushButton(Dialog)
        self.btn_encrypt.setGeometry(QtCore.QRect(130, 540, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(Dialog)
        self.btn_decrypt.setGeometry(QtCore.QRect(440, 540, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CAESAR CIPHER"))
        self.label_2.setText(_translate("Dialog", "Plain_text:"))
        self.label_3.setText(_translate("Dialog", "Key:"))
        self.label_4.setText(_translate("Dialog", "Cipher_text:"))
        self.btn_encrypt.setText(_translate("Dialog", "Encrypt"))
        self.btn_decrypt.setText(_translate("Dialog", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
