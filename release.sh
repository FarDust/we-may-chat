python manage.py migrate
cd ./frontend/chat-room
export NPM_CONFIG_PRODUCTION=false
npm install
npm run build-local
cd ../../
python manage.py collectstatic --dry-run --noinput