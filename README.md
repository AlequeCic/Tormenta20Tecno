# API de Fichas de Personagem de Tormenta 20

Essa é uma API simples feita em Django + Django REST Framework para gerenciar fichas de personagens do sistema Tormenta 20. 

---

## Funcionalidades

- Criar fichas de personagem
- Listar fichas cadastradas
- Atualizar informações da ficha
- Deletar fichas
- Endpoints com documentação via Swagger

---

## Tecnologias usadas

- Python 3.10+
- Django
- Django REST Framework
- drf-yasg (para documentação Swagger)

---
1.**Clone o repositório:**

```bash
git clone https://github.com/AlequeCic/Tormenta20Tecno.git
cd seu-repositorio
```

2.**Crie um ambiente virtual:**

```bash
# Criação do ambiente virtual
python -m venv venv

# Ativação do ambiente:
venv\Scripts\activate
```

3.**Instale as dependências do projeto:**

```bash
pip install -r requirements.txt
```

4.**Aplique as migrações do banco de dados:**

```bash
python manage.py migrate
```

5.**Inicie o servidor de desenvolvimento:**

```bash
python manage.py runserver
```

## Depois disso, você poderá acessar:

- API de fichas: http://127.0.0.1:8000/api/fichas/
- Documentação Swagger: http://127.0.0.1:8000/docs/

