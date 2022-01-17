#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <array>
#include<fstream>
using namespace std;
int main() {
	//ofstream os{ "numbers.txt" };
	//if (!os){
	//	cerr << "파일 오픈에 실패하였습니다" << endl;
	//	exit(1);
	//}
	//for (int i = 0; i < 100; i++)
	//	os << i << " ";
	ofstream os("numbers.txt", ios::app);
	if (!os) {
		cerr << "실패" << endl;
		exit(1);
	}
	os << "내가 추가했지롱" << endl;
	return 0;
}
