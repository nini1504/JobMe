import pandas as pd
from Database.db import get_connection

conn = get_connection()
cur = conn.cursor()

df = pd.read_excel("Pandas/salario.xlsx")
cargos = df["Cargo"].dropna().unique()

for cargo in cargos:
    cur.execute(
        "INSERT INTO cargos (nome) VALUES (%s);",
        (cargo,)
    )

conn.commit()
cur.close()
conn.close()

print("Cargos inseridos com sucesso!")