#ifndef ENCRYPTION
#define ENCRYPTION
class Encryption {
private:
	std::string str;
public:
	Encryption();
	void output();
	void output_hex();
	friend Encryption operator+ (const Encryption&, const std::string&);
	friend Encryption operator- (const Encryption&, const std::string&);
	void operator= (const Encryption&);
	void operator= (const std::string&);
	char& operator[] (int i);
};
#endif