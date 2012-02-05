from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app



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

class Qxapp(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers.add_header('Set-Cookie','com.liquidityspot.user=%s;' % user)     
            self.redirect('/system/index.html')
        else:
            self.redirect(users.create_login_url(self.request.uri))
        
#################################################################

application = webapp.WSGIApplication(
                                     [('/myBids', MyBids),
                                      ('/qxapp', Qxapp),
                                      ('/', Search)                                      
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
