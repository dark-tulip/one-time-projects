/**
Input:
3 3 12
DISABLE 1 2
DISABLE 2 1
DISABLE 3 3
GETMAX
RESET 1
RESET 2
DISABLE 1 2
DISABLE 1 3
DISABLE 2 2
GETMAX
RESET 3
GETMIN

Output:
1
2
1
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;


enum Commands {
    RESET,
    GETMAX,
    GETMIN,
    DISABLE,
}

class Server {
    boolean isActive = true;
}

class DataCenter {

    private final List<Server> servers;

    private int resets = 0;

    public DataCenter(int serversCnt) {
        this.servers = Stream.generate(Server::new).limit(serversCnt).collect(Collectors.toList());
    }

    int dcNumber;

    public void resetAll() {
        this.servers.forEach(s -> s.isActive = true);
        resets += 1;
    }

    public void disableServer(int serverIndex) {
        this.servers.get(serverIndex).isActive = false;
    }

    public int getActiveServersCnt() {
        return (int) this.servers.stream().filter(s -> s.isActive).count();
    }

    public int get_f_x() {
        return this.resets * this.getActiveServersCnt();
    }

}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        int q = Integer.parseInt(temp[2]);

        List<DataCenter> dataCenters = Stream.generate(() -> new DataCenter(m))
                .limit(n)
                .collect(Collectors.toList());

        {
            int dcCnt = 1;
            for (var dc : dataCenters) {
                dc.dcNumber = dcCnt++;
            }
        }

        while (q-- > 0) {
            String[] commandArgs = br.readLine().split(" ");
            String baseCommand = commandArgs[0];
            
            if (Commands.DISABLE.toString().equals(baseCommand)) {
                int dcIndex = Integer.parseInt(commandArgs[1]) - 1;    // порядок в серверах в программе идет с нуля
                int serverIndex = Integer.parseInt(commandArgs[2]) - 1;

                dataCenters.get(dcIndex).disableServer(serverIndex);

            } else if (Commands.RESET.toString().equals(baseCommand)) {
                int dcIndex = Integer.parseInt(commandArgs[1]) - 1;
                dataCenters.get(dcIndex).resetAll();

            } else if (Commands.GETMAX.toString().equals(baseCommand)) {
                DataCenter dc = dataCenters.stream().max(Comparator.comparingInt(DataCenter::get_f_x)).orElse(null);
                System.out.println(dc.dcNumber);

            } else if (Commands.GETMIN.toString().equals(baseCommand)) {
                DataCenter dc = dataCenters.stream().min(Comparator.comparingInt(DataCenter::get_f_x)).orElse(null);
                System.out.println(dc.dcNumber);

            }
        }
    }
}
