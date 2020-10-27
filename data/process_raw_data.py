import numpy as np

data_in = np.genfromtxt("raw_data.csv", dtype=np.object, delimiter=",")
x = np.zeros(shape=(len(data_in), 124), dtype=np.float32)
y = np.zeros(shape=(len(data_in)), dtype=np.float32)

# Stored in arrays so each word is mapped to a number (the index)
types = ["TV", "Movie", "OVA", "ONA", "Special", "Music", "Unknown"]
sources = ["4-koma manga", "Book", "Card game", "Digital manga", "Game", "Light novel", "Manga", "Music", "Novel", "Original",
           "Picture book", "Radio", "Visual novel", "Web manga", "Other", "Unknown"]
ratings = ["G - All Ages", "PG - Children", "PG-13 - Teens 13 or older", "R - 17+ (violence & profanity)", "R+ - Mild Nudity", "Rx - Hentai", "None"]
genres = ["Action", "Adventure", "Cars", "Comedy", "Dementia", "Demons", "Drama", "Ecchi", "Fantasy", "Game",
          "Harem", "Hentai", "Historical", "Horror", "Josei", "Kids", "Magic", "Martial Arts", "Mecha", "Military",
          "Music", "Mystery", "Parody", "Police", "Psychological", "Romance", "Samurai", "School", "Sci-Fi", "Seinen",
          "Shoujo", "Shoujo Ai", "Shounen", "Shounen Ai", "Slice of Life", "Space", "Sports", "Super Power", "Supernatural", "Thriller",
          "Vampire", "Yaoi", "Yuri"]
studios = ["Toei Animation", "Sunrise", "Production I.G", "J.C.Staff", "Madhouse", "TMS Entertainment", "Studio Deen", "Studio Pierrot", "OLM", "Nippon Animation",
           "A-1 Pictures", "DLE", "Shin-Ei Animation", "Tastunoko Production", "Xebec", "Gonzo", "Bones", "Shaft", "Kyoto Animation", "Satelight",
           "Silver Link.", "Brain&#039;s Base", "Production Reed", "Gainax", "Doga Kobo", "Arms", "Magic Bus", "Mushi Production", "Zexcs", "Studio 4Â°C",
           "LIDENFILMS", "Seven", "Studio Hibari", "feel.", "ufotable", "Studio Comet", "Gallop", "MAPPA", "Kachidoki Studio", "Haoliners Animation League",
           "Ajia-Do", "Studio Ghibli", "Wit Studio", "Lerche", "TNK", "P.A. Works", "Diomedea", "Artland", "Asahi Production", "Actas"]

for i in range(len(data_in)):
    # x
    # Columns 0 to 6 store type
    x[i][0 + types.index(str(data_in[i][1]).lstrip("b'").rstrip("'"))] = 1
    # Columns 7 to 22 store source
    x[i][7 + sources.index(str(data_in[i][2]).lstrip("b'").rstrip("'"))] = 1
    # Columns 23 to 29 store rating
    x[i][23 + ratings.index(str(data_in[i][3]).lstrip("b'").rstrip("'"))] = 1
    # Columns 30 to 72 store genre
    for genre in [genre.strip() for genre in str(data_in[i][4]).lstrip("b'").rstrip("'").split(";")]:
        if genre != "":
            x[i][30 + genres.index(genre)] = 1
    # Columns 73 to 123 store genre; column 123 is used if the studio does not match the 50 studios on the list
    matched_studio = False
    for studio in [studio.strip() for studio in str(data_in[i][5]).lstrip("b'").rstrip("'").split(";")]:
        if studio != "" and studio in studios:
            x[i][73 + studios.index(studio)] = 1
            matched_studio = True
    if not matched_studio:
        x[i][123] = 1

    # y
    # Stores scores
    y[i] = float(str(data_in[i][0]).lstrip("b'").rstrip("'"))

np.savetxt("x.csv", x, delimiter=",")
np.savetxt("y.csv", y, delimiter=",")