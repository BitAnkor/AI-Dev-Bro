from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx

# Cargar .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Instancia de FastAPI
app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Plantillas Jinja2
templates = Jinja2Templates(directory="app/templates")

# CORS (si usas frontend separado o deploy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cámbialo si usas dominio propio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Rutas de frontend (Jinja2) ----------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/portfolio", response_class=HTMLResponse)
async def portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request})



# ---------- Ruta API para el Copilot ----------

@app.post("/api/copilot")
async def copilot_api(request: Request):
    body = await request.json()
    question = body.get("question")

    if not question:
        return JSONResponse({"error": "Falta pregunta"}, status_code=400)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": question}],
                "temperature": 0.7
            }
        )

    if response.status_code != 200:
        return JSONResponse({"error": "Error al conectar con OpenAI"}, status_code=500)

    return response.json()


