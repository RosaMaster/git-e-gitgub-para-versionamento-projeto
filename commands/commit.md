### Commits no Git

Um **commit** em um repositório **git** registra uma fotografia (snapshot) de todos os arquivos no seu diretório. É como um grande copy&paste, mas ainda melhor!

O **Git** tem por objetivo manter os **commits** tão leves quanto possível, de forma que ele não copia cegamente o diretório completo toda vez que você commita. Ele pode (quando possível) comprimir um commit como um conjunto de mudanças (ou um "delta") entre uma versão do seu repositório e a seguinte.

O **Git** também mantém um histórico de quando ocorreu cada commit. É por isso que a maioria dos commits tem ancestrais acima de si -- que indicamos usando setas na nossa visualização. Manter a história é ótimo para todos que trabalham no projeto!

Há muito para aprender, mas por enquanto pense nos commits como snapshots do seu projeto. Os commits são muito leves, e mudar de um para outro é extremamente rápido!

<br>

#### Comitando todos os arquivos

Antes de realizar o commit execute o comando para verificar e validar  os arquivos alterados use

~~~bash
git status
~~~

Adicione todos os arquivos modificados ao staging area

~~~bash
git add .
~~~

Faça o commit das alterações com uma mensagem descritiva

~~~bash
git commit -m "Sua mensagem de commit"
~~~

<br>

#### Comitando arquivo específico

Para fazer o commit de um arquivo específico no Git, siga os passos abaixo

~~~bash
git add caminho/do/arquivo
~~~

Faça o commit das alterações com uma mensagem descritiva

~~~bash
git commit -m "Sua mensagem de commit"
~~~

´Substitua caminho/do/arquivo pelo caminho do arquivo que você deseja adicionar e "Sua mensagem de commit" por uma descrição significativa das alterações feitas´

