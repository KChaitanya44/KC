from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io

app = FastAPI()

@app.post("/convert")
async def convert_csv_to_json(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    return df.to_dict(orient='records')
