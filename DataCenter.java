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


// V2

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;


class Server {
  boolean isActive = true;
}

class DataCenter {
  private int resets = 0;   // число перезапусков
  private int actives;      // число рабочих (не выключенных) серверов
  Server[] servers;

  public DataCenter(int serversCnt) {
    servers = new Server[serversCnt];

    for(Server server: servers) {
      server = new Server();
    }

    actives = serversCnt;
  }

  public void resetAll() {
    resets++;
    for (var server: servers) {
      server.isActive = true;
    }
    actives = servers.length;
  }

  /**
   * starts from ZERO to n - 1 servers
   */
  public void disableOne(int serverPosition) {
    // повторно выключить сервер нельзя
    if (servers[serverPosition].isActive) {
      actives --;
      servers[serverPosition].isActive = false;
    }
  }

  public int getMul() {
    return resets * actives;
  }
}


public class Main {
  public static final String RESET = "RESET";
  public static final String GETMIN = "GETMIN";
  public static final String GETMAX = "GETMAX";

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int q = Integer.parseInt(st.nextToken());

    // region init servers
    DataCenter[] dataCenters = (DataCenter[]) Stream.generate(() -> new DataCenter(m)).limit(n).toArray();

    while (q-- > 0) {
      StringTokenizer st2 = new StringTokenizer(br.readLine());
      String event = st2.nextToken();

      if (event.startsWith(GETMAX)) {
        // получить номер дата-центра с наибольшим произведением R_i  * A_i
        int maxi = 0;
        int maxMul = dataCenters[0].getMul();

        for(int i = 1; i < m; i++) {
          if (dataCenters[i].getMul() > maxMul) {
            maxMul = dataCenters[i].getMul();
            maxi = i;
          }
        }
        System.out.println(maxi + 1);

      } else if (event.startsWith(GETMIN)) {
        // получить номер дата-центра с наименьшим произведением R_i  * A_i
        int mini = 0;
        int minMul = dataCenters[0].getMul();

        for(int i = 1; i < m; i++) {
          if (dataCenters[i].getMul() < minMul) {
            minMul = dataCenters[i].getMul();
            mini = i;
          }
        }
        System.out.println(mini + 1);

      } else if (event.startsWith(RESET)) {
        int dcNum =  Integer.parseInt(st2.nextToken()) - 1;
        dataCenters[dcNum].resetAll();

      } else {
        int dcNum =  Integer.parseInt(st2.nextToken()) - 1;
        int serverNum =  Integer.parseInt(st2.nextToken()) - 1;
        dataCenters[dcNum].disableOne(serverNum);

      }
    }
  }
}
