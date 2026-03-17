import React, { useEffect, useState } from 'react';
import './Empresas.css';

const Empresas = () => {

  const [empresas, setEmpresas] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:5000/api/empresas")
      .then(res => res.json())
      .then(data => setEmpresas(data))
      .catch(err => console.error("Erro ao buscar empresas:", err))

  }, []);

  return (
    <div className="empresas-container">

      <h1>Página de Empresas</h1>

      <div className="empresas-grid">

        {empresas.map((empresa) => (

          <div className="empresa-card" key={empresa.id}>

            <img
              src={`/${empresa.imagem}`}
              alt={empresa.nome}
              className="empresa-logo"
            />
            <h3>{empresa.nome}</h3>

            <a href={empresa.linkedin} target="_blank" rel="noopener noreferrer">
              Ver no Linkedin
            </a>

          </div>

        ))}

      </div>

    </div>
  );
};

export default Empresas;