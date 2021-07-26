from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'mlbPlayersData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblMlbPlayersImport')
    result = cursor.fetchall()
    js = json.dumps(result)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


# API Endpoints are below...
@app.route('/api/v1/players', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblMlbPlayersImport')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/player/<int:player_id>', methods=['GET'])
def api_retrieve(player_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblMlbPlayersImport WHERE id=%s', player_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)