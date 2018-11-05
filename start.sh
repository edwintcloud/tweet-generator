clear
echo "Starting Development Server..."
gunicorn server:app --bind localhost:5000 --access-logfile -