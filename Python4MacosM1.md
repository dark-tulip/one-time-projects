## Сменить версию питона

```bash
brew install pyenv
pyenv install 3.7.12
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
pyenv global 3.7.12
pyenv local 3.7.12
```
