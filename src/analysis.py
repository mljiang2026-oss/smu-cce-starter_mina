"""Data-fetching functions based on the project's exploratory notebooks."""

import pandas as pd
import yfinance as yf


def _get_stock(ticker: str) -> yf.Ticker:
    """Return a Yahoo Finance ticker after checking the user input."""
    if not ticker or not ticker.strip():
        raise ValueError("Enter a ticker symbol, such as MU or GOOG.")
    return yf.Ticker(ticker.strip().upper())


def get_filings(ticker: str) -> dict[str, pd.DataFrame]:
    """Return the statement tables shown in the filings notebook."""
    stock = _get_stock(ticker)
    return {
        "Income Statement": stock.financials.head(),
        "Balance Sheet": stock.balance_sheet.head(),
        "Cash Flow": stock.cashflow.head(),
    }


def get_news(ticker: str) -> pd.DataFrame:
    """Return up to five recent news items in a display-ready table."""
    stock = _get_stock(ticker)
    articles = stock.news or []
    rows = []

    for article in articles[:5]:
        content = article.get("content", article)
        provider = content.get("provider", {})
        url = content.get("canonicalUrl", {})
        rows.append(
            {
                "Title": content.get("title", "No title"),
                "Description": content.get("description", "No description"),
                "Publisher": provider.get("displayName", ""),
                "Published": content.get("pubDate", ""),
                "URL": url.get("url", ""),
            }
        )

    return pd.DataFrame(rows)


def get_stock_price_and_ratings(ticker: str) -> dict[str, object]:
    """Return the current price and recent analyst recommendations."""
    stock = _get_stock(ticker)
    info = stock.info
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    recommendations = stock.recommendations

    if recommendations is None:
        recommendations = pd.DataFrame()

    return {
        "price": price,
        "currency": info.get("currency", ""),
        "recommendations": recommendations.tail(10),
    }