import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
import numpy as np
import jikanpy

# Loads model
model = models.load_model("model", compile = True)

# Stored in arrays so each word is mapped to a number (the index)
types = ["TV", "Movie", "OVA", "ONA", "Special", "Music", "Unknown"]
sources = ["4-koma manga", "Book", "Card game", "Digital manga", "Game", "Light novel", "Manga", "Music", "Novel", "Original", "Picture book", "Radio", "Visual novel", "Web manga", "Other", "Unknown"]
ratings = ["G - All Ages", "PG - Children", "PG-13 - Teens 13 or older", "R - 17+ (violence & profanity)", "R+ - Mild Nudity", "Rx - Hentai", "None"]
genres = ["Action", "Adventure", "Cars", "Comedy", "Dementia", "Demons", "Drama", "Ecchi", "Fantasy", "Game", "Harem", "Hentai", "Historical", "Horror", "Josei", "Kids", "Magic", "Martial Arts", "Mecha", "Military", "Music", "Mystery", "Parody", "Police", "Psychological", "Romance", "Samurai", "School", "Sci-Fi", "Seinen", "Shoujo", "Shoujo Ai", "Shounen", "Shounen Ai", "Slice of Life", "Space", "Sports", "Super Power", "Supernatural", "Thriller", "Vampire", "Yaoi", "Yuri"]

jikan = jikanpy.Jikan()

while True:
    # Gets user input
    request = int()
    while True:
        try:
            request = int(input("\nType the MyAnimeList ID of the anime: "))
            if (request > 0):
                break
            else:
                print("\nID must be a positive integer.")
        except ValueError:
            print("\nID must be a positive integer.")

    try:
        a = jikan.anime(request)

        # Gets data of requested anime
        x = np.zeros(shape=(1, 74), dtype=np.float32)
        try:
            x[0][0] = a["episodes"]
        except (KeyError, TypeError):
            pass
        try:
            x[0][1 + types.index(a["type"])] = 1
        except (KeyError, TypeError):
            pass
        try:
            x[0][8 + sources.index(a["source"])] = 1
        except (KeyError, TypeError):
            pass
        try:
            x[0][24 + ratings.index(a["rating"])] = 1
        except (KeyError, TypeError):
            pass
        try:
            for genre in a["genres"]:
                if genre != "":
                    x[0][31 + genres.index(genre["name"])] = 1
        except (KeyError, TypeError):
            pass

        # Normalizes first element in x to between 0 and 1
        x[0][0] = -10**(-0.01 * x[0][0]) + 1

        # Prints requested anime's title
        try:
            print("\nTitle: {}".format(a["title"]))
        except (KeyError, TypeError):
            print("\nTitle: N/A")

        prediction = model.predict([x])
        print("Predicted Score: {:.2f}".format(prediction[0][0]))

        # Prints actual score if available
        try:
            y = a["score"]
            print("Actual Score: {}".format(y))
        except (KeyError, TypeError):
            print("Actual Score: N/A")

    except jikanpy.exceptions.APIException:
        print("\nFailed to find the anime.")