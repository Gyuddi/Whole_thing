//#include <iostream>
//#include <string>
//#include <ctime>
//#include <cstdlib>
//using namespace std;

//int main() {
//	const int student = 10;
//	int scores[student];
//	int sum = 0;
//	int i, average;
//	for (i = 0; i < student; i++) {
//		cout << "학생들의 성적을 입력하시오:" ;
//		cin >> scores[i];
//		sum += scores[i];
//	}
//	average = sum / student;
//	cout << "전체 평균: " << average;
//
//	return 0;
//}

//int main() {
//	int list[] = { 1,2,3,4,5,6,7,8,9,10 };
//	for (int& i : list) {
//		cout << i << " ";
//	}
//	for (int & i : list) {
//		i = i * 2;
//	}
//	for (int& i : list) {
//		cout << i << " ";
//	}
//	return 0;
//}

//int main() {
//	int list[100];
//	for (int i = 0; i < 100; i++) {
//		list[i] = rand() % 100 + 1;
//	}
//	int max = list[1];
//	for (int& i : list)
//		cout << i << endl;
//	
//	for (int& i : list) {
//		if (i > max) {
//			max = i;
//		}
//	}
//	cout << "가장 큰 수는" << max;
//	return 0;
//}

//#define WIDTH 3
//#define HEIGHT 9
//int main() {
//	int table[WIDTH][HEIGHT];
//	for (int a = 0; a < HEIGHT; a++) {
//		for (int b = 0; b < WIDTH; b++) {
//			table[a][b] = (a + 1) * (b + 1);
//		}
//	}
//	for (int a = 0; a < HEIGHT; a++) {
//		
//		for (int b = 0; b < WIDTH; b++) {
//			cout << table[a][b] << " ";
//		}
//		cout << endl;
//	}
//return 0;
//}
//
//int main() {
//	srand(time(NULL));
//	int i = rand() % 100;
//	cout << i;
//	return 0;
//}const Point& p