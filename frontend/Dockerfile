# Install dependencies and build using Node
FROM node:18 AS builder

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm install

COPY . .

RUN npm run build

# Serve using a lightweight image
FROM node:18-slim AS runner

WORKDIR /app

# Only copy necessary files
COPY --from=builder /app/.next .next
COPY --from=builder /app/public public
COPY --from=builder /app/package.json .

RUN npm install --omit=dev

EXPOSE 3000

CMD ["npx", "next", "start"]
