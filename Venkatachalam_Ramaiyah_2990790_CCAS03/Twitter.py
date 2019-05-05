from google.appengine.ext import ndb
class Twitter(ndb.Model):
    UserName = ndb.StringProperty()
    PersonalInfo = ndb.StringProperty()
    Tweet = ndb.StringProperty(repeated=True)
    Followers = ndb.StringProperty(repeated=True)
    Followings = ndb.StringProperty(repeated=True)

class Tweeet(ndb.Model):
     Feed = ndb.StringProperty(repeated=True)
     User = ndb.StringProperty(repeated=True)
