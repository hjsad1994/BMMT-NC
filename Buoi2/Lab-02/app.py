from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher 

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for Caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('caesar_result.html', text=text, key=key, encrypted_text=encrypted_text)
#    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Router routes for Playfair cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    
    encrypted_text = playfair.playfair_encrypt(plain_text, matrix)
    return f"Plain text: {plain_text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    
    decrypted_text = playfair.playfair_decrypt(cipher_text, matrix)
    return f"Cipher text: {cipher_text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

# Router routes for Vigenère cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    
    encrypted_text = vigenere.vigenere_encrypt(plain_text, key)
    return f"Plain text: {plain_text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    
    decrypted_text = vigenere.vigenere_decrypt(cipher_text, key)
    return f"Cipher text: {cipher_text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

# Router routes for Rail Fence cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    plain_text = request.form['inputPlainText']
    num_rails = int(request.form['inputNumRails'])
    railfence = RailFenceCipher()
    
    encrypted_text = railfence.rail_fence_encrypt(plain_text, num_rails)
    return f"Plain text: {plain_text}<br>Number of rails: {num_rails}<br>Encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    cipher_text = request.form['inputCipherText']
    num_rails = int(request.form['inputNumRailsDecrypt'])
    railfence = RailFenceCipher()
    
    decrypted_text = railfence.rail_fence_decrypt(cipher_text, num_rails)
    return f"Cipher text: {cipher_text}<br>Number of rails: {num_rails}<br>Decrypted text: {decrypted_text}"

# Router routes for Transposition cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    transposition = TranspositionCipher()
    
    encrypted_text = transposition.encrypt(plain_text, key)
    return f"Plain text: {plain_text}<br>Key: {key}<br>Encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyDecrypt'])
    transposition = TranspositionCipher()
    
    decrypted_text = transposition.decrypt(cipher_text, key)
    return f"Cipher text: {cipher_text}<br>Key: {key}<br>Decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
