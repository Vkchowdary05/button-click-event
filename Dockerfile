# Use official lightweight Nginx image
FROM nginx:alpine

# Metadata
LABEL maintainer="DevOps Team"
LABEL description="Button Click Event Webpage with Alert Notification"

# Copy static assets to web directory
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css
COPY app.js /usr/share/nginx/html/app.js

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

# Expose HTTP port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
