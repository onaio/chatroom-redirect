import cherrypy


class SupportChatRoom(object):
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("http://www.hipchat.com/gmAP6cMyi")

cherrypy.quickstart(SupportChatRoom())
