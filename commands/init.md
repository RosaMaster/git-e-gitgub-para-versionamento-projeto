### Comando git init

Para criar um repositório local e subir alterações para o GitHub, siga os passos abaixo

1. Criar um Repositório Local
    - Navegue até o diretório onde deseja criar o repositório

~~~bash
cd /caminho/do/diretorio
~~~

2. Inicialize um novo repositório Git

~~~bash
git init
~~~

3. Adicione arquivos ao repositório

~~~bash
git add .
~~~

4. Faça o primeiro commit

~~~bash
git commit -m "Primeiro commit"
~~~

5. Crie um Repositório no GitHub
    - Acesse o [GitHub](https://github.com/) e crie um novo repositório:
        - Vá para GitHub e clique em "New repository"
        - Dê um nome ao repositório e clique em "Create repository"

6. Conectar o Repositório Local ao GitHub
    - Adicione o repositório remoto

~~~bash
git remote add origin https://github.com/usuario/nome-do-repositorio.git
~~~

7. Verifique o repositório remoto

~~~bash
git remote -v
~~~

8. Subir Alterações para o GitHub
    - Envie as alterações para o repositório remoto:

~~~bash
git push -u origin main
~~~

#### Resumo dos Comandos

~~~bash
# Navegar até o diretório
cd /caminho/do/diretorio

# Inicializar um repositório Git
git init

# Adicionar arquivos ao repositório
git add .

# Fazer o primeiro commit
git commit -m "Primeiro commit"

# Adicionar o repositório remoto
git remote add origin https://github.com/usuario/nome-do-repositorio.git

# Verificar o repositório remoto
git remote -v

# Enviar as alterações para o repositório remoto
git push -u origin main
~~~

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comando-git-init)
