# 1 - Preparação dos Dados (★)
#
# Crie uma função chamada carregar_dados que não recebe parâmetros e retorna um DataFrame do Pandas contendo os dados do arquivo "INFwebNet_Data.json" (criado no TP2). A função deve:
#
# Verificar se todas as colunas estão presentes e se os dados foram carregados corretamente.
# Preencher os campos vazios com o valor "Não Informado" onde houver dados faltantes.
# import pandas as pd
"""Carrega os dados do arquivo JSON e retorna um DataFrame com os valores preenchidos como 'Não Informado' em caso de dados faltantes."""
# def carregar_dados():
#     try:
#         df = pd.read_json("INFwebNet_Data.json")
#         colunas = ["nome", "idade", "cidade", "estado"]
#         for coluna in colunas:
#             if coluna not in df.columns:
#                 raise ValueError(f"Coluna ausente: {coluna}")
#         df.fillna("Não Informado", inplace=True)
#         return df
#     except FileNotFoundError:
#         print("Erro: Arquivo 'INFwebNet_Data.json' não encontrado.")
#     except ValueError as a:
#         print(f"Erro nos dados: {a}")
#     except Exception as e:
#         print(f"Erro inesperado: {e}")
#
# if __name__ == "__main__":
#     dados = carregar_dados()
#     if dados is not None:
#         print(dados.head())
# import pandas as pd


# 2 - Extração de Plataformas (★)
#
# Crie uma função chamada extrair_plataformas que recebe como parâmetro o DataFrame retornado pela função carregar_dados e retorna um set contendo os nomes únicos das plataformas de jogos mencionadas pelos usuários na coluna "plataforma" associada aos jogos que eles jogam. Salve este set em um arquivo chamado "plataformas.txt", com um nome de plataforma por linha.
#
# Observação: Certifique-se de utilizar um set para garantir a unicidade dos nomes das plataformas.

"""Extrai e retorna um conjunto único de plataformas mencionadas na coluna 'plataforma' do DataFrame."""

# import pandas as pd
# def carregar_dados():
#     try:
#         df = pd.read_csv("dados_usuarios.csv", sep=";")
#         for col in df.columns:
#             df[col].fillna("Não Informado" if df[col].dtype == "object" else -1, inplace=True)
#         return df
#     except Exception as e:
#         print(f"Erro: {e}")
#         return None
#
#
# def extrair_jogos_e_plataformas(df):
#     jogos = set()
#     plataformas = set()
#     for jogos_info in df.get("jogos", []):
#         if isinstance(jogos_info, str):
#             try:
#                 jogos_lista = ast.literal_eval(jogos_info)
#
#                 for jogo, plataforma in jogos_lista:
#                     jogos.add(jogo)
#                     plataformas.add(plataforma)
#             except:
#                 pass
#     with open("plataformas.txt", "w") as file:
#         file.write("Jogos:\n")
#         file.writelines(f"{jogo}\n" for jogo in sorted(jogos))
#         file.write("\nPlataformas:\n")
#         file.writelines(f"{plataforma}\n" for plataforma in sorted(plataformas))
#
#     return jogos, plataformas
# def main():
#     df = carregar_dados()
#     if df is not None:
#         jogos, plataformas = extrair_jogos_e_plataformas(df)
#         print("Jogos extraídos:", jogos)
#         print("Plataformas extraídas:", plataformas)
#         print(f"Total de jogos únicos: {len(jogos)}")
#         print(f"Total de plataformas únicas: {len(plataformas)}")
#
#
# if __name__ == "__main__":
#     main()

# 3 - Tratamento de Exceções ao Carregar Plataformas (★)
#
# Implemente uma função chamada carregar_plataformas que tenta carregar o arquivo "plataformas.txt" e retorna uma lista com os nomes das plataformas. Se o arquivo não for encontrado, a função deve:
#
# Exibir uma mensagem de erro informando que o arquivo está em falta.
# Solicitar ao usuário que insira o caminho correto do arquivo ou digite 'sair' para encerrar o programa.
# Se o usuário fornecer um novo caminho, tentar carregar o arquivo novamente.
# Se o usuário digitar 'sair', encerrar o programa.
"""Tenta carregar o arquivo de plataformas e retorna uma lista de nomes, solicitando o caminho ao usuário caso o arquivo esteja ausente."""
pass

# import os
# def carregar_plataformas():
#     while True:
#         try:
#             caminho_arquivo = input("Digite o caminho do arquivo plataformas.txt ou 'sair' para encerrar: ").strip()
#
#             if caminho_arquivo.lower() == 'sair':
#                 print("Encerrando o programa.")
#                 exit()
#
#             # Verifica se o arquivo existe
#             if not os.path.exists(caminho_arquivo):
#                 print(f"O arquivo '{caminho_arquivo}' não foi encontrado. Tente novamente.")
#                 continue
#
#             with open(caminho_arquivo, mode="r") as file:
#                 linhas = file.readlines()
#
#             plataformas = []
#             in_plataformas = False
#             for linha in linhas:
#                 if "Plataformas" in linha:
#                     in_plataformas = True
#                 elif in_plataformas:
#                     if linha.strip():
#                         plataformas.append(linha.strip())
#                     else:
#                         break
#
#             if plataformas:
#                 print("Plataformas carregadas com sucesso:")
#                 for plataforma in plataformas:
#                     print(plataforma)
#             else:
#                 print("Não foi possível encontrar plataformas no arquivo.")
#
#             return plataformas
#
#         except FileNotFoundError:
#             print("Erro: O arquivo 'plataformas.txt' não foi encontrado.")
#             caminho_novo = input("Digite o caminho correto do arquivo ou 'sair' para encerrar: ").strip()
#
#             if caminho_novo.lower() == 'sair':
#                 print("Encerrando o programa.")
#                 exit()
#             continue
#
#         except Exception as e:
#             print(f"Erro ao tentar carregar o arquivo: {e}")
#             caminho_novo = input("Digite o caminho correto do arquivo ou 'sair' para encerrar: ").strip()
#
#             if caminho_novo.lower() == 'sair':
#                 print("Encerrando o programa.")
#                 exit()
#             continue
# carregar_plataformas()

# 4 - Download de Páginas da Wikipédia (★★)
# Crie uma função chamada baixar_paginas_wikipedia que recebe como parâmetro a lista de plataformas retornada pela função carregar_plataformas e retorna uma lista com os caminhos para os arquivos gerados. Para cada plataforma, a função deve:
# Formar a URL correspondente na Wikipédia em português no formato https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{Nome_da_Plataforma}, substituindo {Nome_da_Plataforma} pelo nome da plataforma, utilizando underscores (_) no lugar de espaços.
# Utilizar a biblioteca urllib para fazer o download da página HTML.
# Salvar o conteúdo HTML em arquivos individuais chamados "plataforma_Nome.html", onde Nome é o nome da plataforma, substituindo espaços por underscores.
# Exemplo:
# Para a plataforma "PlayStation 4", a URL seria https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_4 e o arquivo salvo seria "plataforma_PlayStation_4.html".

"""Tenta carregar o arquivo de plataformas e retorna uma lista de nomes, solicitando o caminho ao usuário caso o arquivo esteja ausente."""

# import urllib.request
# import os
#
# def baixar_paginas_wikipedia(plataformas):
#     caminhos_arquivos = []
#
#     for plataforma in plataformas:
#         plataforma_url = plataforma.replace(" ", "_")
#
#
#         url = f"https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{plataforma_url}"
#         nome_arquivo = f"plataforma_{plataforma_url}.html"
#
#         try:
#             print(f"Baixando a página para {plataforma}...")
#             urllib.request.urlretrieve(url, nome_arquivo)
#
#             caminhos_arquivos.append(os.path.abspath(nome_arquivo))
#             print(f"Arquivo salvo como {nome_arquivo}")
#
#         except Exception as e:
#             print(f"Erro ao baixar a página para {plataforma}: {e}")
#
#     return caminhos_arquivos
#
# plataformas = ["Mobile", "PC", "PlayStation 4", "Xbox One"]
# caminhos = baixar_paginas_wikipedia(plataformas)
# print("Arquivos gerados:", caminhos)

# 5 - Tratamento de Exceções no Download (★★)
#
# Modifique a função baixar_paginas_wikipedia para incluir tratamento de exceções durante o download. Se ocorrer um erro (como HTTPError ou URLError):
#
# Registrar o nome da plataforma e o erro em um arquivo de log chamado "erros_download.txt".
# Continuar o processo de download para as próximas plataformas.
# Desafio recurso extra (implementação opcional):
# Caso a página retorne erro 404, parsear a estrutura similar à:
#
# <p> <b>A Wikipédia não possui um artigo com este nome exato.</b> Por favor, <a href="/wiki/Especial:Pesquisar/Lista_de_jogos_para_Nintendo_switch" title="Especial:Pesquisar/Lista de jogos para Nintendo switch">procure por <i>Lista de jogos para Nintendo switch</i> na Wikipédia</a> para buscar por títulos alternativos. </p>

"""Faz o download das páginas da Wikipédia para cada plataforma e salva em arquivos HTML individuais."""
pass


# Utilizar o valor de href para baixar a página correta.
#
# import urllib.request
# import os
# import urllib.error
# from bs4 import BeautifulSoup
#
#
# def baixar_paginas_wikipedia(plataformas):
#     caminhos_arquivos = []
#     def registrar_erro(plataforma, erro):
#         with open("erros_download.txt", "a", encoding="utf-8") as log:
#             log.write(f"Erro ao baixar a página para {plataforma}: {erro}\n")
#
#     for plataforma in plataformas:
#         plataforma_url = plataforma.replace(" ", "_")
#         url = f"https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{plataforma_url}"
#         nome_arquivo = f"plataforma_{plataforma_url}.html"
#
#         try:
#             print(f"Baixando a página para {plataforma}...")
#             urllib.request.urlretrieve(url, nome_arquivo)
#             caminhos_arquivos.append(os.path.abspath(nome_arquivo))
#             print(f"Arquivo salvo como {nome_arquivo}")
#
#         except urllib.error.HTTPError as e:
#             if e.code == 404:
#                 print(f"Erro 404 para {plataforma}. Tentando buscar a página alternativa...")
#                 try:
#                     response = urllib.request.urlopen(url)
#                     html = response.read()
#                     soup = BeautifulSoup(html, 'html.parser')
#                     link_alternativo = soup.find('a', href=True, text='procure por')
#                     if link_alternativo:
#                         novo_url = "https://pt.wikipedia.org" + link_alternativo['href']
#                         print(f"Redirecionando para {novo_url}...")
#                         urllib.request.urlretrieve(novo_url, nome_arquivo)
#                         caminhos_arquivos.append(os.path.abspath(nome_arquivo))
#                         print(f"Arquivo salvo como {nome_arquivo}")
#                     else:
#                         print(f"Nenhum link alternativo encontrado para {plataforma}")
#                 except Exception as e:
#                     registrar_erro(plataforma, str(e))
#             else:
#                 registrar_erro(plataforma, str(e))
#
#         except urllib.error.URLError as e:
#             registrar_erro(plataforma, str(e))
#
#         except Exception as e:
#             registrar_erro(plataforma, str(e))
#
#     return caminhos_arquivos
#
# plataformas = ["Mobile", "PC", "PlayStation 4", "Xbox One"]
# caminhos = baixar_paginas_wikipedia(plataformas)
# print("Arquivos gerados:", caminhos)


# 6 - Parsing das Páginas HTML (★★)
#
# Crie uma função chamada parsear_paginas que recebe o caminho do arquivo HTML criado como parâmetro. A função deve:
#
# Utilizar o BeautifulSoup para parsear o conteúdo HTML do arquivo.
# Extrair o título da página (tag <title>) e confirmar se ao menos parte do título extraído corresponde ao nome da plataforma. Ignore diferenças de maiúsculas/minúsculas e acentuação.
# Se o título não corresponder, levantar uma exceção personalizada e registrar o caso em um arquivo "erros_parse.txt".
"""Lê e valida o conteúdo de um arquivo HTML, extraindo informações sobre os jogos disponíveis para a plataforma."""
# import unicodedata
# from bs4 import BeautifulSoup
# def parsear_paginas(caminho_arquivo):
#     try:
#         with open(caminho_arquivo, 'r', encoding='utf-8') as file:
#             html_content = file.read()
#         soup = BeautifulSoup(html_content, 'html.parser')
#         titulo = soup.title.string if soup.title else ""
#         nome_plataforma = caminho_arquivo.split("plataforma_")[1].split(".html")[0].replace("_", " ")
#         titulo_normalizado = unicodedata.normalize('NFD', titulo.lower()).encode('ascii', 'ignore').decode('utf-8')
#         plataforma_normalizada = unicodedata.normalize('NFD', nome_plataforma.lower()).encode('ascii', 'ignore').decode(
#             'utf-8')
#
#         print(f"Título extraído: {titulo}")
#         print(f"Plataforma esperada: {nome_plataforma}")
#
#         if plataforma_normalizada not in titulo_normalizado:
#             raise ValueError(f"Título incorreto para {nome_plataforma}. Título extraído: '{titulo}'")
#
#         print(f"Título correto encontrado para {nome_plataforma}.")
#
#     except ValueError as e:
#         with open("erros_parse.txt", "a", encoding="utf-8") as log:
#             log.write(f"{e}\n")
#         print(f"Erro: {e}")
#
#     excepnt(f"Plataforma esperada: {nome_plataforma}")
#
#         if plataforma_normalizada not in titulo_normalizado:
#             raise ValueError(f"Título incorreto para {nome_plataforma}. Título extraído: '{titulo}'")
#
#         print(f"Título correto encontrado para {nome_plataforma}.")
#
#     except ValueError as e:
#         with open("erros_parse.txt", "a", encoding="utf-8") as log:
#             log.write(f"{e}\n")
#         print(f"Erro: {e}")
#nt(f"Plataforma esperada: {nome_plataforma}")
#
#         if plataforma_normalizada not in titulo_normalizado:
#             raise ValueError(f"Título incorreto para {nome_plataforma}. Título extraído: '{titulo}'")
#
#         print(f"Título correto encontrado para {nome_plataforma}.")
#
#     except ValueError as e:
#         with open("erros_parse.txt", "a", encoding="utf-8") as log:
#             log.write(f"{e}\n")
#         print(f"Erro: {e}")
#
#     except Exception as e:
#         print(f"Ocorreu um erro ao processar o arquivo {caminho_arquivo}: {e}")
#
#
# caminho_arquivo = "plataforma_PlayStation_4.html"
# parsear_paginas(caminho_arquivo)

# 7 - Extração de Tabelas de Jogos (★★)
#
# Dentro da função parsear_paginas, após a verificação do título, a função deve:
#
# Localizar a ou as tabelas que contêm a lista de jogos disponíveis para a plataforma. Essas tabelas geralmente estão identificadas pela classe "wikitable" ou possuem um cabeçalho específico.
# Extrair os dados dos jogos, incluindo as colunas disponíveis (por exemplo, "Título", "Desenvolvedor", "Data de lançamento", etc.).
# Armazenar os dados em uma estrutura de dados conforme o formato especificado no item 9.
# Observação: Certifique-se de capturar todas as tabelas relevantes que contêm listas de jogos.
#
# from bs4 import BeautifulSoup
# def parsear_paginas(caminho_arquivo):
#     try:
#         with open(caminho_arquivo, 'r', encoding='utf-8') as file:
#             html_content = file.read()
#         soup = BeautifulSoup(html_content, 'html.parser')
#
#         titulo = soup.title.string.strip() if soup.title else "Título não encontrado"
#         print(f"Título extraído: {titulo}")
#         nome_plataforma = caminho_arquivo.split("plataforma_")[1].split(".html")[0].replace("_", " ")
#         print(f"Plataforma esperada: {nome_plataforma}")
#
#         if nome_plataforma.lower() not in titulo.lower():
#             with open("erros_parse.txt", "a", encoding="utf-8") as log:
#                 log.write(f"Erro no título para {nome_plataforma}: '{titulo}'\n")
#             print(f"Erro: O título '{titulo}' não corresponde à plataforma '{nome_plataforma}'.")
#             return
#         tabelas = soup.find_all('table', class_='wikitable')
#         if not tabelas:
#             print(f"Nenhuma tabela de jogos encontrada para {nome_plataforma}.")
#             return
#         jogos = []
#         for tabela in tabelas:
#             linhas = tabela.find_all('tr')
#             cabecalhos = [th.text.strip() for th in linhas[0].find_all('th')] if linhas else []
#
#             for linha in linhas[1:]:
#                 colunas = [td.text.strip() for td in linha.find_all('td')]
#                 if len(colunas) >= len(cabecalhos):
#                     jogo = {cabecalhos[i]: colunas[i] for i in range(len(cabecalhos))}
#                     jogos.append(jogo)
#         if jogos:
#             print(f"Jogos extraídos para {nome_plataforma}:")
#             for jogo in jogos:
#                 print(jogo)
#         else:
#             print(f"Nenhum jogo extraído para {nome_plataforma}.")
#
#     except FileNotFoundError:
#         print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
#     except Exception as e:
#         print(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")
#
# caminho_arquivo = "plataforma_PlayStation_4.html"
# parsear_paginas(caminho_arquivo)


# 8 - Uso de Expressões Regulares (★★)
# Crie uma função chamada extrair_urls_emails que percorre todos os arquivos "plataforma_Nome.html" e, utilizando expressões regulares em conjunto com o BeautifulSoup, extrai todas as URLs e e-mails presentes nas páginas. Armazene esses dados em um dicionário com as chaves "urls" e "emails" e salve em um arquivo JSON chamado "conexoes_plataformas.json".
# regex e-mail: r"^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$"
# regex urls: r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)"

# import os
# import re
# import json
# from bs4 import BeautifulSoup
#
# def extrair_urls_emails(diretorio):
#     resultado = {"urls": set(), "emails": set()}
#     regex_email = r"([\w\.-]+@[\w\.-]+\.\w+)"
#     regex_url = r"((https?|ftp):\/\/[^\s/$.?#].[^\s]*)"
#
#     try:
#         arquivos_html = [arquivo for arquivo in os.listdir(diretorio) if
#                          arquivo.startswith("plataforma_") and arquivo.endswith(".html")]
#
#         if not arquivos_html:
#             print("Nenhum arquivo HTML encontrado.")
#             return
#
#         for arquivo in arquivos_html:
#             caminho_arquivo = os.path.join(diretorio, arquivo)
#             with open(caminho_arquivo, "r", encoding="utf-8") as file:
#                 conteudo = file.read()
#             soup = BeautifulSoup(conteudo, "html.parser")
#             urls = re.findall(regex_url, conteudo)
#             resultado["urls"].update(url[0] for url in urls)
#             emails = re.findall(regex_email, conteudo)
#             resultado["emails"].update(emails)
#         resultado["urls"] = list(resultado["urls"])
#         resultado["emails"] = list(resultado["emails"])
#
#         with open("conexoes_plataformas.json", "w", encoding="utf-8") as json_file:
#             json.dump(resultado, json_file, indent=4, ensure_ascii=False)
#
#         print("Dados extraídos e salvos em conexoes_plataformas.json.")
#     except Exception as e:
#         print(f"Erro ao processar os arquivos: {e}")
# diretorio_html = "./"
# extrair_urls_emails(diretorio_html)


#  9 - Exportação dos Dados (★★★)
#
# Crie uma função chamada exportar_dados_jogos que recebe a estrutura de dados com os jogos extraídos e salva em um arquivo JSON chamado "dados_jogos_plataformas.json" no seguinte formato:
# [
#   {
#     "plataforma": "Nome_da_Plataforma",
#     "jogos": [
#       {
#         "nome_jogo": "Nome_do_Jogo",
#         "dados_jogo": {
#           "campo_1": "valor_1",
#           "campo_2": "valor_2",
#           ...
#         }
#       },
#       ...
#     ]
#   },
#   ...
# ]
# Observações:
# Os "campos" em "dados_jogo" devem ser os nomes das colunas da tabela extraída.
# Certifique-se de que todos os dados estão corretamente estruturados conforme o formato acima.
#
# import json
#
# def exportar_dados_jogos(dados_jogos):
#     try:
#         dados_exportacao = []
#
#         for plataforma, jogos in dados_jogos.items():
#             plataforma_dados = {
#                 "plataforma": plataforma,
#                 "jogos": []
#             }
#
#             for jogo, dados in jogos.items():
#                 jogo_dados = {
#                     "nome_jogo": jogo,
#                     "dados_jogo": dados
#                 }
#                 plataforma_dados["jogos"].append(jogo_dados)
#
#             dados_exportacao.append(plataforma_dados)
#
#         with open("dados_jogos_plataformas.json", "w", encoding="utf-8") as arquivo_json:
#             json.dump(dados_exportacao, arquivo_json, indent=4, ensure_ascii=False)
#         print("Dados exportados para 'dados_jogos_plataformas.json'.")
#
#     except Exception as e:
#         print(f"Erro ao exportar os dados: {e}")
#
# dados_jogos_exemplo = {
#     "PlayStation 4": {
#         "GTA V": {"Desenvolvedor": "Rockstar", "Data de Lançamento": "2013"},
#         "The Witcher 3": {"Desenvolvedor": "CD Projekt Red", "Data de Lançamento": "2015"}
#     },
#     "PC": {
#         "Valorant": {"Desenvolvedor": "Riot Games", "Data de Lançamento": "2020"},
#         "Minecraft": {"Desenvolvedor": "Mojang", "Data de Lançamento": "2011"}
#     }
# }
#
# exportar_dados_jogos(dados_jogos_exemplo)

# 10 - Associação de Jogos aos Usuários (★★)

# Crie uma função chamada associar_jogos_usuarios que recebe como parâmetros:
# O DataFrame dos usuários retornado por carregar_dados.
# A estrutura de dados com os jogos extraídos no formato especificado.
# A função deve:
# Para cada usuário, verificar quais jogos mencionados por ele estão presentes na lista de jogos extraídos das páginas das plataformas.
# Criar uma associação entre o usuário, o jogo e a plataforma correspondente.
# Atualizar o DataFrame dos usuários, adicionando uma coluna que contém uma lista de dicionários com os jogos e plataformas associados.
#
# import json
# import pandas as pd
#
# def associar_jogos_usuarios(df_usuarios, jogos_por_plataforma):
#     try:
#         def mapear_jogos(jogos_usuario):
#             associacoes = []
#             for plataforma, jogos in jogos_por_plataforma.items():
#                 for jogo in jogos_usuario:
#                     if jogo in jogos:
#                         associacoes.append({"jogo": jogo, "plataforma": plataforma})
#             return associacoes
#
#         df_usuarios["jogos_associados"] = df_usuarios["jogos"].apply(
#             lambda jogos: mapear_jogos(eval(jogos)) if jogos != "Não Informado" else []
#         )
#
#         print("Associações de jogos e plataformas concluídas.")
#         return df_usuarios
#
#     except Exception as e:
#         print(f"Erro ao associar jogos aos usuários: {e}")
#
# dados_usuarios = {
#     "id": ["a7d3a358", "e439f93f"],
#     "nome": ["Matheus", "Camila"],
#     "jogos": ["['Overwatch', 'Minecraft']", "['Apex Legends', 'Minecraft']"]
# }
#
# jogos_extraidos = {
#     "PC": {
#         "Overwatch": {"Desenvolvedor": "Blizzard", "Data de Lançamento": "2016"},
#         "Minecraft": {"Desenvolvedor": "Mojang", "Data de Lançamento": "2011"}
#     },
#     "PlayStation 4": {
#         "GTA V": {"Desenvolvedor": "Rockstar", "Data de Lançamento": "2013"}
#     }
# }
# df_usuarios = pd.DataFrame(dados_usuarios)
# resultado = associar_jogos_usuarios(df_usuarios, jogos_extraidos)
# print(resultado)
#
# 11 - Atualização do Banco de Dados (★★)
#
# Crie uma função chamada atualizar_banco_dados que atualiza o banco de dados SQLite "INFwebNET_DB.db", criado no TP3, adicionando uma nova tabela chamada "Jogos_Plataformas" que contém as informações dos jogos e plataformas extraídos. Use SQLAlchemy e Pandas para realizar esta operação.
#
# from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
# import pandas as pd
# def carregar_jogos_e_plataformas(txt_path="plataformas.txt"):
#     jogos = []
#     plataformas = []
#     try:
#         with open(txt_path, "r") as file:
#             lines = file.readlines()
#         jogos_index = lines.index("Jogos:\n") + 1
#         plataformas_index = lines.index("Plataformas:\n") + 1
#         jogos = [line.strip() for line in lines[jogos_index:plataformas_index - 1] if line.strip()]
#         plataformas = [line.strip() for line in lines[plataformas_index:] if line.strip()]
#     except Exception as e:
#         print(f"Erro ao carregar o arquivo {txt_path}: {e}")
#
#     return jogos, plataformas
# def atualizar_banco_dados(db_path="sqlite:///INFwebNET_DB.db", txt_path="plataformas.txt"):
#     jogos, plataformas = carregar_jogos_e_plataformas(txt_path)
#
#     if not jogos or not plataformas:
#         print("Jogos ou plataformas não encontrados no arquivo.")
#         return
#
#     engine = create_engine(db_path)
#     metadata = MetaData()
#
#     jogos_plataformas_table = Table(
#         "Jogos_Plataformas", metadata,
#         Column("id", Integer, primary_key=True, autoincrement=True),
#         Column("jogo", String, nullable=False),
#         Column("plataforma", String, nullable=False)
#     )
#
#     try:
#         metadata.create_all(engine)
#         print("Tabela Jogos_Plataformas criada com sucesso.")
#     except Exception as e:
#         print(f"Erro ao criar a tabela Jogos_Plataformas: {e}")
#
#     # Preparando os dados para inserir na nova tabela
#     data = [{"jogo": jogo, "plataforma": plataforma} for jogo in jogos for plataforma in plataformas]
#     df = pd.DataFrame(data)
#
#     try:
#         df.to_sql("Jogos_Plataformas", con=engine, if_exists="append", index=False)
#         print("Dados inseridos na tabela Jogos_Plataformas com sucesso.")
#     except Exception as e:
#         print(f"Erro ao inserir dados na tabela Jogos_Plataformas: {e}")
# if __name__ == "__main__":
#     atualizar_banco_dados()


# 12 Consulta aos Dados (★★)
# Crie uma função chamada consultar_usuarios_por_jogo que recebe como parâmetro o nome de um jogo e retorna uma lista de usuários que jogam esse jogo. A função deve:
# Permitir que o nome do jogo seja fornecido pelo usuário via input().
# Realizar a consulta no banco de dados atualizado.
# Exibir os nomes dos usuários encontrados.
#
# import sqlite3
# def consultar_usuarios_por_jogo():
#     conn = sqlite3.connect('INFwebNET_DB.db')
#     cursor = conn.cursor()
#     nome_jogo = input("Digite o nome do jogo: ")
#
#     query = """
#     SELECT id, jogo, plataforma
#     FROM Jogos_Plataformas
#     WHERE jogo = ?
#     """
#
#     cursor.execute(query, (nome_jogo,))
#     resultados = cursor.fetchall()
#
#     if resultados:
#         print(f"Usuários que jogam '{nome_jogo}':")
#         for resultado in resultados:
#             print(f"ID: {resultado[0]}, Plataforma: {resultado[2]}")
#     else:
#         print(f"Nenhum usuário encontrado jogando '{nome_jogo}'.")
#     conn.close()
# consultar_usuarios_por_jogo()
#

# 13 Análise Estatística (★★)

# Crie uma função chamada plataforma_mais_popular que utiliza o banco de dados para calcular qual é a plataforma mais popular entre os usuários da INFwebNET, com base nos jogos que eles jogam. A função deve:
# Contar o número de usuários que jogam jogos em cada plataforma.
# Exibir o nome da plataforma mais popular e o número de usuários.

# from sqlalchemy import create_engine
# import pandas as pd
# def plataforma_mais_popular(db_path="sqlite:///INFwebNET_DB.db"):
#     engine = create_engine(db_path)
#     query = """
#     SELECT p.plataforma, COUNT(DISTINCT u.nome || ' ' || u.sobrenome) as num_usuarios
#     FROM Jogos_Plataformas p
#     JOIN Usuarios_Historicos u ON u.jogos LIKE '%' || p.jogo || '%'
#     GROUP BY p.plataforma
#     ORDER BY num_usuarios DESC
#     LIMIT 1;
#     """
#
#     try:
#         df = pd.read_sql(query, engine)
#         if not df.empty:
#             plataforma = df.iloc[0]['plataforma']
#             num_usuarios = df.iloc[0]['num_usuarios']
#             print(f"A plataforma mais popular é {plataforma} com {num_usuarios} usuários.")
#         else:
#             print("Nenhum dado encontrado.")
#     except Exception as e:
#         print(f"Erro ao realizar a consulta: {e}")
#
# if __name__ == "__main__":
#     plataforma_mais_popular()
#
# 14 - Guardando as Informações (★)
#
# Crie uma função chamada salvar_dados_completos que não recebe parâmetros e salva todas as informações associadas (usuários, jogos, plataformas) em um arquivo JSON chamado "INFwebNET_Completo.json". O arquivo deve conter uma lista de usuários, onde cada usuário possui seus dados pessoais e uma lista de jogos que ele joga, com as respectivas plataformas.
# import json
# from sqlalchemy import create_engine
# import pandas as pd
#
#
# def salvar_dados_completos():
#     db_path = "sqlite:///INFwebNET_DB.db"
#     engine = create_engine(db_path)
#
#     query = """
#     SELECT u.id, u.nome, u.sobrenome, u.jogos, p.jogo, p.plataforma
#     FROM Usuarios_Historicos u
#     JOIN Jogos_Plataformas p ON u.jogos LIKE '%' || p.jogo || '%'
#     """
#
#     try:
#         df = pd.read_sql(query, engine)
#
#         usuarios = {}
#
#         for _, row in df.iterrows():
#             usuario_id = row['id']
#             nome_completo = f"{row['nome']} {row['sobrenome']}"
#             jogo = row['jogo']
#             plataforma = row['plataforma']
#
#             if usuario_id not in usuarios:
#                 usuarios[usuario_id] = {
#                     'nome': nome_completo,
#                     'jogos': []
#                 }
#             usuarios[usuario_id]['jogos'].append({'jogo': jogo, 'plataforma': plataforma})
#
#         usuarios_list = list(usuarios.values())
#
#         with open("INFwebNET_Completo.json", "w", encoding="utf-8") as json_file:
#             json.dump(usuarios_list, json_file, ensure_ascii=False, indent=4)
#
#         print("Dados salvos com sucesso no arquivo 'INFwebNET_Completo.json'.")
#
#     except Exception as e:
#         print(f"Erro ao salvar os dados: {e}")
#
# if __name__ == "__main__":
#     salvar_dados_completos()

# 15 Documentação do Código (★)

# Documente adequadamente ao menos as cinco funções que você considere mais importantes e complexas do seu código usando docstrings no formato PEP 257, explicando o propósito de cada função, os parâmetros esperados e os valores retornados.

# def salvar_dados_completos():
#     """
#     Salva informações de usuários, jogos e plataformas em um arquivo JSON chamado 'INFwebNET_Completo.json'.
#     A função consulta o banco de dados para obter informações sobre os usuários, os jogos que jogam e as plataformas associadas,
#     e então salva esses dados em um arquivo JSON estruturado. Não recebe parâmetros e não retorna valores. Exibe uma mensagem de erro
#     caso haja falha ao acessar o banco de dados ou salvar o arquivo JSON.
#     """
# def carregar_jogos_e_plataformas(txt_path="plataformas.txt"):
#     """
#     Carrega jogos e plataformas a partir de um arquivo de texto e retorna duas listas com essas informações.
#     A função lê o arquivo de texto indicado (por padrão, 'plataformas.txt'), que contém listas de jogos e plataformas,
#     e retorna duas listas: uma com os jogos e outra com as plataformas. O parâmetro 'txt_path' é opcional e tem o valor padrão 'plataformas.txt'.
#     Retorna uma tupla contendo duas listas, sendo a primeira com os jogos (strings) e a segunda com as plataformas (strings).
#     Exibe uma mensagem de erro caso haja falha ao ler o arquivo de texto.
#     """
# def consultar_usuarios_por_jogo():
#     """
#     Consulta e exibe os usuários que jogam um jogo específico, com base no nome fornecido.
#     A função solicita ao usuário o nome de um jogo e consulta o banco de dados para encontrar todos os usuários que jogam esse jogo,
#     exibindo seus nomes. Não recebe parâmetros, e o nome do jogo é fornecido via input(). Não retorna valores, apenas exibe os nomes dos usuários.
#     Exibe uma mensagem de erro caso ocorra um problema durante a consulta ao banco de dados.
#     """
# def atualizar_banco_dados():
#     """
#     Atualiza o banco de dados SQLite, adicionando uma tabela de jogos e plataformas a partir de um arquivo de texto.
#     A função lê informações do arquivo de texto 'plataformas.txt' e cria uma nova tabela chamada 'Jogos_Plataformas' no banco de dados,
#     sem remover dados existentes. Não recebe parâmetros e não retorna valores, apenas atualiza o banco de dados. Exibe uma mensagem de erro
#     caso haja falha ao acessar o banco de dados ou ao processar o arquivo de texto.
#     """
# def plataforma_mais_popular():
#     """
#     Calcula e exibe a plataforma mais popular entre os usuários, com base nos jogos que eles jogam.
#     A função realiza uma consulta ao banco de dados para contar o número de usuários que jogam jogos em cada plataforma
#     e exibe a plataforma com mais usuários. Não recebe parâmetros e não retorna valores, apenas exibe a plataforma mais popular e o número de usuários.
#     Exibe uma mensagem de erro caso ocorra um problema durante a execução da consulta ao banco de dados.
#     """

# 16 - Relatório Final (★★)
#
# Elabore um breve relatório (máximo de duas páginas) descrevendo as etapas realizadas, as dificuldades encontradas e como as competências foram aplicadas na resolução do problema. E, opcionalmente, sua percepção e feedback sobre o curso.

# No projeto, desenvolvi um conjunto de funções para trabalhar com dados de usuários e jogos em plataformas de videogame. Comecei carregando os dados de um arquivo JSON e tratei casos de dados faltantes, preenchendo-os com "Não Informado". Depois, extraí as plataformas únicas dos jogos e salvei essas informações em um arquivo de texto.
# Houve também o desenvolvimento de funções para baixar páginas da Wikipédia relacionadas às plataformas, fazer parsing dos arquivos HTML e extrair informações dos jogos. Usei expressões regulares para capturar URLs e e-mails dessas páginas e salvei essas informações em um arquivo JSON.
# Para organizar os dados, associei os jogos aos usuários e atualizei um banco de dados SQLite com essas informações. Também criei funções para consultar quais usuários jogam determinados jogos e para identificar a plataforma mais popular entre os usuários.
# Durante o processo, enfrentei desafios como lidar com erros ao baixar as páginas, tratar exceções e garantir que os dados fossem salvos corretamente em formatos como JSON e banco de dados. Apesar das dificuldades, consegui aplicar várias técnicas de programação, como o uso de bibliotecas como Pandas, BeautifulSoup, SQLAlchemy e expressões regulares.
# Esse projeto me ajudou a melhorar minhas habilidades de programação e me deu uma boa experiência prática com manipulação de dados, web scraping e integração de sistemas. Acredito que o aprendizado foi muito útil, e estou mais preparado para resolver problemas complexos de programação agora.