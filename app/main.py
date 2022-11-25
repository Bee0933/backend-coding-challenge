# pylint: disable=import-error
from endpoints import router
from fastapi import FastAPI
import uvicorn

# app instance
app = FastAPI()

# include routers
app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8001)
