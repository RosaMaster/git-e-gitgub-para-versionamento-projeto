### Branch no Git

Uma **branch (ramificação)** no Git é uma linha paralela de desenvolvimento que permite que você trabalhe em diferentes funcionalidades, correções de bugs ou experimentos de forma isolada do código principal. Cada branch pode ter seu próprio conjunto de commits e histórico de alterações

<br>

#### Vantagens do Uso de Branches

- **Isolamento**: Permite trabalhar em diferentes funcionalidades ou correções de bugs sem interferir no código principal

- **Colaboração**: Facilita a colaboração entre desenvolvedores, permitindo que cada um trabalhe em sua própria branch

- **Histórico**: Mantém um histórico claro e organizado das mudanças feitas no projeto

- **Flexibilidade**: Permite experimentar novas ideias ou tecnologias sem afetar o código principal

`Branches são uma ferramenta poderosa no Git que ajudam a organizar e gerenciar o desenvolvimento de software de forma eficiente e colaborativa`

<br>

#### Tipos de Branches

- **Branch principal**: Geralmente chamada de **main** ou **master**, é a linha principal de desenvolvimento<br>

    ´normalmente utilizada para o ambiente produtivo´

- **Branch de feature**: Criada a partir da branch principal para desenvolver novas funcionalidades

- **Branch de bugfix**: Criada para corrigir bugs específicos

- **Branch de release**: Usada para preparar uma nova versão de lançamento

<br>

#### Comandos Básicos

Criar uma nova branch

~~~bash
git checkout -b nome-da-branch
~~~

Mudar para uma branch existente

~~~bash
git checkout nome-da-branch
~~~

Listar todas as branches

~~~bash
git branch
~~~

Deletar uma branch

~~~bash
git branch -d nome-da-branch
~~~

Mesclar uma branch

~~~bash
git checkout main
git merge nome-da-branch
~~~

Veja um exemplo de fluxo de trabalho com branches [AQUI](./fluxo-de-trabalho-com-branches.md)
