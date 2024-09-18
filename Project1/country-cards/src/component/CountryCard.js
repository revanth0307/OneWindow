import React from 'react';
import './CountryCard.css';

const CountryCard = ({ country }) => {
  return (
    <div className="card">
      {/* Add the university logo */}
      <div className="logo-container">
        <img src={country.university.logo} alt="University Logo" className="university-logo" />
      </div>

      <div className="card-header">
        <div className="card-header-left">
          <h2>{country.name}</h2>
          <p className="course-info">M.Sc. / Full-time / On Campus</p>
        </div>
        <div className="check-match">
          <span>Check match</span>
          <span className="heart-icon">❤</span>
        </div>
      </div>
      
      {/* Update the university details */}
      <div className="university-details">
        <strong>{country.university.name}</strong>
        <p>{country.university.location}</p>
        <span className="ranking">{country.university.ranking}</span>
      </div>

      <div className="cost-duration">
        <p><strong>Cost:</strong> {country.cost_of_education.tuition_fees}</p>
        <p><strong>Duration:</strong> 2 years</p>
      </div>

      <button className="program-button">View Programme Information</button>
    </div>
  );
};

export default CountryCard;
