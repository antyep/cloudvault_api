FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
