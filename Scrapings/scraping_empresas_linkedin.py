import requests
from bs4 import BeautifulSoup
import os
from Database.db import get_connection

url = 'https://www.linkedin.com/pulse/linkedin-top-companies-2025-10-melhores-empresas-de-u8rxc/'
pasta_imagens = "Imagens"

resposta = requests.get(url)
print(resposta)

if resposta.status_code == 200:

    soup = BeautifulSoup(resposta.content, 'html.parser')

    lista_h2 = soup.find_all('h2')
    empresas = []
    links = []

    iniciar_captura = False

    for h2 in lista_h2:

        if 'Mercado Livre' in h2.text.strip():
            iniciar_captura = True

        if iniciar_captura:

            nome = h2.text.strip()
            empresas.append(nome)

            link_tag = h2.find_next('a')

            if link_tag and link_tag.has_attr('href'):
                links.append(link_tag['href'])

    empresas = empresas[:10]
    links = links[:10]

    # conexão com banco
    conn = get_connection()
    cur = conn.cursor()

    for empresa, link in zip(empresas, links):

        nome = empresa.strip()

        # procurar imagem correspondente
        imagem = None

        for arquivo in os.listdir(pasta_imagens):

            if nome.lower() in arquivo.lower():

                imagem = f"{pasta_imagens}/{arquivo}"
                break

        cur.execute("""
            INSERT INTO empresas (nome, linkedin, imagem)
            VALUES (%s, %s, %s);
        """, (nome, link, imagem))

    conn.commit()
    cur.close()
    conn.close()

    print("Empresas inseridas com sucesso!")