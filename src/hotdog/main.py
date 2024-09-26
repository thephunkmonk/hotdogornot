from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def predict():
	return "I have predicted your doom!"
