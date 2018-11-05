clear
echo "Starting Development Server..."
gunicorn server:app --bind localhost:5000 --workers=1 --access-logfile - --worker-class "egg:meinheld#gunicorn_worker"