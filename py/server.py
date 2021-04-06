from flask import Flask, jsonify, render_template, request
from index import index
import json, os

SEARCH_DIRECTORY = 'test_index_directory'
app = Flask(__name__)
index = index()
index.build(SEARCH_DIRECTORY)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    file_path = request.args.get('file')
    file_name = os.path.basename(file_path)
    search_term = request.args.get('term')
    with open(file_path) as f:
        file_contents = ''.join(f.readlines())
    return render_template('info.html', file_path=file_path, file_name=file_name, file_contents=file_contents, search_term=search_term)

@app.route('/search/files/<term>')
def searchfiles(term):
    return jsonify(index.search_files(term))

@app.route('/search/words/<term>')
def searchwords(term):
    return jsonify(index.search(term))

if __name__ == '__main__':
    app.run(debug=True, port=5000)