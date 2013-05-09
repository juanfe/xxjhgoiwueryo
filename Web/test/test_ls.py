from funkload.FunkLoadTestCase import FunkLoadTestCase


class LS(FunkLoadTestCase):
    def setUp(self):
        self.server_url = self.conf_get('main', 'url')

    def test_get(self):
        server_url = self.server_url
        self.get(server_url + "/",
                description="Get /")
        ret = self.get(server_url + "/_ah/login",
                params = [["email", "juajara@gmail.com"],
                    ["action", "Login"],
                    ["continue", "http://localhost:8080/"]],
                description="Login test")
        print 80*"~"
        #print (ret)
        #print (ret.body)
        #print self.getBody()
        print self.getLastUrl()
        #print dir(FunkLoadTestCase)
        print 80*"~"
        #self.assert_("login" not in self.getLastUrl(), "Error in login")
        self.assert_(ret.code in [200, 302, 304], "expecting a 200 or 302 or 405")

    def test_ls(self):
        server_url = self.server_url
        res = self.get(server_url, description='Get url')
        self.assertEqual(res.code, 200)
        self.assertEqual(res.body, """<html>
<head>
  <title>Login</title>
</head>
<body>

<form method="get" action="http://localhost:8080/_ah/login"
      style="text-align:center; font: 13px sans-serif">
  <div style="width: 20em; margin: 1em auto;
              text-align:left;
              padding: 0 2em 1.25em 2em;
              background-color: #d6e9f8;
              border: 2px solid #67a7e3">
    <h3>Not logged in</h3>
    <p style="padding: 0; margin: 0">
      <label for="email" style="width: 3em">Email:</label>
      <input name="email" type="email" value="test@example.com" id="email"/>
    </p>
    <p style="margin: .5em 0 0 3em; font-size:12px">
      <input name="admin" type="checkbox" value="True"
        id="admin"/>
        <label for="admin">Sign in as Administrator</label>
    </p>
    <p style="margin-left: 3em">
      <input name="action" value="Login" type="submit"
             id="submit-login" />
      <input name="action" value="Logout" type="submit"
             id="submit-logout" />
    </p>
  </div>
  <input name="continue" type="hidden" value="http://localhost:8080/"/>
</form>

</body>
</html>
""")

if __name__ in ('main', '__main__'):
    unittest.main()
