@app.get("/hello")
def hello():
    return {"message": "hello depuis la version déployée sur Azure"}