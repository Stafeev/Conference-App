App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
2. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
3. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
4. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
5. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting
   your local server's address (by default [localhost:8080][5].)
6. Generate your client library(ies) with [the endpoints tool][6].
7. Deploy your application.

## Task 1
Session and Speaker classes were first implemented in models.py. Conference.py contains corresponding endpoints and methods.
Base class Session has the following fileds:
    name            = ndb.StringProperty(required=True) 
    highlights      = ndb.StringProperty()
    speaker         = ndb.StringProperty()
    duration        = ndb.IntegerProperty()
    typeOfSession   = ndb.StringProperty()
    date            = ndb.DateProperty()
    startTime       = ndb.TimeProperty()
    speakerKey      = ndb.StringProperty()
speakerKey is a speakerID key. Speaker is the name of the speaker and it's used in getSessionsBySpeaker, for example, to query sessions by Speaker name.
Speaker class is implemented with the following fields:
    displayName = ndb.StringProperty(required=True)
    profileKey = ndb.StringProperty() - profile key is used if speaker is also an atendee
    biography = ndb.StringProperty()
Methods to work with Speaker:
    _createSpeakerObject(self, request) - creates Speaker object
    addSpeaker(self, request) - add Speaker
For Sessions:
    getConferenceSessions - return requested sessions for the conference (by websafeConferenceKey)
    getConferenceSessionsByType - return requested sessions for the conference (by websafeConferenceKey and type of session)
    getSessionsBySpeaker(self, request) - return requested sessions (by speaker)
    _sessionAdd(self, request) is used to add sessions from user's list of sessions (sessionKeysWishList)
    _sessionRemove(self, request) is used to delete sessions from user's list of sessions (sessionKeysWishList)
The flow of calls
    create a conference
    create a speaker
    create a session, using the speaker key returned in the second step
## Task 2
I added to profile class field sessionKeysWishList = ndb.StringProperty(repeated=True) to store a wishlist of sessions.Also we have to followng endpoint methods.

addSessionToWishlist: Saves a session to a user's wishlist.
Calls function _sessionAdd with to append session: prof.sessionKeysToWishlist.append(session.key) saving a session to wishlist.

getSessionsInWishlist: return a user's wishlist by fetching profile and wishlist.
## Task 3
getConferenceSessionFeed: returns a conference's sorted feed sessions occurring after today.
getSpeakers: returns all speakers
Also there is endpoint to add Speaker:
    @endpoints.method(SpeakerForm, SpeakerForm,path='speaker',http_method='POST', name='addSpeaker')
    def addSpeaker(self, request):
        """Create a new speaker"""
        return self._createSpeakerObject(request)

Queries are only allowed to have one inequality filter, and it would cause a BadRequestError to filter on both startDate and typeOfSession.
So we need to code this inside method queryProblem(self, request):
        sessionsByStartTime = Session.query(Session.startTime < request.startTime)
        sessionsByType = Session.query(Session.typeOfSession == request.typeOfSession)
Here we choose all sessions which starttime is before requested start time (7 am, for example).
Then we query sessions by type. Then we iterate over sessionsByType and check that this session is not in sessionsByStartTime and then add it to the dictionary and output the result.
## Task 4
getFeaturedSpeaker() checks the speaker when a new session is added to a conference.
Featured Speakers are stored in MEMCACHE_SPEAKER_KEY and set in _createSessionObject method.
            set featuredSpeakerText in memcache
            memcache.set(MEMCACHE_SPEAKER_KEY, featuredSpeakerText)
Then we call getFeaturedSpeaker() which simply fetches memcache.

[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
