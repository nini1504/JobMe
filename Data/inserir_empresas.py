import pandas as pd
from Database.db import get_connection

conn = get_connection()
cur = conn.cursor()

df = pd.read_excel("Data/empresas_linkedin.xlsx")

nomes = df["Nome da Empresa"].dropna().unique()
links = df["Link LinkedIn"].dropna().unique()

for _, row in df.iterrows():
    nome = row["Nome da Empresa"]
    link = row["Link LinkedIn"]

    cur.execute("""
        INSERT INTO empresas (nome, linkedin)
        VALUES (%s, %s);
    """, (nome, link))


conn.commit()
cur.close()
conn.close()

print("Empresas inseridas com sucesso!")