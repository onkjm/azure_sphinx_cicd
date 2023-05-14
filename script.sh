echo =========================
echo make html
echo =========================
make html

echo =========================
echo deploy html
echo =========================
cp -R $1/s/build/html/* /usr/local/var/www/myapi/

echo =========================
echo restart nginx
echo =========================
/opt/homebrew/bin/nginx -s reload

echo =========================
echo set env vars
echo =========================
export MEILISEARCH_HOST_URL=$2
export MEILISEARCH_API_KEY=$3

echo =========================
echo docs scraping
echo =========================
cd /Users/on/docs-scraper
source .venv/bin/activate
pipenv run ./docs_scraper $1/s/docs-scraper/myapi.json
