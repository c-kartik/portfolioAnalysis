import React, { useState } from 'react';
import axios from 'axios';

function PortfolioForm() {
  const [tickers, setTickers] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [riskFreeRate, setRiskFreeRate] = useState(0.03);
  const [results, setResults] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/optimize', {
        tickers: tickers.split(","),
        start_date: startDate,
        end_date: endDate,
        risk_free_rate: riskFreeRate
      });
      setResults(response.data);
    } catch (error) {
      console.error('Error fetching optimization results:', error);
    }
  };

  return (
    <div>
      <h1>Portfolio Optimization</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter tickers (comma separated)"
          value={tickers}
          onChange={(e) => setTickers(e.target.value)}
        />
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
        <input
          type="number"
          step="0.01"
          value={riskFreeRate}
          onChange={(e) => setRiskFreeRate(parseFloat(e.target.value))}
        />
        <button type="submit">Optimize Portfolio</button>
      </form>

      {results && (
        <div>
          <h2>Optimization Results</h2>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default PortfolioForm;
