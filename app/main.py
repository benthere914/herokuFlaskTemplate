from flask import Flask
from flask_cors import CORS
from .config import Config
from .models import db, User
from .routes import auth_routes
from .auth_token import guard

# import any blueprints from routes folder
app = Flask(__name__)

app.config.from_object(Config)
@app.route('/')
def home_route():
    return {"message": "got to the home route"}

app.register_blueprint(auth_routes, url_prefix='/auth')

# register blueprints to app

guard.init_app(app, User)
db.init_app(app)
CORS(app)

if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True)
