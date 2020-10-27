import numpy as np

data_in = np.genfromtxt("raw_data.csv", dtype=np.object, delimiter=",")
x = np.zeros(shape=(len(data_in), 74), dtype=np.float32)
y = np.zeros(shape=(len(data_in)), dtype=np.float32)

# Stored in arrays so each word is mapped to a number (the index)
types = ["TV", "Movie", "OVA", "ONA", "Special", "Music", "Unknown"]
sources = ["4-koma manga", "Book", "Card game", "Digital manga", "Game", "Light novel", "Manga", "Music", "Novel", "Original", "Picture book", "Radio", "Visual novel", "Web manga", "Other", "Unknown"]
ratings = ["G - All Ages", "PG - Children", "PG-13 - Teens 13 or older", "R - 17+ (violence & profanity)", "R+ - Mild Nudity", "Rx - Hentai", "None"]
genres = ["Action", "Adventure", "Cars", "Comedy", "Dementia", "Demons", "Drama", "Ecchi", "Fantasy", "Game", "Harem", "Hentai", "Historical", "Horror", "Josei", "Kids", "Magic", "Martial Arts", "Mecha", "Military", "Music", "Mystery", "Parody", "Police", "Psychological", "Romance", "Samurai", "School", "Sci-Fi", "Seinen", "Shoujo", "Shoujo Ai", "Shounen", "Shounen Ai", "Slice of Life", "Space", "Sports", "Super Power", "Supernatural", "Thriller", "Vampire", "Yaoi", "Yuri"]

for i in range(len(data_in)):
    # x
    # Column 0 stores number of episodes
    x[i][0] = float(str(data_in[i][2]).lstrip("b'").rstrip("'"))
    # Columns 1 to 7 store type
    x[i][1 + types.index(str(data_in[i][0]).lstrip("b'").rstrip("'"))] = 1
    # Columns 8 to 23 store source
    x[i][8 + sources.index(str(data_in[i][1]).lstrip("b'").rstrip("'"))] = 1
    # Columns 24 to 30 store rating
    x[i][24 + ratings.index(str(data_in[i][3]).lstrip("b'").rstrip("'"))] = 1
    # Columns 31 to 73 store genre
    for genre in [genre.strip() for genre in str(data_in[i][5]).lstrip("b'").rstrip("'").split(";")]:
        if genre != '':
            x[i][31 + genres.index(genre)] = 1

    # y
    # Stores scores
    y[i] = float(str(data_in[i][4]).lstrip("b'").rstrip("'"))

# Normalizes first column in x to between 0 and 1
min = x[0][0]
max = x[0][0]
for row in x:
    if row[0] < min:
        min = row[0]
    if row[0] > max:
        max = row[0]
for i in range(len(x)):
    x[i][0] = (x[i][0] - min) / (max - min)

np.savetxt("x.csv", x, delimiter=",")
np.savetxt("y.csv", y, delimiter=",")