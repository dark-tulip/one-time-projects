### Задание по анализу консенсуса для блокчейн сетей.

1. Установить PRISM

```bash
./install.sh
```
2. Установить consencus_analyzer https://github.com/lvanan/prog-autom-consensus-analyzer

```bash
make
```
3. Запустить
```
bin/run resources/cnf-1/cnf_1_properties.yaml resources/cnf-simple.yaml results false
```

<img width="1244" alt="image" src="https://github.com/user-attachments/assets/d105b5d1-19a8-4729-91f3-58445ec954fc" />


output:

```bash
tansh@MacBook-Pro-tansh consensus-analyzer % python -m json.tool results/results.json 
{
    "modelCheckResultList": [
        {
            "backwardTransitions": [
                []
            ],
            "probability": 0.9703235025,
            "expectedMessages": 5.0,
            "id": 589873731,
            "epochTimestamp": 1743972351724
        }
    ],
    "specification": [
        [
            1,
            1,
            1,
            1,
            1
        ],
        [
            1,
            1,
            1,
            1,
            0
        ]
    ],
    "organizations": [
        "Org1",
        "Org2",
        "Org1",
        "Org2",
        "Org3"
    ]
}
```
