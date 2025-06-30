# Site de Filmes em Python

Este projeto é um site de filmes feito com Flask e integração com a API gratuita TMDb.

## Funcionalidades
- Buscar filmes por nome
- Exibir detalhes e pôster dos filmes
- Frontend simples em HTML/CSS

## Como usar
1. Crie uma conta gratuita em https://www.themoviedb.org/ para obter sua chave de API (API Key).
2. Crie um arquivo `.env` na raiz do projeto com o conteúdo:
   ```
   TMDB_API_KEY=coloque_sua_chave_aqui
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o site:
   ```bash
   flask run
   ```
5. Acesse em http://localhost:5000

## Estrutura
- `app.py`: Backend Flask
- `templates/`: HTML
- `static/`: CSS

