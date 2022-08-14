#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int is_simple(int num){
    for (int i = 2; i <= (int)sqrt(num); i++){
        if (num % i == 0){
            return 0;
        }
    }
    return 1;

}

int main() {
    int cnt = 0; // Просто счетчик для красивого вывода
    cout << "\nВсе простые трехзначные числа: " << endl;
    for(int i = 100; i <= 999; i++){
        if(is_simple(i) == 1){
            cout << i <<" ";
            cnt++;
        }  
        if (cnt % 10 == 0){
            cout << endl;
            cnt+=1;
        }
    }   
}
