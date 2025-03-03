from .settings import app, TEMPLATES
# from fastapi.responses import HTMLResponse
import fastapi.requests as requests

# відправляємо сповіщення на головну сторінку веб-сайту 
@app.get("/{name}")
async def get_response(name: str, request: requests.Request):
    return TEMPLATES.TemplateResponse(
        request= request,
        name = 'base.html',
        context= {'name': name}
    )




    # return HTMLResponse(content= '<h1>Головна сторінка</h1>')
    # return {"name": "Masha"}