#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;



int main()
{
	srand(time(NULL);
	int dice1 = (rand() % 6) + 1;
	int dice2 = (rand() % 6) + 1;

	cout << "두 주사위 합=" << dice1 + dice2 << endl;
	return 0;
}
//main함수는 exe.를 통해 호출되고 main이 끝나면 프로그램 종류
