from classhandlers.bloghandlerclass import BlogHandler
from models.post import Post

# from models.comment import Comment
# from google.appengine.ext import db
from globalfunctions import *

class BlogFront(BlogHandler):
    def get(self):
         posts = greetings = Post.all().order('-created')
         self.render('front.html', posts = greetings )

