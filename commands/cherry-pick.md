### Comando git cherry-pick

O comando **git cherry-pick** é usado para aplicar commits específicos de uma branch em outra. Ele permite que você selecione commits individuais e os aplique a uma branch diferente, sem a necessidade de mesclar branches inteiras. Isso é útil quando você deseja aplicar correções de bugs ou funcionalidades específicas de uma branch para outra.

#### Usos Comuns do git cherry-pick

1. Aplicar um commit específico

`Este comando aplica o commit especificado pela hash à branch atual`

~~~bash
git cherry-pick <commit-hash>
~~~

2. Aplicar uma série de commits

`Este comando aplica todos os commits desde o commit inicial até o commit final (inclusive) à branch atual`

~~~bash
git cherry-pick <commit-hash-inicial>^..<commit-hash-final>
~~~

3. Aplicar múltiplos commits específicos

`Este comando aplica os commits especificados, um após o outro, à branch atual`

~~~bash
git cherry-pick <commit-hash-1> <commit-hash-2> <commit-hash-3>
~~~


Veja um exemplo prático do comando cherry-pick [AQUI](./exemplo-cherry-pick-pratico.md)

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#branch-no-git)
