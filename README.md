# ASTRA

ASTRA is a small starter web app that shows how HTML, CSS, JavaScript, and Python work together. The browser draws the page. Flask on the server builds a time-of-day greeting from the name you type.

## What it does

1. Opens a single page with a name field.
2. Sends that name to `/api/hello` as JSON.
3. Shows a greeting (`Good morning` / `Good afternoon` / `Good evening`) plus the server clock.

`/api/status` is a health check that reports the app name and stack.

## Stack

| Layer | Role |
| --- | --- |
| HTML (`templates/index.html`) | Page structure and form |
| CSS (`static/css/style.css`) | Layout and look |
| JavaScript (`static/js/app.js`) | Form submit and API call |
| Python / Flask (`app.py`) | Serves the page and greeting API |

## Run

```powershell
python -m pip install -r requirements.txt
python app.py
```


