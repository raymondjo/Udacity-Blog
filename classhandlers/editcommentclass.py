from classhandlers.bloghandlerclass import BlogHandler
# from models.user import User
# from models.comment import Comment
from google.appengine.ext import db
from globalfunctions import *

class EditComment(BlogHandler):
    def get(self,post_id, comment_id):
        postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
        comment = db.get(key)
       
        if not comment:
            self.redirect('/login')

        if self.user and self.user.key().id() == comment.user_id :
            render_text = comment.content.replace('\n', '<br>')
            self.render('editcomment.html' ,post_id = post_id, content = render_text )
         
        elif not self.user :
            self.redirect('/login')
        else:
            self.write("You cannot edit this comment becuase you are not the one who wrote this.")
    

    def post(self, post_id, comment_id):
        if not self.user:
            self.redirect('/login')
       
        postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
        comment = db.get(key)
       
        if not comment:
            self.redirect('/login')
        
        if self.user and self.user.key().id() == comment.user_id :        
            content = self.request.get('content')

            if  content:
                comment.content = content
                comment.put()

                self.redirect('/%s' % str(post_id))
            else:
               error = "content, please!"
               self.render("editcomment.html", content=content, error=error)
        else:
            self.write("You cannot edit this comment becuase you are not the one who wrote this.")
