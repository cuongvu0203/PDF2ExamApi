FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#  Copy code
COPY ./main.py /code/
#  Copy code
COPY ./extractPDF /code/extractPDF
#  Copy code
COPY ./images /code/images
#  Copy code
COPY ./uploads /code/uploads
# CMD app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8540"]
