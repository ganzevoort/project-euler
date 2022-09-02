FROM python

# No puffer on in/out for python
ENV PYTHONUNBUFFERED 1

# Create virtualenv
WORKDIR /code
COPY ./requirements.txt ./
RUN python -m venv /.venv
RUN /.venv/bin/pip install --upgrade pip
RUN /.venv/bin/pip install -r requirements.txt

COPY --chown=code:code . /code

ENTRYPOINT ["/.venv/bin/python"]
CMD ["euler.py"]
