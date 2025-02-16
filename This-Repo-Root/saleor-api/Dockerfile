# Step 1: Use Python 3.12 as the base image
FROM python:3.10

# Step 2: Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Step 3: Install system dependencies
RUN apt update && apt install -y --no-install-recommends \
    gettext \
    libffi8 \
    libgdk-pixbuf2.0-0 \
    liblcms2-2 \
    libopenjp2-7 \
    libssl3 \
    libtiff6 \
    libwebp7 \
    shared-mime-info \
    mime-support \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*  # Clean up apt cache

# Step 4: Create a Non-Root User and Set Ownership
RUN useradd -m saleor
RUN mkdir -p /app && chown -R saleor:saleor /app

# Step 5: Switch to the Non-Root User
USER saleor

# Step 6: Set the Working Directory
WORKDIR /app
COPY requirements.txt .

# Step 7: Copy the Application Code
COPY --chown=saleor:saleor . /app

# Step 8: Install Dependencies
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.4 python3 -   
RUN pip install --no-cache-dir -r requirements.txt

# Step 9: Expose the Application Port
EXPOSE 8000

# Step 10: Start the Application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "saleor.wsgi:application"]

