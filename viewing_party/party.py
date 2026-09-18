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

    # Go over the user's watchlist and check if the title of the movie the user has watched is there
    # If so, remove that movie from the watchlist, add it to watched, and break out of the loop
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            add_to_watched(user_data, movie)
            break

    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):

#   Calculate the average rating of all movies in the watched list
    avg_rating = 0.0
    total_watched_movies = len(user_data["watched"])
    rating_sum = 0

    if not len(user_data["watched"]) == 0:
        for movie in user_data["watched"]:
            rating_sum += movie["rating"]    # Add all the ratings
        avg_rating = rating_sum / total_watched_movies    # Calculate Average

    return avg_rating

def get_most_watched_genre(user_data):

# Determine which genre is most frequently occurring in the watched list
    genre_counts = {}    # Dictionary to keep track of how many times each genre appears
    most_watched_genre = None
    most_watched_genre_count = 0

    for movie in user_data["watched"]:
        # Get the genre of the current movie
        genre = movie["genre"]
        # Check if the genre is already in the dictionary
        if genre in genre_counts:    # Update the count of each genre in the dictionary
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1
            
    # Compare count of each genre
    for genre in genre_counts:
        if genre_counts[genre] > most_watched_genre_count:
            most_watched_genre_count = genre_counts[genre]
            most_watched_genre = genre

    return most_watched_genre

# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):

    # Store the titles of the movies watched by the user's friends in a list
    friends_movie_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_titles.append(movie["title"])

    # Determine which movies the user has watched, 
    # but none of their friends have watched
    user_unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movie_titles:
            user_unique_movies.append(movie)

    return user_unique_movies

def get_friends_unique_watched(user_data):

    # Store the titles of the movies watched by the user in a list
    user_movie_titles = []
    for movie in user_data["watched"]:
        user_movie_titles.append(movie["title"])

    # Determine which movies at least one of the user's 
    # friends have watched, but the user has not watched
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_movie_titles and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)       

    return friends_unique_movies

# ------------- WAVE 4 --------------------

def get_available_recs(user_data):

    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    # Go over each movie in the friends_unique_movies list and check if the "host" 
    # of the movie is a service that is in the user's "subscriptions". 
    # If so, add it to the recommended_movies list
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)    # User's most frequently watched genre
    friends_watched = get_friends_unique_watched(user_data)    # User has not watched, at least one friend watched it
    recommended_movies = []

    for movie in friends_watched:
    # The "genre" of the movie is the same as the user's most frequent genre
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):

    user_watched = get_unique_watched(user_data)    # Get "Only User" watched movies
    recommended_movies = []

    for movie in user_data["favorites"]:    # The movie is in the user's "favorites"
        if movie in user_watched:    # None of the user's friends have watched it
            recommended_movies.append(movie)

    return recommended_movies
