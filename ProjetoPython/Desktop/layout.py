import requests
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt

# a pessoa deve ter ,no mínimo, 10 anos e no máximo 100 anos
# datas futuras ou inexistentes não são autorizadas
# permitir numero e letra no cep
# n pode ter vírgula ou ponto e vírgula ou ponto nos campos
# o cep deve ser mostrado assim que tiver 8 números, independente se os outros campos foram preenchidos ou não
# o rg, cpf, data de nascimento, senha e cep só podem funcionar com um limite mínimo de caracteres
# mostrar o horário que aconteceu o cadastro
# mostrar a idade da pessoa com base na data dela e a data atual

#mini campo para guardar os dados do usuário
def login(nome, rg, cpf, dataNascimento, nomeMae, senha):
    QMessageBox.information(telaLogin, "Sucesso", f"Bem-vindo, {nome}!\nRG: {rg}\nCPF: {cpf}\nData de Nascimento: {dataNascimento}\nNome da Mãe: {nomeMae}")


def tratarCEP(codigoCEP):
    url = f"https://viacep.com.br/ws/{codigoCEP}/json/"
    try:    
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                caixaTextoRua.setText(data.get("logradouro", ""))
                caixaTextoBairro.setText(data.get("bairro", ""))
                caixaTextoCidade.setText(data.get("localidade", ""))
                caixaTextoUF.setText(data.get("uf", ""))
            else:
                QMessageBox.warning(telaLogin, "Erro", "CEP não encontrado.")
        else:
            QMessageBox.critical(telaLogin, "Erro", "Falha na consulta do CEP.")

    except Exception as e:
        QMessageBox.critical(telaLogin, "Erro", f"Ocorreu um erro: {str(e)}")



#Verifiação de prenchimento dos campos  
def validaCampos():
    nome = caixaTextoNome.text()
    cpf = caixaTextoCpf.text()
    dataNascimento = caixaTextoDataNascimento.text()
    rg = caixaTextoRg.text()
    nomeMae = caixaTextoNomeMae.text() 
    senha = caixaTextoSenha.text()
    cep = caixaTextoCEP.text()
    rua = caixaTextoRua.text()
    bairro = caixaTextoBairro.text()
    cidade = caixaTextoCidade.text()
    uf = caixaTextoUF.text()
    senha = caixaTextoSenha.text()
    dataAtual = QDate.currentDate()
    dataNascimento = QDate.fromString(dataNascimento, "dd/MM/yyyy")

    #Verificação de usuário e senha 
    if nome == '' or senha == '' or cpf == '..-' or dataNascimento == '//' or rg == '..-' or nomeMae == '':
        QMessageBox.critical(telaLogin, "Atenção", "Para validação todos os campos devem ser informados")
    if nome == senha or nomeMae == senha:
        QMessageBox.critical(telaLogin, "Aviso!", "a senha não pode ser igual ao nome")
        caixaTextoSenha.clear()

    #Verificação de CEP
    if cep < 8:
        QMessageBox.critical(telaLogin, "Atenção", "O CEP deve conter 8 números")

    #Verificação de CPF, RG e Data de Nascimento
    if dataNascimento > dataAtual and  (dataAtual - dataNascimento) <= 10 or (dataAtual - dataNascimento) >= 100:
        QMessageBox.critical(telaLogin, "Atenção", "A data de nascimento não pode ser futura e a pessoa deve ter no mínimo 10 anos")  
    if rg != 9:
        QMessageBox.critical(telaLogin, "Atenção", "O RG deve conter 9 caracteres")
    if cpf != 11:
        QMessageBox.critical(telaLogin, "Atenção", "O CPF deve conter 11 números")
    
    else:
        login(nome, rg, cpf, dataNascimento, nomeMae, senha, cep, rua, bairro, cidade, uf)



#Limpar Campos
def limpaCampos():
    caixaTextoNome.clear()
    caixaTextoCpf.clear()
    caixaTextoDataNascimento.clear()
    caixaTextoRg.clear()
    caixaTextoNomeMae.clear()
    caixaTextoSenha.clear()
    caixaTextoCEP.clear()
    caixaTextoRua.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUF.clear()
    caixaTextoCEP.setFocus()





#Criando aplicação
app = QApplication(sys.argv) 

#Janela
telaLogin = QWidget()
telaLogin.setWindowTitle("Login")
telaLogin.setGeometry(800, 800, 800, 800)

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

TextoRotuloCEP = QLabel("Digite o CEP:", telaLogin)
TextoRotuloCEP.move(80, 330)

textoRotuloRua = QLabel("Rua:", telaLogin)
textoRotuloRua.move(80, 380)

textoRotuloBairro = QLabel("Bairro:", telaLogin)
textoRotuloBairro.move(80, 430)

textoRotuloCidade = QLabel("Cidade:", telaLogin)
textoRotuloCidade.move(80, 480)

textoRotuloUF = QLabel("UF:", telaLogin)
textoRotuloUF.move(80, 530)



#Criando caixa de texto
#Nome
caixaTextoNome = QLineEdit(telaLogin)
caixaTextoNome.move(80, 50)

#CPF
caixaTextoCpf = QLineEdit(telaLogin)
caixaTextoCpf.setInputMask("000.000.000-00")
caixaTextoCpf
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

#CEP
caixaTextoCEP = QLineEdit(telaLogin)
caixaTextoCEP.setFixedWidth(80)
caixaTextoCEP.setInputMask("00000-000")
caixaTextoCEP.move(80, 350)

#Rua
caixaTextoRua = QLineEdit(telaLogin)
caixaTextoRua.setFixedWidth(260)
caixaTextoRua.move(80, 400)
caixaTextoRua.setEnabled(False)

#Bairro
caixaTextoBairro = QLineEdit(telaLogin)
caixaTextoBairro.setFixedWidth(250)
caixaTextoBairro.move(80, 450)
caixaTextoBairro.setEnabled(False)

#Cidade
caixaTextoCidade = QLineEdit(telaLogin)
caixaTextoCidade.setFixedWidth(250)
caixaTextoCidade.move(80, 500)
caixaTextoCidade.setEnabled(False)

#UF
caixaTextoUF = QLineEdit(telaLogin)
caixaTextoUF.setFixedWidth(30)
caixaTextoUF.move(80, 550)
caixaTextoUF.setEnabled(False)

#Criando Botão de buca do CEP
botaoBuscarCEP = QPushButton("Buscar", telaLogin)
botaoBuscarCEP.move(200,350)
#Criando um botão de cadastro
botaoCadastrar = QPushButton('Cadastrar', telaLogin)
botaoCadastrar.move(200, 600)
#botão Limpar campos
botaoCancelar = QPushButton('Cancelar', telaLogin)
botaoCancelar.move(80, 600)

#Conectando o clique do botão a função
botaoCadastrar.clicked.connect(validaCampos)
botaoBuscarCEP.clicked.connect(lambda: tratarCEP(caixaTextoCEP.text()))
botaoCancelar.clicked.connect(limpaCampos)

#Exibindo a janela
telaLogin.show()

#Iniciando o loop de eventos
sys.exit(app.exec_())