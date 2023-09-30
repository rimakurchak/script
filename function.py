import requests
from bs4 import BeautifulSoup

# Function to fetch and display top news headlines
def get_top_news():
    # URL of the news website to scrape
    news_url = "https://example-news-website.com"

    # Send an HTTP GET request to the website
    response = requests.get(news_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find and display the top news headlines
        headlines = soup.find_all("h2", class_="headline")
        print("Top News Headlines:")
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline.text}")
    else:
        print("Failed to fetch news headlines.")

# Main function
def main():
    print("Fetching top news headlines...\n")
    get_top_news()

if __name__ == "__main__":
    main()
