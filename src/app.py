# Import dependencies
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import random
# Set global app
app = Flask(__name__)

# Set security flask
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/")
def index():
    number = random.randint(1,10)
    return "Testing, Flask!"
    # return f"<h1>{number}</h1>"
app.run()
