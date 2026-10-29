# 🎲 Ready2Reload - Automação de Testes End-to-End (E2E)

Suíte de testes automatizados E2E desenvolvida para validar as funcionalidades principais da aplicação web de RPG/Rolagem de Dados **Ready2Reload**. 

O projeto utiliza **Python**, **Selenium WebDriver** e o framework **PyTest**, aplicando o padrão de arquitetura **Page Object Model (POM)** para garantir manutenibilidade, legibilidade e reusabilidade do código.

---

## 🚀 Tecnologias e Ferramentas Utilizadas
* **Python** (Linguagem principal)
* **Selenium WebDriver** (Automação de navegador)
* **PyTest** (Framework de execução e parametrização de testes)
* **PyCharm IDE** (Ambiente de desenvolvimento)
* **Git & GitHub** (Controle de versão)

---

## 🎯 Escopo da Automação (20 Testes Implementados)
A suíte cobre os principais fluxos funcionais da aplicação:
1. **Autenticação e Mesa:** Validação de login, criação de sala/mesa e restrições de campos obrigatórios (pop-up de alerta).
2. **Rolagem de Dados:** Testes para dados padrão (`d4`, `d6`, `d8`, `d10`, `d12`, `d20`, `d100`).
3. **Modificadores e Comandos Personalizados:** Parametrização para comandos complexos (ex: `1d6+2`, `3d6+5`) validando os limites mínimos e máximos esperados.
4. **Contadores e Modificadores de Bônus:** Incremento e decremento de valores de bônus e quantidade de dados, além do botão de reset (`zerar`).
5. **Navegação e Sessão:** Testes de abertura do modal de configurações, fluxo de sair da sala e reconexão.

---

## 📂 Arquitetura do Projeto (Page Object Model)
```text
📦 Projeto-Ready2Reload
 ┣ 📂 .venv               # Ambiente virtual Python
 ┣ 📜 data.py             # Massa de dados e URLs centralizadas
 ┣ 📜 page.py             # Classes de mapeamento de elementos (POM) e Ações
 ┣ 📜 main.py             # Arquivo central de testes (PyTest)
 ┗ 📜 README.md           # Documentação do projeto