from fastapi import FastAPI
from scripts.core.services.billing_services import item_router
import uvicorn
app = FastAPI()

app.include_router(item_router)

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
