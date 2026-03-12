import os
from Database.db import get_connection

pasta_imagens = "Imagens"

conn = get_connection()
cur = conn.cursor()

for arquivo in os.listdir(pasta_imagens):

    if arquivo.endswith(".jpeg"):

        caminho_imagem = f"{pasta_imagens}/{arquivo}"

        # transforma o nome do arquivo no nome da empresa
        nome_empresa = arquivo.replace(".jpeg", "").replace("_", " ")

        print(nome_empresa, caminho_imagem)

        cur.execute("""
            UPDATE empresas
            SET imagem = %s
            WHERE nome = %s
        """, (caminho_imagem, nome_empresa))

conn.commit()
cur.close()
conn.close()

print("Imagens inseridas com sucesso!")