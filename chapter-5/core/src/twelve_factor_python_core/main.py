from fastapi import FastAPI, status

app = FastAPI()


@app.get("/data/{location_id}")
def read_data(location_id: str):
    return {"data": [123]}


@app.post("/data/{location_id}", status_code=status.HTTP_201_CREATED)
def post_item(location_id: str, data: dict):
    return data
