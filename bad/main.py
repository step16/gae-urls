import webapp2

class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("got a request for %s" % self.request.path)

app = webapp2.WSGIApplication([(r'.*', MyHandler)])
