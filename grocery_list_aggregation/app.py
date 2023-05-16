import uvicorn
from scripts.config import Service
host = Service.host
port = Service.port

if __name__ == '__main__':
    uvicorn.run("main:app", host=host, port=port, reload=True)
