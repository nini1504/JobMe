import React from "react";
import { useParams } from "react-router-dom";
import SalarioGrafico from "../../components/Grafico/SalarioGrafico";
import "./Cargo.css";

const Cargo = () => {

  const { nome } = useParams();

  return (
    <div style={{padding:"60px", textAlign:"center"}}>

      <h1 className="cargo-titulo">Salários para {nome}</h1>

      <p className="cargo-descricao">Comparação salarial por nível</p>

      <div style={{width:"600px", margin:"0 auto"}}>
        <SalarioGrafico />
      </div>

    </div>
  );

};

export default Cargo;