FROM python

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]