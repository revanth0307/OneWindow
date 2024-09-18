import React from 'react';
import './App.css';
import countryData from './component/data';
import CountryCard from './component/CountryCard';  

function App() {
  return (
    <div className="App">
      <h1>Country Cards</h1>
      <div className="card-list">
        {countryData.map((country, index) => (
          <CountryCard key={index} country={country} />
        ))}
      </div>
    </div>
  );
}

export default App;
