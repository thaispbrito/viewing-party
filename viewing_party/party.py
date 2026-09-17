# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not title or not genre or not rating:
        return None

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    return new_movie

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            add_to_watched(user_data,movie)
            break

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

#   Calculate the average rating of all movies in the watched list
    avg_rating = 0.0
    total_watched_movies = len(user_data["watched"])
    rating_sum = 0

    if not len(user_data["watched"]) == 0:
        for movie in user_data["watched"]:
            rating_sum+=movie["rating"]         #Add all the ratings
        avg_rating = rating_sum / total_watched_movies  #Calculate Average
    return avg_rating

def get_most_watched_genre(user_data):

# Determine which genre is most frequently occurring in the watched list
    genre_counts = {}   #Dictionary keep track of how many times each genre appears
    most_watched_genre = None
    most_watched_genre_count = 0

    for movie in user_data["watched"]:
        # Get the genre of the current movie
        genre = movie["genre"]
        # Check if the genre is already in the dictionary
        if genre in genre_counts:   #Update the count of each genre in the dictionary
            genre_counts[genre]+= 1
        else:
            genre_counts[genre] = 1
            
    # Compare count of each genre
    for genre in genre_counts:
        if genre_counts[genre] > most_watched_genre_count:
            most_watched_genre_count = genre_counts[genre]
            most_watched_genre = genre
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie["title"])

    # which movies user has watched but none of friends have watched
    result = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            result.append(movie)

    # return list of dicts that represents a list of movies
    return result

def get_friends_unique_watched(user_data):

    user_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie["title"])

    # which movies at least one of the user's friends have watched, but the user has not watched
    result = []
    result_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_movies and movie["title"] not in result_titles:
                result.append(movie)
                result_titles.append(movie["title"])        

    return result

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"
# Return the list of recommended movies

    result = []
    movie_list = get_friends_unique_watched(user_data)

    for movie in movie_list:
        if movie["host"] in user_data["subscriptions"]:
            result.append(movie)

    return result

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)  #User's most frequently watched genre
    friends_watched = get_friends_unique_watched(user_data) #User has not watched, at least one friend watchec it
    recommended_movies = []

    for movie in friends_watched:
    # The "genre" of the movie is the same as the user's most frequent genre
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):

    user_watched = get_unique_watched(user_data) #Get "Only User" watched movies
    recommended_movies = []

    for movie in user_data["favorites"]:    #The movie is in the user's "favorites"
        if movie in user_watched:           #None of the user's friends have watched it
            recommended_movies.append(movie)

    return recommended_movies
