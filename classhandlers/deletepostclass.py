from classhandlers.bloghandlerclass import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from globalfunctions import *

class DeletePost(BlogHandler):
    def get(self, post_id):
         post = Post.get_by_id(int(post_id), parent=blog_key())

         if not post:
             return self.redirect('/login')

         if self.user and self.user.key().id() == post.user_id :
             postKey = db.Key.from_path('Post', int(post_id), parent = blog_key())
             comments = db.GqlQuery(
               "select * from Comment where ancestor is :1 ", postKey)
             for p in comments:
                 p.delete()

             post.delete()

             self.redirect('/')

         elif not self.user :
            self.redirect('/login')
         else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            comments = db.GqlQuery(
                "select * from Comment where ancestor is :1 order by created desc limit 10", key)

            error = "You don't have permission to delete this post"
            self.render("permalink.html", post=post, comments=comments, error=error)