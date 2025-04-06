### 1. Задание по анализу консенсуса для блокчейн сетей.

1. Установить PRISM

```bash
./install.sh
```
2. Установить consencus_analyzer https://github.com/lvanan/prog-autom-consensus-analyzer

```bash
make
```
3. Запустить (один конфиг файл)
```
bin/run resources/cnf-simple.yaml results false
```

<img width="891" alt="image" src="https://github.com/user-attachments/assets/d3c70d13-5a2e-4cab-8649-e8ee117d9cd9" />

output:

```bash
tansh@MacBook-Pro-tansh consensus-analyzer % python -m json.tool results/results.json   
```

```json    
{
    "modelCheckResultList": [
        {
            "backwardTransitions": [
                []
            ],
            "probability": 0.25,
            "expectedMessages": 2.0,
            "id": 1174361318,
            "epochTimestamp": 1743972880101
        }
    ],
    "specification": [
        [
            1,
            1
        ]
    ],
    "organizations": [
        "Org1",
        "Org2"
    ]
}
```
4. Запустить c разделением (файла props и specs)

- separate spec + config
- true or false to run transitiva mode otherwise
- Без обратных переходов (false): система моделирует только "прямой путь"
- С обратными переходами (true): система моделирует и сбои, и повторы, и восстанавливаемость

```bash
tansh@MacBook-Pro-tansh consensus-analyzer % bin/run resources/cnf-1/cnf_1_properties.yaml resources/cnf-1/cnf_1_spec.yaml results false
Specification DNF form: (Org3&Org2&Org1)
writing results to json in results/results.json

tansh@MacBook-Pro-tansh consensus-analyzer % python -m json.tool results/results.json                                                   
{
    "modelCheckResultList": [
        {
            "backwardTransitions": [
                []
            ],
            "probability": 0.97027425,
            "expectedMessages": 3.0,
            "id": 589873731,
            "epochTimestamp": 1743973525001
        }
    ],
    "specification": [
        [
            1,
            1,
            1
        ]
    ],
    "organizations": [
        "Org1",
        "Org2",
        "Org3"
    ]
}
```

- **что внутри props файла? cnf_1_properties.yaml**

```yaml
tansh@MacBook-Pro-tansh consensus-analyzer % cat resources/cnf-1/cnf_1_properties.yaml
Organizations:
  -
    Name: Org1

    # Probability to accept nxt transaction. based on the historical data
    Pr: 0.995

  -
    Name: Org2

    # Probability to accept nxt transaction. based on the historical data
    Pr: 0.99

  -
    Name: Org3

    # Probability to accept nxt transaction. based on the historical data
    Pr: 0.985
```

- **что внутри спеки? cnf_1_spec.yaml**
```bash
tansh@MacBook-Pro-tansh consensus-analyzer % cat resources/cnf-1/cnf_1_spec.yaml      
```
```yaml
Policies:
  Endorsement:
    Type: Signature
    Rule: "(Org3 & Org2 & Org1)"% 
```

### 1.2 Изменить файл спецификации таким образом, чтобы транзакция была принята всей сетью в случае, если большинство организаций ее подтвердили.

нужно изменить `Rule` в файле спеки
- зададим правило большинства `OutOf`
- `OutOf(k, OrgA, OrgB, ...)` - нужно согласие от минимум k организаций

```yaml
Policies:
  Endorsement:
    Type: Signature
    Rule: "OutOf(2, Org3, Org2, Org1)"
```


```bash
 bin/run resources/cnf-1/cnf_1_properties.yaml resources/cnf-1/cnf_1_spec.yaml results false
```

<img width="960" alt="image" src="https://github.com/user-attachments/assets/8f3abe48-ebbc-47f9-94e5-1ab2b29f0e74" />

### 1.3 Запустить анализ. Ознакомиться с результатом в выходном json-файле. Объяснить значение полученной вероятности.
```
{
    "modelCheckResultList": [
        {
            "backwardTransitions": [
                []
            ],
            "probability": 0.995,
            "expectedMessages": 3.0,
            "id": 1160264930,
            "epochTimestamp": 1743975282045
        }
    ],
    "specification": [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
        [1, 0, 0]
    ],
    "organizations": [
        "Org1",
        "Org2",
        "Org3"
    ]
}
```
- Блок организаций. Просто список участвующих организаций `organizations: ["Org1", "Org2", "Org3"]`
- Блок спецификаций, возможная комбинация голосов от организаций `specification`
- `backwardTransitions: [[]]`  использовались ли обратные переходы ( откаты состояний)
- `"expectedMessages": 3.0,` - в среднем потребуется 3 сообщения между организациями, чтобы достичь консенсуса
- `probability: 0.995` - при текущих правилах (например, OutOf(2, Org1, Org2, Org3)) и вероятностях, система почти всегда (99.5% случаев) придёт к согласию

### 1.4 Запустить анализ с обратными переходами. Ознакомиться с результатом в выходном json-файле. Выбрать одну из моделей, в соответствии с которой будет происходить отправка сообщений.


```bash
tansh@MacBook-Pro-tansh consensus-analyzer % bin/run resources/cnf-1/cnf_1_properties.yaml resources/cnf-1/cnf_1_spec.yaml results true
Specification DNF form: (OutOf(2, Org3, Org2, Org1))
writing results to json in results/results.json
building dependency and saving in in results/graph.png
2025-04-07 01:04:04.232 java[391:7403691] +[IMKClient subclass]: chose IMKClient_Modern
2025-04-07 01:04:04.232 java[391:7403691] +[IMKInputSession subclass]: chose IMKInputSession_Modern
tansh@MacBook-Pro-tansh consensus-analyzer % cat results/results.json
```

```json
{"modelCheckResultList":[{"backwardTransitions":[],"probability":0.995,"expectedMessages":3.0,"id":0,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1]],"probability":0.99500074625,"expectedMessages":3.0000022499999996,"id":544724190,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,0,-1]],"probability":0.9949992314744376,"expectedMessages":3.0004477945511248,"id":1972439101,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1]],"probability":0.9950738842354971,"expectedMessages":3.000222766539187,"id":2007328737,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1]],"probability":0.9949249658418053,"expectedMessages":3.044991943677834,"id":1936628443,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,-1,-1]],"probability":0.9950497524875,"expectedMessages":3.0001500075001246,"id":1830908236,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,-1,-1]],"probability":0.994948769912625,"expectedMessages":3.03014897764975,"id":277630005,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":1288354730,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[1,0,-1]],"probability":0.9949999999966419,"expectedMessages":3.0004500674999997,"id":-1777804005,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1]],"probability":0.995074630596875,"expectedMessages":3.0002250168749995,"id":-1742914369,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1]],"probability":0.9949257699491221,"expectedMessages":3.044994357002865,"id":-1813614663,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[0,-1,-1]],"probability":0.9950497524875,"expectedMessages":3.0001500075001246,"id":-1919334870,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[1,-1,-1]],"probability":0.9949504939699814,"expectedMessages":3.030152277775558,"id":822354195,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":1833078920,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,0,-1]],"probability":0.9950731488376583,"expectedMessages":3.0006706498567493,"id":-315199458,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[1,0,-1]],"probability":0.994924194978668,"expectedMessages":3.045453339998246,"id":-385899752,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,0,-1],[0,-1,-1]],"probability":0.9950490132898778,"expectedMessages":3.0005978468274943,"id":-491619959,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,-1,-1],[1,0,-1]],"probability":0.994948769912625,"expectedMessages":3.03014897764975,"id":-2044898190,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":-1034173465,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1]],"probability":0.9949999992814528,"expectedMessages":3.045221537667894,"id":-351010116,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,-1,-1]],"probability":0.9951236441109965,"expectedMessages":3.000372796316503,"id":-456730323,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,-1,-1]],"probability":0.9950243726792113,"expectedMessages":3.0303772483723295,"id":-2010008554,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":-999283829,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,-1,-1]],"probability":0.994975461179155,"expectedMessages":3.0451465320912154,"id":-527430617,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[1,-1,-1]],"probability":0.9948730570170121,"expectedMessages":3.0760575888097077,"id":-2080708848,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":-1069984123,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,-1,-1],[0,-1,-1]],"probability":0.99499999005,"expectedMessages":3.03030301,"id":2108538241,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":-1175704330,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1565984735,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[1,0,-1]],"probability":0.9950738953098043,"expectedMessages":3.0006729008641875,"id":229524732,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[1,0,-1]],"probability":0.9949250011093013,"expectedMessages":3.0454557083161022,"id":158824438,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":0.9950490132898778,"expectedMessages":3.0005978468274943,"id":53104231,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":0.9949504939699814,"expectedMessages":3.030152277775558,"id":-1500174000,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":-489449275,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1]],"probability":0.9950007567807054,"expectedMessages":3.0452238560126585,"id":193714074,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[0,-1,-1]],"probability":0.9951236441109965,"expectedMessages":3.000372796316503,"id":87993867,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[1,-1,-1]],"probability":0.9950251265015634,"expectedMessages":3.0303795441610593,"id":-1465284364,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":-454559639,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[0,-1,-1]],"probability":0.994975461179155,"expectedMessages":3.0451465320912154,"id":17293573,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[1,-1,-1]],"probability":0.9948739957002172,"expectedMessages":3.0760601918976755,"id":-1535984658,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":-525259933,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":0.99499999005,"expectedMessages":3.03030301,"id":-1641704865,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":-630980140,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":2110708925,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[1,0,-1]],"probability":0.994999241630975,"expectedMessages":3.0456829578276405,"id":1621428985,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9951229160989751,"expectedMessages":3.00082072441797,"id":1515708778,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,-1,-1],[1,0,-1]],"probability":0.9950243726792113,"expectedMessages":3.0303772483723295,"id":-37569453,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":973155272,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9949746974531645,"expectedMessages":3.045607927579371,"id":1445008484,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[1,-1,-1],[1,0,-1]],"probability":0.9948730570170121,"expectedMessages":3.0760575888097077,"id":-108269747,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":902454978,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.99499999005,"expectedMessages":3.03030301,"id":-213989954,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":796734771,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-756543460,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,-1,-1]],"probability":0.9950505017562954,"expectedMessages":3.0453760530822294,"id":1479898120,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[1,-1,-1]],"probability":0.9949489783992436,"expectedMessages":3.076292031747657,"id":-73380111,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":937344614,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,-1,-1],[0,-1,-1]],"probability":0.9950746301978003,"expectedMessages":3.0305303089923807,"id":-179100318,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":831624407,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-721653824,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[1,-1,-1],[0,-1,-1]],"probability":0.9949241896247245,"expectedMessages":3.0762154810841364,"id":-249800612,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":760924113,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-792354118,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-898074325,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[1,0,-1]],"probability":0.994999999244422,"expectedMessages":3.045685276875,"id":-2128814121,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":0.9951229160989751,"expectedMessages":3.00082072441797,"id":2060432968,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":0.9950251265015634,"expectedMessages":3.0303795441610593,"id":507154737,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":1517879462,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":0.9949746974531645,"expectedMessages":3.045607927579371,"id":1989732674,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":0.9948739957002172,"expectedMessages":3.0760601918976755,"id":436454443,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":1447179168,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.99499999005,"expectedMessages":3.03030301,"id":330734236,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":1341458961,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-211819270,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[0,-1,-1]],"probability":0.9950505017562954,"expectedMessages":3.0453760530822294,"id":2024622310,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1]],"probability":0.9949497435870732,"expectedMessages":3.0762943976405173,"id":471344079,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":1482068804,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":0.9950746301978003,"expectedMessages":3.0305303089923807,"id":365623872,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015075376884422,"id":1376348597,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-176929634,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":0.9949241896247245,"expectedMessages":3.0762154810841364,"id":294923578,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":1305648303,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-247629928,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-353350135,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9950497517195224,"expectedMessages":3.045837518100426,"id":-842630075,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[1,-1,-1],[1,0,-1]],"probability":0.9949489783992436,"expectedMessages":3.076292031747657,"id":1899058990,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":-1385183581,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9950746301978003,"expectedMessages":3.0305303089923807,"id":1793338783,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":-1490903788,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1250785277,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9949241896247245,"expectedMessages":3.0762154810841364,"id":1722638489,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":-1561604082,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1180084983,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1074364776,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[1,-1,-1],[0,-1,-1]],"probability":0.9949999935293292,"expectedMessages":3.0764497093979353,"id":1757528125,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":-1526714446,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1214974619,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1109254412,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1038554118,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":0.9950497517195224,"expectedMessages":3.045837518100426,"id":-297905885,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":0.9949497435870732,"expectedMessages":3.0762943976405173,"id":-1851184116,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":-840459391,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9950746301978003,"expectedMessages":3.0305303089923807,"id":-1956904323,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.015527683417085,"id":-946179598,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1795509467,"epochTimestamp":1743976899937},{"backwardTransitions":[[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9949241896247245,"expectedMessages":3.0762154810841364,"id":-2027604617,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":-1016879892,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1724809173,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1619088966,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":0.9949999935293292,"expectedMessages":3.0764497093979353,"id":-1992714981,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0605240604667303,"id":-981990256,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1759698809,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":1653978602,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1583278308,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9949999935293292,"expectedMessages":3.0764497093979353,"id":-565000070,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":445724655,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-1107553576,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-1213273783,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-1283974077,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-1249084441,"epochTimestamp":1743976899937},{"backwardTransitions":[[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":0.9949999935293292,"expectedMessages":3.0764497093979353,"id":-20275880,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.060990177135678,"id":990448845,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-562829386,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0455296482412058,"id":-668549593,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-739249887,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":-704360251,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":723354660,"epochTimestamp":1743976899937},{"backwardTransitions":[[-1,-1,-1],[0,1,-1],[1,1,-1],[0,0,-1],[1,-1,-1],[1,0,-1],[0,-1,-1]],"probability":1.0,"expectedMessages":3.0919090686339907,"id":1268078850,"epochTimestamp":1743976899937}],"specification":[[1,1,1],[1,0,1],[1,1,0],[1,0,0]],"organizations":["Org1","Org2","Org3"]}%
```

- Каждый элемент в `modelCheckResultList` один вариант модели консенсуса, в которой были определённые обратные переходы (т.е. система могла "откатиться" в некоторых состояниях) и были рассчитаны:

- "probability" — вероятность достижения консенсуса при таком поведении
- "expectedMessages" — сколько сообщений в среднем потребуется
- "backwardTransitions" — какие обратные переходы допущены. `-1` - откат назад, `0` - начальное состояние, `1` - подтвердил

нарисуем выведенный граф:
![graph](https://github.com/user-attachments/assets/9aa4c295-b677-4aa7-af21-2dca2825b7c5)

выберем модель и сохраним в отдельном файле `selected_model.json`

```json
{
  "modelCheckResultList": [
    {
      "backwardTransitions": [[0, 1, -1]],
      "probability": 0.9950738842354971,
      "expectedMessages": 3.000222766539187,
      "id": 2007328737
    }
  ],
  "organizations": ["Org1", "Org2", "Org3"]
}
```
### 1.5 Передать json-файл в модуль планировщика. Запустить модуль планировщика. Ознакомиться с результатами логов. Объяснить полученный результат.

запустим тесты на проекте consencus scheduler

<img width="1417" alt="image" src="https://github.com/user-attachments/assets/a9bbe438-40f3-4c21-87a5-78211193ad1e" />


разберем один лог файл

```logs
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Send for confirmation to Org1 finished with response true
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Send for confirmation to Org2 finished with response false
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Send for confirmation to Org3 finished with response true
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Consensus is reached with 3 messages
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Send for confirmation to Org1 finished with response false
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Send for confirmation to Org2 finished with response false
Apr 07, 2025 1:46:38 AM services.SendingConfirmationServiceImpl sendForConfirmationToOrganization
INFO: Send for confirmation to Org3 finished with response true
```
- 2 из 3 организаций подтвердили — этого достаточно для выполнения правила OutOf(2, Org1, Org2, Org3).
Консенсус достигнут.
