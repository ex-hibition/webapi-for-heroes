from flask import Blueprint, jsonify
from flask_cors import cross_origin
from purchases.purchases import Purchases

purchase = Blueprint('purchases', __name__)

purchases = Purchases()

"""一覧を返す"""
@purchase.route('/purchases', methods=['GET', ])
@cross_origin()
def get_all():
    return jsonify(purchases.get_purchases()), 200


"""指定されたidのデータを返す"""
@purchase.route('/purchases/<target_id>', methods=['GET', 'POST'])
@cross_origin()
def get_purchase(target_id):
    return jsonify(purchases.get_user_purchases(target_id=target_id)), 200
