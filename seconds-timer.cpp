#include <iostream>
#include <unistd.h> // для usleep

int main() {
  
    using namespace std;
  
    cout << "\n---Программа таймер времени---\n";
    int hours = 0, minutes = 0, secunds = 0;
    cout<<"Для завершения работы программы нажмите CTRL+C \n\n";
    int need;
    cout << "Введите количество секунд таймера: ";
    cin >> need;

    for(int i = 0; i < need; i++){
        // форматированный вывод
        printf("%.2d:%.2d:%.2d\n", hours, minutes, secunds);
        if(secunds > 59){
            secunds = 0;
            minutes++;
        }
        if(minutes > 59){
            minutes = 0;
            hours++;
        }
        if(hours >= 23){
            hours = 0;
        }
        // usleep работает для 0.001 мс, значение 1 000 000 занчит 1 сек 
        usleep(1000000);
        // Цикл работает 1 раз в секунду
        secunds++;
    }
    cout << "Время вышло!" << endl;
}
