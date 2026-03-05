import pandas as pd
from Database.db import get_connection

conn = get_connection()
cur = conn.cursor()

df = pd.read_excel("Data/salario.xlsx")
ano = 2025

for _, row in df.iterrows():
    nome_cargo = row["Cargo"]
    junior = row["Júnior"]
    pleno = row["Pleno"]
    senior = row["Sênior"]
    media = row["Média"]

    # buscar id do cargo
    cur.execute(
        "SELECT id FROM cargos WHERE nome = %s;",
        (nome_cargo,)
    )

    resultado = cur.fetchone()

    if resultado:
        id_cargo = resultado[0]

        cur.execute("""
            INSERT INTO salarios 
            (id_cargo, ano, salario_junior, salario_pleno, salario_senior, media)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (id_cargo, ano, junior, pleno, senior, media))

    else:
        print(f"Cargo não encontrado: {nome_cargo}")

conn.commit()
cur.close()
conn.close()

print("Salários inseridos com sucesso!")