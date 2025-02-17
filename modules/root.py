from .settings import app

# відправляємо сповіщення на головну сторінку веб-сайту 
@app.get("/")
async def get_response():
    return {"name": "Masha"}