from fastapi import FastAPI

from scripts.services.gt_services import gt_router

app = FastAPI()

app.include_router(gt_router)
