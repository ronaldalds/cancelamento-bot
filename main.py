from fastapi import FastAPI

from api.urls import api_router_v1
from core.settings import settings

app = FastAPI()
app.include_router(api_router_v1, prefix="/cancelamento/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port="8888", log_level="info", reload=True)