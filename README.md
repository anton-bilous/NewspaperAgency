# NewspaperAgency
A website about newspaper agency

## How to run the project?

1. Clone the project

   ```bash
   git clone https://github.com/anton-bilous/NewspaperAgency
   ```

2. Create virtual environment

    ```bash
    cd NewspaperAgency
    python -m venv venv
    ```

3. Activate the virtual environment

   Linux/MacOS:

   ```bash
   . venv/bin/activate
   ```

   Windows:

   ```cmd
   venv\Scripts\activate
   ```

4. Install requirements

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations

   ```bash
   python manage.py migrate
   ```

6. Run the development version of site

   ```bash
   DJANGO_DEBUG=1 python manage.py runserver
   ```

7. (optional) Run in production mode

   - Create certificate and key files
   - Generate static files

     ```bash
     python manage.py collectstatic --no-input
     ```

   - Run the project

     ```bash
     python -m gunicorn newspaper_agency.asgi:application -k uvicorn.workers.UvicornWorker --certfile cert.crt --keyfile cert.key
     ```
