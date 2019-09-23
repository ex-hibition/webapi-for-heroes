from flask import Flask
from heroes.app import hero
from purchases.app import purchase

if __name__ == '__main__':

    app = Flask(__name__)
    app.register_blueprint(hero, url_prefix='/angular')
    app.register_blueprint(purchase, url_prefix='/sample')
    app.run(host='0.0.0.0', port=80, debug=True)
