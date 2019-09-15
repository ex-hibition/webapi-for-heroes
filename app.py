from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from heroes import Heroes

hero = Blueprint('hero', __name__)

"""一覧を返す"""
@hero.route('/heroes', methods=['GET', ])
@cross_origin()
def get_heroes():
    return jsonify(heroes.get_heroes()), 200


"""名前を更新する"""
@hero.route('/heroes', methods=['PUT', ])
@cross_origin()
def update_hero():
    # 呼び出し元から引き渡されたjsonデータ
    data = request.json
    # データ更新
    heroes.update_hero(data)
    return jsonify(f"updated hero id={data.get('id')}"), 200


"""ヒーローを追加する"""
@hero.route('/heroes', methods=['POST'])
@cross_origin()
def add_hero():
    # 呼び出し元から引き渡されたjsonデータ
    data = request.json
    # データ追加
    result = heroes.add_hero(data)
    return jsonify(result), 200


"""id指定されたヒーローを返す"""
@hero.route('/heroes/<target_id>', methods=['GET', 'POST'])
@cross_origin()
def get_hero(target_id):
    return jsonify([x for x in heroes.get_heroes() if x['id'] == int(target_id)].pop()), 200


"""ヒーローを削除する"""
@hero.route('/heroes/<target_id>', methods=['DELETE'])
@cross_origin()
def delete_hero(target_id):
    heroes.delete_hero(int(target_id))
    return jsonify(f"deleted hero id={target_id}"), 200


"""ヒーローを検索する"""
@hero.route('/heroes/', methods=['GET'])
@cross_origin()
def search_hero():
    name = request.args.get('name')
    result = heroes.search_hero(name)
    return jsonify(result), 200


if __name__ == '__main__':
    heroes = Heroes()

    app = Flask(__name__)
    app.register_blueprint(hero, url_prefix='/angular')
    app.run(host='0.0.0.0', port=80, debug=True)
