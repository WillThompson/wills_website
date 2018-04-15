#!/usr/bin/python
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/app/")

activate_this = '/var/www/html/app/app/virtual/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app import app as application
application.secret_key = '123456789a!'
