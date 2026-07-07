# Importa a classe WebBot, responsável por controlar o navegador.
from botcity.web import WebBot

# Importa o recurso By, utilizado para localizar elementos na página.
from botcity.web.browsers import By

# Cria uma função responsável por realizar o login no Portal Fake.
def realizar_login(bot: WebBot):

    # Exibe uma mensagem informando que a automação de login foi iniciada.
    print("--- [BotCity] Iniciando Automação de Login ---")

    # Simula o preenchimento do usuário no campo de login.
    print("Preenchendo o usuário: admin_escola")

    # Simula o preenchimento da senha de acesso.
    print("Preenchendo a senha: ****")

    # Exibe a mensagem de sucesso na autenticação.
    print("Login realizado com sucesso! Acessando o painel principal.")