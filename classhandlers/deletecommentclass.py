from classhandlers.bloghandlerclass import BlogHandler
# from models.user import User
from models.post import Post
from models.comment import Comment
from globalfunctions import *

class DeleteComment(BlogHandler):
    def get(self, post_id, comment_id):
        postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
        comment = db.get(key)
    
        if self.user and self.user.key().id() == comment.user_id :
            comment.delete()
            self.redirect('/%s' % str(post_id))

        elif not self.user :
            self.redirect('/login')
        else:
            self.write("You don't have permission to delete this comment.")