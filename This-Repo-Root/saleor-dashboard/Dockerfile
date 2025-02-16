# Step 1: Builder Stage (Build the Saleor Dashboard)
FROM node:18-alpine AS builder

# Install bash for compatibility with scripts
RUN apk add --no-cache bash

# Step 2: Set up the working directory
WORKDIR /app

# Step 3: Manage dependencies (copy only package.json for better caching)
COPY package.json package-lock.json ./

# Set CI to 1 to avoid interactive prompts and install dependencies
ARG API_URL
ARG APP_MOUNT_URI
ARG APPS_MARKETPLACE_API_URL
ARG APPS_TUNNEL_URL_KEYWORDS
ARG STATIC_URL
ARG SKIP_SOURCEMAPS
ARG LOCALE_CODE

ENV API_URL=${API_URL:-http://localhost:8000/graphql/}
ENV APP_MOUNT_URI=${APP_MOUNT_URI:-/dashboard/}
ENV APPS_MARKETPLACE_API_URL=${APPS_MARKETPLACE_API_URL:-https://apps.saleor.io/api/v2/saleor-apps}
ENV APPS_TUNNEL_URL_KEYWORDS=${APPS_TUNNEL_URL_KEYWORDS}
ENV STATIC_URL=${STATIC_URL:-/dashboard/}
ENV SKIP_SOURCEMAPS=${SKIP_SOURCEMAPS:-true}
ENV LOCALE_CODE=${LOCALE_CODE:-EN}

# Install dependencies with legacy-peer-deps flag
RUN npm ci --legacy-peer-deps

# Step 4: Copy application files
COPY nginx/ ./nginx/
COPY assets/ ./assets/
COPY locale/ ./locale/
COPY scripts/ ./scripts/
COPY src/ ./src/
COPY vite.config.js tsconfig.json ./
COPY *.d.ts ./
COPY schema.graphql introspection.json introspection*.json ./
COPY .featureFlags/ .featureFlags/

# Step 6: Build the application
RUN npm run build

# Step 7: Runner Stage (Serve with Nginx)
FROM nginx:stable-alpine AS runner

# Step 8: Set up the working directory
WORKDIR /app
# Copy built application files from builder stage
COPY --from=builder /app/build/ /app/

# Remove default Nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy built files from the builder stage
COPY --from=builder /app/build/ /usr/share/nginx/html/
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/replace-env-vars.sh /docker-entrypoint.d/50-replace-env-vars.sh

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
