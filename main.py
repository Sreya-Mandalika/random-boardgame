import requests
from bs4 import BeautifulSoup
import random

#fetching web content and extracting table with the top 100 games
def scrape_board_games(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve webpage.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    games_table = soup.find('table', {'class': 'collection_table'})
    if not games_table:
        print("No table found on the page.")
        return []

    rows = games_table.find_all('tr', {'id': 'row_'}) #the rows have ids such as "row_x"
    games = []

    for row in rows:
        game_rank = row.find('td', {'class': 'collection_rank'}).text.strip()
        game_name = row.find('td', {'class': 'collection_objectname'}).text.strip()
        game_rating = row.find('td', {'class': 'collection_bggrating'}).text.strip()
        game_url = 'https://boardgamegeek.com' + row.find('td', {'class': 'collection_objectname'}).find('a')['href']

        games.append({
            'rank': game_rank,
            'name': game_name,
            'rating': game_rating,
            'url': game_url
        })

    return games

#selects + displays random game from the list
def display_random_game(games):
    if not games:
        print("No games available to display.")
        return

    random_game = random.choice(games)

    game_rank = random_game['rank']
    game_name = " ".join(random_game['name'].split())
    game_rating = random_game['rating'].strip()
    game_url = random_game['url']

    print("Board Game Recommendation:")
    print(f"Rank: {game_rank}")
    print(f"Name: {game_name}")
    print(f"Rating: {game_rating}")
    print(f"More Info: {game_url}\n")


def main():
    url = "https://boardgamegeek.com/browse/boardgame"
    games = scrape_board_games(url)
    display_random_game(games)


if __name__ == "__main__":
    main()
