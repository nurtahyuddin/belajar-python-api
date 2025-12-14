from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "API Python Berhasil!",
        "framework": "FastAPI",
        "pesan": "Halo dari Lubuntu!"
    }

@app.get("/item/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "pesan": "Ini adalah endpoint dinamis"}

if __name__ == "__main__":
    import uvicorn
    # Mengambil port dari Environment Variable (penting untuk Cloud nanti)
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)