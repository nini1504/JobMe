import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Banner.css';

const Banner = () => {
  const [cargo, setCargo] = useState("");//guarda oq digita
  const navigate = useNavigate();//faz a navegação

  const buscar = () => {
    if (cargo.trim() !== "") {
      navigate(`/cargo/${cargo}`);
    }
  };

  return (
    <div className="banner-container">
      <h1 className="banner-title">
        Descubra o futuro da <br />
        <span className="text-highlight">sua carreira em TI</span>
      </h1>

      <p className="banner-subtitle">
        Salários e empresas de tecnologia. Tudo centralizado para <br />
        você tomar as melhores decisões profissionais.
      </p>

      <div className="banner-search-box">
        <input
          type="text"
          placeholder="Buscar por cargos e salários"
          value={cargo}
          onChange={(e) => setCargo(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") buscar();
          }}
        />
        <button className="search-button" onClick={buscar}>
          Buscar
        </button>
      </div>
    </div>
  );
};

export default Banner;