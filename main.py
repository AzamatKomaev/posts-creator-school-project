import sys
import pathlib

from fastapi import FastAPI  # импортируем сторонние модули

app = FastAPI()  # создаем объект app


current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(current_dir))

# создаем функцию, которая будет выводить "I am working"
# каждый раз, когда пользователь будет переходить по адресу
# http://{домен}/
@app.get("/")
def test_route():
    return "I am working!"
