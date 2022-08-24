import java.util.Scanner;

class CeaserCipher {
    // келесі функция символды динамикалык жиымга косу ушин колданылады
    public static char[] append_char_to_array(char arr[], char ch) 
    { 
        int size_of_array = arr.length;

        char newarr[] = new char[size_of_array + 1]; 
  
        for (int i = 0; i < size_of_array; i++) 
            newarr[i] = arr[i]; 
  
        newarr[size_of_array] = ch; 
  
        return newarr; 
    } 
    // Келесі функция акпаратты кери шифрлау ушин колданылады
    public static String decrypt_text(String encrypted_text, int key)
    {
        System.out.println("\n\n------------STARTED TEXT DECRYPTION------------\n");
        String result = "";  // кери шифрланган текст осы жолгажазылады

        char text_symbols[] = encrypted_text.toCharArray(); // кери шифрлауга кажет текст осы символдык жиымга жазылады

        char decrypted_text[] = {}; // кери шифрланган текст осы символдык жиымга жазылады

        for (char ch : text_symbols){ // символ бойынша жолды окимыз
            
            char now_ch = ch; 
       
            if (now_ch >= 'A' && now_ch <='Z'){  // Агылшын бас ариптери бойынша
                now_ch = (char)(ch - key);
                if(now_ch < 'A'){
                    now_ch = (char)(now_ch + 'Z' - 'A' + 1);
                }
            } 
            else if (now_ch >= 'a' && now_ch <='z'){ // Агылшын кіші ариптери бойынша
                now_ch = (char)(ch - key);
                if(now_ch < 'a'){
                    now_ch = (char)(now_ch + 'z' - 'a' + 1);
                }
            } 

            else if (now_ch >= 'А' && now_ch <='Я'){ // Орыс бас ариптери бойынша
                now_ch = (char)(ch - key);
                if(now_ch < 'А'){
                    now_ch = (char)(now_ch + 'Я' - 'А' + 1);
                }
            }
            else if (now_ch >= 'а' && now_ch <='я'){ // Орыс кіші ариптери бойынша
                now_ch = (char)(ch - key);
                if(now_ch < 'а'){
                    now_ch = (char)(now_ch + 'я' - 'а' + 1);
                }
            }
            else {
                now_ch = ch;
            }

            decrypted_text = append_char_to_array(decrypted_text, now_ch); // Символды динамикалык жиымга косу
        }
        System.out.print("Кері шифрланған тексттің нәтижесі:\n");
        for (char ch : decrypted_text){  // Символдар бойынша результатты, кері шифрланган текстті шығарамыз
            System.out.print(ch);
            result+=ch;
        }
        return result;  // Нәтижеге кері шифрланған жолды қайтарады
    }

    public static String encrypt_text(String text, int key)
    {
        System.out.println("\n\n------------STARTED TEXT ENCRYPTION------------\n");
        char text_symbols[] = text.toCharArray(); // Шифрланатын текст осы жиымга жазылады

        char encrypted_text[] = {};  //  шифрланган текст осы жиымга жазылады
        String result = "";  //  шифрланган текст осы жолга жазылады
        for (char ch : text_symbols){
            
            char now_ch = ch;
       
            if (ch >= 'A' && ch <='Z'){   // Агылшын бас әріптері бойынша
                now_ch = (char)((ch + key - 65) % 26 + 65); 
            } 
            else if (ch >= 'a' && ch <='z'){
                now_ch = (char)((ch + key - 97) % 26 + 97);  // Агылшын кіші әріптері бойынша
            } 
            else if (ch >= 'А' && ch <='Я'){
                now_ch = (char)((ch + key - 'А') % 32 + 'А');  // Орыс бас әріптері бойынша
            } 
            else if (ch >= 'а' && ch <='я'){
                now_ch = (char)((ch + key - 'а') % 32 + 'а');  // Орыс кіші әріптері бойынша
            } 
            else {
                now_ch = ch;  // Алфавит әріпі болмаса, символды шифрламай сол калпында калдырамыз
            }

            encrypted_text = append_char_to_array(encrypted_text, now_ch); // Символды динамикалык жиымга косу

        }
        System.out.print("Шифрланған тексттің нәтижесі:\n");
        for (char ch : encrypted_text){ // Символдар бойынша результатты, шифрланган текстті шығарамыз
            System.out.print(ch);
            result+=ch;
        }
        return result; // Нәтижеге шифрланған жолды қайтарады
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("\nЦЕЗАРЬ ШИФРІН АҚПАРАТТЫ ЖАСЫРУ ҮШІН ҚОЛДАНАТЫН ПРОГРАММА\n");

        System.out.print("Жасырылынатын текстті енгізіңіз:\n");
        String text = in.nextLine();
        //String text = "abc xyz абв эюя";

        System.out.print("Шифрлау кілтін енгізіңіз, key: ");
        //int key = 3;
        int key = in.nextInt();

        
        String enc_text = encrypt_text(text, key);
        decrypt_text(enc_text, key);

        in.close();
    }
}
