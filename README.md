# now-playing-bio

Puts the song you're currently listening to in your bsky bio. 

# Server

`pip install -r requirements.txt`

`mv .env.example .env`

Then fill out .env with the appropriate data.

You'll need to set up a server that can accept the webhook. Run main.py and put it behind the reverse proxy of your choice.

# Client

The preferred way to use this is via MacroDroid (because that's what I use), but you could definitely cook up something with Apple Shortcuts, Tasker, or a shell script. All you need to do is send a request to $your_server/now_playing with the query parameters `api_key` (which is whatever you want it to be), `artist` and `track`.

To set up MacroDroid, download the [macro file](integrations/Now_Playing_to_Webhook.macro) to your phone, open MacroDroid, and click "Import/Export" from the home page. Once you have it imported, change `your-server.com` in the HTTP Request to the url for your server, and the api_key query parameter to your API key.

If you don't use Pano Scrobbler, change the notification constraint to whatever music apps you use. Or just remove it if you want all media to be in your bio.

If you write an integration for any other apps, please submit it to this repo.
