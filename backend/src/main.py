from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def example():
    return {"message": "Hello from fastapi backend"}


# def main():
#     print("Hello from backend!")


# if __name__ == "__main__":
#     main()

"""
 2. Auto Price Tracker & Deal Notifier
“Track product prices across sites, get notified when they drop.”

💡 What It Does
User enters a product URL (Amazon, Best Buy, etc.). App scrapes price data daily and alerts when it drops below a threshold. Historical chart included.

🧰 Tech Stack
FastAPI: backend scheduler + scraper

Playwright/BeautifulSoup: extract prices

React: dashboard of tracked products

PostgreSQL: user products, price history

Docker: cron-based scraping in containers

🚀 Stretch Goals
Add email notifications

Add price history graphs (Chart.js or d3)

Use AI to summarize product reviews

💼 Why It’s Impressive
Highly relatable

Shows automation + scraping + user value

Can be expanded to airlines, hotels, or even crypto later

"""
