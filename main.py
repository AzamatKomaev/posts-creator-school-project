from fastapi import FastAPI  # импортируем сторонние модули

app = FastAPI()  # создаем объект app


# создаем функцию, которая будет выводить "I am working"
# каждый раз, когда пользователь будет переходить по адресу
# http://{домен}/
@app.get("/")
def test_route():
    return "I am working!"
