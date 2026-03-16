from flask import Flask, jsonify
from flask_cors import CORS
import pdfplumber
import pandas as pd
import re
import sys
import os

# Adiciona o diretório do projeto ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Database.db import get_connection

app = Flask(__name__)
CORS(app)

def converter_moeda(valor):
    return float(valor.replace('.', '').replace(',', '.'))

@app.route('/api/salarios', methods=['GET'])
def obter_salarios():
    arquivo = "tabela.pdf"
    dados = []
    # regra pra captura de dados 
    # (.+?) regra para capturar o nome do cargo (qualquer caractere, não guloso)
    # \s+ um ou mais espaços em branco
    # ([\d\.]+,\d{2}) regra para capturar o salário
    padrao = re.compile(r"(.+?)\s+([\d\.]+,\d{2})\s+([\d\.]+,\d{2})\s+([\d\.]+,\d{2})")

    # Extração dos dados dos cargos do PDF
    with pdfplumber.open(arquivo) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            for linha in text.split('\n'):
                match = padrao.search(linha)
                if match:
                    dados.append({
                        "Cargo": match.group(1).strip(),
                        "Junior": match.group(2), 
                        "Pleno": match.group(3),
                        "Senior": match.group(4)
                    })

    if not dados:
        return jsonify({"erro": "Nenhum dado extraído do PDF"}), 400

    # Tirando a media dos salários
    df = pd.DataFrame(dados)
    for col in ["Junior", "Pleno", "Senior"]:
        df[col] = df[col].apply(converter_moeda)
    
    df["Media"] = df[["Junior", "Pleno", "Senior"]].mean(axis=1).round(2)

    # Insere os cargos no banco de dados
    conn = get_connection()
    cur = conn.cursor()
    ano = 2025

    for _, row in df.iterrows():
        nome_cargo = row["Cargo"]
        junior = row["Junior"]
        pleno = row["Pleno"]
        senior = row["Senior"]
        media = row["Media"]

        # Busca o ID do cargo
        cur.execute("SELECT id FROM cargos WHERE nome = %s;", (nome_cargo,))
        resultado = cur.fetchone()

        # Verifica se achou, se não achou, cria um novo
        if resultado:
            id_cargo = resultado[0]
        else:
            cur.execute("INSERT INTO cargos (nome) VALUES (%s);", (nome_cargo,))
            cur.execute("SELECT id FROM cargos WHERE nome = %s;", (nome_cargo,))
            id_cargo = cur.fetchone()[0]

        # Insere na tabela de salários com o ID garantido
        cur.execute("""
            INSERT INTO salarios 
            (id_cargo, ano, salario_junior, salario_pleno, salario_senior, media)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (id_cargo, ano, junior, pleno, senior, media))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "mensagem": "Salários e cargos inseridos com sucesso no banco de dados!",
        "total_inseridos": len(df)
    })

@app.route('/api/listagem', methods=['GET'])
def listar_banco():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT c.nome, s.ano, s.salario_junior, s.salario_pleno, s.salario_senior, s.media 
                    FROM salarios s 
                    JOIN cargos c ON s.id_cargo = c.id;
                """)
                rows = cur.fetchall()
                
        return jsonify([{
            "cargo": r[0], 
            "ano": r[1], 
            "salario_junior": float(r[2]) if r[2] is not None else 0,
            "salario_pleno": float(r[3]) if r[3] is not None else 0,
            "salario_senior": float(r[4]) if r[4] is not None else 0,
            "media": float(r[5]) if r[5] is not None else 0
        } for r in rows])
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/api/empresas', methods=['GET'])
def listar_empresas():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, nome, linkedin, imagem 
                    FROM empresas;
                """)
                rows = cur.fetchall()
                
        # Monta a lista de dicionários lidando com possíveis valores nulos (None)
        empresas = [{
            "id": r[0],
            "nome": r[1],
            "linkedin": r[2] if r[2] else "",
            "imagem": r[3] if r[3] else ""
        } for r in rows]

        return jsonify(empresas)
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)