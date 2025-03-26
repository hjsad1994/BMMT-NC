import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BTN_GENERATE.clicked.connect(self.call_api_gen_keys)
        self.ui.BTN_ENCRYPT.clicked.connect(self.call_api_encrypt)
        self.ui.BTN_DECRYPT.clicked.connect(self.call_api_decrypt)
        self.ui.BTN_SIGN.clicked.connect(self.call_api_sign)
        self.ui.BTN_VERIFY.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5001/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
                
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5001/api/rsa/encrypt"
        payload = {
            "message": self.ui.TXT_PLAINTEXT.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.TXT_CIPHERTEXT.setText(data["encrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5001/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.TXT_CIPHERTEXT.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.TXT_PLAINTEXT.setText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5001/api/rsa/sign"
        payload = {
            "message": self.ui.TXT_INFORMATION.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.TXT_SIGNATURE.setText(data["signature"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5001/api/rsa/verify"
        payload = {
            "message": self.ui.TXT_INFORMATION.toPlainText(),
            "signature": self.ui.TXT_SIGNATURE.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                if data["is_verified"]:
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verified Fail")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())