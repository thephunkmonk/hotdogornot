from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def predict(da_dawg):
	return "I have predicted your doom!"
