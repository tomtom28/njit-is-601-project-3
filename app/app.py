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


# API Endpoints are below...
# View all Players
@app.route('/api/v1/players', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblMlbPlayersImport')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


# View a single Player record by Id
@app.route('/api/v1/player/<int:player_id>', methods=['GET'])
def api_retrieve(player_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblMlbPlayersImport WHERE id=%s', player_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


# Add a New Player
@app.route('/api/v1/player', methods=['POST'])
def api_add() -> str:
    content = request.json
    cursor = mysql.get_db().cursor()
    input_data = (content['fld_Name'], content['fld_Team'],
                  content['fld_Position'], content['fld_Age'],
                  content['fld_Height_inches'], content['fld_Weight_lbs'])
    sql_insert_query = """INSERT INTO tblMlbPlayersImport (fld_Name,fld_Team,fld_Position,fld_Age,fld_Height_inches,fld_Weight_lbs) VALUES (%s, %s,%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, input_data)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


# Update an existing Player by Id
@app.route('/api/v1/player/<int:player_id>', methods=['PUT'])
def api_edit(player_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    input_data = (content['fld_Name'], content['fld_Team'],
                  content['fld_Position'], content['fld_Age'],
                  content['fld_Height_inches'], content['fld_Weight_lbs'], player_id)
    sql_update_query = """UPDATE tblMlbPlayersImport t SET t.fld_Name = %s, t.fld_Team = %s, t.fld_Position = 
        %s, t.fld_Age = %s, t.fld_Height_inches = %s, t.fld_Weight_lbs = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, input_data)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


# Delete an existing Player by Id
@app.route('/api/v1/player/<int:player_id>', methods=['DELETE'])
def api_delete(player_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblMlbPlayersImport WHERE id = %s """
    cursor.execute(sql_delete_query, player_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


# Jinga Template Views are below...
# Home Page - View all Players
@app.route('/', methods=['GET'])
def index():
    user = {'username': 'MLB Players Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblMlbPlayersImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, players=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)