from fastapi import FastAPI
from routers import users, products, routes, eco_actions

app = FastAPI(title="Eco App Backend with Firebase Auth")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(routes.router)
app.include_router(eco_actions.router)

@app.get("/")
def home():
    return {"message": "Eco App Backend Running with Firebase Auth"}
