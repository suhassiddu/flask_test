import os
import psycopg2
from urllib import parse as urlparse
from flask import Flask, send_from_directory, request
from flask_cors import CORS
from flask_restful import Resource, Api 

db_url = urlparse.urlparse(os.environ.get('PGURL'))
auth = 'dbname={0} user={1} password={2} host={3}'.format(
        db_url.path[1:],
        db_url.username,
        db_url.password,
        db_url.hostname)
conn = psycopg2.connect(auth)
db = conn.cursor()
app = Flask(__name__, static_url_path='')
app._static_folder = 'public'
CORS(app)
api = Api(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')

class Banks(Resource):
    def get(self):
        return []
    def put(self):
        try:
            data = request.get_json(silent=True)
            db.execute('''
                select br.*
                from banks ba, branches br
                where ba.id = br.bank_id and
                lower(ba.name) = '{0}' and
                lower(br.city) = '{1}'; '''.format(
                    str(data['name']).lower(),
                    str(data['city']).lower()))
            rows = db.fetchall()
            rows = list(map(lambda r: {
                'ifsc': r[0],
                'branch': r[2],
                'address': r[3],
                'district': r[5],
                'state': r[6]}, rows))
            return rows
        except Exception as e:
            try:
                conn.rollback()
            except psycopg2.InterfaceError:
                pass
            print(e)
            return []
            
class Ifsc(Resource):
    def get(self, ifsc=''):
        try:
            db.execute('''
                select *
                from branches b
                where lower(b.ifsc) = '{}' '''.format(str(ifsc).lower()))
            r = db.fetchall()
            r = r[0]
            bank_id = r[1]
            r = {
                'branch': r[2],
                'address': r[3],
                'city': r[4],
                'district': r[5],
                'state': r[6]
            }
            db.execute('''
                select b.name
                from banks b
                where b.id = {} '''.format(bank_id))
            bank_name = db.fetchall()
            bank_name = bank_name[0][0]
            r['name'] = bank_name
            return r
        except Exception as e:
            try:
                conn.rollback()
            except psycopg2.InterfaceError:
                pass
            print(e)
            return {}

api.add_resource(Ifsc, '/ifsc/<string:ifsc>', '/ifsc/')
api.add_resource(Banks, '/banks/')

if __name__ == '__main__':
    app.run()
    conn.close()
