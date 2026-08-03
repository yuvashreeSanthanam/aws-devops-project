# Step 1: Use an official Python image
FROM python:3.13-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file
COPY requirements.txt .

# Step 4: Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application code
COPY app/ .

# Step 6: Expose port 5000
EXPOSE 5000

# Step 7: Start the Flask application
CMD ["python", "app.py"]