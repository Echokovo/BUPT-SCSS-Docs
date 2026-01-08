#include <iostream>
#include <string>
class Encryption {
public:
    Encryption(char key) : key(key) {}
    virtual std::string encrypt(const std::string& plaintext) = 0;
    virtual std::string decrypt(const std::string& ciphertext) = 0;
    virtual void display() const = 0;
    virtual ~Encryption() = default;
protected:
    std::string plaintext;
    std::string ciphertext;
    char key;
};
class XORPublic : public Encryption {
public:
    XORPublic(char key) : Encryption(key) {}
    std::string encrypt(const std::string& plaintext) override {
        this->plaintext = plaintext;
        this->ciphertext = plaintext;
        for (char& c : this->ciphertext) {
            c ^= key;
        }
        return this->ciphertext;
    }
    std::string decrypt(const std::string& ciphertext) override {
        return encrypt(ciphertext);
    }
    // 异或运算的对称性
    void display() const override {
        std::cout << "Public XOR Encryption Class" << "\n";
    }
};
class XORPrivate : private Encryption {
public:
    XORPrivate(char key) : Encryption(key) {}
    std::string encrypt(const std::string& plaintext) {
        this->plaintext = plaintext;
        this->ciphertext = plaintext;
        for (char& c : this->ciphertext) {
            c ^= key;
        }
        return this->ciphertext;
    }
    std::string decrypt(const std::string& ciphertext) {
        return encrypt(ciphertext);
    }
    // 异或运算的对称性
    void display() const {
        std::cout << "Private XOR Encryption Class" << "\n";
    }
    Encryption* getBasePointer() {
        return this;
    }
    // 提供基类指针访问的方法
};
int main() {
    XORPublic publicXor('k');
    XORPrivate privateXor('k');


    std::string plaintext = "Hello World",encrypted,decrypted;
    encrypted = publicXor.encrypt(plaintext);
    decrypted = publicXor.decrypt(encrypted);
    std::cout << "Public Derived XOR Encryption:" << "\n";
    publicXor.display();
    std::cout << "Plaintext: " << plaintext << "\n";
    std::cout << "Encrypted: " << encrypted << "\n";
    std::cout << "Decrypted: " << decrypted << "\n" << "\n";
    Encryption* basePtrPublic = &publicXor;
    // 公有派生类可直接调用
    encrypted = basePtrPublic->encrypt(plaintext);
    decrypted = basePtrPublic->decrypt(encrypted);
    std::cout << "Accessing Public Derived XOR Encryption via Base Pointer:" << "\n";
    basePtrPublic->display();
    std::cout << "Plaintext: " << plaintext << "\n";
    std::cout << "Encrypted: " << encrypted << "\n";
    std::cout << "Decrypted: " << decrypted << "\n" << "\n";


    encrypted = privateXor.encrypt(plaintext);
    decrypted = privateXor.decrypt(encrypted);
    std::cout << "Private Derived XOR Encryption:" << "\n";
    privateXor.display();
    std::cout << "Plaintext: " << plaintext << "\n";
    std::cout << "Encrypted: " << encrypted << "\n";
    std::cout << "Decrypted: " << decrypted << "\n" << "\n";
    Encryption* basePtrPrivate = privateXor.getBasePointer();
    // 通过基类指针调用私有派生类对象的方法
    encrypted = basePtrPrivate->encrypt(plaintext);
    decrypted = basePtrPrivate->decrypt(encrypted);
    std::cout << "Accessing Private Derived XOR Encryption via Base Pointer:" << "\n";
    basePtrPrivate->display();
    std::cout << "Plaintext: " << plaintext << "\n";
    std::cout << "Encrypted: " << encrypted << "\n";
    std::cout << "Decrypted: " << decrypted << "\n";


    return 0;
}