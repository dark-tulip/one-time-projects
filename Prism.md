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
