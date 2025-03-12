from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def caeser_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = CaesarCipher().encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = CaesarCipher().decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)