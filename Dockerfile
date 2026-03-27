# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install uv (fast dependency manager)
RUN pip install uv

# Install dependencies
RUN uv pip install --system .

# Expose port (for HF Spaces / server)
EXPOSE 7860

# Start the app
CMD ["python", "-m", "server.app"]