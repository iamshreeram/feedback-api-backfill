# Feedback API Backfill

This python script will backfill Feedback API events. Event data is requested from GET feedback/events.json and then individual events are posted to existing webhook endpoint URLs.

The Feedback API is a whitelisted API. Contact your Twitter account manager for details.

## Before you start

- Run the script against a development webhook endpoint or use the provided webapp (optional instructions below). 

- Validate that the incoming data meets the requirements of your production environment.

- Ensure your webhook endopoint can handle duplicate events. If for some reason the script fails, you may need to re-run the script.

- If your webhook endpoint requires authentication you may need to modify the webhook request.

## Running the script

1. Install python dependencies.

    `pip install -r requirements.txt`


1. Using config_sample.py as a template, create a config.py and fill in Twitter API keys, webhook URLs and other configraution settings.

1. (optional) Start webserver to simulate webhook endpoints and test incomcoming event data. Setup config.py to POST data to `http://127.0.0.1:5000/us/webhook`. The webapp will print incoming event data to the terminal window.

	`python webhookapp.py`


1. Run backfill.py to initiate backfilling to webhooks.

    `python backfill.py`