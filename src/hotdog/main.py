from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from transformers import pipeline
import io
from typing import Union

app = FastAPI()

@app.get("/predict")
async def hotdog():
	model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

	return "I have predicted your doom!"

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
	img = await file.read()
	model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
	
	from PIL import Image
	img = Image.open(io.BytesIO(img))
	
	p = model(img)
	label = get_max_label(p)
	return label
