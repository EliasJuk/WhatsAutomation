<h1  align="center"> WhatsAutomation </h1>
<h4 align="center">Sistema de envio de mensagens automáticas</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/EliasJuk/WhatsAutomation">	
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/EliasJuk/WhatsAutomation">
	
  <a href="https://github.com/EliasJuk/WhatsAutomation/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/EliasJuk/WhatsAutomation">
  </a>
  
  <a href="https://github.com/EliasJuk/WhatsAutomation/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/EliasJuk/WhatsAutomation">
  </a>
  
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen"> 
<p>

<p align="center">
  <a href="#-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-How-To-Use">How To Use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Versions">Versions</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-license">License</a>
</p>

## 💻 Project

WhatsAutomation é uma aplicação para envio de mensagens e imagens automática a partir de uma planilha de contato

<h1 align="center">
    <img alt="interface" title="#interface" src="readme/screenshot.png"/>
</h1>

## ❔ How To Use

Para clonar e rodar a aplicação, você precisará do [Git](https://git-scm.com/) e [Python](https://www.python.org/) instalados em seu computador
- Clone o repositorio do projeto em sua maquina

```bash
# Clonar Projeto
$ git clone https://github.com/EliasJuk/WhatsAutomation/
```

- Baixe a versão do [chromedriver](https://chromedriver.chromium.org/downloads) compativel com a versão do chrome em sua maquina e coloque na pasta principal do projeto

- Para criar o ambiente virtual e instalr os pacotes do projeto
```bash
# Acesse o local do projeto
$ cd WhatsAutomation

# Criar Ambiente Virtual
$ python3 -m venv venv

# Ativar ambiente virtual
$ cd venv/Scripts
$ activate.bat

# Com o ambiente virtual ativado instale os pacotes
$ pip install -r requirements.txt

# Run Project
$ Python main.py
```

## 📁 Versions
  - Versão: [v0.1](https://github.com/EliasJuk/WhatsAutomation/tree/main/versions/v0.1)
    - Envio de Mensagens de texto e imagem unica
    - Envio de mensagem com base em planilha de contatos
    - Suporte ao Google Chrome

---
## :memo: License

This project is under the MIT license. See the [LICENSE](LICENSE.md) for details.