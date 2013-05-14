from google.appengine.api import users

# In this script you allow menus for the diferents type of users

class Page:
    HOME = 1
    SEARCH = 2
    CALC = 3
    MYBIDS = 4
    LOGOUT = 5
    USERS = 6
    DEMODATA = 7
    DEMORECREATE = 8
    NOTALLOW = 9


class HomePage:
    url = "/home"
    text = 'Home'
    groups = ['Admin', 'Demo', 'MO', 'Broker', 'Engine', 'Guest']


class SearchPage:
    url = "/search"
    text = 'Search loans'
    groups = ['Admin', 'MO', 'Broker', 'Guest', 'Demo']


class CalcPage:
    url = "/calc"
    text = 'Calculate'
    groups = ['Admin', 'Engine', 'Demo']


class MyBidsPage:
    url = "/mybids"
    text = 'My bids'
    groups = ['Admin', 'MO', 'Broker', 'Demo']


class LogoutPage:
    url = "/logout"
    text = 'Logout'
    groups = ['Admin', 'MO', 'Broker', 'Engine', 'Guest', 'Demo']


class NotAllowpage:
    url = "/notallow"
    text = 'Not Allowed'
    groups = ['Admin', 'MO', 'Broker', 'Engine', 'Guest', 'Demo']


class UsersPage:
    url = "/manusers"
    text = 'Users'
    groups = ['Admin', 'Demo']


class DemoData:
    url = "/DataTesting"
    text = "Create Demo Data"
    groups = ['Demo']


class DemoRecreate: 
    url = "/RecreateData"
    text = "Update Demo Data"
    groups = ['Demo']
