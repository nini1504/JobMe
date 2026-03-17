import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import SalarioGrafico from "../../components/Grafico/SalarioGrafico";
import "./Cargo.css";

const Cargo = () => {

  const { nome } = useParams();
  const [dados, setDados] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/listagem?cargo=${nome}`)
      .then(res => res.json())
      .then(data => {
        if (data.length > 0) {
          setDados(data[0]);
        }
      })
      .catch(err => console.error(err));
  }, [nome]);

return (
  <div className="cargo-container">

    <h1>Salários para {nome}</h1>

    {dados ? (
      <div className="cargo-content">

        <p style={{ fontSize: "20px", color: "#747171" }}>
          Média: <strong>R$ {dados.media}</strong>
        </p>

        <div className="grafico-container">
          <SalarioGrafico dados={dados} />
        </div>

      </div>
    ) : (
      <p style={{ fontSize: "20px", color: "#747171" }}>
        Carregando...
      </p>
    )}

  </div>
);
};

export default Cargo;