from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.visits import increment_visits
from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    count = increment_visits()
    return templates.TemplateResponse("index.html", {"request": request, "visits": count})

@app.get("/feedback")
async def feedback(request: Request):
    return templates.TemplateResponse("feedback.html", {"request": request})



@app.get("/projects")
def projects(request: Request):
    proyectos = [
        {
            "titulo": "AI Dev Bro",
            "descripcion": "Asistente IA que presenta tu portafolio y ayuda en tu búsqueda laboral.",
            "repositorio": "https://github.com/BitAnkor/AI-Dev-Bro",
            "tags": ["FastAPI", "Tailwind", "OpenAI"]
        },
        {
            "titulo": "Otro Proyecto",
            "descripcion": "Descripción breve de otro proyecto.",
            "repositorio": "#",
            "tags": ["Python", "MongoDB"]
        },
    ]
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "proyectos": proyectos
    })


