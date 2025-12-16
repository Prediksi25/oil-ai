from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Location(BaseModel):
    lat: float
    lon: float

@app.post("/analyze")
def analyze(loc: Location):
    jarak = round(random.uniform(0.5,4),2)
    kedalaman = random.randint(1800,3200)
    antiklin = jarak < 2
    cekungan = True

    score = 0
    if jarak < 1.5: score += 35
    if kedalaman > 2500: score += 30
    if antiklin: score += 20
    if cekungan: score += 15

    status = "RENDAH"
    if score >= 70: status = "TINGGI"
    elif score >= 45: status = "SEDANG"

    return {
        "jarak_patahan_km": jarak,
        "kedalaman_m": kedalaman,
        "antiklin": antiklin,
        "dalam_cekungan": cekungan,
        "potensi_minyak": score,
        "status": status
    }