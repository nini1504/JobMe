import requests
from bs4 import BeautifulSoup
from Database.db import get_connection

url = 'https://www.linkedin.com/pulse/linkedin-top-companies-2025-10-melhores-empresas-de-u8rxc/'

# É necessario simular navegador real pq porque o LinkedIn bloqueia acessos de scripts automatizados
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
resposta = requests.get(url, headers=headers)
print(resposta)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')
    
    lista_h2 = soup.find_all('h2')
    empresas = []
    links = []
    iniciar_captura = False

    if lista_h2:
        for h2 in lista_h2:
            if 'Mercado Livre' in h2.text.strip():
                iniciar_captura = True
            if iniciar_captura:
                empresas.append(h2.text.strip())
                link_tag = h2.find_next('a')
                if link_tag and link_tag.has_attr('href'):
                    links.append(link_tag['href'])
    else:
        print("não encontrei h2.")

    empresas = empresas[:10]
    links = links[:10]

    # conexão com banco
    conn = get_connection()
    cur = conn.cursor()

    for empresa, link in zip(empresas, links):

        nome = empresa.strip()

        cur.execute("""
            INSERT INTO empresas (nome, linkedin)
            VALUES (%s, %s);
        """, (nome, link))

    conn.commit()
    cur.close() 
    conn.close()

    print("Empresas inseridas com sucesso!")
