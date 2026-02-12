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
            QMessageBox.critical(telaConsultaCEP, "Atenção", "Para consulta o CEP deve ser informado")
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
                QMessageBox.warning(telaConsultaCEP, "Erro", "CEP não encontrado.")
        else:
            QMessageBox.critical(telaConsultaCEP, "Erro", "Falha na consulta do CEP.")

    except Exception as e:
        QMessageBox.critical(telaConsultaCEP, "Erro", f"Ocorreu um erro: {str(e)}")


app = QApplication(sys.argv)

telaCadastro = QWidget()
telaCadastro.setWindowTitle("Verificação de CEP com API")
telaCadastro.setGeometry(100, 100, 600, 120)
               