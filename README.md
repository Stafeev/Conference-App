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
## Task 2
addSessionToWishlist: given a session websafe key, saves a session to a user's wishlist.
Calls function _sessionAdd with parameter add=true to append session: prof.sessionKeysToWishlist.append(session.key)

getSessionsInWishlist: return a user's wishlist.
## Task 3
getConferenceSessionFeed: returns a conference's sorted feed sessions occurring after today.
getSpeakers: returns all speakers

Queries are only allowed to have one inequality filter, and it would cause a BadRequestError to filter on both startDate and typeOfSession.
So we need to check this in Python code inside method queryProblem(self, request).
## Task 4
getFeaturedSpeaker() checks the speaker when a new session is added to a conference
If there is more than one session by this speaker at this conference it add a new Memcache entry that features the speaker and session names. 

[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
