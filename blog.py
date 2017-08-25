import webapp2
from google.appengine.ext import db

# classhandlers
from classhandlers.bloghandlerclass import BlogHandler
from classhandlers.blogfrontclass   import BlogFront
from classhandlers.loginclass       import Login
from classhandlers.logoutclass      import Logout
from classhandlers.newpostclass     import NewPost
from classhandlers.postpageclass    import PostPage
from classhandlers.registerclass    import Register
from classhandlers.signupclass      import Signup
from classhandlers.editpostclass    import EditPost
from classhandlers.deletepostclass  import DeletePost
from classhandlers.addcommentclass  import AddComment
from classhandlers.editcommentclass  import EditComment
from classhandlers.deletecommentclass  import DeleteComment
from classhandlers.likepostclass  import LikePost



app = webapp2.WSGIApplication([ ('/?', BlogFront),
                               ('/([0-9]+)', PostPage),
                               ('/([0-9]+)/edit', EditPost),
                               ('/([0-9]+)/delete', DeletePost),
                               ('/([0-9]+)/addcomment', AddComment),
                               ('/([0-9]+)/editcomment/([0-9]+)', EditComment),
                               ('/([0-9]+)/deletecomment/([0-9]+)', DeleteComment),
                               ('/([0-9]+)/like', LikePost),
                               
                               ('/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ],
                              debug=True)
