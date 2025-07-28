from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"User ID received: {user_id}"}

@app.get("/search")
def search_name(name: str):
    return {"message": f"Searching for: {name}"}

@app.get("/users/{user_id}/details")
def user_details(user_id: int, show_email: bool = False):
    return {
        "user_id": user_id,
        "show_email": show_email
    }
