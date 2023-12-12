#include <iostream>
#include <fstream>
using namespace std;

int fuel_extra(int mass) {
	int extra = mass / 3 - 2;

	if (extra > 0) return extra + fuel_extra(extra);
	return 0;
}

int main() {
	ifstream file ("../__in/01.txt");
	int mass, fuel_modules = 0, fuel_total = 0;

	while (file >> mass)
	{
		int fuel = mass / 3 - 2;
		fuel_modules += fuel;
		fuel_total += fuel + fuel_extra(fuel);
	}

	cout << "Part 1: " << fuel_modules << endl;
	cout << "Part 2: " << fuel_total << endl;
	return 0;
}
