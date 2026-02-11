import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

#mini campo para guardar os dados do usuário
def login(nome, rg, cpf, dataNascimento, nomeMae, senha):
    QMessageBox.information(telaLogin, "Sucesso", f"Bem-vindo, {nome}!\nRG: {rg}\nCPF: {cpf}\nData de Nascimento: {dataNascimento}\nNome da Mãe: {nomeMae}")


#Função para começar o campo mascarado do começo do campo
def move_cursor():
    line_edit = QLineEdit()
    line_edit.setCursorPosition(0)
    line_edit.focusInEvent = lambda event: (
    QLineEdit.focusInEvent(line_edit, event),
    line_edit.setCursorPosition(0)
)


#Verifiação de prenchimento dos campos  
def validaCampos():
    nome = caixaTextoNome.text()
    cpf = caixaTextoCpf.text()
    dataNascimento = caixaTextoDataNascimento.text()
    rg = caixaTextoRg.text()
    nomeMae = caixaTextoNomeMae.text() 
    senha = caixaTextoSenha.text()
    

    #Verificação de usuário e senha 
    if nome == '' or senha == '' or cpf == '..-' or dataNascimento == '//' or rg == '..-' or nomeMae == '':
        QMessageBox.critical(telaLogin, "Atenção", "Para validação todos os campos devem ser informados")

    elif nome == senha or nomeMae == senha:
        QMessageBox.critical(telaLogin, "Aviso!", "a senha não pode ser igual ao nome")
        caixaTextoSenha.clear()

    else:
        login(nome, rg, cpf, dataNascimento, nomeMae, senha)

#Limpar Campos
def limpaCampos():
    caixaTextoNome.clear()
    caixaTextoCpf.clear()
    caixaTextoDataNascimento.clear()
    caixaTextoRg.clear()
    caixaTextoNomeMae.clear()
    caixaTextoSenha.clear()


#Criando aplicação
app = QApplication(sys.argv) 

#Janela
telaLogin = QWidget()
telaLogin.setWindowTitle("Login")
telaLogin.setGeometry(100, 100, 300, 400)

#Rótulo(label)
#Nome
textoRotuloNome = QLabel('Nome Completo:', telaLogin)
textoRotuloNome.move(80, 30)

#CPF
textoRotuloCpf = QLabel('CPF: ', telaLogin)
textoRotuloCpf.move(80, 80)

#RG
textoRotuloRg = QLabel('RG: ', telaLogin)
textoRotuloRg.move(80, 130)

#Data de Nascimento
textoRotuloDataNascimento = QLabel('Data de Nascimento: ', telaLogin)
textoRotuloDataNascimento.move(80, 180)

#Nome da Mãe
textoRotuloNomeMae = QLabel('Nome da Mãe: ', telaLogin) 
textoRotuloNomeMae.move(80, 230)

#Senha
textoRotuloSenha = QLabel('Senha: ', telaLogin)
textoRotuloSenha.move(80, 280)


#Criando caixa de texto
#Nome
caixaTextoNome = QLineEdit(telaLogin)
caixaTextoNome.move(80, 50)

#CPF
caixaTextoCpf = QLineEdit(telaLogin)
caixaTextoCpf.setInputMask("000.000.000-00")
caixaTextoCpf.setCursorMoveStyle(Qt.LogicalMoveStyle)
caixaTextoCpf.setCursorPosition(0)
caixaTextoCpf.move(80, 100)

#RG
caixaTextoRg = QLineEdit(telaLogin)
caixaTextoRg.setInputMask("00.000.000-0")
caixaTextoRg.setCursorMoveStyle(Qt.LogicalMoveStyle)
caixaTextoRg.setCursorPosition(0)
caixaTextoRg.move(80, 150)

#Data de Nascimento
caixaTextoDataNascimento = QLineEdit(telaLogin)
caixaTextoDataNascimento.setInputMask("00/00/0000")
caixaTextoDataNascimento.setCursorMoveStyle(0)
caixaTextoDataNascimento.move(80, 200)

#Nome da Mãe
caixaTextoNomeMae = QLineEdit(telaLogin)
caixaTextoNomeMae.move(80, 250)

#Senha
caixaTextoSenha = QLineEdit(telaLogin)
caixaTextoSenha.setEchoMode(QLineEdit.Password)
caixaTextoSenha.move(80, 300)


#Criando um botão de cadastro
botaoCadastrar = QPushButton('Cadastrar', telaLogin)
botaoCadastrar.move(150, 350)

#botão Limpar campos
botaoCancelar = QPushButton('Cancelar', telaLogin)
botaoCancelar.move(60, 350)

#conexão do banco a função
botaoCadastrar.clicked.connect(validaCampos)
botaoCancelar.clicked.connect(limpaCampos)

#Exibindo a janela
telaLogin.show()

#Iniciando o loop de eventos
sys.exit(app.exec_())