import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family='Microsoft YaHei')
if __name__ == '__main__':
    data_Beijing, data_Gansu = dict(), dict()
    with open('./chenji.html', 'r', encoding = 'utf-8') as f:
        data = re.findall(
            '<tr>\s*<td>\d\d\d\d</td>\s*<td>\w\w</td>\s*<td>\d\d\d</td>\s*<td>\d\d\d</td>\s*<td>\d\d\d</td>\s*<td>\d\d\d</td>\s*<td>\d\d\d</td>\s*</tr>',
            f.read())
        for d in data:
            for i in [' ', '\n', '<tr>', '</tr>', '<td>']:
                d = d.replace((i ), '')
            d = d.split('</td>')
            d[0] = int(d[0])
            if d[1] == '北京':
                data_Beijing[d[0]] = list()
                data_Beijing[d[0]].extend(int(d[i].strip()) for i in [2, 3, 4, 5, 6])
            else:
                data_Gansu[d[0]] = list()
                data_Gansu[d[0]].extend(int(d[i].strip()) for i in [2, 3, 4, 5, 6])
    # print(data_Beijing)
    # print(data_Gansu)
    s = ['最低分', '平均分', '最高分', '省控线']
    for i in range(4):
        x, y = list(), list()
        for k, v in data_Beijing.items():
            x.append(k)
            y.append(v[i])
        plt.plot(x, y, label = s[i])
    plt.legend()
    plt.title('北京')
    plt.grid(True)
    plt.show()
    for i in range(4):
        x, y = list(), list()
        for k, v in data_Gansu.items():
            x.append(k)
            y.append(v[i])
        plt.plot(x, y, label = s[i])
    plt.legend()
    plt.title('甘肃')
    plt.grid(True)
    plt.show()