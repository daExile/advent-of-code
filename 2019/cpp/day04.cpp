#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Counter {
	int p1, p2;

	Counter() { p1 = 0; p2 = 0;	}

	Counter& inc(int code) { p1 += code & 1; p2 += (code >> 1) & 1; return *this; }
};

int check_number(int n) {
    int part1 = 0, prev_digit = 9, digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    while (n > 0) {
        int digit = n % 10;
        if (digit > prev_digit) return 0;
        prev_digit = digit;
        digits[digit]++;
        n /= 10;
    }

    for (int i: digits) {
        if (i == 2) return 3;
        if (i > 2) part1 = 1;
    };
    return part1;
}

int main() {
    string input;
    ifstream file("../__in/04.txt"); getline(file, input); file.close();

    int a = stoi(input.substr(0, 6)), b = stoi(input.substr(7));
    Counter c;

    for (int i = a; i <= b; i++) c.inc(check_number(i));
    cout << "Part 1: " << c.p1 << endl;
    cout << "Part 2: " << c.p2 << endl;
    return 0;
}
