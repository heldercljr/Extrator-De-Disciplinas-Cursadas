import mechanicalsoup
import re

from disciplina import Disciplina

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

browser = mechanicalsoup.StatefulBrowser(user_agent=user_agent)

url = "https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/"

browser.open(url)

# Seleciona o formulário de login

browser.select_form()

# Matrícula antiga da UFCG

login = "118210158"
senha = "helder.cpp2019"
comando = "AlunoLogin"

browser["login"] = login
browser["senha"] = senha
browser["command"] = comando

# Submissão do formulário e login

browser.submit_selected()

# Encaminhamento para a página do histórico escolar

browser.open(url + "Controlador?command=AlunoHistorico")

# Armazena a página web em uma variável

page = browser.get_current_page()

# Remove as tags span

for span in page.find_all("span"):
	span.decompose()

# Encontra a tabela de Disciplinas
table = page.find("tbody")

# Remove as tags da tabela e deixa apenas os textos

table = re.sub('<[^>]*>', '', str(table))

# Transforma a tabela que antes era uma string em uma lista

table = table.split("\n")

# Remove caracteres desnecessários da tabela

table = [s.strip() for s in table if not s.isspace() and s != ""]

# Transforma os elementos desestruturados em tuplas

table = zip(*[iter(table)]*8)

# Transforma as tuplas da tabela em objetos da classe Disciplina

disciplinas = [Disciplina(*t) for t in table]

for disc in disciplinas:
	print(disc)

