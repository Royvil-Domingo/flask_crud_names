# CRUD Names — Flask + Vercel

## Project structure

Keep `app.py` and `requirements.txt` at the project root, with `base.html` and `index.html` inside `templates/`.

## Local run

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Vercel deployment

1. Push this project to a GitHub repository. The repository should contain `app.py`, `requirements.txt`, `.python-version`, and the `templates/` directory at its root.
2. In Vercel, choose **Add New → Project**, import the GitHub repository, and deploy.
3. Leave Build Command and Output Directory at their automatically detected/default values; do not set `dist` as the output directory.

Vercel's current Flask support can detect the WSGI `app` object in `app.py`; a `vercel.json` file is not required for this project.

## Important data limitation

This beginner example stores names in the Python list `names`. It is temporary, in-memory data, not a persistent database. On Vercel, data can reset or appear inconsistent between requests/instances. Use a hosted database for persistent records. The app also has no login or authorization, so anyone who can access it can add, edit, or delete names. Do not use it for private or important data until you add authentication, CSRF protection, and a database.
