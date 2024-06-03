# Telegram bot Factory ➤ 🐍 

Um template básico e simples para criação de bots do telegram.

## Indice:

1. [Iniciando](#iniciando);
2. [Estrutura](#estrutura);
3. [Stack](#stack);

### Iniciando

- Crie uma venv usando o comando `make create-venv`;
- Ative sua venv usando o comando `python3 source .venv/bin/activate`;
- Instale as dependências usando o comando `make install`;
- Use o [BotFather](https://t.me/botfather) para gerar seu token;
- Use o templete do arquivo `.env.example` para criar seu arquivo `.env`;
- Insira seu token no arquivo `.env`;
- Pronto, agora é só rodar usando o comando `make run`;
- Para gerar um novo arquivo de comando basta usar o comando `make gen NAME=NomeDoSeuComando`;

### Estrutura

A intenção deste repositório é dar um atalho para a criação de qualquer bot para o telegram que você pretenda criar.
A estrutura foi planejada para manter todos os comandos do bot em arquivos unicos dentro da pasta [commands](app/commands), e a configuração dos serviços na pasta [config](app/config/).
Tambem foi criado uma estrutura inicial para banco de dados usando o sqlite caso possua algum comando que seja nescessário manter dados salvos.

> OBS: Todos os comandos gerados automaticamente são incluidos no [construtor](app/commands/__init__.py) da pasta de comandos, caso deseje criar um comando na mão não esqueça de adiciona-lo no construtor para a aplicação percorre-lo

### Stack

Por se tratar de apenas um facilitador de criação de bots, toda a logica dos bots pertence a lib [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html)