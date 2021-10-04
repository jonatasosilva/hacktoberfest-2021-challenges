# Contribuindo

## Preparação

#### 1. Faça um fork do repositório
[Bifurcar um repo - GitHub Docs](https://docs.github.com/pt/github/getting-started-with-github/quickstart/fork-a-repo)

#### 2. Crie um clone do seu fork
```sh
git clone https://github.com/SEU-USERNAME/hacktoberfest-2021-challenges
```

## Resolvendo um desafio

#### 1. Crie uma branch no formato desafio/linguagem/seu username
```sh
# Exemplo com o desafio de recursão em Elixir
git checkout -b recursao/elixir/GustavoGarciaPereira main
```

#### 2. Crie os diretórios no mesmo formato do passo anterior
```sh
# Exemplo com o desafio de recursão em Elixir
mkdir recursao/elixir/GustavoGarciaPereira
```

#### 3. Adicione o seu código no diretório

#### 4. Faça o commit das alterações
```sh
git add .
```

```sh
git commit -m 'Finalizando o desafio'
```

#### 5. Faça o push da sua branch
```sh
# Exemplo com o desafio de recursão em Elixir
git push origin recursao/elixir/GustavoGarciaPereira
```

#### 6. Crie um pull request
[Criando uma pull request a partir de uma bifurcação - GitHub Docs](https://docs.github.com/pt/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

## Atualizando o seu fork
Quando novos desafios forem incluídos você terá que atualizar o seu fork

#### 1. Configure um remote para sincronizar alterações no fork
```sh
git remote add upstream https://github.com/return-forty-two/hacktoberfest-2021-challenges.git
```

#### 2. Sincronize as alterações no fork
```sh
git checkout main
```

```sh
git fetch upstream
```

```sh
git merge upstream/main
```

[Sincronizar uma bifurcação - GitHub Docs](https://docs.github.com/pt/github/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

## Dúvidas
Se tiver dúvidas você pode enviá-las no Discord.
