from app import app
from flask import jsonify, render_template, flash, redirect, url_for, make_response, abort, request
import yaml
from yaml import load, dump, Loader
import json

user = None
stream = None
url = 'http://127.0.0.1:5000/'


def Load():
    global user, stream
    stream = open('app/db/user.yaml', 'r')
    user = yaml.load(stream, Loader=yaml.FullLoader)
    stream.close()


def Save():
    global user, stream
    stream = open('app/db/user.yaml', 'w')
    stream.write(yaml.dump(user, default_flow_style=False))
    stream.close()


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@app.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': 'Conflict'}), 409)


@app.route('/')
@app.route('/index')
def index():
    return make_response(render_template('index.html', title='Glowna'), 200)


@app.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    global user
    try:
        Load()
        return jsonify({id: json.dumps(user['user'][id])}), 200
    except KeyError:
        abort(400)


@app.route('/user/<string:id>', methods=['POST'])
def add_user(id):
    global user
    if not request.json:
        abort(400)
    else:
        Load()
        d = dict(**{'user': {id: request.json}})
        x = user
        for a in d['user']:
            x['user'].update({a: d['user'][a]})
        user = x
        Save()
        return make_response(jsonify({'url': url + 'user/'+id}), 201)


@app.route('/user/<string:id>', methods=['DELETE'])
def delete_user(id):
    try:
        Load()
        del user['user'][id]
        return make_response(' ', 204)
    except KeyError:
        return abort(409)




