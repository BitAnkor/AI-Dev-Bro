from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.visits import increment_visits
from app.comments import load_comments, save_comment
from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    count = increment_visits()
    return templates.TemplateResponse("index.html", {"request": request, "visits": count})

@app.get("/feedback")
def feedback_form(request: Request):
    comments = load_comments()
    return templates.TemplateResponse("feedback.html", {"request": request, "comments": comments})

@app.post("/feedback")
def submit_comment(name: str = Form(...), comment: str = Form(...), rating: int = Form(...)):
    save_comment(name,comment,rating)
    return RedirectResponse("/feedback", status_code=303)