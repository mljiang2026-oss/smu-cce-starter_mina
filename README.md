# Cloud Computing for Economics: Starter Repo

This project contains course lessons, exploratory notebooks, and a beginner-friendly Streamlit app for exploring market data.

## Run the app

From the project root, create and activate a virtual environment, install dependencies, and start Streamlit:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```

Enter a ticker such as `MU` or `GOOG`, choose an analysis, and select **Run**. The app retrieves data through yfinance, so an internet connection is required; availability depends on Yahoo Finance.

## Analyses

- **Filings** displays the latest income statement, balance sheet, and cash flow tables provided by Yahoo Finance. These are financial statements, not SEC filing documents.
- **News** displays up to five recent news items for the ticker.
- **Stock price ratings** displays the current price and up to ten recent analyst recommendation rows.

The reusable data functions are in `src/analysis.py`; `src/app.py` contains the Streamlit interface. The original exploratory notebooks remain in `notebooks/`, and the lesson material is in `lessons/`.