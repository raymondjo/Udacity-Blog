from google.appengine.ext import db
from classhandlers.bloghandlerclass import BlogHandler
from globalfunctions import *
# from models.post import Post
# from models.comment import Comment

class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        # post = Post.get_by_id(int(post_id), parent=blog_key())
        comments = db.GqlQuery(
            "select * from Comment where ancestor is :1 order by created desc limit 10", key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", p = post, comments = comments)