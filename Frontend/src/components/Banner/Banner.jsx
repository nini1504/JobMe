import React from 'react';
import './Banner.css';

const Banner = () => {
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
        <input type="text" placeholder="Buscar por cargos e salários" />
        <button className="search-button">Buscar</button>
      </div>
    </div>
  );
};

export default Banner;