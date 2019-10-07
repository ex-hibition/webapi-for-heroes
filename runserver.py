from flask import Flask
from heroes.app import hero
from purchases.app import purchase
from billing.app import bill

if __name__ == '__main__':

    app = Flask(__name__)
    app.register_blueprint(hero, url_prefix='/angular')
    app.register_blueprint(purchase, url_prefix='/sample')
    app.register_blueprint(bill, url_prefix='/bill')
    app.run(host='0.0.0.0', port=80, debug=True)
