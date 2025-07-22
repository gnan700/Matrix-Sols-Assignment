from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import string, random, qrcode
from io import BytesIO
import base64

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(20), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not URLMap.query.filter_by(short_code=code).first():
            return code

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url')
        custom_code = request.form.get('custom_code', '').strip()

        if not original_url:
            return render_template('index.html', error="Please enter a valid URL.")

        if custom_code:
            if not custom_code.isalnum():
                return render_template('index.html', error="Custom code must be alphanumeric.")
            if URLMap.query.filter_by(short_code=custom_code).first():
                return render_template('index.html', error="Custom code already taken.")
            short_code = custom_code
        else:
            short_code = generate_short_code()

        existing = URLMap.query.filter_by(original_url=original_url).first()
        if existing and not custom_code:
            short_code = existing.short_code
        else:
            new_map = URLMap(original_url=original_url, short_code=short_code)
            db.session.add(new_map)
            db.session.commit()

        short_url = request.host_url + short_code
        qr_img = qrcode.make(short_url)
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()

        return render_template('index.html', short_url=short_url, qr_code=qr_code)

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_map = URLMap.query.filter_by(short_code=short_code).first()
    if url_map:
        url_map.visits += 1
        db.session.commit()
        return redirect(url_map.original_url)
    return "Invalid short URL.", 404

@app.route('/analytics')
def analytics():
    urls = URLMap.query.all()
    return render_template('analytics.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
