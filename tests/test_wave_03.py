import pytest
from viewing_party.party import *
from tests.test_constants import *

### Helper function to calculate count
def count_value(my_collection, value):
    '''
    This helper function was created to calculate the count
    in test_friends_unique_movies_not_duplicated() test function

    It counts how many times a value appears in a collection

    Input:
        my_collection: a collection of values to search, like a list
        value: the value to count

    Output:
        An integer representing the number of times the value appears
        in the collection
    '''

    count = 0
    for item in my_collection:
        if item == value:
            count += 1

    return count

# @pytest.mark.skip()
def test_my_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Assert
    assert len(amandas_unique_movies) == 2
    assert FANTASY_2 in amandas_unique_movies
    assert INTRIGUE_2 in amandas_unique_movies
    assert amandas_data == clean_wave_3_data()

# @pytest.mark.skip()
def test_my_not_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()
    amandas_data["watched"] = []

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Assert
    assert len(amandas_unique_movies) == 0

# @pytest.mark.skip()
def test_friends_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Assert
    assert len(friends_unique_movies) == 3
    assert INTRIGUE_3 in friends_unique_movies
    assert HORROR_1 in friends_unique_movies
    assert FANTASY_4 in friends_unique_movies
    assert amandas_data == clean_wave_3_data()

# @pytest.mark.skip()
def test_friends_unique_movies_not_duplicated():
    # Arrange
    amandas_data = clean_wave_3_data()
    amandas_data["friends"][0]["watched"].append(INTRIGUE_3)

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Assert
    assert len(friends_unique_movies) == 3
    assert count_value(friends_unique_movies, INTRIGUE_3) == 1

# @pytest.mark.skip()
def test_friends_not_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [
            HORROR_1,
            FANTASY_1,
            INTRIGUE_1
        ],
        "friends": [
            {
                "watched": [
                    HORROR_1,
                    FANTASY_1,
                ]
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Assert
    assert len(friends_unique_movies) == 0
