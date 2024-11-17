from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Pawel"}


@app.get("/health-check")
async def health():
    return {"message":"All is well"}
