from classhandlers.bloghandlerclass import BlogHandler
from models.user import User

class Login(BlogHandler):
    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        # User model :
        # user.login function used to get user if it
        # found or not
        # if it found -> return user object
        # else return NONE
        u = User.login(username, password)
        # check if there a user or not
        if u:
            # self.login(u) -> set cookies to user browser 
            self.login(u)
            self.redirect('/')
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error = msg)