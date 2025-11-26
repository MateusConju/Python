from fastapi import FastAPI, Depends
from .app import PageQuery

app = FastAPI()
PageQuery = dependencies.PageQuery

@app.get("/products")
def list_products(pager:PageQuery = Depends(PageQuery)):
    return {"offset": pager.offset, "limit": pager.size}

@app.get("/admin-zone")
def admin_dashboard():
    return {'msg': 'Seja Bem Vindo, Admin'}

@app.get("/editor-content")
def editor_content():
    return {'msg': 'Seja Bem Vindo, Editor'}