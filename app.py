from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load Quran data
with open('quran_data/quran.json', 'r', encoding='utf-8') as f:
    quran = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', quran=quran)

@app.route('/surah/<int:surah_id>')
def surah(surah_id):
    surah_data = quran[str(surah_id)]
    return render_template('surah.html', surah=surah_data, surah_id=surah_id)

if __name__ == '__main__':
    app.run(debug=True)
