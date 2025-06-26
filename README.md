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
LOGIN ![login](https://github.com/user-attachments/assets/ededc810-df8b-4e27-aeb8-d9d005c7fa9e)

HOME ![home](https://github.com/user-attachments/assets/60e5a652-a329-4702-b254-d3ad021906ee)

Comments ![Comments](https://github.com/user-attachments/assets/d6bf5c9f-90d4-46a7-987e-52b3de7f99e8)

My Perfil ![Meu-Perfil](https://github.com/user-attachments/assets/af4df200-59bb-41a7-8ce4-6f69c5ec1ac7)

Config Account ![ConfigAccount](https://github.com/user-attachments/assets/e45d6a8c-de2e-480a-b82c-4f050a5c0267)

































    
