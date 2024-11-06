from flask import Flask

from app.controller.ai_controller import ai_blueprint
from app.utils.dependency_injector import injector

app = Flask(__name__)
app.config.from_object('config')

injector.configure()

app.register_blueprint(ai_blueprint, url_prefix='/ai')

if __name__ == '__main__':
    app.run(debug=True)
