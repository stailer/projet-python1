# Utiliser une image de base Python
FROM python:3.9 as base

# Installer Tesseract OCR
#RUN apt-get update && apt-get install -y tesseract-ocr

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN pip install requests
RUN pip install watchdog
RUN pip install pyopenssl

COPY start.sh /app/

# Exposer le port utilisé par l'application Flask
EXPOSE 5000 5679

CMD [ "/app/start.sh" ]

