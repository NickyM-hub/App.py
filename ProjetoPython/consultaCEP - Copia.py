import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox  


def limpaCampos():
    caixaTextoCEP.clear()
    caixaTextoRua.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUF.clear()
    caixaTextoCEP.setFocus()


def validaCampos():
        codigoCEP = caixaTextoCEP.text()

        if codigoCEP == '':
            QMessageBox.critical(telaCadastro, "Atenção", "Para consulta o CEP deve ser informado")
            caixaTextoCEP.setFocus()
        else:
            tratarCEP(codigoCEP)

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
                QMessageBox.warning(telaCadastro, "Erro", "CEP não encontrado.")
        else:
            QMessageBox.critical(telaCadastro, "Erro", "Falha na consulta do CEP.")

    except Exception as e:
        QMessageBox.critical(telaCadastro, "Erro", f"Ocorreu um erro: {str(e)}")


app = QApplication(sys.argv)

telaCadastro = QWidget()
telaCadastro.setWindowTitle("Verificação de CEP com API")
telaCadastro.setGeometry(100, 100, 600, 120)

#Criando Rótulos (label)
TextoRotuloCEP = QLabel("Digite o CEP:", telaCadastro)
TextoRotuloCEP.move(10, 10)

textoRotuloRua = QLabel("Rua:", telaCadastro)
textoRotuloRua.move(10, 40)

textoRotuloBairro = QLabel("Bairro:", telaCadastro)
textoRotuloBairro.move(10, 60)

textoRotuloCidade = QLabel("Cidade:", telaCadastro)
textoRotuloCidade.move(270, 60)

textoRotuloUF = QLabel("UF:", telaCadastro)
textoRotuloUF.move(530, 60)

#Criando Caixa de Texto
#CEP
caixaTextoCEP = QLineEdit(telaCadastro)
caixaTextoCEP.setFixedWidth(80)
caixaTextoCEP.setInputMask("00000-000")
caixaTextoCEP.move(10, 30)

#Rua
caixaTextoRua = QLineEdit(telaCadastro)
caixaTextoRua.setFixedWidth(260)
caixaTextoRua.move(300, 30)
caixaTextoRua.setEnabled(False)

#Bairro
caixaTextoBairro = QLineEdit(telaCadastro)
caixaTextoBairro.setFixedWidth(250)
caixaTextoBairro.move(10, 80)
caixaTextoBairro.setEnabled(False)

#Cidade
caixaTextoCidade = QLineEdit(telaCadastro)
caixaTextoCidade.setFixedWidth(250)
caixaTextoCidade.move(270, 80)
caixaTextoCidade.setEnabled(False)

#UF
caixaTextoUF = QLineEdit(telaCadastro)
caixaTextoUF.setFixedWidth(30)
caixaTextoUF.move(530, 80)
caixaTextoUF.setEnabled(False)

#Criando Botão de buca do CEP
botaoBuscarCEP = QPushButton("Buscar", telaCadastro)
botaoBuscarCEP.move(100, 25)

#Conectando o clique do botão a função
botaoBuscarCEP.clicked.connect(validaCampos)

#Criando Botão de Limpar os campos
botaoLimpar = QPushButton("Limpar buscar", telaCadastro)
botaoLimpar.move(200, 25)

#Conectando o clique do botão a função
botaoLimpar.clicked.connect(limpaCampos)

telaCadastro.show()
sys.exit(app.exec_())