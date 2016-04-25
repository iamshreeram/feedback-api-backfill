# Copyright (C) 2015 Twitter, Inc.

import requests
import json
import time
from requests_oauthlib import OAuth1

import config


def get_oauth():
	'''
	Generates an OAuth object

	Returns:
		OAuth1: Instance of OAuth1 with app keys in configruation
	'''

	oauth = OAuth1(config.CONSUMER_KEY,
		client_secret=config.CONSUMER_SECRET,
		resource_owner_key=config.ACCESS_TOKEN,
		resource_owner_secret=config.ACCESS_TOKEN_SECRET)

	return oauth


def get_events(from_time, to_time, next_cursor=None):
	'''
	Requests a page of feedback events

  Args:
    from_time (int): Epoch timestamp in milliseconds.
    to_time (int): Epoch timestamp in milliseconds. 
    next_cursor (unicode): To retrieve pages.
  '''

	params = {
		'from_time': from_time,
		'to_time': to_time,
		'count': config.EVENTS_PAGE_COUNT
	}

	req = requests.get(url=config.API_URL, params=params, headers={ 'content-type': 'application/json' }, auth=get_oauth())

	if req.status_code == requests.codes.ok:
		response_body = json.loads(req.text)

		# for all events in response post to webhooks
		feedback_events = response_body.get('events')
		for event in feedback_events:
			post_to_webhooks(event)

		# check for paging cursor
		next_cursor = response_body.get('next_cursor', None)
		if next_cursor is not None:

			print type(next_cursor)
			# request next page of events
			time.sleep(config.FEEDBACK_API_SLEEP)
			
			print 'Requesting next page of events.'
			get_events(from_time, to_time, next_cursor)

		else:
			print 'Events backfill complete.'

	else:
		# handle non 200 OK response
		pass


def post_to_webhooks(feedback_event):
	'''
	Posts feedback event object to all webhook endpoints

  Args:
    feedback_event (dict): Dictionary representing Feedback event from API.
	'''

	# post event to each each webhook URL
	for webhook in config.WEBHOOKS_CONFIGS:
		webhook_name = webhook.get('name')
		webhook_url = webhook.get('url')

		print 'Sending POST request to webhook %s: %s' % (webhook_name, webhook_url)
		time.sleep(config.WEBHOOK_SLEEP)
		req = requests.post(url=webhook_url, json=json.dumps(feedback_event), headers={ 'content-type': 'application/json' })
		
		# handle webhook response
		print 'Webhook response code: %s' % req.status_code


if __name__ == '__main__':
	get_events(from_time=config.START_TIME, to_time=config.END_TIME)

	