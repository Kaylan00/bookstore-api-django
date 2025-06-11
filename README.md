# API de Livraria (Bookstore API)

Uma API RESTful simples e robusta para gerenciar o catálogo de uma livraria, construída com Django, Django REST Framework e Docker.

## Descrição

Este projeto é uma API completa de livraria que permite aos usuários navegar por livros, autores e gêneros. Usuários autenticados podem se registrar, fazer login, adicionar novos livros ao catálogo e escrever avaliações (reviews). O projeto conta com um sistema de permissões robusto, garantindo que usuários só possam modificar o conteúdo que eles mesmos criaram. A API também é equipada com filtros avançados, validadores e é totalmente documentada via Swagger UI.

## Funcionalidades Principais

-   **Ambiente Dockerizado:** Totalmente containerizado com Docker e Docker Compose para uma configuração fácil e um desenvolvimento consistente.
-   **API RESTful:** Construída com Django REST Framework, seguindo os princípios REST.
-   **Operações CRUD Completas:** Funcionalidades de Criar, Ler, Atualizar e Deletar para Livros, Autores, Gêneros e Reviews.
-   **Autenticação de Usuário:** Sistema de autenticação por token para registro (`/api/auth/register`) e login (`/api/auth/login`).
-   **Permissões Avançadas:** Sistema de permissão customizado (`IsOwnerOrReadOnly`) que garante que um usuário só possa editar ou apagar suas próprias contribuições (livros e reviews).
-   **Relacionamento de Dados Rico:** Utiliza `ForeignKey` e `ManyToManyField` para criar uma estrutura de dados lógica e flexível.
-   **Filtros Avançados:** Poderosas capacidades de filtragem na listagem de livros, incluindo por nome do gênero, busca por parte do título e por intervalo de datas (`start_date`/`end_date`).
-   **Validação de Dados:** Validadores customizados para garantir a integridade dos dados em campos como ISBN e data de publicação.
-   **Documentação Automática da API:** Documentação interativa disponível via Swagger UI, gerada automaticamente a partir do código.

## Tecnologias Utilizadas

-   **Backend:** Python, Django, Django REST Framework
-   **Banco de Dados:** PostgreSQL
-   **Containerização:** Docker, Docker Compose
-   **Documentação da API:** drf-spectacular (Swagger/OpenAPI)
-   **Filtragem:** django-filter

## Como Iniciar o Projeto

Você pode rodar este projeto de duas maneiras: usando Docker (método recomendado e mais simples) ou configurando o ambiente manualmente em sua máquina.

### Método 1: Com Docker (Recomendado)

**Pré-requisitos:**
-   [Git](https://git-scm.com/)
-   [Docker](https://www.docker.com/products/docker-desktop/)
-   [Docker Compose](https://docs.docker.com/compose/)

**Instalação:**
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Kaylan00/bookstore-api-django.git](https://github.com/Kaylan00/bookstore-api-django.git)
    cd bookstore-api-django
    ```

2.  **Crie o arquivo de ambiente (`.env`):**
    Crie um arquivo chamado `.env` na raiz do projeto e cole o seguinte conteúdo:
    ```ini
    # .env
    POSTGRES_DB=bookstore
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    DB_NAME=bookstore
    DB_USER=user
    DB_PASSWORD=password
    DB_HOST=db
    DB_PORT=5432
    ```

3.  **Construa e execute os containers:**
    ```bash
    docker-compose up -d --build
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    docker-compose exec app python manage.py migrate
    ```

5.  **Crie um superusuário:**
    ```bash
    docker-compose exec app python manage.py createsuperuser
    ```

### Método 2: Manualmente (Sem Docker)

**Pré-requisitos:**
-   [Git](https://git-scm.com/)
-   Python 3.11+
-   PostgreSQL instalado e rodando na sua máquina.

**Instalação:**
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Kaylan00/bookstore-api-django.git](https://github.com/Kaylan00/bookstore-api-django.git)
    cd bookstore-api-django
    ```

2.  **Configure o Banco de Dados PostgreSQL:**
    Você precisará criar um banco de dados e um usuário no seu PostgreSQL local. Usando `psql`, os comandos seriam parecidos com estes:
    ```sql
    CREATE DATABASE bookstore;
    CREATE USER user WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE bookstore TO user;
    ```

3.  **Crie e ative um ambiente virtual Python:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Crie e configure o arquivo de ambiente (`.env`):**
    Crie o arquivo `.env` e **lembre-se de alterar o `DB_HOST` para `localhost`**, pois o banco de dados está rodando na sua própria máquina.
    ```ini
    # .env
    POSTGRES_DB=bookstore
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    DB_NAME=bookstore
    DB_USER=user
    DB_PASSWORD=password
    DB_HOST=localhost # <-- MUDANÇA IMPORTANTE
    DB_PORT=5432
    ```
    *Para que o Django leia este arquivo fora do Docker, você precisará carregar essas variáveis no seu terminal antes de iniciar o servidor, por exemplo, com o comando `export $(cat .env | xargs)`.*

6.  **Execute os comandos do Django:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```
### Executando a Aplicação

A aplicação agora deve estar rodando em `http://localhost:8000`.

-   **Admin do Django:** `http://localhost:8000/admin/`
-   **Raiz da API:** `http://localhost:8000/`
-   **Documentação da API (Swagger UI):** `http://localhost:8000/swagger`

## Principais Endpoints da API

| Método | URL                            | Descrição                                         |
| :----- | :----------------------------- | :-------------------------------------------------- |
| `POST` | `/api/auth/register/`          | Registra um novo usuário.                           |
| `POST` | `/api/auth/login/`             | Faz login para obter um token de autenticação.       |
| `GET`  | `/api/books/`                  | Lista todos os livros. Suporta filtros.             |
| `POST` | `/api/books/`                  | Cria um novo livro (Requer autenticação).         |
| `GET`  | `/api/books/{id}/`             | Retorna os detalhes de um livro específico.         |
| `PUT`  | `/api/books/{id}/`             | Atualiza um livro (Requer ser o dono).              |
| `DELETE`  | `/api/books/{id}/`             | Apaga um livro (Requer ser o dono).                 |
| `GET`  | `/api/reviews/`                | Lista todos os reviews.                             |
| `POST` | `/api/reviews/`                | Cria um novo review (Requer autenticação).        |

*(Endpoints para `authors` e `genres` seguem uma estrutura similar.)*

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
