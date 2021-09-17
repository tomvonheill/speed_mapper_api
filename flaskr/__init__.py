import random
from flask import Flask, jsonify, abort
from .db import get_engine, get_db_config, read_sql

def create_app(test_config=None):
    app = Flask(__name__)
    engine = get_engine(get_db_config('speed_test'))

    def create_compliment(adjectives,noun):
        adjective_string = ', '.join(adjectives)
        return f"You are a {adjective_string} {noun}"

    @app.route('/get_all_data', methods = ['GET'])
    def get_all_data():
        query = read_sql('./flaskr/models/get_all.sql')
        result = engine.execute(query)
        results = [res._asdict() for res in result]
        return jsonify({'success':True,'results':results})
    return app

if __name__ == 'main':
    app = create_app()
    app.run()