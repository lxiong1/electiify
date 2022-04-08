# Electiify

A voting web application.

## Pre-requisites

Install machine dependencies:

- `python3`
- `pipenv`
- `docker`

Install project dependencies with command:

- `pipenv sync --dev`

## Development

### Running

Run the following command to run the application:

```commandline
./entrypoint.sh
```

Available endpoints:

```text
POST api/questions/
GET api/questions/
GET api/questions/<int:question_id>/
PATCH api/questions/<int:question_id>/
DELETE api/questions/<int:question_id>/

POST api/questions/<int:question_id>/answers/
GET api/questions/<int:question_id>/answers/
GET api/questions/<int:question_id>/answers/<int:answer_id>
```

### Testing

Run the following command to test:

```commandline
pytest
```

Run the following command to view test coverage:

```commandline
pytest --cov=polls --cov-report=term
```

### Static Analysis

Run the following command to auto-format code:

```commandline
black .
```

Run the following command to lint code:

```commandline
flake8 .
```
