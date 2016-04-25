# API settings
API_URL = 'https://api.twitter.com/1.1/feedback/events.json'
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'you_access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# All webhook endpoints that need to recieve backfill data
# name (optional)
# url (required)
WEBHOOKS_CONFIGS = [{
	'name': 'prod-us',
	'url': 'http://127.0.0.1:5000/us/webhook'
},
{
	'name': 'prod-eu',
	'url': 'http://127.0.0.1:5000/eu/webhook'
}]

# Time in seconds to sleep between requests
FEEDBACK_API_SLEEP = 0.75 # stays within 1000/15 min rate limit
WEBHOOK_SLEEP = 0.25

# Max number of events recevied from each feedback API request
EVENTS_PAGE_COUNT = 100;

# Epoch timestamp in milliseconds
START_TIME = 1451635200000
END_TIME = 1461193685380