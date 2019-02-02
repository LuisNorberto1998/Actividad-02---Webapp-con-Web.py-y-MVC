import web
import config as config

class Main:
    def __init__(self):
        pass

    def GET(self):
        return config.render.index()