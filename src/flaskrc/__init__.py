from flask import Flask

from flaskrc.config.FlaskConfig import configurar_app

app: Flask = Flask(__name__, instance_relative_config=True)

configurar_app(app)
