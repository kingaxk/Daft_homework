# main.py

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}