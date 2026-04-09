import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

janelinha = uic.loadUi("telinha.ui")

def enviar_nome():
    nome = janelinha.txtNome.text()
    janelinha.label_2.setText(f"Olá, {nome}")

janelinha.btnEnviar.clicked.connect(enviar_nome)
janelinha.show()

sys.exit(app.exect_())