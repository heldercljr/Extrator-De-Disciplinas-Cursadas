import mechanicalsoup
import re
import csv

from disciplina import Disciplina

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

browser = mechanicalsoup.StatefulBrowser(user_agent=user_agent)

url = "https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/"

browser.open(url)

# Seleciona o formulário de login

browser.select_form()

# Coleta dos dados de matrícula do aluno

login = input("Digite seu número de matrícula: ")
senha = input("Digite sua senha: ")
comando = "AlunoLogin"

browser["login"] = login
browser["senha"] = senha
browser["command"] = comando

# Submissão do formulário e login

browser.submit_selected()

# Encaminhamento para a página do histórico escolar

browser.open(url + "Controlador?command=AlunoHistorico")

# Armazenamento da página web em uma variável

page = browser.get_current_page()

# Remoção das tags span

for span in page.find_all("span"):
    span.decompose()

# Encontra a tabela de Disciplinas

tabela = page.find("tbody")

# Remove as tags da tabela e deixa apenas os textos

tabela = re.sub('<[^>]*>', '', str(tabela))

# Transforma a tabela que antes era uma string em uma lista

tabela = tabela.split("\n")

# Remove caracteres desnecessários da tabela

tabela = [s.strip() for s in tabela if not s.isspace() and s != ""]

# Transforma os elementos desestruturados em tuplas

tabela = zip(*[iter(tabela)]*8)

# Transforma as tuplas da tabela em objetos da classe Disciplina

disciplinas = [Disciplina(*t) for t in tabela]

# Abertura do arquivo .csv a ser exportado

with open("disciplinas.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:

    # Criação do escritor CSV

    escritor = csv.writer(arquivo_csv, delimiter=",",
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Criação do cabeçalho do arquivo .csv

    cabecalho = ['Código', 'Nome', 'Tipo', 'Créditos',
                 'Carga Horária', 'Média', 'Situação', 'Período']

    # Escrita do cabeçalho

    escritor.writerow(cabecalho)

    # Linhas do arquivo a serem escritas

    linhas = [[disciplina.codigo, disciplina.nome, disciplina.tipo, disciplina.creditos, disciplina.carga_horaria,
               disciplina.media, disciplina.situacao, disciplina.periodo] for disciplina in disciplinas]

    # Escrita das linhas

    escritor.writerows(linhas)
