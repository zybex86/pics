# Picture Uploader

---

## Requirements

* Python >= 3.8
* Django >= 3.2
* API via DRF
* Line length = 100
* Language: Eng
* Tests using pytest and django-pytest
* Docker support

## How to Run

You can run the application in two ways:

### Local development

1. Clone git repository:

    git clone https://github.com/zybex86/pics.git

1. Create a virtual environment:

    mkvirtualenv -p python3 env_name 

1. Activate virtual enviornment:

    workon env_name

1. Upgrade pip:

    pip install -U pip

1. Install requirements:

    pip install -r requirements.txt

1. Create and migrate the database:

    python manage.py migrate

1. Create superuser account:

    python manage.py createsuperuser

1. Run dev server:

    python manage.py runserver

### Docker

1. Run the docker command from the base directory:

    docker-compose up
