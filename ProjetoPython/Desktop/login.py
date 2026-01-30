import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

#Verifiação de prenchimento dos campos  
def validaCampos():
    usuario = caixaTextoUsuario.text()
    senha = caixaTextoSenha.text()

    #Verificação de usuário e senha 
    if usuario == '' or senha == '':
        QMessageBox.critical(telaLogin, "Atenção", "Para validação os dois campos devem ser informados")
        limpaCampos()
    else:
        login(usuario, senha)

def login(usuario, senha):

    if usuario == "admin" and senha == "pass123$"
        QMessageBox.information(telaLogin)   