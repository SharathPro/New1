import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
def scrape_analyst_recommendations(time_period):
    url = "https://www.investing.com/stock-screener/Service/SearchStocks"
    # Define the payload parameters for the POST request
    payload = {
        'country[]': '3',
        'exchange[]': '50',
        'sector': '0',
        'industry': '0',
        'pn': '1',
        'order[col]': 'name',
        'order[dir]': 'a'
    }
    # Send a POST request to retrieve the stock list
    response = requests.post(url, data=payload)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table that contains the stock list
    table = soup.find('table', {"id": "economicCalendarData"})
    if(table is not None):
        # Find all rows in the table (excluding the header row)
        rows = table.find_all('tr')[1:]
        recommendations = []
        # Iterate over each row to scrape analyst recommendations for each stock
        for row in rows:
            a = row.find('a')
            if(a is None):
                continue
            symbol = a['href'].split('/')[-1]
            stock_name = row.find('a').text.strip()
            # Create the URL for the analyst recommendations of the stock
            recommendations_url = "https://www.investing.com/equities/{symbol}-recommendations"
            # Send a GET request to the URL
            print(f"Getting recommendations for  {symbol} from URL {recommendations_url}")
            response = requests.get(recommendations_url)
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find the table that contains the analyst recommendations
            table = soup.find('table', {"class":"recommendationsByCompany"})
            if(table is None):
                print("not found for {symbol}")
                continue
            # Find all rows in the table (excluding the header row)
            rows = table.find_all('tr')[1:]
            # Iterate over each row and extract the relevant data for yesterday's recommendations
            for row in rows:
                columns = row.find_all('td')
                date = columns[0].text.strip()
                rating = columns[1].text.strip()
                analyst = columns[2].text.strip()
                # Check if the recommendation is from yesterday
                recommendation_date = datetime.strptime(date, '%b %d, %Y')
                yesterday = datetime.now() - timedelta(days=1)
                if recommendation_date.date() == yesterday.date():
                    # Store the recommendation data in a dictionary
                    recommendation = {
                        'Symbol': symbol,
                        'Stock Name': stock_name,
                        'Date': date,
                        'Rating': rating,
                        'Analyst': analyst
                    }
                    recommendations.append(recommendation)
        return recommendations
    return None
# Usage example: Scrape analyst recommendations for all stocks listed on NSE from yesterday
recommendations = scrape_analyst_recommendations('1day')
if(recommendations is not None):
    for recommendation in recommendations:
        print(recommendation)
print("No Recommendations found")