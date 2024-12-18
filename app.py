from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from models import Users, User  # Import your User class and the Users list

# Initialize Flask & Flask-Login
app = Flask(__name__)
app.secret_key = 'mysecretkey'
login_manager = LoginManager()
login_manager.init_app(app)

# Load user callback for Flask-login
@login_manager.user_loader
def load_user(user_id):
    return next((user for user in Users if user.id == int(user_id)), None)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']  # Use lowercase for variable consistency
        password = request.form['password']
        
        # Correct user lookup and password check
        user = next((user for user in Users if user.username == username and user.password == password), None)
        
        if user:
            login_user(user)  # Log the user in
            return redirect(url_for('protected_route'))  # Redirect to the protected route
    
    return render_template('login.html')  # Ensure the template exists

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Logout the user
    return redirect(url_for('login'))  # Redirect to login

# Protected route (requires login)
@app.route('/protected')
@login_required
def protected_route():
    return 'Welcome to the protected route. You are logged in Unicord -Kenya!'  # Protected content

@app.route('/')
def home():
    return redirect(url_for('login')) 


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging for more detailed error messages
