#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


class MainHandler(webapp2.RequestHandler):
    def get(self):
    	t = get_template('base.html')
    	html = t.render(Context({'site_name': now}))
        self.response.write(html)
        
    def current_datetime(request):
    	now = datetime.datetime.now()
    	t = get_template('base.html')
    	html = t.render(Context({'current_date': now}))
    	return HttpResponse(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
