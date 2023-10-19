from datetime import datetime
from dotenv import load_dotenv
from PIL import Image
import re
import requests
import sys
import tmdbsimple as tmdb
import os

load_dotenv()


def get_movie_poster(movie_name, year):
    try:
        if TMDB_API_KEY == None:
            tmdb.API_KEY = os.getenv("TMDB_API_KEY")
        else:
            tmdb.API_KEY = TMDB_API_KEY    
        search = tmdb.Search()
        search.movie(query=movie_name, year=year)
        if search.total_results <= 0:
            raise ValueError
        for movie in search.results:
            if (
                movie["title"].lower() == movie_name.lower()
                and re.search(str(year), movie["release_date"]) != None
            ):
                poster_url = f"https://image.tmdb.org/t/p/w342{movie['poster_path']}"
                original_poster = Image.open(requests.get(poster_url, stream=True).raw)
                original_poster.save("poster.jpg")
                print("Movie found. The poster has been downloaded as \"poster.jpg\"")
                return
        raise ValueError
    
    except ValueError:
        print("Movie not found")
            

def validate_name(name):
    return bool(name)

def validate_year(year):
    current_year = datetime.now().year
    return 1900 <= year <= current_year
    




def main():
    name = input("Insert the name of the movie: ")
    while not validate_name(name):
        name = input("Please, insert a valid movie title: ")
    while True:
        try:
            year = input("Insert the year of the movie: ")
            if validate_year(int(year)):
                break
            else:
                print(f"Not a valid year (1900 - {datetime.now().year})") 
        except ValueError:
            print("Invalid input, value is not a number")    
    get_movie_poster(name, year)


if __name__ == "__main__":
    main()
