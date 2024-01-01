# Etape 1: Construire l'application
FROM node:14 as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Etape 2: Servir l'application
FROM nginx:alpine
COPY --from=build /app/dist/angular-app /usr/share/nginx/html
