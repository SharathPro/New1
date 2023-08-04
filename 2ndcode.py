import requests
from bs4 import BeautifulSoup
import json
def scrape_stockbroker_recommendations():
    url = "https://in.investing.com/equities/apple-computer-inc-opinion"
    # Set appropriate headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        recommendations = []
        # Find the table containing the stockbroker recommendations
        table = soup.find("table")
        # Extract rows from the table
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 5:  # Ensure we have the correct columns
                stock_symbol = cols[0].text.strip()
                broker_name = cols[1].text.strip()
                rating = cols[2].text.strip()
                target_price = cols[3].text.strip()
                date = cols[4].text.strip()
                recommendation = {
                    "stock_symbol": stock_symbol,
                    "broker_name": broker_name,
                    "rating": rating,
                    "target_price": target_price,
                    "date": date,
                }
                recommendations.append(recommendation)
        return recommendations
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []
if __name__ == "__main__":
    recommendations = scrape_stockbroker_recommendations()
    for rec in recommendations:
        print(rec)

abc=json.dumps(rec)