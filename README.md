# Welcome to the Random Boardgame Generator!
This project scrapes boardgame data from https://boardgamegeek.com/ and presents a random game from the top 100 boardgames.

## Data and purpose
This scraper uncovers the following data about each top 100 board game:
- Rank
- Name (+ description)
- Rating
- URL

The purpose of this scraper is to generate a random boardgame for people who are looking to try a new boardgame. Since this
only includes games from the top 100 rankings, it's a perfect way for people to try new and popular games.

## Website
The website used is https://boardgamegeek.com/. This website has a lot of information on a lot of different boardgames,
and while it does have APIs, they are hard to access and lack proper information + documentation. This makes the website an
ideal candidate for webscraping, as it allows users to scrape most of its general pages. 

## How to use
1. Git clone this repo onto the user's local device
2. Pip install -r requirements.txt
3. Run the main.py file - it will generate a random board game. You can run this as many times as you want; it will give you a different board game every time. 
