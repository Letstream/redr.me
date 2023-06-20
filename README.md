## Redr.me | Open Source URL Redirection Service focused on Anonymity
An Open Source and simple to Use Self Hosted Redirection Service made in Django focused on Anonymity.

To use you can visit: https://redr.me/

## Features
- No Tracking and Instant Redirection
- Open Source
- Easy to Self Host and Customise
- Open API for redr.me Official Instance

## Components

- API Core [This Project]
- [Frontend](https://github.com/letstream/redr.me-frontend)

## Requirements
Make sure you have [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) installed. Python version >= 3.6 is required.

The Project uses PostgreSQL >= 11 as Database Host.

You also need Django, and other dependencies. These can be installed by running:

```
pip install -r requirements.txt 
```
### Variables

After you have installed the packages mentioned above, create an `.env` file at `app/settings/` or provide the following environment variables as available in `app/settings/sample.env`

### Setting up Database

After you have defined the variables mentioned above, navifate to your `app` folder with your terminal and run:
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
```
### Running server
Lastly, you can start the server by running:
```
python manage.py runserver
```

### Coming Soon

- Deployment Configuration and Guidelines
- Integration with LetStat (Launching soon)
- API and Contribution Docs

### Contributors
<a href="https://github.com/letstream/redr.me/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=letstream/redr.me" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
