#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <map>
#include <algorithm>
using namespace std;

struct Point {
	int x, y;

	Point(int x, int y) { this -> x = x; this -> y = y;	}

	bool operator<(const Point& other) const { return (x < other.x || (x == other.x && y < other.y)); }
};

Point get_dir(char c) {
	switch (c) {
		case 'U': return Point(0, 1); break;
		case 'D': return Point(0, -1); break;
		case 'L': return Point(-1, 0); break;
		case 'R': return Point(1, 0); break;
	}
	return Point(0, 0);
}

Point operator+(Point a, Point b) {	return Point(a.x + b.x, a.y + b.y); }

map<Point, int> parse_input(string input) {
	map<Point, int> out;
	Point p = Point(0, 0);
	int step = 0;

	regex segment ("([UDLR][0-9]+)");
	sregex_iterator iter = sregex_iterator(input.begin(), input.end(), segment);
	while (iter != sregex_iterator()) {
		string t = iter -> str();
		Point dir = get_dir(t[0]);
		for (int i = 1; i <= stoi(t.substr(1)); i++) {
			++step;
			p = p + dir;
			out.emplace(p, step);
		}
	    ++iter;
	}

	return out;
}

int main() {
	ifstream file ("../__in/03.txt");
	string line;
	map<Point, int> wire1, wire2;
	vector<Point> keys1, keys2, match;
	vector<int> manhattan, steps;

	getline(file, line);
	wire1 = parse_input(line);

	getline(file, line);
	wire2 = parse_input(line);

	transform(wire1.begin(), wire1.end(), back_inserter(keys1), [](const pair<Point, int> &item){ return item.first; });
	transform(wire2.begin(), wire2.end(), back_inserter(keys2), [](const pair<Point, int> &item){ return item.first; });
	set_intersection(keys1.begin(), keys1.end(), keys2.begin(), keys2.end(), back_inserter(match));

	transform(match.begin(), match.end(), back_inserter(manhattan), [](const Point &item){ return abs(item.x) + abs(item.y); });
	transform(match.begin(), match.end(), back_inserter(steps), [&wire1, &wire2](const Point &item){ return wire1[item] + wire2[item]; });
	cout << "Part 1: " << *min_element(manhattan.begin(), manhattan.end()) << endl;
	cout << "Part 2: " << *min_element(steps.begin(), steps.end()) << endl;
	return 0;
}
