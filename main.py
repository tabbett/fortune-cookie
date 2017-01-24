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
import random

def getRandomFortune():
    fortunes=[
        "I see much code in your future",
        "Consider eating more fortune cookies",
        "You have tamed the mighty Python, now you must free it on the Great Spider Web!"
    ]

    index = random.randint(0,2)
    
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        
        fortune = getRandomFortune()
        fortune_paragraph = "<p> Your fortune: <strong>" + fortune + "</strong></p>"

        lucky_number = random.randint(1,100)
        number_sentence = "<p> Your lucky number: <strong>" + str(lucky_number) + "</strong></p>"

        another_cookie_button = "<a href='.'><button>Another cookie plz</button></a>"
        
        self.response.write(header+fortune_paragraph+number_sentence+another_cookie_button)
 

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
