from fastapi import FastAPI, Depends
from app.context import ServerContext

app = FastAPI()

def get_server_context():
    return ServerContext()

@app.post("/data")
def create_data(item: dict, context: ServerContext = Depends(get_server_context)):
    result = context.service.create_data(item)
    return result

@app.get("/data")
def read_data(context: ServerContext = Depends(get_server_context)):
    result = context.service.get_all_data()
    return result