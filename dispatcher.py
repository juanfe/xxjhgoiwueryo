from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import urllib

class JsonStore(db.Model):
    content = db.TextProperty()

class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/welcome.html",dict))

class Search(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/search.html",dict))

class PlaceBids(webapp.RequestHandler):
    def get(self):       
        self.response.out.write(template.render("templates/placeBids.html",dict))
        
class MyBids(webapp.RequestHandler):
    def get(self):       
        self.response.out.write(template.render("templates/myBids.html",dict))

def getUser():
    user = users.get_current_user()
    if user:
        return users.get_current_user().email()
    else:
        return None

def userCookie():
    userCookieKey = 'com.liquidityspot.user'
    user = getUser()
    if user:
        return '%s=%s;' % (userCookieKey, user)
    else:
        return '%s=; Max-Age=0; Path=/' % userCookieKey

class Qxapp(webapp.RequestHandler):
    def get(self):
        user = getUser()
        self.response.headers.add_header('Set-Cookie',userCookie())
        if user:
            self.redirect('/system/index.html')
        else:
            self.redirect(users.create_login_url(self.request.uri))

def bidsKey():
    entityKind = 'JsonStore'
    key = getUser()
    return db.Key.from_path(entityKind, key)

class Persist(webapp.RequestHandler):
    def post(self):
        text = self.request.get('bids') 
        text = urllib.unquote(text.encode('ascii')).decode('utf-8')
        logging.info(text)
        jsonStore = JsonStore(parent=bidsKey())
        jsonStore.content = db.Text(text)
        jsonStore.put()
            
class Retrieve(webapp.RequestHandler):
    def get(self):
        jsonStores = db.GqlQuery("SELECT * "
                            "FROM JsonStore "
                            "WHERE ANCESTOR IS :1 ",
                            bidsKey())
        jsonStore = None
        for jsonStore in jsonStores:
            logging.info(jsonStore.content)
        self.response.out.write(jsonStore.content)
        
            

class Logout(webapp.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/qxapp'))
        
#################################################################

application = webapp.WSGIApplication(
                                     [('/myBids', MyBids),
                                      ('/qxapp', Qxapp),
                                      ('/save', Persist),
                                      ('/bids', Retrieve),
                                      ('/logout', Logout),
                                      ('/', Search)                                      
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
