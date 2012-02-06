from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import urllib

class JsonStore(db.Model):
    content = db.StringProperty()

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

class Qxapp(webapp.RequestHandler):
    def get(self):
        user = getUser()
        logging.debug(user)
        if user:
            self.response.headers.add_header('Set-Cookie','com.liquidityspot.user=%s;' % user)     
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
        jsonStore.content = text
        jsonStore.put()
        #jsonStores = db.GqlQuery("SELECT * "
                            #"FROM JsonStore "
                            #"WHERE ANCESTOR IS :1 ",
                            #bidsKey())
        #for retrievesJsonStore in jsonStores:
            #logging.info(retrievesJsonStore.content)
            
class Retrieve(webapp.RequestHandler):
    def get(self):
        jsonStores = db.GqlQuery("SELECT * "
                            "FROM JsonStore "
                            "WHERE ANCESTOR IS :1 ",
                            bidsKey())
        for jsonStore in jsonStores:
            self.response.out.write(jsonStore.content)
            logging.info(jsonStore.content)
            break
        
#################################################################

application = webapp.WSGIApplication(
                                     [('/myBids', MyBids),
                                      ('/qxapp', Qxapp),
                                      ('/save', Persist),
                                      ('/bids', Retrieve),
                                      ('/', Search)                                      
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
