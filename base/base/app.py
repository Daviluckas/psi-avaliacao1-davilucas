from flask import Flask
from blueprints.produtos import produtos_bp
from blueprints.auth import auth_bp

app = Flask(__name__)

app.secret_key = "quitanda-secreta"

app.register_blueprint(produtos_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)