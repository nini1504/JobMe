import React from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <h2>JOBME</h2>
      </div>
      
      
      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/empresas">Empresas</Link>
      </div>
    </nav>
  );
};

export default Navbar;