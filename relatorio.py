# Importa a classe WebBot, responsável por controlar o navegador.
from botcity.web import WebBot

# Importa o recurso By, utilizado para localizar elementos na página.
from botcity.web.browsers import By

# Cria uma função responsável por exportar os relatórios no Portal Fake.
def exportar_relatorio(bot: WebBot):

    # Exibe uma mensagem informando que a automação de relatórios foi iniciada.
    print("--- [BotCity] Iniciando Automação de Relatórios ---")

    # Simula o clique no botão de exportar dados da tabela.
    print("Acessando o menu de Relatórios Gerenciais...")

    # Simula o download do arquivo PDF/Excel.
    print("Fazendo o download do arquivo: relatorio_final_alunos.pdf")

    # Exibe a mensagem de sucesso na operação.
    print("Relatório exportado com sucesso para a pasta de Downloads!")