from classhandlers.bloghandlerclass import BlogHandler

class Logout(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/')