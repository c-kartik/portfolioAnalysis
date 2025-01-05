from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PortfolioRequest(BaseModel):
    tickers: list[str]
    start_date: str
    end_date: str
    risk_free_rate: float

@app.post("/optimize")
def optimize_portfolio(request: PortfolioRequest):
    # Mock response for testing
    return {"message": "Optimization results will go here!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
