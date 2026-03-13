import sys
import requests
import folium
import tempfile
import time
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QDate, QUrl
from datetime import date, datetime

#variáveis globais
ultimo_cep = ""
ultima_rua = ""
ultimo_bairro = ""
ultima_cidade = ""
ultimo_uf = ""

#guardar dados do usuário
def login(nome, cin, dataNascimento, idade, nomeMae, senha, cep, rua, bairro, cidade, uf):
    dataFormatada = dataNascimento.toString("dd/MM/yyyy")
    QMessageBox.information(telaLogin, "Cadastro concluído com sucesso!", f"Bem-vindo, {nome}!\nCIN: {cin}\nData de Nascimento: {dataFormatada}\nIdade: {idade}\nNome da Mãe: {nomeMae}")

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
                
                ultimo_cep = codigoCEP
                ultima_rua = rua
                ultimo_bairro = bairro
                ultima_cidade = cidade
                ultimo_uf = uf
                mostrar_mapa(ultimo_cep, ultima_rua, ultimo_bairro, ultima_cidade, ultimo_uf)
                
            else:
                QMessageBox.warning(telaLogin, "Erro", "CEP não encontrado.")
        else:
            QMessageBox.critical(telaLogin, "Erro", "Falha na consulta do CEP.")

    except Exception as e:
        QMessageBox.critical(telaLogin, "Erro", f"Ocorreu um erro: {str(e)}")

def mostrar_mapa(cep, rua, bairro, cidade, uf):
    time.sleep(1)
    try:
        #converção de endereço
        endereco = f"{rua}, {bairro}, {cidade}, {uf}, Brasil"
        url_geo = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': endereco,
            'format': 'json',
            'limit': 1
        }
        headers = {
            'User-Agent': 'SistemaCadastroEndereco/1.0 (moura2007nick@gmail.com)'
        }
        
        response = requests.get(url_geo, params=params, headers=headers, timeout=10)
        dados = response.json()
        print(dados)
        if dados:
            lat = float(dados[0]['lat'])
            lon = float(dados[0]['lon'])
            
            #mapa
            mapa = folium.Map(location=[lat, lon], zoom_start=16)
            
            #marcador
            folium.Marker(
                [lat, lon],
                popup=f"<b>CEP: {cep}</b><br>{rua}<br>{bairro}<br>{cidade}/{uf}",
                icon=folium.Icon(color='red', icon='home')
            ).add_to(mapa)
            
            #arquivo temporário
            with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
                mapa.save(f.name)
                temp_file = f.name
            
            # Atualiza o mapa
            mapa_view.setUrl(QUrl.fromLocalFile(temp_file))
        else:
            QMessageBox.warning(telaLogin, "Aviso", "Não foi possível encontrar a localização no mapa")
            
    except Exception as e:
        QMessageBox.critical(telaLogin, "Erro", f"Erro ao gerar mapa: {str(e)}")

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
            QMessageBox.critical(telaLogin, "Erro", "Falha na consulta da data atual.\nVerifique sua conexão com a internet.")
            return None
    except Exception as e:
        QMessageBox.critical(telaLogin, "Erro", f"Ocorreu um erro: {str(e)}")
        return None

def mensagensZueira(idade):
    if idade >= 100:
        print("Pedido negado")
    elif idade >= 90:
        print("Testemunha ocular da invenção da roda")
    elif idade >= 80:
        print("Patrocinado por: Dentadura Sorriso e Andador Speed")
    elif idade >= 70:
        print("Fila do banco virou a única atividade social da semana")
    elif idade >= 60:
        print("Remédio genérico é seu melhor amigo")
    elif idade >= 50:
        print("'No meu tempo é que era bom...'")
    elif idade >= 40:
        print("Barriga de chope: oficializada")
    elif idade >= 30:
        print("Sentiu dor na lombar só de ler isso")
    elif idade >= 20:
        print("Crise dos 20: 'Já era pra eu estar...")
    elif idade >= 18:
        print("Maior de idade")
    elif idade >= 13:
        print("Aborrecente")
    elif idade >= 10:
        print("Merenda escolar virou o único motivo pra ir à aula")
    elif idade >= 5:
        print("Cotoco de gente")
    else:
        print("Pedido negado")

def calcIdade(dataNascimento):

    data_nascimento = date(
        dataNascimento.year(),
        dataNascimento.month(),
        dataNascimento.day()
    )    

    hoje = QDate.currentDate()    
    
    idade = hoje.year() - data_nascimento.year  
    
    return idade

#Verifiação de prenchimento dos campos  
def validaCampos():
    nome = caixaTextoNome.text()
    cin = caixaTextoCIN.text()
    dataNascimento = caixaTextoDataNascimento.text()
    nomeMae = caixaTextoNomeMae.text() 
    senha = caixaTextoSenha.text()
    cep = caixaTextoCEP.text()
    rua = caixaTextoRua.text()
    bairro = caixaTextoBairro.text()
    cidade = caixaTextoCidade.text()
    uf = caixaTextoUF.text()
    dataAtual = QDate.currentDate()    
    dataNascimento = QDate.fromString(dataNascimento, "dd/MM/yyyy")
    idade = calcIdade(dataNascimento)
    caixaTextoIdade.setText(str(idade))
    if botaoZueira.isChecked():
        mensagensZueira(idade)


    #Verificação de usuário e senha 
    if nome == '' or senha == '' or cin == '..-' or dataNascimento == '//' or nomeMae == '' or cep == '.....-...' or rua == '' or bairro == '' or cidade == '' or uf == '':
        QMessageBox.critical(telaLogin, "Atenção", "Para validação todos os campos devem ser informados")
    if nome == senha or nomeMae == senha:
        QMessageBox.critical(telaLogin, "Aviso!", "a senha não pode ser igual ao nome")
        caixaTextoSenha.clear()

    #Verificação de caracteres especiais nos nomes
    if any(i in nome for i in [';', ',', '.',  '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        QMessageBox.critical(telaLogin, "Atenção", "O nome não pode conter caracteres especiais como vírgula, ponto ou ponto, vírgula e números.")
        return
    if any(i in nomeMae for i in [';', ',', '.',  '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        QMessageBox.critical(telaLogin, "Atenção", "O nome da mãe não pode conter caracteres especiais como vírgula, ponto ou ponto e vírgula.")
        return

    #Verificação de CEP
    if len(cep) < 8:
        QMessageBox.critical(telaLogin, "Atenção", "O CEP deve conter 8 números")
        return

    #Verificação de senha
    if len(senha) < 8:
        QMessageBox.critical(telaLogin, "Atenção", "A senha deve conter no mínimo 8 caracteres")
        return

    #Verificação de datas

    #data futura
    if QDate(dataNascimento) > dataAtual: 
        QMessageBox.critical(telaLogin, "Atenção", "A data não pode ser futura.")
        return
    #data inexistente
    if not QDate(dataNascimento).isValid():
        QMessageBox.critical(telaLogin, "Atenção", "Data de nascimento inválida.")
        return
    #verificação de idade
    if idade < 5:
        QMessageBox.critical(telaLogin, "Atenção", "O usuário deve ter mais de 5 anos.")
        return
    if idade > 100:
        QMessageBox.critical(telaLogin, "Atenção", "O usuário deve ter menos que 100 anos.")
        return
    
    #verificação de CPF
    if len(cin) != 14:
        QMessageBox.critical(telaLogin, "Atenção", "O CPF deve conter 11 números")
        return
    
    else:
        login(nome, cin, dataNascimento, idade, nomeMae, senha, cep, rua, bairro, cidade, uf)


#Limpar Campos
def limpaCampos():
    caixaTextoNome.clear()
    caixaTextoCIN.clear()
    caixaTextoDataNascimento.clear()
    caixaTextoNomeMae.clear()
    caixaTextoSenha.clear()
    caixaTextoCEP.clear()
    caixaTextoRua.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUF.clear()
    caixaTextoCEP.setFocus()
    caixaTextoIdade.setFocus()




#Criando aplicação
app = QApplication(sys.argv) 

#Janela
telaLogin = QWidget()
telaLogin.setWindowTitle("Login")
telaLogin.setGeometry(800, 800, 800, 800)

mapa_view = QWebEngineView(telaLogin)
mapa_view.setGeometry(400, 30, 380, 550)

criar_mapa_inicial()

#Rótulo(label)
#Nome
textoRotuloNome = QLabel('Nome Completo:', telaLogin)
textoRotuloNome.move(80, 30)

#CPF
textoRotuloCIN = QLabel('CIN (CPF): ', telaLogin)
textoRotuloCIN.move(80, 80)



#Data de Nascimento
textoRotuloDataNascimento = QLabel('Data de Nascimento: ', telaLogin)
textoRotuloDataNascimento.move(80, 180)

#Idade
textoRotuloIdade = QLabel('Idade: ', telaLogin)
textoRotuloIdade.move(250, 180)

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
caixaTextoCIN = QLineEdit(telaLogin)
caixaTextoCIN.setInputMask("000.000.000-00")
caixaTextoCIN.move(80, 100)

#Data de Nascimento
caixaTextoDataNascimento = QLineEdit(telaLogin)
caixaTextoDataNascimento.setInputMask("00/00/0000")
caixaTextoDataNascimento.move(80, 200)

#Idade 
caixaTextoIdade = QLineEdit(telaLogin)
caixaTextoIdade.move(250 ,200)
caixaTextoIdade.setEnabled(False)

#Nome da Mãe
caixaTextoNomeMae = QLineEdit(telaLogin)
caixaTextoNomeMae.move(80, 250)

#Senha
caixaTextoSenha = QLineEdit(telaLogin)
caixaTextoSenha.setEchoMode(QLineEdit.Password)
caixaTextoSenha.move(80, 300)

#CEP
caixaTextoCEP = QLineEdit(telaLogin)
caixaTextoCEP.setInputMask("00000-000")
caixaTextoCEP.setFixedWidth(80)
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

#Botão zoeira
botaoZueira = QPushButton("Ver classificação?",telaLogin)
botaoZueira.setCheckable(True)
botaoZueira.setObjectName('botaoZueira')
botaoZueira.move(250, 225)

botaoZueira.setStyleSheet("""
            QPushButton {
                background-color: #999999;
                color: white;
            }
            QPushButton:hover {
                background-color: #fffa5e;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #a4ff5e;
                color: #000000;
            }
            QPushButton:checked {
                background-color: #a4ff5e;
                color: #000000;
            }
""")

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