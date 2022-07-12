# Import dependencies
from flask import Flask
from flask_wtf.csrf import CSRFProtect
# Set global app
app = Flask(__name__)

# Set security flask
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/")
def index():
    return f"Testing, Flask!"