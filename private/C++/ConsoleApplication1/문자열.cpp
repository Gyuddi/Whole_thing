//#include <iostream>
//#include <string>
//#include <ctime>
//#include <cstdlib>
//using namespace std;

//int main() {
//	string s1, add;
//	cout << "�̸��� �Է��Ͻÿ�: ";
//	cin >> s1;
//	cin.ignore();
//	
//	cout << "�ּҸ� �Է��Ͻÿ�: ";
//	getline(cin, add);
//	cout << add << "��" << s1 << "�� �ȳ��ϼ���?" << endl;
//	return 0;
//
//}
//int main() {
//	string list[] = { "ö��", "����", "�浿" };
//		for (auto & a:list){
//			cout << a + "�� �ȳ�?" << endl;
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
//			cout << "�����ϼ̽��ϴ�!";
//			break;
//		}
//	}
//	return 0;
//}
