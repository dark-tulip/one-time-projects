/* Какой то проект... с нодами. Считалка на круглом столе */

public class CircleTable{
    
    // Келесі тізім классы донгелек үстелдің моделін құрайды

    static class Node{
        String human;         // осы айнымалы адамның аты үшін жауап береді
        Node next_human;      // тізімдегі келесі адамға сілтеме
    };
    
    // Алдымен тізімде ойыншылар жок деп саналады.
    // Программаны бастамас бурын донгелек байланысты тізімді кураймыз

    static Node create_Circle_table_List(Node last_player, String human)
    {
        // Осы функцияны тек бір рет қана шақырамыз
        // тізімде элементтер жоқ болса ғана

        if (last_player != null){
            return last_player;
        }
    
        // Динамикалық өзгерісті қамтамасыз ету үшін жаңа объекті ретіндегі тізімді құраймыз

        Node tmp_node = new Node();
    
        // Тізімдегі ойыншыларды құрыстыру, сілтеме беру
        tmp_node.human = human;
        last_player = tmp_node;
    
        // Сілтемелерді орналастыру, соңғы таңдалғаннан келесісіне
        last_player.next_human = last_player;

        // Тізімнің басындағы сілтеме осы ойыншыға берілсін
        return last_player;
    }
    
    // Келесі функция дөңгелек тізімнің басына, яғни ең бірінші адамға сілтеме беріп басына отырғызады,
    // қалған ойыншыларды бір позицияға оңға жылжытудың орнына, сілтемені ғана бере салады

    static Node add_to_head_of_table(Node last_player, String human)
    {

        // Тізімде ойыншылар жоқ болса, жаңа тізім құру функциясын шақырады
        if (last_player == null){
            return create_Circle_table_List(last_player, human);
        }

        // уақытша жумыс истеу тізімін құраймыз

        Node tmp_node = new Node();
        
        // қалған ойыншыларды бір позицияға оңға жылжытудың орнына, сілтемені ғана бере салады
        // сол адамға бере салады
        tmp_node.human = human;
        tmp_node.next_human = last_player.next_human;
        last_player.next_human = tmp_node;
    
        return last_player;
    }
    
    // Келесі функция дөңгелек тізімдегі үстелдің соңына ойыншыны отырғызып орналастыруға мүмкіндік береді

    static Node add_to_end_of_table(Node last_player, String human)
    {
        // Егер үстелде, яғни тізімде адамдар жок болса, жана тізім куруга сілтеме берілсін
        if (last_player == null)
            return create_Circle_table_List(last_player, human);
        
        // уақытша жумыс істеу тізімі құрылады
        Node tmp_node = new Node();
        
        // жаңа ойыншы енгізіліп, тізімнің бастапқы сілтемесі сол ойыншыға берілсін
        tmp_node.human = human;
        tmp_node.next_human = last_player.next_human;
        last_player.next_human = tmp_node;
        last_player = tmp_node;
       
        // нәтижесінде жаңа сілтеме қайтарылады
        return last_player;
    }
    
    // Келесі функция дөңгелек тізімнің ішінен адамды сол элементке дейин енгізеді
    // яғни сол адамға дейін отырғызады

    static Node add_after_insert(Node last_player, String human, String item)
    {
        // тізім құрастырылмаған болса ештеңке қайтармайды

        if (last_player == null)
            return null;

        // Уақытша тізім
        Node tmp_node, now;

        // Осы айнымалыда сол адамның сілтемесі тұрсын
        now = last_player.next_human;

        // Орындаймыз, дөңгелек үстелдегі адамның басына оралмағанша

        do{
            if (now.human == item)  // Іздеп отырған адам табылса
            {
                // Жаңа тізім құрып арасына отырғызамыз
                tmp_node = new Node();
                tmp_node.human = human;
                tmp_node.next_human = now.next_human;
                now.next_human = tmp_node;
    
                if (now == last_player)
                    last_player = tmp_node;
                return last_player;
            }
            now = now.next_human;

        // Орындаймыз, дөңгелек үстелдегі адамның басына оралмағанша
        } while(now != last_player.next_human);
    
        System.out.println(item + ", бұл адам дөңгелек үстелде табылмады");
        return last_player;
    
    }
    
    // Келесі функция тізімде отырған барлық ойыншыларды басып шығарады

    static void show_table_players(Node last_player)
    {
        Node now;

        // Тізімде ойыншы жоқ болса келесі хабарламаны басып шығарады
        if (last_player == null)
        {
            System.out.println("Өкінішке орый үстелде ойыншылар жоқ");
            return;
        }
    
        // Cілтемені тізімнің басына береді, оны соңғысынан алады

        now = last_player.next_human;

        // Келесі хабарламаны шығарады
        System.out.print("\n\nҮстелде отырған ойыншылар келесі ретпен саналады:\n");
       
        // Әрбір ойыншыны тізімдеп шығарады
        do
        {
            System.out.print(now.human + " ");
            now = now.next_human;

            // Ойыншылардан бастапқы ойыншыға жетпегенше ойыншыларды басып шығарады    
        }  while(now != last_player.next_human);

        System.out.print("\n");
    
    }
    
    // Ойынның негізгі функциясы, адамды санаушы тақпақпен таңдайды, аргумент ретінде санаушыдағы сөздер санын қабылдайды
    // тізімнің басынан бастап санайды
    static void choose_one(Node last_player, int cnt){
        
        Node now;
        // егер тақпақтағы сөз саны адам санынан көп болса, тізімнің басына оралады

        now = last_player.next_human;  // Осы ойыншыдан бастаймыз

        System.out.print("\nСанауды бастайық, санаймыз, санаймыз\n");
        for(int i = 0; i < cnt - 1; i++){   
            // Санаушыға дейінгі цикл
            System.out.print("\n" + now.human + ", санауышпен өтіп кеттін, дөңгелекпен айналып келесі адамға көшеміз......" );
            
            // Келесі адамға көшеміз
            now = now.next_human;  
            if (now == last_player.next_human){
                now = last_player.next_human;
            }
        }

        System.out.print("\n\nСанадық, санадық, " + now.human + " саған таңдау жасадық, сен жүргізуші боласың\n");
    }
    
    //Келесі функция тақпақтың ішіндегі сөздердің санын санайды
    public static int CountWords(String str){

        System.out.println("\nСанаушы тақпақ: " + str);

        String[] words = str.split(" ");

        System.out.print("Санаушы тақпақтағы сөздер саны: " + words.length);
        
        return words.length;
    }
    
    // Ойын ішіндегі адамдардың санын санайды
    public static int count_players(Node last_player){
        Node now;   
        int cnt = 0;
        now = last_player.next_human;   // Соңғы адамнан бастайық

        do
        {
            // Келесі адамға көшу
            now = now.next_human;  
            // Санаушыны бірге үлкейту
            cnt+=1;
    
        } while(now != last_player.next_human);

        System.out.print("\nҮстелдегі адам саны: " + cnt);
        return cnt;

    }

    // Негізгі функция main
    public static void main(String args[])
    {
        String str = "Санап едік алты, бір екі үш төрт бес алты соңы";
        // Тақпақтағы сөз санын санау
        int counting_of_words = CountWords(str);

        Node last_player = null;

        // Дөңгелекті тізімді құраймыз
        last_player = create_Circle_table_List(last_player, "Айдын");
        
        // Басына адамды отырғызамыз
        last_player = add_to_head_of_table(last_player, "Максат");
        last_player = add_to_head_of_table(last_player, "Дана");
        
        // Үстелдің соңына адамды отырғызамыз
        last_player = add_to_end_of_table(last_player, "Айгерім");
        last_player = add_to_end_of_table(last_player, "Жазира");
        last_player = add_to_end_of_table(last_player, "Аида");
        last_player = add_to_end_of_table(last_player, "Анель");
        last_player = add_to_end_of_table(last_player, "Кайрат");
        
        // Аиданы Айнурға дейін отырғызамыз адамды отырғызамыз
        last_player = add_after_insert(last_player, "Айнур", "Аида");

        // Ойыншы санын санау
        count_players(last_player);
        // Дөңгелек тізімді шығару
        show_table_players(last_player);
        // Ойыншыны тақпақпен таңдау
        choose_one(last_player, counting_of_words);
    }
}
