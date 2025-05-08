📝 Blog com Django

Este projeto é um sistema de blog desenvolvido com o framework Django. A aplicação permite criação de contas, postagens, comentários e gerenciamento de perfil, sendo ideal para praticar e consolidar conhecimentos em desenvolvimento web com Django.
🔧 Funcionalidades Implementadas

    Cadastro, login e logout de usuários;

    CRUD completo de usuários, postagens e imagem de perfil;

    Upload de imagens nos posts;

    Página de perfil com informações editáveis;

    Sistema de comentários por post;

    Interface simples e funcional.

🗂 Estrutura do Projeto

    accounts/: gerenciamento de usuários e perfis;

    posts/: sistema de postagens e comentários;

    templates/: HTML renderizado com suporte a Bootstrap;

    media/: armazenamento local de arquivos enviados.

🛠 Tecnologias Utilizadas

    Python 3.10+

    Django 4.x

    SQLite (com suporte futuro para PostgreSQL)

    HTML5, CSS3, Bootstrap 5

    JavaScript (mínimo)



Como Executar Localmente

1. Clone o repositório:
   
    git clone https://github.com/vtrdll/blog.git

    cd blog

3. Crie e ative um ambiente virtual:

    python -m venv venv

    source venv/bin/activate  # Linux/Mac

    venv\Scripts\activate     # Windows

3. Instale as dependências:
   
    pip install -r requirements.txt

5. Aplique as migrações:
   
    python manage.py makemigrations
  
    python manage.py migrate

6. Crie um superusuário (opcional):
   
   python manage.py createsuperuser

8. Execute o servidor:
   
   python manage.py runserver

   Acesse http://127.0.0.1:8000/ no navegador para usar o blog.



🖼 Capturas de Tela
![HOME](https://github.com/user-attachments/assets/9d9fa2ee-85d1-4808-884a-18920d9f592d)
![Comments](https://github.com/user-attachments/assets/d6bf5c9f-90d4-46a7-987e-52b3de7f99e8)
![ConfigAccount](https://github.com/user-attachments/assets/e45d6a8c-de2e-480a-b82c-4f050a5c0267)
































    
