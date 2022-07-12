# Import dependencies
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import secrets
# Set global app
app = Flask(__name__)

# Set security flask
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/")
def index():
    # number = secrets.randbelow(10)
    return f"Testing, Flask!"