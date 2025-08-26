🎓 College Finder Backend

AI-powered college recommendation and comparison platform using Django REST API and Ollama AI (LLaMA 3.2 model).

✅ Key Features

Role-based Access:

Student → Enter details, view AI recommendations, save favorites

Parent → Linked to student profile

Admin → Manage all college data

College Search & Filters: By location, courses, budget, and facilities

AI-Powered Comparison: Ollama suggests the best-fit colleges

Favorites & Analytics:

Save and track favorites

Monitor trends and engagement

🛠 Tech Stack

Backend: Django, Django REST Framework

AI: Ollama with LLaMA 3.2 model

Database: PostgreSQL or SQLite

Dependency Manager: uv
 (recommended) or pip

📦 Installation
1. Clone Repository
git clone https://github.com/your-username/college-finder-backend.git
cd college-finder-backend

2. Set up environment

Using uv:

uv init
uv add django djangorestframework requests


Or pip:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt

3. Configure Settings

In settings.py:

OLLAMA_API_URL = "http://localhost:11434/api/generate"

4. Migrate & Run
python manage.py migrate
python manage.py runserver

🔑 API Endpoints
AI Features
Endpoint	Method	Description
/api/recommend-colleges/	POST	Recommend colleges by location & preferences
/api/compare-colleges/	POST	Compare multiple colleges using AI
✅ Example: Recommend Colleges
curl -X POST http://127.0.0.1:8000/api/recommend-colleges/ \
-H "Content-Type: application/json" \
-d '{
  "location": "Kathmandu",
  "preferences": "Affordable tuition, good hostel facilities"
}'

✅ Example: Compare Colleges
curl -X POST http://127.0.0.1:8000/api/compare-colleges/ \
-H "Content-Type: application/json" \
-d '{
  "college_ids": [1, 2, 3],
  "preferences": "Strong engineering faculty, low fees"
}'

📊 Analytics

Popular colleges by searches & favorites

AI recommendation usage stats

User activity tracking

🤖 Ollama Setup

Install Ollama: https://ollama.com/download

Pull the model:

ollama pull llama3.2


Start Ollama service:

ollama serve

🏗 Project Architecture
Client (Web/Mobile)
       |
       v
Django REST API -----> Database (PostgreSQL)
       |
       v
   Ollama AI Engine


(Can replace with a diagram image if needed.)

✅ Future Roadmap

Student application tracking

Advanced analytics dashboard

Recommendation fine-tuning with user feedback

Parent monitoring features

📄 License

MIT License – free to use and modify.
