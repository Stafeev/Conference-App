#!/usr/bin/env python
import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache
from models import Session
from conference import MEMCACHE_SPEAKER_KEY


class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        ConferenceApi._cacheAnnouncement()


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
        """Set Featured Speaker in Memcache."""
        sessions = Session.query().filter(Session.speakerKey == self.request.get('speakerKey'))
        # Add one key the session key can't be found in the queried sessions
        not_found = not any(s.key.urlsafe() == self.request.get('sessionKey') for s in sessions)
        sessions = Session.query().filter(Session.speakerKey == self.request.get('speakerKey')).count()
        # Add one key the session key can't be found in the queried sessions
        if sessions > 1:
            memcache.set(MEMCACHE_SPEAKER_KEY, '%s is our Featured Speaker' % self.request.get('speakerDisplayName'))
        self.response.set_status(204)


app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/set_featured_speaker', SetFeaturedSpeakerHandler),
], debug=True)
