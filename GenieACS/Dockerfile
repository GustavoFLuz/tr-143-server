# Use Node.js LTS version as base image
FROM node:20-alpine

# Install necessary system dependencies
RUN apk add --no-cache \
    git \
    python3 \
    make \
    gcc \
    g++ \
    wget

# Set working directory
WORKDIR /opt/genieacs

# Clone GenieACS repository
RUN git clone https://github.com/genieacs/genieacs.git .

# Install dependencies
RUN npm install

# Install PM2 for process management
RUN npm install pm2 -g

# Copy TR-143 specific configuration
COPY tr143-config.json config/

# Expose necessary ports
EXPOSE 7557 7558 7559

# Create volumes for persistent data
VOLUME ["/opt/genieacs/config", "/opt/genieacs/logs"]

# Set environment variables
ENV NODE_ENV=production
ENV GENIEACS_CWMP_PORT=7557
ENV GENIEACS_NBI_PORT=7558
ENV GENIEACS_WEBSOCKET_PORT=7559

# Start GenieACS using PM2
CMD ["pm2-runtime", "npm", "start"]