# Importa a biblioteca Pandas, utilizada para ler e manipular planilhas do Excel.
import pandas as pd

# Importa a classe WebBot, responsável por controlar o navegador.
from botcity.web import WebBot

# Importa o recurso By, utilizado para localizar elementos na página (ID, nome, XPath etc.).
from botcity.web.browsers import By

# Cria uma função responsável por cadastrar os usuários da planilha no Portal Fake.
def cadastrar_usuarios_do_excel(bot: WebBot):

    # Exibe uma mensagem informando que a automação foi iniciada.
    print("--- [BotCity] Iniciando Automação de Cadastro via Excel ---")

    # Lê o arquivo 'usuarios.xlsx' e armazena seus dados na variável 'dados'.
    dados = pd.read_excel("usuarios.xlsx")

    # Percorre cada linha da planilha, uma por vez.
    for index, linha in dados.iterrows():

        # Exibe no terminal o nome do usuário que está sendo cadastrado.
        print(f"Cadastrando o usuário: {linha['Nome']} {linha['Sobrenome']}")