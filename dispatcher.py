from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app



class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/search.html",dict))

class PlaceBids(webapp.RequestHandler):
    def get(self):
        
        
        self.response.out.write(template.render("templates/placeBids.html",dict))


#################################################################

application = webapp.WSGIApplication(
                                     [('/', HomePage)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
