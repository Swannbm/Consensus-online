FROM python:3.9-alpine

EXPOSE 8000

# ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PATH = "${PATH}:/root/.poetry/bin"

RUN apk add --no-cache gcc python3-dev musl-dev libffi-dev curl
RUN pip install --upgrade pip
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN alias ll="ls -alh"


WORKDIR /app
COPY ./src ./
COPY pyproject.toml poetry.lock ./


RUN poetry config virtualenvs.create false
RUN poetry install

RUN python ./manage.py migrate

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]