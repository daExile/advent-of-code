#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
using namespace std;

int intcode_run(vector<int> code, int noun, int verb) {
	code[1] = noun; code[2] = verb;
	int ptr = 0;

	while (code[ptr] != 99) {
		switch (code[ptr]) {
			case 1:	code[code[ptr + 3]] = code[code[ptr + 1]] + code[code[ptr + 2]]; break;
			case 2:	code[code[ptr + 3]] = code[code[ptr + 1]] * code[code[ptr + 2]]; break;
		}
		ptr += 4;
	}
	return code[0];
}

int main() {
	ifstream file ("../__in/02.txt");
	string input;
	vector<int> code;
	getline(file, input);

	regex integer ("(-?[0-9]+)");
	sregex_iterator iter = sregex_iterator(input.begin(), input.end(), integer);

	while (iter != sregex_iterator()) {
	    code.push_back(stoi(iter -> str()));
	    ++iter;
	}
	cout << "Part 1: " << intcode_run(code, 12, 2) << endl;

	int noun, verb;
	for (noun = 0; noun < 100; noun++) {
		for (verb = 0; verb < 100; verb++) {
			if (intcode_run(code, noun, verb) == 19690720) goto quits;
		}
	}
quits:
	cout << "Part 2: " << noun * 100 + verb << endl;
	return 0;
}
