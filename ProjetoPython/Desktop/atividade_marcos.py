import requests
import folium
import sys 
import tempfile
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit
from PyQt5.QtCore import QDate, QUrl
from datetime import date, datetime

ultimo_cep = ""
ultima_rua = ""
ultimo_bairro = ""
ultima_cidade = ""
ultimo_uf = ""

#mini campo para guardar os dados do usuário
def login(nome, rg, cpf, dataNascimento, nomeMae, senha, cep, rua, bairro, cidade, uf):
    dataFormatada = dataNascimento.toString("dd/MM/yyyy")
    QMessageBox.information(telaUpgradeLogin, "Cadastro concluído com sucesso!", f"Bem-vindo, {nome}!\nRG: {rg}\nCPF: {cpf}\nData de Nascimento: {dataFormatada}\n Nome da Mãe: {nomeMae}")

def mostrar_mapa(cep, rua, bairro, cidade, uf):
    try:
        # Converte endereço em coordenadas
        endereco = f"{rua}, {bairro}, {cidade}, {uf}, Brasil"
        url_geo = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': endereco,
            'format': 'json',
            'limit': 1
        }
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url_geo, params=params, headers=headers, timeout=10)
        dados = response.json()
        
        if dados:
            lat = float(dados[0]['lat'])
            lon = float(dados[0]['lon'])
            
            # Cria o mapa com folium
            mapa = folium.Map(location=[lat, lon], zoom_start=16)
            
            # Adiciona marcador
            folium.Marker(
                [lat, lon],
                popup=f"<b>CEP: {cep}</b><br>{rua}<br>{bairro}<br>{cidade}/{uf}",
                icon=folium.Icon(color='red', icon='home')
            ).add_to(mapa)
            
            # Salva em arquivo temporário
            with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
                mapa.save(f.name)
                temp_file = f.name
            
            # Atualiza o mapa_view existente
            mapa_view.setUrl(QUrl.fromLocalFile(temp_file))
        else:
            QMessageBox.warning(telaUpgradeLogin, "Aviso", "Não foi possível encontrar a localização no mapa")
            
    except Exception as e:
        QMessageBox.critical(telaUpgradeLogin, "Erro", f"Erro ao gerar mapa: {str(e)}")

def criar_mapa_inicial():
    mapa = folium.Map(location=[-15.78, -47.92], zoom_start=4)
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
        mapa.save(f.name)
        temp_file = f.name
    mapa_view.setUrl(QUrl.fromLocalFile(temp_file))

def conferirDataAtual():
    url = "https://todaysdatenow.com/pt-BR/tools/json-date/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # pega só a parte da data
            date_str = data["date"].split("T")[0]

            # converte para objeto datetime
            dataAtual = datetime.strptime(date_str, "%Y-%m-%d")            

            return dataAtual
        else:
            QMessageBox.critical(telaUpgradeLogin, "Erro", "Falha na consulta da data atual.\nVerifique sua conexão com a internet.")
            return None
    except Exception as e:
        QMessageBox.critical(telaUpgradeLogin, "Erro", f"Ocorreu um erro: {str(e)}")
        return None

#Consultando CEP
def tratarCEP(codigoCEP):
    global ultimo_cep, ultima_rua, ultimo_bairro, ultima_cidade, ultimo_uf
    
    url = f"https://viacep.com.br/ws/{codigoCEP}/json/"
    try:    
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                rua = data.get("logradouro", "")
                bairro = data.get("bairro", "")
                cidade = data.get("localidade", "")
                uf = data.get("uf", "")
                
                caixaTextoRua.setText(rua)
                caixaTextoBairro.setText(bairro)
                caixaTextoCidade.setText(cidade)
                caixaTextoUF.setText(uf)
                
                # Guarda os dados para usar no mapa
                ultimo_cep = codigoCEP
                ultima_rua = rua
                ultimo_bairro = bairro
                ultima_cidade = cidade
                ultimo_uf = uf
                
                # JÁ ATUALIZA O MAPA AUTOMATICAMENTE
                mostrar_mapa(ultimo_cep, ultima_rua, ultimo_bairro, ultima_cidade, ultimo_uf)
                
            else:
                QMessageBox.warning(telaUpgradeLogin, "Erro", "CEP não encontrado.")
        else:
            QMessageBox.critical(telaUpgradeLogin, "Erro", "Falha na consulta do CEP.")

    except Exception as e:
        QMessageBox.critical(telaUpgradeLogin, "Erro", f"Ocorreu um erro: {str(e)}")

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
    dataAtual = QDate.currentDate()    
    dataNascimento = QDate.fromString(dataNascimento, "dd/MM/yyyy")



    #Verificação de usuário e senha 
    if nome == '' or senha == '' or cpf == '..-' or dataNascimento == '//' or rg == '..-' or nomeMae == '' or cep == '.....-...' or rua == '' or bairro == '' or cidade == '' or uf == '':
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "Para validação todos os campos devem ser informados")
    if nome == senha or nomeMae == senha:
        QMessageBox.critical(telaUpgradeLogin, "Aviso!", "a senha não pode ser igual ao nome")
        caixaTextoSenha.clear()

    #Verificação de caracteres especiais nos nomes
    if any(i in nome for i in [';', ',', '.',  '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O nome não pode conter caracteres especiais como vírgula, ponto ou ponto, vírgula e números.")
        return
    if any(i in nomeMae for i in [';', ',', '.',  '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O nome da mãe não pode conter caracteres especiais como vírgula, ponto ou ponto e vírgula.")
        return

    #Verificação de CEP
    if len(cep) < 8:
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O CEP deve conter 8 números")
        return

    #Verificação de senha
    if len(senha) < 8:
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "A senha deve conter no mínimo 8 caracteres")
        return

    #Verificação de datas

    #data futura
    if QDate(dataNascimento) > dataAtual: 
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "A data não pode ser futura.")
        return
    #data inexistente
    if not QDate(dataNascimento).isValid():
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "Data de nascimento inválida.")
        return
    #verificação de idade
    if QDate(dataAtual).year() - QDate(dataNascimento).year() < 5:
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O usuário deve ter mais de 5 anos.")
        return
    if QDate(dataAtual).year() - QDate(dataNascimento).year() > 100:
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O usuário deve ter menos que 100 anos.")
        return
    
    #verificação de RG
    if len(rg) != 12:
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O RG deve conter 9 caracteres")
        return
    if any(i in rg for i in [';', ',', '+', 'ç']):
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O rg não pode conter caracteres especiais com ponto e vírgula etc.")
        return
    
    #verificação de CPF
    if len(cpf) != 14:
        QMessageBox.critical(telaUpgradeLogin, "Atenção", "O CPF deve conter 11 números")
        return
    
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
telaUpgradeLogin = QWidget()
telaUpgradeLogin.setWindowTitle("Login")
telaUpgradeLogin.setGeometry(800, 800, 800, 800)

mapa_view = QWebEngineView(telaUpgradeLogin)
mapa_view.setGeometry(400, 30, 380, 550)

criar_mapa_inicial()

#Rótulo(label)
#Nome
textoRotuloNome = QLabel('Nome Completo:', telaUpgradeLogin)
textoRotuloNome.move(80, 30)

#CPF
textoRotuloCpf = QLabel('CPF: ', telaUpgradeLogin)
textoRotuloCpf.move(80, 80)

#RG
textoRotuloRg = QLabel('RG: ', telaUpgradeLogin)
textoRotuloRg.move(80, 130)

#Data de Nascimento
textoRotuloDataNascimento = QLabel('Data de Nascimento: ', telaUpgradeLogin)
textoRotuloDataNascimento.move(80, 180)
#Nome da Mãe
textoRotuloNomeMae = QLabel('Nome da Mãe: ', telaUpgradeLogin) 
textoRotuloNomeMae.move(80, 230)

#Senha
textoRotuloSenha = QLabel('Senha: ', telaUpgradeLogin)
textoRotuloSenha.move(80, 280)

TextoRotuloCEP = QLabel("Digite o CEP:", telaUpgradeLogin)
TextoRotuloCEP.move(80, 330)

textoRotuloRua = QLabel("Rua:", telaUpgradeLogin)
textoRotuloRua.move(80, 380)

textoRotuloBairro = QLabel("Bairro:", telaUpgradeLogin)
textoRotuloBairro.move(80, 430)

textoRotuloCidade = QLabel("Cidade:", telaUpgradeLogin)
textoRotuloCidade.move(80, 480)

textoRotuloUF = QLabel("UF:", telaUpgradeLogin)
textoRotuloUF.move(80, 530)


#Criando caixa de texto
#Nome
caixaTextoNome = QLineEdit(telaUpgradeLogin)
caixaTextoNome.move(80, 50)

#CPF
caixaTextoCpf = QLineEdit(telaUpgradeLogin)
caixaTextoCpf.setInputMask("000.000.000-00")
caixaTextoCpf.move(80, 100)

#RG
caixaTextoRg = QLineEdit(telaUpgradeLogin)
caixaTextoRg.setInputMask("NN.NNN.NNN-N")
caixaTextoRg.setCursorPosition(0)
caixaTextoRg.move(80, 150)

#Data de Nascimento
caixaTextoDataNascimento = QLineEdit(telaUpgradeLogin)
caixaTextoDataNascimento.setInputMask("00/00/0000")
caixaTextoDataNascimento.move(80, 200)
#Nome da Mãe
caixaTextoNomeMae = QLineEdit(telaUpgradeLogin)
caixaTextoNomeMae.move(80, 250)

#Senha
caixaTextoSenha = QLineEdit(telaUpgradeLogin)
caixaTextoSenha.setEchoMode(QLineEdit.Password)
caixaTextoSenha.move(80, 300)

#CEP
caixaTextoCEP = QLineEdit(telaUpgradeLogin)
caixaTextoCEP.setInputMask("00000-000")
caixaTextoCEP.setFixedWidth(80)
caixaTextoCEP.move(80, 350)

#Rua
caixaTextoRua = QLineEdit(telaUpgradeLogin)
caixaTextoRua.setFixedWidth(260)
caixaTextoRua.move(80, 400)
caixaTextoRua.setEnabled(False)

#Bairro
caixaTextoBairro = QLineEdit(telaUpgradeLogin)
caixaTextoBairro.setFixedWidth(250)
caixaTextoBairro.move(80, 450)
caixaTextoBairro.setEnabled(False)

#Cidade
caixaTextoCidade = QLineEdit(telaUpgradeLogin)
caixaTextoCidade.setFixedWidth(250)
caixaTextoCidade.move(80, 500)
caixaTextoCidade.setEnabled(False)

#UF
caixaTextoUF = QLineEdit(telaUpgradeLogin)
caixaTextoUF.setFixedWidth(30)
caixaTextoUF.move(80, 550)
caixaTextoUF.setEnabled(False)
#Criando Botão de buca do CEP
botaoBuscarCEP = QPushButton("Buscar", telaUpgradeLogin)
botaoBuscarCEP.move(200,350)
#Criando um botão de cadastro
botaoCadastrar = QPushButton('Cadastrar', telaUpgradeLogin)
botaoCadastrar.move(200, 600)
#botão Limpar campos
botaoCancelar = QPushButton('Cancelar', telaUpgradeLogin)
botaoCancelar.move(80, 600)

#Conectando o clique do botão a função
botaoCadastrar.clicked.connect(validaCampos)
botaoBuscarCEP.clicked.connect(lambda: tratarCEP(caixaTextoCEP.text()))
botaoCancelar.clicked.connect(limpaCampos)

#Exibindo a janela
telaUpgradeLogin.show()

#Iniciando o loop de eventos
sys.exit(app.exec_())