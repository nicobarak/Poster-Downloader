# POSTER DONWLOADER

## Description:
How many time do you want to share you opinion of a movie in social media? (hopefully a lot)
Here is your solution!
Poster Downloader is a Python program that allows you to download the poster of any movie knowing the name and the year it was released. It takes that information as values and uses an online database to download the actual file.
The program uses the TMDB API, an online huge database from movies and TV Shows and also uses a wrapper to handle that API called "tmdbsimple".
To use this API, it needs an API key, that i've alreaady generated it for free in themoviedb.org. You can run it for free online, but generate your own one to use it for further use.
The use of the wrapper tmdbsimple is also a free open tool for everyone.

## Program consists of these functions:

### get_movie_poster(movie_name, year): 
This function searches for the movie using the given name and year. First, the access key to the TMDb API is configured. The search is then performed and iterated over the results to find an exact match between the movie name and the year of release. If a match is found, the movie poster is downloaded and saved to a file called "poster.jpg", while also displaying a message that the poster has been downloaded. If no match is found, a message is displayed stating that the movie was not found.

### validate_name(): 
This function validate the user's input to prevent an empty str. It checks that a valid name was supplied and returns False if the input was null.

### validate_year(): 
This function validate the user's already validated number. It checks that the number is a valid year (between 1900 and the current year) and it returns a boolean value depending on that validation.

### main(): 
This function is the entry point of the program. It prompts the user for the name of the movie and the year of release, and then uses the above functions to validate the inputs. Finally, it calls the get_movie_poster() function to find and download the corresponding poster, if found.

##

To use the actual program, run it from the command line. It will ask you to enter the name of the movie and the year of release. Once you provide the required data, the program will perform the search and download the poster if it finds a match. The poster will be saved in the file "poster.jpg" in the current directory.

Now that you know all this information, go watch a movie! And then, if you like it (or if you didn't) share its poster.

Thanks for reading!
