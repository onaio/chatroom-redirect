import cherrypy


class SupportChatRoom(object):
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("http://www.hipchat.com/gmAP6cMyi")

    @cherrypy.expose
    def hki(self):
        raise cherrypy.HTTPRedirect("http://www.hipchat.com/gX82m2lSu")

cherrypy.quickstart(SupportChatRoom())
