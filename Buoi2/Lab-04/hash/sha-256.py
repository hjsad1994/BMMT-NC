import hashlib

def calculate_sha256_hash(data):

    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def main():
    text = input("Nhập chuỗi văn bản: ")
    hashed_text = calculate_sha256_hash(text)
    
    print("Chuỗi văn bản đã nhập:", text)
    print("SHA-256 Hash:", hashed_text)

if __name__ == "__main__":
    main()