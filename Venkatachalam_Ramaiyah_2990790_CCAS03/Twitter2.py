import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from Twitter import Twitter
from Twitter import Tweeet
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Name(webapp2.RequestHandler):
    def get(self):

        email = users.get_current_user().email()
        twitter_key = ndb.Key('Twitter', email)
        twitter = twitter_key.get()
        url = users.create_logout_url(self.request.uri)
        if action == 'Submit':
            UserName=self.request.get('input')
            PersonalInfo=self.request.get('input1')
            twitter.UserName=UserName
            twitter.PersonalInfo=PersonalInfo
            twitter.put()
            self.redirect('/')
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'
            sol=sol = Twitter.query().fetch()
            username=self.request.get('usersearch')
        template_values = {'url' : url,'url_string' : url_string,'sol' : sol,'twitter' : twitter}
        template = JINJA_ENVIRONMENT.get_template('Twitter2.html')
        self.response.write(template.render(template_values))
        
class Update(webapp2.RequestHandler):
    def get(self):
        email = users.get_current_user().email()
        twitter_key = ndb.Key('Twitter', email)
        twitter = twitter_key.get()
        q1=twitter.PersonalInfo
        action=self.request.get('button')
        if action == 'Submit':
            info=self.request.get('input1')
            twitter.PersonalInfo=PersonalInfo
            twitter.put()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'
            sol=sol = Twitter.query().fetch()
            username=self.request.get('usersearch')
        template_values = {'url' : url,'url_string' : url_string,'q1' : q1,'twitter' : twitter}
        template = JINJA_ENVIRONMENT.get_template('Twitter2.html')
        self.response.write(template.render(template_values))

    def post(self):
        email = users.get_current_user().email()
        twitter_key = ndb.Key('Twitter', email)
        twitter = twitter_key.get()
        action=self.request.get('button')
        mm=ndb.Key('Tweeet','data')
        s=mm.get()
        name=twitter.UserName
        if action == 'Submit':
            tweet=self.request.get('Tweeet')
            twitter.Tweet.append(tweet)
            s.Feed.append(tweet)
            s.User.append(tweet)
            s.put()
            twitter.put()
            self.redirect('/')
