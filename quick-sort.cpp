#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void quick_sort_of_array(int *arr, int first_border, int last_border){  // Или сортировка Тони Хоара
  
    //cout << "-----------------QUICK SORT STARTED------------" << endl;
    int f = first_border, l = last_border;  // первая и последняя границы будут нужны для перебора элементов в массиве
    int middle_element = arr[(f + l) / 2];  // Вычисление опирающегося элемента
    while (f < l){ // пока мы внутри границ массива
        while (arr[f] > middle_element){ // пока не дошли до опорного серединного элемента увеличиваем границу
            f++;
        }
        while (arr[l] < middle_element){ // пока не дошли до опорного серединного элемента уменьшаем правую границу
            l--;
        }
        if (f <= l){    
            int tmp = arr[f]; // перестановка элементов
            arr[f] = arr[l];
            arr[l] = tmp;
            f++;
            l--;
        }
    }  
    // Обратный вызов функции если массив не отсортирован
    if (first_border < l){
        quick_sort_of_array(arr, first_border, l);
    }
    if (f < last_border){
        quick_sort_of_array(arr, f, last_border);
    }
    //cout << "-----------------QUICK_SORT_COMPLETED----------" << endl;
}

int find_max(int *arr, int length_of_array){

    // Несмотря на то что самая быстрая сортировка, по времени занимает О(N*log(N)),  
    // самый быстрый способ найти максимальный элемент в неотсортированном массиве 
    // это пройтись линейно и затратить на это О(N) времени 
    
    int max = arr[0];  // пусть максимальным будет первый элемент
    for(int i= 1; i < length_of_array; i++){
        if (arr[i] > max){  // если найден больше поменяем максимальный эелемент
            max=arr[i];
        }
    }
    cout << "\nMaximum element of the array is: " << max << endl;
    return max;
}

int find_max_with_sort(int *arr, int length_of_array){

    quick_sort_of_array(arr, 0, length_of_array - 1);   // вызываем быструю сортировку

    int max = arr[0];  // пусть максимальным будет первый элемент

    cout << "\nMaximum element of the SORTED array is: " << max << endl;
    return max;
}


void print_array(int *arr, int length_of_array){
    cout << "\n-----------------PRINTED ARRAY--------------" << endl;
    for(int i = 0; i < length_of_array; i++){
        cout << arr[i] << "\t";  // Просто печатаем элементы массива
    }
    cout << endl;
}


int main() {
    int const N = 15;   // количество элементов в массиве
    
    srand(time(0));
    
    int arr[N]; 
    
    for(int i = 0; i < N; i++){
        arr[i] = rand()%20 + 1;  // Создаем массив с рандомными элементами
    }
    cout << "Before sort array" << endl;  // до сортировки печатаем
    print_array(arr, N);

    cout << "\nМаксимальныый элемент без сортировки c линейным поиском";  // до сортировки печатаем
    find_max(arr, N); 
    
    cout << "\nМаксимальныый элемент с сортировкой Тони Хоара";  // до сортировки печатаем

    find_max_with_sort(arr, N);
   
    return 0;
}
