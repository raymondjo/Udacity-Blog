from classhandlers.bloghandlerclass import BlogHandler
from models.user import User
from models.post import Post
from globalfunctions import *

class EditPost(BlogHandler):
    def get(self, post_id):
         post = Post.get_by_id(int(post_id), parent=blog_key())
         if not post:
             return self.redirect('/login')

         if self.user and self.user.key().id() == post.user_id :
            render_text = post.content.replace('\n', '<br>')
            self.render('editpost.html' , p = post, content = render_text )
         
         elif not self.user :
            self.redirect('/login')
         else:
            self.write("You cannot edit this post becuase you are not the one who wrote this post.")
    

    def post(self, post_id):
        if not self.user:
            self.redirect('/login')

        post = Post.get_by_id(int(post_id), parent=blog_key())
        if not post:
             return self.redirect('/login')
            
        if self.user and self.user.key().id() == post.user_id :        
            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:
                post.subject = subject
                post.content = content
                post.put()

                self.redirect('/%s' % str(post.key().id()))
            else:
               error = "subject and content, please!"
               self.render("editpost.html", subject=subject, content=content, error=error)
        else:
            self.write("You cannot edit this post becuase you are not the one who wrote this post.")
