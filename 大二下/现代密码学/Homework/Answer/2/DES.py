import binascii
 
class ArrangeSimpleDES():
    def __init__(self):
        self.noE_flag = 0
        self.noS_flag = 0
        self.noP_flag = 0
        # 出初始化DES加密的参数
        self.ip = [
            58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7,
        ]  # ip置换
 
        self.ip1 = [
            40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25,
        ]  # 逆ip置换
        self.E = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1,
        ]  # E置换，将32位明文置换位48位
        self.noE = [
            4,5,
            8,9,
            12,13,
            16,17,
            20,21,
            24,25,
            28,29,
            1,32
        ]
        self.P = [
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25,
        ]  # P置换，对经过S盒之后的数据再次进行置换
        # 设置默认密钥
        # self.K = '1010101100110100100001101001010011011001011100111010001011010011'
        self.K = '0001001100110100010101110111100110011011101111001101111111110001'
        self.k1 = [
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4,
        ]  # 密钥的K1初始置换
        self.k2 = [
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32,
        ]
 
        self.k0 = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, ]  # 秘钥循环移位的位数
 
        self.S = [
            [
                0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7,
                0x0, 0xf, 0x7, 0x4, 0xe, 0x2, 0xd, 0x1, 0xa, 0x6, 0xc, 0xb, 0x9, 0x5, 0x3, 0x8,
                0x4, 0x1, 0xe, 0x8, 0xd, 0x6, 0x2, 0xb, 0xf, 0xc, 0x9, 0x7, 0x3, 0xa, 0x5, 0x0,
                0xf, 0xc, 0x8, 0x2, 0x4, 0x9, 0x1, 0x7, 0x5, 0xb, 0x3, 0xe, 0xa, 0x0, 0x6, 0xd,
            ],
            [
                0xf, 0x1, 0x8, 0xe, 0x6, 0xb, 0x3, 0x4, 0x9, 0x7, 0x2, 0xd, 0xc, 0x0, 0x5, 0xa,
                0x3, 0xd, 0x4, 0x7, 0xf, 0x2, 0x8, 0xe, 0xc, 0x0, 0x1, 0xa, 0x6, 0x9, 0xb, 0x5,
                0x0, 0xe, 0x7, 0xb, 0xa, 0x4, 0xd, 0x1, 0x5, 0x8, 0xc, 0x6, 0x9, 0x3, 0x2, 0xf,
                0xd, 0x8, 0xa, 0x1, 0x3, 0xf, 0x4, 0x2, 0xb, 0x6, 0x7, 0xc, 0x0, 0x5, 0xe, 0x9,
            ],
            [
                0xa, 0x0, 0x9, 0xe, 0x6, 0x3, 0xf, 0x5, 0x1, 0xd, 0xc, 0x7, 0xb, 0x4, 0x2, 0x8,
                0xd, 0x7, 0x0, 0x9, 0x3, 0x4, 0x6, 0xa, 0x2, 0x8, 0x5, 0xe, 0xc, 0xb, 0xf, 0x1,
                0xd, 0x6, 0x4, 0x9, 0x8, 0xf, 0x3, 0x0, 0xb, 0x1, 0x2, 0xc, 0x5, 0xa, 0xe, 0x7,
                0x1, 0xa, 0xd, 0x0, 0x6, 0x9, 0x8, 0x7, 0x4, 0xf, 0xe, 0x3, 0xb, 0x5, 0x2, 0xc,
            ],
            [
                0x7, 0xd, 0xe, 0x3, 0x0, 0x6, 0x9, 0xa, 0x1, 0x2, 0x8, 0x5, 0xb, 0xc, 0x4, 0xf,
                0xd, 0x8, 0xb, 0x5, 0x6, 0xf, 0x0, 0x3, 0x4, 0x7, 0x2, 0xc, 0x1, 0xa, 0xe, 0x9,
                0xa, 0x6, 0x9, 0x0, 0xc, 0xb, 0x7, 0xd, 0xf, 0x1, 0x3, 0xe, 0x5, 0x2, 0x8, 0x4,
                0x3, 0xf, 0x0, 0x6, 0xa, 0x1, 0xd, 0x8, 0x9, 0x4, 0x5, 0xb, 0xc, 0x7, 0x2, 0xe,
            ],
            [
                0x2, 0xc, 0x4, 0x1, 0x7, 0xa, 0xb, 0x6, 0x8, 0x5, 0x3, 0xf, 0xd, 0x0, 0xe, 0x9,
                0xe, 0xb, 0x2, 0xc, 0x4, 0x7, 0xd, 0x1, 0x5, 0x0, 0xf, 0xa, 0x3, 0x9, 0x8, 0x6,
                0x4, 0x2, 0x1, 0xb, 0xa, 0xd, 0x7, 0x8, 0xf, 0x9, 0xc, 0x5, 0x6, 0x3, 0x0, 0xe,
                0xb, 0x8, 0xc, 0x7, 0x1, 0xe, 0x2, 0xd, 0x6, 0xf, 0x0, 0x9, 0xa, 0x4, 0x5, 0x3,
            ],
            [
                0xc, 0x1, 0xa, 0xf, 0x9, 0x2, 0x6, 0x8, 0x0, 0xd, 0x3, 0x4, 0xe, 0x7, 0x5, 0xb,
                0xa, 0xf, 0x4, 0x2, 0x7, 0xc, 0x9, 0x5, 0x6, 0x1, 0xd, 0xe, 0x0, 0xb, 0x3, 0x8,
                0x9, 0xe, 0xf, 0x5, 0x2, 0x8, 0xc, 0x3, 0x7, 0x0, 0x4, 0xa, 0x1, 0xd, 0xb, 0x6,
                0x4, 0x3, 0x2, 0xc, 0x9, 0x5, 0xf, 0xa, 0xb, 0xe, 0x1, 0x7, 0x6, 0x0, 0x8, 0xd,
            ],
            [
                0x4, 0xb, 0x2, 0xe, 0xf, 0x0, 0x8, 0xd, 0x3, 0xc, 0x9, 0x7, 0x5, 0xa, 0x6, 0x1,
                0xd, 0x0, 0xb, 0x7, 0x4, 0x9, 0x1, 0xa, 0xe, 0x3, 0x5, 0xc, 0x2, 0xf, 0x8, 0x6,
                0x1, 0x4, 0xb, 0xd, 0xc, 0x3, 0x7, 0xe, 0xa, 0xf, 0x6, 0x8, 0x0, 0x5, 0x9, 0x2,
                0x6, 0xb, 0xd, 0x8, 0x1, 0x4, 0xa, 0x7, 0x9, 0x5, 0x0, 0xf, 0xe, 0x2, 0x3, 0xc,
            ],
            [
                0xd, 0x2, 0x8, 0x4, 0x6, 0xf, 0xb, 0x1, 0xa, 0x9, 0x3, 0xe, 0x5, 0x0, 0xc, 0x7,
                0x1, 0xf, 0xd, 0x8, 0xa, 0x3, 0x7, 0x4, 0xc, 0x5, 0x6, 0xb, 0x0, 0xe, 0x9, 0x2,
                0x7, 0xb, 0x4, 0x1, 0x9, 0xc, 0xe, 0x2, 0x0, 0x6, 0xa, 0xd, 0xf, 0x3, 0x5, 0x8,
                0x2, 0x1, 0xe, 0x7, 0x4, 0xa, 0x8, 0xd, 0xf, 0xc, 0x9, 0x0, 0x3, 0x5, 0x6, 0xb,
            ],
        ]  # 16进制表示S盒的数据，S盒是为了将48位转换为32位，有8个盒子
 
    def __substitution(self, table: str, self_table: list) -> str:
        """
        :param table: 需要进行置换的列表,是一个01字符串
        :param self_table: 置换表，在__init__中初始化了
        :return: 返回置换后的01字符串
        """
        sub_result = ""
        for i in self_table:
            sub_result += table[i - 1]
        return sub_result

    def __substitution_noE(self, table: str, self_table: list) -> str:
        sub_result = ""
        for i in self_table:
            if i not in self.noE:
                sub_result += table[i - 1]
            else:
                sub_result += '0'
        return sub_result
 
    def str2bin(self, string: str) -> str:
        """
        将明文转为二进制字符串:
        :param string: 任意字符串
        :return:二进制字符串
        """
        plaintext_list = list(bytes(string, 'utf8'))  # 将字符串转成bytes类型，再转成list
        result = []  # 定义返回结果
        for num in plaintext_list:
            result.append(bin(num)[2:].zfill(8))  # 将列表的每个元素转成二进制字符串，8位宽度
        return "".join(result)
 
    def bin2str(self, binary: str) -> str:
        """
        二进制字符串转成字符串
        :param binary:
        :return:
        """
        list_bin = [binary[i:i + 8] for i in range(0, len(binary), 8)]  # 对二进制字符串进行切分，每8位为一组
        list_int = []
        for b in list_bin:
            list_int.append(int(b, 2))  # 对二进制转成int
        result = bytes(list_int).decode()  # 将列表转成bytes，在进行解码，得到字符串
        return result
 
    def __bin2int(self, binary: str) -> list:
        """
        由于加密之后的二进制无法直接转成字符，有不可见字符在，utf8可能无法解码，所以需要将二进制字符串每8位转成int型号列表，用于转成bytes再转hex
        :param binary: 二进制字符串
        :return: int型列表
        """
        list_bin = [binary[i:i + 8] for i in range(0, len(binary), 8)]  # 对二进制字符串进行切分，每8位为一组
        list_int = []
        for b in list_bin:
            list_int.append(int(b, 2))
        return list_int
 
    def __int2bin(self, list_int: list) -> str:
        result = []
        for num in list_int:
            result.append(bin(num)[2:].zfill(8))
        return ''.join(result)
 
    def __get_block_list(self, binary: str) -> list:
        """
        对明文二进制串进行切分，每64位为一块，DES加密以64位为一组进行加密的
        :type binary: 二进制串
        """
        len_binary = len(binary)
        if len_binary % 64 != 0:
            binary_block = binary + ("0" * (64 - (len_binary % 64)))
            return [binary_block[i:i + 64] for i in range(0, len(binary_block), 64)]
        else:
            return [binary[j:j + 64] for j in range(0, len(binary), 64)]
 
    def modify_secretkey(self):
        """
        修改默认密钥函数
        :return: None
        """
        print('当前二进制形式密钥为:{}'.format(self.K))
        print("当前字符串形式密钥为：{}".format(self.bin2str(self.K)))
        newkey = input("输入新的密钥（长度为8）：")
        if len(newkey) != 8:
            print("密钥长度不符合，请重新输入：")
            self.modify_secretkey()
        else:
            bin_key = self.str2bin(newkey)
            self.K = bin_key
            print("当前二进制形式密钥为:{}".format(self.K))
 
    def __f_funtion(self, right: str, key: str):
        """
        :param right: 明文二进制的字符串加密过程的右半段
        :param key: 当前轮数的密钥
        :return: 进行E扩展，与key异或操作，S盒操作后返回32位01字符串
        """
        # 对right进行E扩展
        if self.noE_flag == 1:
            e_result = self.__substitution_noE(right, self.E)
        else:
            e_result = self.__substitution(right, self.E)
        # 与key 进行异或操作
        xor_result = self.__xor_function(e_result, key)
        # 进入S盒子
        if self.noS_flag == 1:
            s_result = self.__s_box_noS(xor_result)
        else:
            s_result = self.__s_box(xor_result)
        # 进行P置换
        if self.noP_flag == 1:
            p_result = s_result
        else:
            p_result = self.__substitution(s_result, self.P)
        return p_result
 
    def __get_key_list(self):
        """
        :return: 返回加密过程中16轮的子密钥
        """
        key = self.__substitution(self.K, self.k1)
        left_key = key[0:28]
        right_key = key[28:56]
        keys = []
        for i in range(1, 17):
            move = self.k0[i - 1]
            move_left = left_key[move:28] + left_key[0:move]
            move_right = right_key[move:28] + right_key[0:move]
            left_key = move_left
            right_key = move_right
            move_key = left_key + right_key
            ki = self.__substitution(move_key, self.k2)
            keys.append(ki)
        return keys
 
    def __xor_function(self, xor1: str, xor2: str):
        """
        :param xor1: 01字符串
        :param xor2: 01字符串
        :return: 异或操作返回的结果
        """
        size = len(xor1)
        result = ""
        for i in range(0, size):
            result += '0' if xor1[i] == xor2[i] else '1'
        return result
 
    def __s_box(self, xor_result: str):
        """
        :param xor_result: 48位01字符串
        :return: 返回32位01字符串
        """
        result = ""
        for i in range(0, 8):
            # 将48位数据分为6组，循环进行
            block = xor_result[i * 6:(i + 1) * 6]
            line = int(block[0] + block[5], 2)
            colmn = int(block[1:5], 2)
            res = bin(self.S[i][line*16 + colmn])[2:]
            if len(res) < 4:
                res = '0' * (4 - len(res)) + res
            result += res
        return result
    
    def __s_box_noS(self, xor_result: str):
        """
        :param xor_result: 48位01字符串
        :return: 返回32位01字符串
        """
        result = ""
        for i in range(0, 8):
            # 将48位数据分为6组，循环进行
            block = xor_result[i * 6:(i + 1) * 6]
            result += block[1:5]
        return result
 
    def __iteration(self, bin_plaintext: str, key_list: list):
        """
        :param bin_plaintext: 01字符串，64位
        :param key_list: 密钥列表，共16个
        :return: 进行F函数以及和left异或操作之后的字符串
        """
        left = bin_plaintext[0:32]
        right = bin_plaintext[32:64]
        for i in range(0, 16):
            print(i, "\n", 'L:', left, "    R:", right, '\n')
            next_lift = right
            f_result = self.__f_funtion(right, key_list[i])
            next_right = self.__xor_function(left, f_result)
            left = next_lift
            right = next_right
        bin_plaintext_result = left + right
        return bin_plaintext_result[32:] + bin_plaintext_result[:32]
 
    def encode(self, plaintext):
        """
        :param plaintext: 明文字符串
        :return: 密文字符串
        """
        bin_plaintext_block = self.__get_block_list(plaintext)
        ciphertext_bin_list = []
        key_list = self.__get_key_list()
        for block in bin_plaintext_block:
            # 初代ip置换
            sub_ip = self.__substitution(block, self.ip)
            ite_result = self.__iteration(sub_ip, key_list)
            # 逆ip置换
            sub_ip1 = self.__substitution(ite_result, self.ip1)
            ciphertext_bin_list.append(sub_ip1)
        ciphertext_bin = ''.join(ciphertext_bin_list)
        return ciphertext_bin
 
    def decode(self, ciphertext):
        '''
        :param ciphertext: 密文字符串
        :return: 明文字符串
        '''
        bin_ciphertext = ciphertext
        bin_plaintext_list = []
        key_list = self.__get_key_list()
        key_list = key_list[::-1]
        bin_ciphertext_block = [bin_ciphertext[i:i + 64] for i in range(0, len(bin_ciphertext), 64)]
        for block in bin_ciphertext_block:
            sub_ip = self.__substitution(block, self.ip)
            ite = self.__iteration(sub_ip, key_list)
            sub_ip1 = self.__substitution(ite, self.ip1)
            bin_plaintext_list.append(sub_ip1)
        bin_plaintext = ''.join(bin_plaintext_list)
        return bin_plaintext
 
    def main(self):
        select = input("Please selecting:\n1、Encryption\t 2、Decrpytion\nYour selecting:")
        if select == '1':
            # plaintext = '1011100011010101101110000100001011010101001110011001010111100111'
            plaintext = '0000000100100011010001010110011110001001101010111100110111101111'
            # print("Your plaintext is:{}".format(plaintext))
            ciphertext = self.encode(plaintext)
            print("The ciphertext is:{}".format(ciphertext))
        elif select == '2':
            plaintext = input("Input ciphertext：")
            # print("Your ciphertext is:{}".format(plaintext))
            plaintext = self.decode(plaintext)
            print("The plaintext is:{}".format(plaintext))
            # print(len(plaintext))
        else:
            input("Please selecting again！")
            self.main()
 
 
if __name__ == '__main__':
    mydes = ArrangeSimpleDES()
    # mydes.noE_flag = 1
    # mydes.noS_flag = 1
    # mydes.noP_flag = 1
    while True:
        mydes.main()
        print("")