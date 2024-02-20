# Agify

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Potential Improvements](#potential-improvements)
- [License](#license)

## Overview

A Simple REST API that guesses the age of a person by their name

## Prerequisites

- You need to have Python3.xx installed in order to run this application.
- Docker (optional)

## Installation

### Method 1 (Using docker-compose)
```bash
docker-compose up -d
```

### Method 2 (Local installation)
```bash
# Clone the repository
git clone https://github.com/coderboy-exe/Agify.git

# Navigate to the project directory
cd Agify

# Create a virtual environment (my_env)
python -m venv my-env

# Activate your virtual environment
# Windows (Assuming you are using a bash terminal)
source my-env/Scripts/activate
# Linux
source my-env/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver

```

## Usage

Access the application at [http://localhost:8000](http://localhost:8000).


## API Endpoints

##### `POST /api/human-age/`
Request Body
```json
{
    "name": "Joe"
}
```
Response
```json
{
    "name": "joe",
    "age": 65,
    "date_of_birth": 1959
}
```

## Testing

Run the unit and Integration tests

```bash
# Run the tests
python manage.py test
```

All tests should pass


## Potential Improvements
- Monitoring & Logging: to track application performance and resource usage, capture errors, warnings, and other important events
- Security: security measures such as CSRF protection,SSL/TSL and user authentication
- Scalability: introducing a load-balancer to implement horizontal scaling, hence allowing the application to be scalable.
- Rate-Limiting: this will help prevent abuse and protect against DDoS attacks.
- Continuous Integration & Deployment (CI/CD): setting up CI/CD pipelines to automate the build, test, and deployment processes, using tools like Jenkins, GithubActions.


## License

This project is free for distribution under the [MIT License](#license).
