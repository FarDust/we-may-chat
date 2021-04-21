python manage.py migrate
cd ./frontend/chat-room
npm install
npm run build-local
cd ../../
python manage.py collectstatic --dry-run --noinput