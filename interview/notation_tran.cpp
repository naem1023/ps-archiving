#include <string>
#include <iostream>

using namespace std;

void trans(string& ans, int n, int base) {
	if (n) {
		// recursion with new quotient
		trans(ans, n / base, base);

		// get remainder
		int rest = n % base;

		// If less than 9, express by number.
		if (rest <= 9)
			ans += (rest + '0');
		// If more than 9, expres by character.
		else ans += rest - 10 + 'A';
	}
}

int main() {
	int n, base;
    cin >> n >> base;
    string ans;

	trans(ans, n, base);
	
	cout << ans << endl;

	return 0;
}