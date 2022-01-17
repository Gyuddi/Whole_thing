//#include <iostream>
//#include <string>
//#include <ctime>
//#include <cstdlib>
//using namespace std;

//int main() {
//	string s1, add;
//	cout << "이름을 입력하시오: ";
//	cin >> s1;
//	cin.ignore();
//	
//	cout << "주소를 입력하시오: ";
//	getline(cin, add);
//	cout << add << "의" << s1 << "님 안녕하세요?" << endl;
//	return 0;
//
//}
//int main() {
//	string list[] = { "철수", "영희", "길동" };
//		for (auto & a:list){
//			cout << a + "야 안녕?" << endl;
//	}
//	return 0;
//}

//int main() {
//	string solution;
//	char ch;
//	string list[] = { "the", "apple", "programming","language"
//	};
//	srand(time(0));
//	int n = rand() % 4;
//	solution = list[n];
//	int length = solution.length();
//	string guess(length, '_' );
//	while (true) {
//		cout << guess << endl;
//		cin >> ch;
//		for (int a = 0; a < length; a++) {
//			if (solution[a] == ch) {
//				guess[a] = ch;
//			}
//		}
//		if (solution == guess) {
//			cout << solution << endl;
//			cout << "성공하셨습니다!";
//			break;
//		}
//	}
//	return 0;
//}
