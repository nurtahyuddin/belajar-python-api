# Gunakan image python yang ringan
FROM python:3.11-slim

WORKDIR /app

# Salin daftar library dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode program
COPY . .

# Jalankan aplikasi
CMD ["python", "main.py"]