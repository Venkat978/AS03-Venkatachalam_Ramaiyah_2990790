import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from Twitter import Twitter
from Twitter import Tweeet
from Twitter2 import Name
from Twitter2 import Update
from Twitter3 import Bio
from Twitter3 import Delete
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Twitter1(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        url_string = ''
        welcome = 'Welcome back'
        twitter = None
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'
            email = users.get_current_user().email()
            twitter_key = ndb.Key('Twitter', email)
            twitter = twitter_key.get()
            TK=ndb.Key('Tweeet','data')
            K=TK.get()
            if K==None:
                K=Tweeet(id='data')
                K.put()
            if twitter == None:
                welcome = 'Welcome to the application'
                twitter = Twitter(id=email)
                twitter.put()
            if twitter.UserName==None:
                self.redirect('/name')
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'
        sol=sol = Twitter.query().fetch()
        username=self.request.get('usersearch')
        finaluser=None
        q1=0
        tweetsearch=self.request.get('tweetsearch')
        finaltweet=[]
        q2=0
        action=self.request.get('button')
        if action=='Search':
            for a in sol:
                if a.UserName==username:
                    q1=q1+1
                    finaluser=username
        if action=='Tweet Search':
            for a in sol:
                for b in a.Tweet:
                    if tweetsearch in b:
                        q2=q2+1
                        finaltweet.append(b)
        followerslist=0
        followinglist=0
        if twitter!=None:
            for a in twitter.Followers:
                    followerslist=followerslist+1
            for b in twitter.Followings:
                    followinglist=followinglist+1

        tweet_key = ndb.Key('Tweeet', 'data')
        tweetkey = tweet_key.get()
        f1=[]
        twe=[]
        if tweetkey!=None:
            for a in reversed(tweetkey.Feed):
                f1.append(a)
            f1 = f1[:50]
            for b in reversed(tweetkey.User):
                twe.append(b)
            twe=twe[:50]
        st = map(' --> '.join,zip(twe,f1))

        template_values = {'url' : url,'url_string' : url_string,'user' : user,'welcome' : welcome,'twitter' : twitter,'q1':q1,'finaluser':finaluser,'q2':q2,'finaltweet':finaltweet,'followerslist':followerslist,'followinglist':followinglist,'st':st}
        template = JINJA_ENVIRONMENT.get_template('Twitter1.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', Twitter1),
('/name', Name),('/update',Update),
('/bio/(.*)',Bio),('/delete/(.*)',Delete)], debug=True)
