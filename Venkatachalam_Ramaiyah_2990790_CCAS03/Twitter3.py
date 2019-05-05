import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from Twitter import Twitter
from Twitter import Tweeet
import os

class Bio(webapp2.RequestHandler):
    def get(self,id):
        self.response.headers['Content-Type'] = 'text/html'
        user=id
        query = Twitter.query(Twitter.UserName == user)
        E=[]
        for a in query:
            for b in reversed(a.tweet):
                E.append(b)
        E = E[:50]
        template_values={'query':query,'E':E}
        template=JINJA_ENVIRONMENT.get_template('Twitter3.html')
        self.response.write(template.render(template_values))
    def post(self,id):
        email = users.get_current_user().email()
        twitter_key = ndb.Key('Twitter', email)
        twitter = twitter_key.get()
        UserName=twitter.UserName
        user=id
        emails=None
        newusername=None
        query = Twitter.query(twitter.UserName == user)
        for a in query:
            emails=a.key.id()
        action=self.request.get('button')
        if action == 'FOLLOW':
                twitter_keys = ndb.Key('Twitter', emails)
                twitter = twitter_keys.get()
                new_username=twitter.UserName
                if username==twitter.UserName:
                        self.redirect('/Bio/%s'%(my))
                else:
                    if username in twitter.Followers:
                            self.redirect('/')
                    else:
                            twitter.Followers.append(username)
                            twitter.Followings.append(newusername)
                            twitter.put()
                            twitter.put()
                            self.redirect('/Bio/%s'%(my))
        if action == 'UNFOLLOW':
            twitter_keys = ndb.Key('Twitter', emails)
            twitter = twitter_keys.get()
            new_username=twitter.UserName
            if username in twitter.Followers:
                twitter.Followers.remove(UserName)
                twitter.put()
                if new_username in twitter.Followings:
                    twitter.Followings.remove(new_username)
                    twitter.put()
            self.redirect('/Bio/%s'%(my))



class Delete(webapp2.RequestHandler):
    def get(self,id):
        self.response.headers['Content-Type'] = 'text/html'
        my=id
        email = users.get_current_user().email()
        twitter_key = ndb.Key('Twitter', email)
        twitter = twitter_key.get()
        u=twitter.tweet
        u=u[::-1]
        template_values={'twitter':twitter,'u':u}
        template=JINJA_ENVIRONMENT.get_template('Twitter3.html')
        self.response.write(template.render(template_values))
    def post(self,id):
        action = self.request.get('button')
        email = users.get_current_user().email()
        twitter_key = ndb.Key('Twitter', email)
        twitter = twitter_key.get()
        data_key = ndb.Key('Tweeet', 'data')
        data = data_key.get()
        my=id
        tt=None
        if action == 'delete':
            e=myuser.Tweet
            e=e[::-1]
            del e[int(self.request.get('index')) - 1]
            e=e[::-1]
            twitter.Tweet=l
            twitter.put()
            tw=self.request.get('users_name')
            data.Feed.remove(tw)
            data.put()
            self.redirect('/Delete/%s'%(my))
        if action=='Edit':
            new=self.request.get('users_name')
            n=myuser.Tweet
            n=n[::-1]
            new=n[int(self.request.get('index'))-1]
            u=myuser.Tweet
            u=u[::-1]
            u[int(self.request.get('index'))-1]=self.request.get('users_name')
            u=u[::-1]
            twitter.Tweet=l
            twitter.put()
            data.Feed[db.Feed.index(tw1)]=tw
            data.put()
            self.redirect('/')
