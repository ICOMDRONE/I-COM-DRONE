#!/bin/bash

echo "Yeni kod alınıyor..."
git pull origin master

echo "Docker Compose ile konteyner güncelleniyor..."
docker-compose down
docker-compose up -d --build

echo "Güncelleme tamamlandı!"

