# Stock Portfolio Analysis Tool
•	Developed a stock portfolio optimization tool to analyze historical data, visualize risk-return trade-offs, and optimize portfolios by minimizing volatility or maximizing risk-adjusted returns. 
•	Built using React for frontend interface, Python for data analysis, and connected to a FastAPI backend via RESTful APIs. Used Postman to test and validate the REST API, with Uvicorn as an ASGI for local development server.
•	Utilized yfinance to fetch historical stock data, Pandas and NumPy for data manipulation, and SciPy for optimizing portfolio allocation which maximizes Sharpe ratio and minimize risk. Risk minimizing algorithms analyze the covariance matrix of asset returns and allocating weights to reduce overall portfolio volatility through diversification.
•	Employed Scikit-learn for data preprocessing and feature engineering. Used principal component analysis to reduce dimensionality, allowing the model to handle larger datasets/portfolios more efficiently. 
•	Currently using PyTorch to implement LSTM-based time-series forecasting, capturing complex dependencies in historical stock data – this would allow in-depth insight into performances of individual industries that affect the stock market as a whole.
•	Aim to experiment multiple models and evaluate their performances using Scikit-learn.
•	UI allows users to input ticker symbols, date ranges, and desired risk-free rate for optimized portfolio results.
