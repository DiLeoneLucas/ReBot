# 🤖 ReBot — Automação de Redefinição de Senhas no Microsoft Intune

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)
![Microsoft Intune](https://img.shields.io/badge/Microsoft%20Intune-0078D4?style=flat&logo=microsoft&logoColor=white)

## 📌 Sobre o projeto

O **ReBot** é uma ferramenta de automação desenvolvida em Python para agilizar o processo de redefinição de senhas de usuários em lote no ambiente Microsoft Intune.

A solução utiliza a biblioteca **Pandas** para realizar a leitura e o processamento de uma lista de usuários disponibilizada em arquivo CSV e o **Selenium** para automatizar as operações realizadas no navegador.

O objetivo principal é reduzir o trabalho operacional repetitivo, aumentar a produtividade da equipe de suporte técnico e otimizar atividades relacionadas ao gerenciamento de contas de usuários.

## 🎯 Objetivos

- Automatizar a redefinição de senhas em lote.
- Processar listas de usuários através de arquivos CSV.
- Reduzir intervenções manuais nas atividades de suporte.
- Diminuir o tempo necessário para execução de tarefas repetitivas.
- Aumentar a produtividade da equipe de TI.
- Padronizar processos operacionais de atendimento.

## ⚙️ Funcionamento

O fluxo de funcionamento da ferramenta é dividido em etapas:

1. **Inicialização:** abertura do Google Chrome com depuração remota habilitada.
2. **Leitura dos dados:** utilização do Pandas para carregar os usuários disponibilizados em CSV.
3. **Automação:** utilização do Selenium para interagir com o navegador e executar as operações no Microsoft Intune.
4. **Processamento em lote:** execução sequencial das redefinições de senha dos usuários selecionados.

## 📊 Resultados

De acordo com os resultados obtidos no ambiente de utilização, a ferramenta apresenta capacidade de processamento de aproximadamente:

| Indicador | Resultado |
|---|---:|
| Redefinições de senha | 240 |
| Tempo estimado | 1 hora |
| Média de processamento | 4 usuários por minuto |

A produtividade pode variar conforme a conexão, o desempenho do ambiente e o tempo de resposta do Microsoft Intune.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal da automação. |
| Pandas | Leitura e processamento dos arquivos CSV. |
| Selenium | Automação das interações com o navegador. |
| Google Chrome | Navegador utilizado na execução da automação. |
| Microsoft Intune | Ambiente de gerenciamento de usuários e redefinição de senhas. |

## 📂 Estrutura do repositório

```text
ReBot/
│
├── Scripts/
│   └── Scripts de automação Python
│
├── Abre chrome.bat
│
└── .gitignore
```

## 🚀 Pré-requisitos

Para executar o projeto, é necessário:

- Windows.
- Python instalado.
- Google Chrome instalado.
- Bibliotecas Pandas e Selenium.
- Acesso autorizado ao ambiente Microsoft Intune.
- Permissões necessárias para realizar a redefinição de senhas.

## ▶️ Inicialização

O repositório disponibiliza o arquivo `Abre chrome.bat`, utilizado para iniciar o Google Chrome com a porta de depuração remota `9222`.

Para iniciar:

1. Abra o diretório do projeto.
2. Execute `Abre chrome.bat`.
3. Aguarde a inicialização do navegador.
4. Execute os scripts Python conforme a configuração do ambiente.

## 🔐 Segurança

Como a ferramenta realiza operações administrativas relacionadas a contas de usuários, alguns cuidados são fundamentais:

- Utilizar exclusivamente em ambientes autorizados.
- Proteger os arquivos CSV utilizados no processamento.
- Não armazenar senhas ou credenciais diretamente no código.
- Não compartilhar informações pessoais dos usuários.
- Restringir o acesso aos arquivos e ao ambiente de execução.
- Garantir que as operações sejam realizadas por profissionais autorizados.

## 👨‍💻 Desenvolvedor

**Lucas Fernandes Di Leone**

Desenvolvimento de soluções de automação e otimização de processos de Tecnologia da Informação.

- GitHub: https://github.com/DiLeoneLucas
- LinkedIn: https://www.linkedin.com/in/lucas-fernandes-di-leone/

---

**ReBot — Automatizando processos, otimizando o suporte técnico e aumentando a produtividade da TI.**
