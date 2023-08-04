import requests
from bs4 import BeautifulSoup
def scrape_analyst_recommendations(stock_symbol):
    url = "https://www.investing.com/equities/{stock_symbol}-recommendations"
    # Send a GET request to the URL
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table that contains the analyst recommendations
    table = soup.find('table', class_='genTbl')
    # Find all rows in the table (excluding the header row)
    rows = table.find_all('tr')[0:]
    recommendations = []
    # Iterate over each row and extract the relevant data
    for row in rows:
        columns = row.find_all('td')
        date = columns[0].text.strip()
        rating = columns[1].text.strip()
        analyst = columns[2].text.strip()
        # Store the recommendation data in a dictionary
        recommendation = {
            'Date': date,
            'Rating': rating,
            'Analyst': analyst
        }
        recommendations.append(recommendation)
    return recommendations
# Usage example: Scrape analyst recommendations for Reliance Industries (RELIANCE.NS)
recommendations = scrape_analyst_recommendations('Reliance Industries')
for recommendation in recommendations:
    print(recommendation)