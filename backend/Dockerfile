# Use full Python image for easier package installs
FROM python:3.12-bookworm

# Install the UV tool from the official container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory inside the container
WORKDIR /app

# Copy your backend project files into the container
COPY . /app

# Install dependencies from pyproject.toml + uv.lock
RUN uv sync --locked

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app with Uvicorn using UV
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
