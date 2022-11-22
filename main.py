import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def test_route():
    return 'It works'


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, log_level="info", reload=True)
