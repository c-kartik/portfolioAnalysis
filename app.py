# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scripts.portfolio_analysis import optimize_portfolio
from scripts.data_fetch import fetch_stock_data
import pandas as pd

app = FastAPI()

# Define request model
class OptimizeRequest(BaseModel):
    tickers: list[str]
    start_date: str
    end_date: str
    risk_free_rate: float

# Define the /optimize POST endpoint
@app.post("/optimize")
async def optimize_portfolio_endpoint(request: OptimizeRequest):
    try:
        # Fetch stock data
        print(f"Fetching data for {request.tickers} from {request.start_date} to {request.end_date}")
        prices, daily_returns = fetch_stock_data(request.tickers, request.start_date, request.end_date)

        if prices is None or daily_returns is None:
            raise HTTPException(status_code=400, detail="Stock data fetch failed.")

        # Compute mean returns and covariance matrix
        mean_returns = daily_returns.mean().values
        cov_matrix = daily_returns.cov().values

        # Print debug output
        print(f"Mean Returns: {mean_returns}")
        print(f"Covariance Matrix: {cov_matrix}")

        # Perform optimization
        optimization_results = optimize_portfolio(mean_returns, cov_matrix, request.risk_free_rate)

        # Print the results for debugging
        print(f"Optimization Results: {optimization_results}")

        # Return the results
        return {
            "optimized_weights": dict(zip(request.tickers, optimization_results['weights'])),
            "expected_return": optimization_results['expected_return'],
            "volatility": optimization_results['volatility'],
            "sharpe_ratio": optimization_results['sharpe_ratio']
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
