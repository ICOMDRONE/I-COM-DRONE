# Resmi Python imajını kullan
FROM python:3.9-slim

# Çalışma dizinini belirle
WORKDIR /app

# Gerekli sistem paketlerini yükle (gcc, python-dev gibi)
RUN apt-get update && apt-get install -y \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Flask dosyalarını kopyala
COPY . .

# Konteyner çalıştırıldığında Flask uygulamasını başlat
CMD ["python", "app.py"]

