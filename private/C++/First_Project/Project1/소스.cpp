#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;

int def() {
	int answer = 46;
	int sug;
	do {
		cout << "정답을 추측하여 보시오:";
		cin >> sug;
	} while (answer == sug); {
			if (answer > sug) {
				cout << "제시한 정수보다 큽니다";
			}
			else
			{
				cout << "제시한 정수보다 작습니다";
			}
	}
	cout << "정답입니다";
	return 0;
}