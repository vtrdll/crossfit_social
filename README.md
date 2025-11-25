<h1 align="center">🏋️‍♂️ Blog CrossFit – Projeto Django</h1>

<p align="center">
  Sistema completo de blog desenvolvido com <strong>Django</strong>, voltado para treinos e ambiente CrossFit.<br>
  Inclui contas, postagens, eventos, times, WOD e muito mais.
</p>

<hr>

<h2>📦 Apps do Projeto</h2>

<h3>🔐 Accounts</h3>
<ul>
  <li>Perfis de usuário</li>
  <li>Gerenciamento de Times</li>
  <li>Gerenciamento de Box (academias)</li>
</ul>

<h3>💬 Social</h3>
<ul>
  <li>Postagens</li>
  <li>Comentários</li>
  <li>Stories (imagens e vídeos)</li>
</ul>

<h3>🏋️ WOD</h3>
<ul>
  <li>Movimentos</li>
  <li>Workouts (WOD – Workout of the Day)</li>
</ul>

<h3>📅 Event</h3>
<ul>
  <li>Criação e edição de eventos</li>
</ul>

<p>✔️ Todos os apps possuem CRUD completo.</p>

<hr>

<h2>🛠 Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.10+</li>
  <li>Django 4.x</li>
  <li>SQLite (suporte futuro para PostgreSQL)</li>
  <li>Bootstrap 5</li>
  <li>HTML5, CSS3, JavaScript</li>
  <li>Redis + Celery</li>
</ul>

<hr>

<h2>🚀 Como Executar Localmente</h2>

<h3>1. Clone o repositório</h3>
<pre>
git clone https://github.com/vtrdll/blog.git
cd blog
</pre>

<h3>2. Crie e ative o ambiente virtual</h3>
<pre>
python -m venv venv
</pre>

<p><strong>Linux/macOS:</strong></p>
<pre>source venv/bin/activate</pre>

<p><strong>Windows:</strong></p>
<pre>venv\Scripts\activate</pre>

<h3>3. Instale as dependências</h3>
<pre>pip install -r requirements.txt</pre>

<hr>

<h3>4. Popule os Movimentos (WOD)</h3>

<pre>
python manage.py shell
</pre>

<pre>
from WOD.scripts import populate_movements
populate_movements()
exit()
</pre>

<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<hr>

<h3>5. Ative Redis e Celery</h3>

<p>Verifique se o Redis está funcionando:</p>

<pre>redis-cli ping</pre>

<p>Se retornar <code>PONG</code>, está ok.</p>

<h4>Abra dois terminais (com a venv ativada):</h4>

<p><strong>Celery Worker</strong></p>
<pre>celery -A app worker --loglevel=info</pre>

<p><strong>Celery Beat</strong></p>
<pre>celery -A app beat --loglevel=info</pre>

<hr>

<h3>6. Crie um superusuário</h3>
<pre>python manage.py createsuperuser</pre>

<h3>7. Execute o servidor</h3>
<pre>python manage.py runserver</pre>

<p>Acesse: <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>

<hr>

<h2>🖼 Capturas de Tela</h2>

<h3>📋 Criar Conta</h3>
<img width="1905" src="https://github.com/user-attachments/assets/150edfe8-ebdb-450f-bd8d-cfbe13159d94"/>

<h3>🧑‍🏫 Editar Perfil</h3>
<img width="1896" src="https://github.com/user-attachments/assets/1fefa5ec-e5e7-4732-887d-7f74ff7a9643"/>

<h3>📝 Criar Post</h3>
<img width="1903" src="https://github.com/user-attachments/assets/42b43ef0-3f33-433e-8ea6-a0d5a99f3454"/>

<h3>🏋️ Criar Time</h3>
<img width="1888" src="https://github.com/user-attachments/assets/20913b44-f076-46f9-8c17-e3b402c60914"/>

<h3>✏️ Editar Time</h3>
<img width="1904" src="https://github.com/user-attachments/assets/be899388-79a8-475b-9ecc-8cda7d5d7d02"/>

<h3>📅 Criar Evento</h3>
<img width="1888" src="https://github.com/user-attachments/assets/7c5a9212-09a0-45b8-b427-3eb7f87cc591"/>

<h3>🔍 Detalhar Evento</h3>
<img width="1911" src="https://github.com/user-attachments/assets/5274ea86-3845-4c73-b282-b2fa700c81ec"/>

<h3>🏋️ Postar WOD</h3>
<img width="1895" src="https://github.com/user-attachments/assets/f5804786-a404-4f8d-9424-25eeba0ba4f3"/>

<h3>🏋️ Criar BOX (Apenas ADMIN)</h3>
<img width="1907" src="https://github.com/user-attachments/assets/a0b2ece6-d08c-46ef-a4c6-48aa65efd5f6" />






<h2>📜 Licença</h2>
<p>Projeto livre para estudo, modificação e aprendizado.</p>

<hr>

<h2>🤝 Contribua</h2>
<p>Pull requests, issues e sugestões são sempre bem-vindas!</p>

