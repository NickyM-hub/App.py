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

    if usuario == "admin" and senha == "pass123$":
        QMessageBox.information(telaLogin, "Sucesso", f"Bem-vindo, {usuario}!")
    else:
        limpaCampos()
        QMessageBox.warning(telaLogin, "Falha no login", "Usuário ou senha inválidos.")

#Limpar Campos
def limpaCampos():
    caixaTextoUsuario.clear()
    caixaTextoSenha.clear()
    caixaTextoUsuario.setFocus() 

#Criando aplicação
app = QApplication(sys.argv) 

#Janela
telaLogin = QWidget()
telaLogin.setWindowTitle("Login")
telaLogin.setGeometry(100, 100, 300, 200)

#Rótulo(label)
#Usuário
textoRotuloUsuario = QLabel('Usuário:', telaLogin)
textoRotuloUsuario.move(80, 30)
#Senha
textoRotuloSenha = QLabel('Senha: ', telaLogin)
textoRotuloSenha.move(80, 80)


#Criando caixa de texto
#Usuário
caixaTextoUsuario = QLineEdit(telaLogin)
caixaTextoUsuario.move(80, 50)
#Senha
caixaTextoSenha = QLineEdit(telaLogin)
caixaTextoSenha.setEchoMode(QLineEdit.Password)
caixaTextoSenha.move(80, 100)


#Criando um botão
botao = QPushButton('Entrar', telaLogin)
botao.move(102, 140)

#conexão do banco a função
botao.clicked.connect(validaCampos)

#Exibindo a janela
telaLogin.show()

#Iniciando o loop de eventos
sys.exit(app.exec_())