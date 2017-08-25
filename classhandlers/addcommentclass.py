from classhandlers.bloghandlerclass import BlogHandler
from models.comment import Comment
from globalfunctions import *


class AddComment(BlogHandler):
    def get(self, post_id):
        if not self.user:
            self.redirect("/login")
        else:
            self.render("addcomment.html")

    def post(self, post_id):
        if not self.user:
            self.redirect("/login")
            # return
        
        content = self.request.get('content')

        if content:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            user_name = self.user.name
            c = Comment(parent=key, user_id=int(self.user.key().id()), content = content, user_name = user_name)
            c.put()
            self.redirect('/' + post_id)
        else:
            error = "content for comment, please!"
            self.render("addcomment.html", content=content, error=error)

