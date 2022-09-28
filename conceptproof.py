from imdb import Cinemagoer

# Function to get directors of a movie
def getDirector(movieTitle):
    im = Cinemagoer()
    directorList = []
    movie = im.search_movie(movieTitle)
    for director in im.get_movie(movie[0].movieID)['directors']:
        directorList.append(director['name'])
    return directorList

# Function to get a list of actors/actresses of similar name
def getPeopleList(person):
    im = Cinemagoer()
    people = im.search_person(person)
    for person in people:
        print(person['name'])

# Get top 10 movies
def getTopNMovies(n):
    im = Cinemagoer()
    top = im.get_top250_movies()
    print('Top ' + str(n) + ' Movies on IMDb:')
    for i in range(n):
        print(str(i+1) + ':' + ' ' + str(top[i]))

# Get bottom 10 movies    
def getBottomNMovies(n):
    im = Cinemagoer()
    bottom = im.get_bottom100_movies()
    print('Bottom ' + str(n) + ' Movies on IMDb:')
    for i in range(n):
        print(str(i+1) + ':' + ' ' + str(bottom[i]))





