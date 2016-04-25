# Copyright (C) 2015 Twitter, Inc.

from flask import Flask, request

webapp = Flask(__name__)

@webapp.route('/us/webhook', methods=['POST'])
def us_webhook():
  print 'us_webhook'
  print request.get_json()
  return 'OK'

@webapp.route('/eu/webhook', methods=['POST'])
def eu_webhook():
  print 'eu_webhook'
  print request.get_json()
  return 'OK'

if __name__ == '__main__':
  webapp.debug = True
  webapp.run()
