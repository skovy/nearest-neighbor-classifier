### Track Nearest Neighbors Classifier

The purpose of this script is to implement a basic K Nearest Neighbors
Classifier using an audio summary generated from Echonest. We can then
classify new tracks using their audio summary and it's nearest neighbors.

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Setup

Relies on the track data generated from Spotify and Echonest in the format
created [using this script](https://github.com/Skovy/spotify-echonest).

#### Add Environment Variables for Spotify/Echonest API's

This is used for the new track being classified.

```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='http://localhost'
export ECHO_NEST_API_KEY='your-echonest-api-key'
```

#### Run the script

- `python main.py <spotify-uri> <n-training-data> <n_neighbors>`
  - `spotify-uri` *(required)*: the Spotify URI of the track to classify
  - `n-training-data` *(optional)*: the total number of tracks to use as training data
  - `n_neighbors` *(optional)*: the number of neighbors to classify with
- Spotify Authentication will open in your default browser (first time only)
- Grant Access
- Copy the URL to the terminal when prompted (contains the Spotify code)
- The track will be classified using existing track data from [this script](https://github.com/Skovy/spotify-echonest))
