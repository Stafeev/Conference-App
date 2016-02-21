#!/usr/bin/env python
import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache
from google.appengine.ext import ndb
from models import Session
from conference import MEMCACHE_SPEAKER_KEY
from conference import ConferenceApi
from models import Session
from models import Speaker


class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),  # from
            self.request.get('email'),  # to
            'You created a new Conference!',  # subj
            'Hi, you have created a following '  # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )


class SetFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        speaker = self.request.get('speaker')
        ConferenceApi._cacheFeaturedSpeaker(speaker)
        self.response.set_status(204)



app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/set_featured_speaker', SetFeaturedSpeakerHandler),
], debug=True)
