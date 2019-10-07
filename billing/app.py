from flask import Blueprint, jsonify
from flask_cors import cross_origin
from billing.billing import Billing

bill = Blueprint('bill', __name__)

billing = Billing()

"""一覧を返す"""
@bill.route('/billing', methods=['GET', ])
@cross_origin()
def get_all():
    return jsonify(billing.get_billing()), 200


"""指定されたidのデータを返す"""
@bill.route('/billing/<target_id>', methods=['GET', 'POST'])
@cross_origin()
def get_billing(target_id):
    return jsonify(billing.get_user_billing(target_id=target_id)), 200
