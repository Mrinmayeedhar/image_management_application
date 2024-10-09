from werkzeug.security import generate_password_hash, check_password_hash

users = {}  # Use a database in production

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    hashed_pw = generate_password_hash(password)
    users[username] = hashed_pw
    return 'Signup successful'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and check_password_hash(users[username], password):
        session['user'] = username
        return 'Login successful'
    return 'Login failed'