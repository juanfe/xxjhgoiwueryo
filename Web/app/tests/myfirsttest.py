'''
Created on Mar 8, 2012

@author: Camilo
'''

import unittest
from webtest import TestApp

from google.appengine.ext import db
from google.appengine.ext import testbed

from dispatcher import application

class MyFirstTest(unittest.TestCase):

    def setUp(self):

        self.testbed = testbed.Testbed()

        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.setup_env(app_id='liquidityspot')
        self.testbed.activate()

        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()

        # create a test server for us to prod
        self.testapp = TestApp(application)

    def tearDown(self):            
        self.testbed.deactivate()

    def testFetchRootURL(self):

        result = self.testapp.get("/")
        self.assertEqual(result.status, "302 Moved Temporarily")
        