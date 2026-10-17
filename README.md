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

## Save and view previous analyses

After an analysis is displayed, select **Save Analysis** to write it as a Markdown file. Each saved file includes its ticker, analysis type, selected parameters, creation date, and results. Saved analyses appear under **Previous Analyses**; select one and click **Show** to open its rendered Markdown in a dialog.

The app creates `analyses-data/` in the project root when needed and saves files there. The location is resolved from `src/analysis_storage.py`, not from the shell's current directory. The folder is ignored by Git and uses the instance's existing disk; no separate EBS volume, CloudFormation change, or environment-specific setup is required.

To verify the feature in GitHub Codespaces or on EC2:

1. Start the app using the command above, run an analysis, and select **Save Analysis**.
2. Confirm a `.md` file was created under `analyses-data/` and the app reports that it was saved.
3. Refresh or restart the app. Under **Previous Analyses**, choose the saved item and select **Show**. The analysis should open in a rendered dialog.
4. Run and save another analysis to confirm it is listed ahead of the older one. Both environments use the same project-relative directory and existing disk.
