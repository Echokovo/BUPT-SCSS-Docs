#include <iostream>
using namespace std;
class Point {
public:
    int x, y, z;
    Point(int x = 0, int y = 0, int z = 0) : x(x), y(y), z(z) {}
    Point operator+(const Point& P) const {
        return Point(x + P.x, y + P.y, z + P.z);
    }
    Point operator-(const Point& P) const {
        return Point(x - P.x, y - P.y, z - P.z);
    }
    Point& operator=(const Point& P) {
        if (this == &P) {
            return *this;
        }
        // 防止自我赋值
        x = P.x;
        y = P.y;
        z = P.z;
        return *this;
    }
    Point& operator++() {
        ++x;
        ++y;
        ++z;
        return *this;
    }
    Point operator++(int) {
        Point temp = *this;
        ++(*this);
        return temp;
    }
    Point& operator--() {
        --x;
        --y;
        --z;
        return *this;
    }
    Point operator--(int) {
        Point temp = *this;
        --(*this);
        return temp;
    }
    const int& operator[](int index) const {
        switch (index) {
        case 0: return x;
        case 1: return y;
        case 2: return z;
        default: cout << "Index out of range\n";return -1;
        //防止下标溢出
        }
    }
    void print() {
        cout << x << " " << y << " " << z << "\n";
    }
};

int main() {
    Point p1(1, 2, 3);
    Point p2(4, 5, 6);
    Point p3;
    p3 = p1 + p2;
    p3.print();
    p3 = p1 - p2;
    p3.print();
    p3 = p1;
    p3.print();
    ++p1;
    p1.print();
    p1++;
    p1.print();
    --p1;
    p1.print();
    p1--;
    p1.print();
    cout << "p1[0] = " << p1[0] << ", p1[1] = " << p1[1] << ", p1[2] = " << p1[2] << "\n";
    cout << "p1[-1] = " << p1[-1];
    return 0;
}
