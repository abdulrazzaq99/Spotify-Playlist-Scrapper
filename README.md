# Spotify Playlist Scrapper

This project retrieves data from a Spotify playlist using the Spotify Web API and stores the information in a JSON file. It includes a Python script that connects to the Spotify API, retrieves track information from a specified playlist, and saves the data in a JSON format.

## Requirements

To run the script, you need to have Python installed on your system along with the `spotipy` library. You can install the required library using pip:

# Package

pip install spotipy

You also need to obtain your client ID and client secret from the Spotify Developer Dashboard to authenticate with the Spotify API.

## Usage

1. Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with your actual Spotify API credentials in the Python script.

2. Replace `playlist_id` with the ID of the playlist you want to scrape.

3. Run the Python script. It will retrieve track information from the specified playlist and store it in a JSON file named `spotify_playlist.json`.

## File Structure

- `spotify_playlist.json`: JSON file containing information about each track in the playlist.
- `spotify_playlist_scrapper.py`: Python script to scrape data from the Spotify playlist and store it in a JSON file.

Feel free to modify and extend the script according to your needs!
