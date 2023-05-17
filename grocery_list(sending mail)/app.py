import uvicorn
from scripts.config import Service

if __name__ == '__main__':
    uvicorn.run("main:app", host=Service.host, port=Service.port)
