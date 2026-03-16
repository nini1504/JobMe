import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Banner from './components/Banner/Banner';
import Empresas from './pages/Empresas/Empresas';
import Cargo from './pages/Cargo/Cargo';


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        
        <Routes>
          <Route path="/" element={
            <div className="top-section">
              <Banner />
            </div>
          } />

          <Route path="/empresas" element={<Empresas />} />

          <Route path="/cargo/:nome" element={<Cargo />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;