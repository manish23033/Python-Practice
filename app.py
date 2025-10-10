from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NUMVERIFY_API_KEY = 'a889542e45a509dd85a7fa5b0e7fbcb9'  # Replace with your real key

def get_phone_info(phone_number):
    url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone_number}&format=1"
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    info = None
    if request.method == 'POST':
        phone = request.form['phone']
        info = get_phone_info(phone)
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True)
