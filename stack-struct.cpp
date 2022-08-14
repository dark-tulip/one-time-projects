#include <iostream>

using namespace std;

struct Stack{
    int head;
    Stack * next;
};

void print_stack(Stack *s) {
    cout << "Элементы стека: ";
    while (s) {  // пока есть элементы печатаем их
        cout << s -> head << "  ";
        s = s -> next;
    }
}

void count(Stack *s){
    Stack *stck;
    int cnt = 0;
    while (s) { 
        s = s -> next;
        cnt++;
    }
    cout << "\nКоличество элементов в стеке " << cnt;
}

void push(Stack *&s, int elem) {
    Stack *new_st = new Stack;
    new_st -> head = elem;
    new_st -> next = s;
    s = new_st;
    cout << "Число " << elem << " добавили в стек " << endl;

}


int main() {
    srand(time(0));
    setlocale(LC_ALL, "ru");
    Stack *stck;  // Cоздаем новый объект стека
    push(stck, 20);
    push(stck, 13);
    push(stck, 1);
    push(stck, 133);
    print_stack(stck);
    count(stck);
}
