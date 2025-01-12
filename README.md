<!-- HEADER -->
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=A0153E&height=140&section=header" alt="header"/>


<!-- TITLE -->
<h2 align="center" alt="title">

    <head>    G I T   E   G I T H U B   P A R A   V E R S I O N A M E N T O   P R O J E T O S    </head>

</h2>


<!-- DESCRIBLE -->
**GIT**<br>
Git é um sistema de controle de versão distribuído, usado para rastrear mudanças no código-fonte durante o desenvolvimento de software. Ele permite que múltiplos desenvolvedores trabalhem em um projeto simultaneamente, mantendo um histórico completo de todas as alterações feitas no código. Git facilita a colaboração, o gerenciamento de versões e a recuperação de versões anteriores do código.

**Github**<br>
GitHub é uma plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git. Ele permite que desenvolvedores colaborem em projetos, revisem código, gerenciem tarefas e documentem seu trabalho. GitHub também oferece funcionalidades como integração contínua, deploy automatizado e uma comunidade ativa para compartilhar e contribuir com projetos de código aberto.

**Gitlab**<br>
GitLab é uma plataforma de DevOps completa que fornece repositórios Git, integração contínua (CI), entrega contínua (CD), gerenciamento de projetos e muito mais. Ele permite que equipes de desenvolvimento colaborem, revisem código, gerenciem tarefas e automatizem o ciclo de vida de desenvolvimento de software. GitLab pode ser hospedado na nuvem ou instalado localmente.

**AWS Codepipeline**<br>
AWS CodePipeline é um serviço de entrega contínua que ajuda a automatizar os pipelines de lançamento de software para atualizações rápidas e confiáveis. Ele permite que você modele, visualize e automatize as etapas necessárias para liberar seu software, desde a compilação e teste até a implantação. CodePipeline se integra com serviços da AWS e ferramentas de terceiros, facilitando a criação de fluxos de trabalho de entrega contínua.

<br>

<!-- LINKS UTEIS -->
| **Documentacao**                                              |
| ------------------------------------------------------------- |
| [Git](https://git-scm.com/)                                   |
| [Github](https://docs.github.com/pt)                          |
| [Gitlab](https://docs.gitlab.com/)                            |
| [AWS Codepipeline](https://docs.aws.amazon.com/codepipeline/) |
| [Git-School](https://github.com/git-school/visualizing-git)   |
| [GitHubDesktop](https://docs.github.com/pt/desktop)           |
| [Github Copilot](https://docs.github.com/pt/copilot)          |

<br>

| **Site de Treinamento**                                               | **Informação**                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Learn-Git-Branching](https://learngitbranching.js.org/?locale=pt_BR) | Este aplicativo foi desenvolvido para ajudar os iniciantes a aprender os poderosos conceitos por trás do branching com o git. Esperamos que você goste deste aplicativo e talvez até aprenda alguma coisa!                                                                               |
| [Visualize Git](https://git-school.github.io/visualizing-git/)        | Visualize Git ilustra o que está acontecendo por baixo dos panos quando você usa operações comuns do Git. Você verá exatamente o que está acontecendo com seu gráfico de commit. Nosso objetivo é dar suporte a todas as operações mais básicas do git, incluindo interação com remotos. |

<br>

<!-- EXTENSÕES -->
| **Extensão**                                                                                       | **Informação**                                                                                                                              |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)                     | Melhora o Git integrado no VS Code. Visualize o histórico de commits, anotações de linha, e muito mais.                                     |
| [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)                | Visualize o histórico de repositórios Git em um gráfico.                                                                                    |
| [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)         | Veja o histórico de commits, compare commits e visualize arquivos alterados.                                                                |
| [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) | Gerencie seus projetos e repositórios Git de forma eficiente.                                                                               |
| [Github Copilot](https://docs.github.com/pt/copilot)                                               | Você pode usar o GitHub Copilot para obter sugestões de preenchimento automático de um programador de par de IA à medida que cria o código. |

`OBS: Opinião pessoal gostei de utilizar o Git Graph`

<br>

<!-- Software e Plataforma -->
| **DOWNLOADS**                                                   |
| --------------------------------------------------------------- |
| [Git](https://git-scm.com/downloads)                            |
| [Github Desktop](https://desktop.github.com/download/)          |
| [Visual Studio Code](https://code.visualstudio.com/download)    |
| [Github Copilot for Studant](https://education.github.com/pack) |

<br>

#### **PASSO A PASSO GIT**

1. Instalar o software **GIT** no sistema operacional: [link](https://git-scm.com/downloads)
    - Baixar arquivo executável

2. Após instalado o software GIT 
    - `OBS: reiniciar a máquina se necessário`
    - Abra um prompt **CMD** ou **Git Bash** em qualquer diretório
        - Para abrir o terminal do **Git Bash**, clique com o botão direito do mouse e escolha a opção **Open Git Bash here**
    - -> execute o comando: **git --version**
    - Aparecerá algo como o exemplo: **git version 2.44.0.windows.1**
    - **Git Bash** instalado com sucesso!

3. Configurando o Git
    - Executar comandos abaixo~no **Git Bash**:

    ~~~bash
    git config --global user.name "Seu Nome"
    git config --global user.email "seu_email@exemplo.com"
    ~~~

    - Para validar a configuração do **GIT** execute

    ~~~bash
    git config --global --list
    ~~~

    - Deverá aparecer no terminal conforme exemplo abaixo:
    ~~~bash
    filter.lfs.clean=git-lfs clean -- %f
    filter.lfs.smudge=git-lfs smudge -- %f
    filter.lfs.process=git-lfs filter-process
    filter.lfs.required=true
    user.name=Seu Nome
    user.email=seu_email@exemplo.com
    ~~~

    - **Git Bash** configurado com sucesso!

4. Clonando um repositório no **Github**
    - Antes de clonar escolher o path LOCAL dentro de um diretório escolhido:
    - Após escolher o LOCAL, clique com o botão direito do mouse e escolha a opção **Open Git Bash here**
    - Para clonar um repositório com o **Git Bash**, basta executar o comando utilizando HTTPS do repositório que deseja clonar:

    ~~~bash
    git clone <URL-do-repositório>
    ~~~

    - EXEMPLO:

    ~~~bash
    git clone https://github.com/usuario/nome-do-repositorio.git
    ~~~

5. Criar uma **BRANCH** para alterar o projeto clonando a **BRANCH** principal com os quatro comandos abaixo:
    `Uma branch (ramificação) no Git é uma linha paralela de desenvolvimento que permite que você trabalhe em diferentes funcionalidades, correções de bugs ou experimentos de forma isolada do código principal. Cada branch pode ter seu próprio conjunto de commits e histórico de alterações.`

    ~~~bash
    git checkout main
    git fetch
    git pull
    git checkout -b nome-da-nova-branch
    ~~~

6. Comitando alterações do código
    `Um commit no Git é uma operação que salva as alterações feitas no código em um repositório. Cada commit cria um ponto no histórico do projeto, permitindo que você registre o estado atual do código e forneça uma mensagem descritiva sobre as mudanças realizadas.`

    - Comando ADD para preparar as alterações para comitar

    ~~~bash
    git add .
    ~~~

    - Comando commit para versionar alterações

    ~~~bash
    git commit -m "Sua mensagem de commit"
    ~~~

7. Enviando commites LOCAIS para um repositório REMOTO
    `O comando push no Git é usado para enviar commits locais para um repositório remoto. Isso atualiza o repositório remoto com as alterações feitas localmente, permitindo que outros colaboradores acessem e integrem essas mudanças.`

    ~~~bash
    git push origin nome-da-branch
    ~~~

8. Validar diretamente via link repositório se as alterações refletiram na **BRANCH** de origem

9. Seguir o fluxo de Pull Request e mergear alterações para as BRANCHs de cada ambiente
    `Um Pull Request (PR) é um processo no Git usado para revisar e integrar mudanças de uma branch para outra, geralmente da branch de feature para a branch principal (main ou master).`

    - Abrir um Pull Request: No repositório remoto (por exemplo, GitHub), navegue até a página do repositório e clique em "New Pull Request". Selecione a branch de origem e a branch de destino.


