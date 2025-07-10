# 💬 Real-Time Chat Application

A basic real-time chat application built with **Django**, **Channels**, **Redis**, and **PostgreSQL**.  
Users can join chat rooms, send and receive messages instantly, and experience WebSocket-based communication in action.

---

## 🚀 Features

- 🔐 User chat rooms with unique names
- 💬 Real-time message exchange using WebSockets
- 🧠 Built on Django + Channels
- ⚡ Redis-backed channel layer
- 🗃️ PostgreSQL for data persistence
- 📜 Minimal, clean interface for quick testing

---

## 🛠️ Tech Stack

| Technology     | Description                        |
|----------------|------------------------------------|
| 🐍 Django       | Web framework (Python)             |
| ⚡ Django Channels | WebSockets support for Django     |
| 🧠 Redis        | Real-time messaging backend        |
| 🐘 PostgreSQL   | Relational database                |
| 🧩 HTML + JS    | Frontend for room & messaging      |

---

## 📂 Project Structure
```
Chat Application/
├── chat/
│ ├── consumers.py # WebSocket handling
│ ├── routing.py # WebSocket URL routes
│ └── views.py # Basic views
├── chat_project/
│ ├── settings.py # Django settings
│ ├── urls.py # App URL conf
│ └── asgi.py # ASGI config for Channels
├── templates/
│ └── chat_test.html # UI for chat room
├── static/ # (optional) CSS/JS assets
├── manage.py
└── requirements.txt
```


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Shashank-712/Chat-Application.git
cd Chat-Application
```
### 2. Create & Activate Virtual Environment
```
python -m venv env
.\env\Scripts\activate   # On Windows
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run Redis Server
```
Make sure Redis is running (via Memurai or Redis CLI):
memurai.exe             # or redis-server.exe
```
### 5. Run the Django App
```
python manage.py migrate
daphne -p 8000 chat_project.asgi:application
```
### 6. Open in Browser
```
Go to: http://127.0.0.1:8000/chat_test/
```
Enter a room name and start chatting 🎉
---
🙌 Acknowledgements
```
Django

Channels

Redis

Memurai (for Windows Redis alternative)
```

💡 Future Enhancements
```
User authentication

Persist chat messages to DB

Add private messaging

Improve frontend with Tailwind or React

Persist chat messages to DB

Add private messaging

Improve frontend with Tailwind or React
```
🙌 Author Made with 💻 by Shashank Rawat👹👉 🔗 github.com/Shashank-712




