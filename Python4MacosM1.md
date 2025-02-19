## Сменить версию питона

```bash
brew install pyenv
pyenv install 3.7.12
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
pyenv global 3.7.12
pyenv local 3.7.12
```


## копировать файл из контейнера в хостовую машину
```
docker cp 67a0d16cb721:/root/edu/mldev/report.html .
```

## pip freeze mldev
```
# pip freeze
asn1crypto==0.24.0
attrs==21.4.0
backcall==0.2.0
cryptography==2.1.4
cycler==0.11.0
decorator==5.1.1
deepdiff==5.7.0
dill==0.3.4
gitdb==4.0.9
GitPython==3.1.18
idna==2.6
importlib-metadata==4.8.3
iniconfig==1.1.1
ipython==7.16.3
ipython-genutils==0.2.0
jedi==0.17.2
jsonschema==3.2.0
jupyter-core==4.9.2
keyring==10.6.0
keyrings.alt==3.0
kiwisolver==1.3.1
markdown-it-py==2.0.1
matplotlib==3.3.4
mdurl==0.1.0
-e git+ssh://git@gitlab.com/tansh/mldev.git@7c9c2654648b2ee5e185941246f960ec84ae7dd7#egg=mldev
more-itertools==8.14.0
nbformat==5.1.3
numpy==1.19.5
ordered-set==4.0.2
packaging==21.3
parso==0.7.1
pexpect==4.9.0
pickleshare==0.7.5
Pillow==8.1.2
pluggy==0.13.1
prompt-toolkit==3.0.36
protobuf==3.14.0
ptyprocess==0.7.0
py==1.11.0
pycrypto==2.6.1
Pygments==2.14.0
PyGObject==3.26.1
pyparsing==3.1.4
pyrsistent==0.18.0
pytest==6.0.2
pytest-html==3.2.0
pytest-metadata==1.11.0
python-dateutil==2.9.0.post0
pyxdg==0.25
PyYAML==6.0.1
ruamel.yaml==0.17.33
ruamel.yaml.clib==0.2.8
scipy==1.5.4
SecretStorage==2.3.1
sh==1.14.3
simpleeval==0.9.13
six==1.17.0
smmap==5.0.0
toml==0.10.2
traitlets==4.3.3
typing_extensions==4.1.1
wcwidth==0.2.13
zipp==3.6.0
```

## 3. mldev run report html
```
pip install recommonmark
cd docs
make html
```

```
xdg-open build/html/index.html  # Для Linux
open build/html/index.html  # Для macOS
start build/html/index.html  # Для Windows
```

<img width="1197" alt="image" src="https://github.com/user-attachments/assets/abc0e555-74e8-4863-87c4-05e7ef353cb1" />

