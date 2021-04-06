from flask import Flask, jsonify, render_template, request
from index import index
import json

SEARCH_DIRECTORY = 'test_index_directory'
app = Flask(__name__)
index = index()
index.build(SEARCH_DIRECTORY)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html', file_path=request.args.get('path'))

@app.route('/search/files/<term>')
def searchfiles(term):
    return jsonify(index.search_files(term))

@app.route('/search/words/<term>')
def searchwords(term):
    return jsonify(index.search(term))

if __name__ == '__main__':
    app.run(debug=True, port=5000)