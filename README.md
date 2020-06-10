# quake_deaths

## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ ,pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone https://github.com/Luanlpg/quake_deaths.git`

- Acesse o repositório: `cd quake_deaths/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o Script de ranking

- Rode: `python processing`

## Rodando a API Flask

- Rode o servidor local com: `python app.py`

## Rodando os testes

- Com a API rodando, abra outro terminal e rode: `pytest -v`

## Endpoints da aplicação

- `GET /games` Retorna Lista com todos os jogos

- `GET /games/<ID>` Retorna jogo correspondente ao id
