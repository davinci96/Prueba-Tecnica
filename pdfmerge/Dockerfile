FROM python:3.9.17-alpine3.18

EXPOSE 5000

ENV SECRET_KEY=51abff7336af65dc3989d491aefd5e8b

RUN mkdir -p /usr/src/pdfmerger

WORKDIR /usr/src/pdfmerger

COPY . ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "--app", "main.py", "--debug", "run", "--host=0.0.0.0" ]