import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Banner from './components/Banner/Banner';
import Empresas from './pages/Empresas/Empresas';

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
        </Routes>
      </div>
    </Router>
  );
}

export default App;