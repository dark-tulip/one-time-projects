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
alabaster==0.7.13
Babel==2.14.0
certifi==2025.1.31
charset-normalizer==3.4.1
commonmark==0.9.1
docutils==0.20.1
exceptiongroup==1.2.2
idna==3.10
imagesize==1.4.1
importlib-metadata==6.7.0
iniconfig==2.0.0
jinja2==3.1.5
MarkupSafe==2.1.5
packaging==24.0
pluggy==1.2.0
pygments==2.17.2
pytest==7.4.4
pytz==2025.1
recommonmark==0.7.1
requests==2.31.0
snowballstemmer==2.2.0
sphinx==5.3.0
sphinx-rtd-theme==2.0.0
sphinxcontrib-applehelp==1.0.2
sphinxcontrib-devhelp==1.0.2
sphinxcontrib-htmlhelp==2.0.0
sphinxcontrib-jquery==4.1
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.3
sphinxcontrib-serializinghtml==1.1.5
tomli==2.0.1
typing-extensions==4.7.1
urllib3==2.0.7
zipp==3.15.0
```

## 3. mldev run report html
```
pip install recommonmark
cd docs
make html
make latexpdf
```

```
xdg-open build/html/index.html  # Для Linux
open build/html/index.html  # Для macOS
start build/html/index.html  # Для Windows
```

## generated html

<img width="1197" alt="image" src="https://github.com/user-attachments/assets/abc0e555-74e8-4863-87c4-05e7ef353cb1" />

## generated pdf

<img width="949" alt="image" src="https://github.com/user-attachments/assets/70511720-d020-4755-88fa-75b71f8e4072" />

