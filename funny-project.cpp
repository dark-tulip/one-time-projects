/* Заказ билетов в кинотеатре, старый добрый проект */

#include <iostream>

using namespace std;


int passwords = 12345;  // пароль
int price = 1000;   // начальная цена билета
string keys_sms = "Feed";   // пин код
int Cash_User = 5000; // деньги имеющиеся у пользователя
int key_sms_bank = 1234;

//movies
string aaa = "Одаренная", bbb = "Ход королевы", ccc = "Человек который познал вечность", ddd = "Число ПИ";
string a_films[4] = { aaa, bbb, ccc,ddd };

//times generation
int a_h = 1, a_m = 40, a_all = a_h * 60 + a_m;
int b_h = 2, b_m = 30, b_all = b_h * 60 + b_m;
int c_h = 1, c_m = 20, c_all = c_h * 60 + c_m;
int d_h = 1, d_m = 50, d_all = d_h * 60 + d_m;
int a_times[4] = { a_all, b_all, c_all, d_all };


//location
string a_l = "Almaty_Cinema", b_l = "Astana_Cinema", c_l = "City_Cinema", d_l = "Some_Cinema";
string a_location[4] = {a_l, b_l, c_l, d_l};


class User {   //класс

    public:   //специфакатор открытый доступ
        //конструктор с несколкими аргументами
        User(string n,string s,string f,string address, string mail) {
            //равнем аргументам и обрабатываем для работаты в классе
            fullname = f;
            surname = s;
            name = n;
            add = address;
            mails = mail;
        }
        // методы для обработки аргументов класса
        void log_password() {
            //массив для хранения параметров
            string a[3] = {name, surname, fullname};
            cout << "--------------------------------------------------------" << endl;
            //вывод аргументов полученного от класса
            cout << "Ваше имя: " << a[0] << ", фамилия: " << a[1] << ", отечество: " << a[2] << endl;
            cout << "Ваш логин: " << mails << endl;
            cout << "Ваш пароль: " << passwords << endl;
            cout << "--------------------------------------------------------" << endl;
        }

    private://закрытый доступ спецификатор
        //приватные переменные доступные только в классе и в наследованных классах от этого класса
        string name, surname, fullname;
        string* a;
        int b;
        string add,mails,AA;
};


class Movie {
    public:
        Movie(string movie_name, string location, int describ, int length_movie, char movietype, int DateTime_Minute, int DateTime_hours) {
            a = movie_name;
            b = location;
            c = describ;
            d = length_movie;
            Date = movietype;
            DateTime = DateTime_Minute;
            D_Hours = DateTime_hours;
        }
    private:
        string a, b;
        char Date;
        int DateTime,D_Hours,c, d;
};

// тут создаем очередь с рандомными значениями от 0 до 1 в промежутке от
// 0 до 30, мы передаем нужное место, и программа заполняет его, 1 или 0  (занято или сбоводно)
int queue(int a) {
    int queue[30];
    for (int i = 0; i < 30; i++)
        queue[i] = rand() % 2;
    return queue[a];
}

// этот метод провоцирует класс который принимает аргументы от методов как в классе
// если аргументы целочисленные, то исползваония классов нежелательно 
// если вместо аргументов имеются ссылки или объекты желательнее исползвать классы
void payments_system(int price_now, int summ,int new_select, string address, string name, string fam, string full, int aa) {
    // этот метод использует все аргументы и методы программы
    int a, b, c;
    string d;
    cout << "--------------------------------------------------------" << endl;
    cout << "Количество билетов:" << summ << endl;
    cout << "Цена за 1 билет:" << price << endl;
    cout << "Сумма билетов:" << summ * price << endl;
    cout << "--------------------------------------------------------" << endl;

    back:
    cout << "--------------------------------------------------------" << endl;
    cout << "Как вы хотите оплатить свой счет?:" << endl;
    cout << "1.Электронно:" << endl;
    cout << "2.Наличными:" << endl;
    cout << "введите число:";
    cin >> a;
    if (a == 1) {
        cout << "Ваш выбор электронно" << endl;
        cout << "--------------------------------------------------------" << endl;
        cout << "Было:" << Cash_User << endl;
        cout << "Остаток на счету:" << Cash_User - (summ * price) << endl;
        if (Cash_User < 0) {
            cout << "Недостаточно средтв, пожалуйста пополните ваш счет" << endl;
            bak:
            cout << "Введите сумму пополнения:";
            cin >> b;
            cout << "Было:" << Cash_User << endl;
            a_1:
            cout << "Введите пин код от смс:" << endl;
            cin >> c;
            if (c == key_sms_bank) {
                cout << "Авторизация успешна пройдена" << endl;
                a_2:
                cout << "Введите второй пин код" << endl;
                cin >> d;
                if (d == keys_sms) {
                    cout << "Данные верны, оплата успешно пройдена" << endl;
                }
                else {
                    cout << "Данные не верны, введите снова:" << endl;
                    goto a_2;
                    cout << "--------------------------------------------------------" << endl;
                }
            }
            else {
                cout << "Данные не верны, занова введите данные " << endl;
                goto a_1;
                cout << "--------------------------------------------------------" << endl;
            }
            cout << "После пополнения:" << Cash_User + b << endl;
            cout << "После оплаты:" << (Cash_User + b) - (summ * price) << endl;
            if (Cash_User < 0) {
                cout << "Недостаточно средств, пожалуйста пополните ваш счет!" << endl;
                cout << "--------------------------------------------------------" << endl;
                goto bak;
            }
        }
    } else {
        cout << "Ваш выбор наличными" << endl;
        cout << "--------------------------------------------------------" << endl;
        cout << "Было:" << Cash_User << endl;
        cout << "Осталось на счету:" << Cash_User - (summ * price) << endl;
        cout << "--------------------------------------------------------" << endl;
        if (Cash_User < 0) {
            cout << "Недостаточно наличных средств, оплатите электронно" << endl;
            cout << "--------------------------------------------------------" << endl;
            goto back;
        }
    }

    cout << "Сумма:" << summ * price << endl;

    if (summ * price > 5000)
        cout << "Вы потратили болше 5 000тг, вам присвоен статус постоянный клиент" << endl;
    else if(summ * price > 15000 && summ * price > 5000)
        cout << "Вы потратили больше 15 000тг, вам присвоен статус золотой киноман" << endl;
    else if(summ * price > 0){
        cout << "Ваш статус гость" << endl;
    }

    cout << "Ваши данные: " << endl;
    cout << "Адрес: " << address << endl;
    cout << "Логин: " << name << endl;
    cout << "Полное имя ползователя: " << full << " "<< fam << " " << full << endl;
    cout << "Фильм: " << a_films[new_select - 1] << endl;
    cout << "Время: " << a_times[new_select - 1] << endl;
    cout << "Локация: " << a_location[new_select-1] << endl;
    cout << "Ряд: " << aa / 10<< ", и место: " << aa << endl;
    cout << "Статус: куплен и занято " << endl;
}

// Вместо создания класса Class Gustomers мы исползвоали метод и передали все нужные аргументы
void tickets_1_Gustomers(int a,int new_select,string address,string name,string surname,string full) {
    k:
    int b, summ = 0, aa;
    cout << "Места кинозала, 1 занято, 0 свободные, выберете места" << endl;
    for (int i = 0; i < 30; i++) {
        cout << "N" << i << ":" << queue(i) << ", ";
        if (i == 9 || i == 19){
            cout << endl;
        }
    }
    cout << endl;
    cin >> aa;
    for (int j; j < a; j++) {
        queue(aa);
        if (queue(aa) == 1) {
            cout << "Это место занято: " << endl;
            goto k;
        }
        summ = summ + a;
    }
    if (aa <= 10) {
        cout << "Передние ряды дороже 0-10:" << endl;
        price = price * 1.2;
        payments_system(price, summ, new_select, address, name, surname, full,aa);
    }
    else if (aa <= 20) {
        cout << "Стандартная сумма билетов 10-20:" << endl;
        price = price * 1;
        payments_system(price, summ, new_select, address, name, surname, full,aa);
    }
    else {
        cout << "Скидна на задние ряды -20% от стоимости билета:" << endl;
        price = price * 0.8;
        payments_system(price, summ, new_select, address, name, surname, full,aa);
    }
}


void tickets(int new_select, string address, string name, string fam, string full) {
    b:
    int a;
    cout << "Сколько билетов вы хотите купить? введите число:" << endl;
    cin >> a;
    if (a > 5) {
        cout << "Нельзя купить более 5 билетов одновременно!" << endl;
        goto b;
    }
    tickets_1_Gustomers(a, new_select, address, name, fam, full);
}


void searsh(int select,string address,string name,string fam,string full) {
    int new_select;
    switch (select) {
        case 1:
            l:
            for (int i = 0; i < 4; i++) {
                cout << "Фильм:" << a_films[i] << endl;
            }
            cout << "Введите названия фильма одну из заданных по номеру:" << endl;
            cin >> new_select;
            if (new_select == 1) {
                cout << "Фильм:"<<a_films[1-1]<<endl;
            }
            else if (new_select == 2) {
                cout << "Фильм:" << a_films[2 - 1] << endl;
            }
            else if (new_select == 3) {
                cout << "Фильм:" << a_films[3 - 1] << endl;
            }
            else {
                cout << "Фильм:" << a_films[4 - 1] << endl;
            }
            tickets(new_select,address,name,fam,full);
            break;
        case 2:
            for (int i = 0; i < 4; i++) {
                cout << "Длительность фильма:" << a_times[i] << endl;
            }
            cout << "Введите длителность фильма:" << endl;
            cin >> new_select;
            if (new_select == 1) {
                cout << "Фильм: " << a_films[1 - 1] << ", Тайминг: " << a_times[new_select - 1] << endl;
            }
            else if (new_select == 2) {
                cout << "Фильм: " << a_films[2 - 1] << ", Тайминг: " << a_times[new_select - 1] << endl;
            }
            else if (new_select == 3) {
                cout << "Фильм: " << a_films[3 - 1] << ", Тайминг: " << a_times[new_select - 1] << endl;
            }
            else {
                cout << "Фильм: " << a_films[4 - 1] << ", Тайминг: " << a_times[4 - 1] << endl;
            }
            tickets(new_select, address, name, fam, full);
            break;
        case 3:
            for (int i = 0; i < 4; i++) {
                cout << "Адреса фильмов полное имя: " << a_films[i] << endl;
            }
            cout << "Введите полное имя кино театра одну из заданных по номеру:" << endl;
            cin >> new_select;
            if (new_select == 1) {
                cout << "Фильм:" << a_films[1 - 1] << ", Названия кинотеатра:"<< a_location[new_select -1]<< endl;
            }
            else if (new_select == 2) {
                cout << "Фильм:" << a_films[2 - 1] << ", Названия кинотеатра:" << a_location[new_select - 1] << endl;
            }
            else if (new_select == 3) {
                cout << "Фильм:" << a_films[3 - 1] << ", Названия кинотеатра:" << a_location[new_select - 1] << endl;
            }
            else {
                cout << "Фильм:" << a_films[4 - 1] << ", Названия кинотеатра:" << a_location[4 - 1] << endl;
            }
            tickets(new_select, address, name, fam, full);
            break;
        default:
            cout << "Вы ввели ошибочную данные будет выбрано значения первое" << endl;
            cout << "--------------------------------------------------------" << endl;
            goto l;
    
    }

    int aa, bb;

    Movie a(aaa, a_l, 3, 120, 'G', a_h, a_m);
    Movie b(bbb, b_l, 2, 110, 'H', b_h, b_m);
    Movie c(ccc, c_l, 3, 90, 'B', c_h, c_m);
    Movie d(ddd, d_l, 1, 150, 'A', d_h, d_m);
}


void print_1(string b, string address, string name, string fam, string full) {
    // метод печати регистрации
    s:
    string b_0;
    int a_0, select;
    cout << "--------------------------------------------------------" << endl;
    cout << "Для входа в систему входите логин и пароль" << endl;
    cout << "Login: ";
    cin >> b_0;
    cout << "Password: ";
    cin >> a_0;
    if (a_0 != passwords || b_0 != b) {
        cout << "Вы ввели неверные данные" << endl;
        // вынужденный переход goto
        goto s;
    }

    cout << "Имеющиеся данные:" << endl;
    for (int i = 0; i < 4; i++) {
        cout << "Фильм: " << a_films[i] << ", Длительность: " << a_times[i] << ", Локация: " << a_location[i] << endl;
    }

    cout << "--------------------------------------------------------" << endl;
    cout << "Введите по каким критериям хотите ввести поиск:(выберите одну)" << endl;
    cout << "1.По названию" << endl;
    cout << "2.По длителности фильма" << endl;
    cout << "3.По адресу" << endl;
    cout << "Select: ";
    cin >> select;
    cout << "--------------------------------------------------------" << endl;
    searsh(select, address, name, fam, full);

}


void print_0(){
    // переменные для хранения данных о клиенте
    string a, b, c, d, e;
    int a_0;
    cout << "--------------------------------------------------------" << endl;
    cout << "Введите ваш адрес: " << endl;
    cin >> a;
    cout << "Введите почту: " << endl;
    cin >> b;
    cout << "Введите телефоный номер: " << endl;
    cin >> a_0;
    cout << "Введите ваше ФИО: " << endl;
    cout << "имя: " << endl;
    cin >> c;
    cout << "фамилия: " << endl;
    cin >> d;
    cout << "отечество: " << endl;
    cin >> e;
    cout << "--------------------------------------------------------" << endl;
    // передаем занчения классу о клиенте
    User s(c, d, e, a, b);
    // вызываем метод регистрации
    s.log_password();
    print_1(b, a, c, d, e);
}


int main()
{
    setlocale(LC_ALL, "Russian");

    print_0();

    cout << "\nДля продажи доступны сеансы, до начала которых остаётся не менее чем 30 минут" << endl;
    cout << "По истечении 1 недели с даты, указанной в билете, данные о нём автоматически удаляются из системы" << endl;
    cout << "-----------------------Удачного просмотра!----------------------------";
    return 0;
  
}
/* P.S. тут есть ошибки */
