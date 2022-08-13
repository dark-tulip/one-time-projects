import java.io.File;     
import java.io.IOException;
import java.util.Scanner;
 
class Main {
 
    public static void main(String[] args) {
         
        try { 
            Scanner sc = new Scanner(new File("text.txt"));    // Начинаем считывание файла со сканером
            int cnt = 1;  // Счетчик абзацев
            System.out.println("-------------------Печатаем содержимое файла-------------");
            
            while (sc.hasNext()) {     // Пока нету конца файла, то есть читается следующая строка
                String str = sc.nextLine();    // Считывание строки
                if (str.isEmpty()){   // Если строка пустая, начинается новый абзац либо заканчивается файл
                    cnt+=1;  // Увеличение счетчика на единицу
                    while(sc.hasNext() && str.isEmpty()){  // Если имеется следующая стока и эти строки лишние разделяющие абзац
                        System.out.println(str);   // Печатаем пустую стооку для полноценного вывода содержимого файла
                        str = sc.nextLine();   // Переходим к след строке
                    }
                }
                System.out.println(str);   
            } 

            System.out.println("-------------------Конец файла-------------");
            sc.close(); // Завершаем построчное сканирование
            System.out.println("Количесвто абзацев в файле " + cnt);

        } catch (IOException e) {  // В случае ошибки с файлом обработка исключений
            System.out.println("File not found!!!");
        }
    } 
}

/* 
Содержимое text.txt:

hello

world




good day)


Have fun
how are you?
*/
