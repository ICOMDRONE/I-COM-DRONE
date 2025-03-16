from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        subprocess.run(['bash', 'deploy.sh'])
        return 'Güncelleme başladı!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

