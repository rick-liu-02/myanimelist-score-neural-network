# myanimelist-score-neural-network

Predicts the user ratings of MyAnimeList entries using a neural network, made in Python with TensorFlow and JikanPy.

Takes the type (TV/Movie/etc), source (Manga/Light Novel/etc), genre(s) and studio(s) into consideration and tries to predict a user rating on a scale of 0 to 10. When rating new entries, the program achieves a mean absolute error of around 0.9, though it regularly outputs scores that are way off.

## Example:

![Screenshot of Program](docs/screenshot_1.png)

Note that the program works (and is specifically designed to work) with entries that do not have actual user ratings yet.
