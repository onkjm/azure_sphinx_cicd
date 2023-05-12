export PATH="/opt/homebrew/bin/pandoc:$PATH"
which pandoc
echo =========================
echo set path to pandoc
echo =========================

make html
echo =========================
echo make html
echo =========================

cp -R $(Agent.BuildDirectory)/s/build/html/* /usr/local/var/www/myapi/
echo =========================
echo deploy html
echo =========================

/opt/homebrew/bin/nginx -s reload
echo =========================
echo restart nginx
echo =========================

export MEILISEARCH_HOST_URL=$1
export MEILISEARCH_API_KEY=$2
set
echo =========================
echo set env vars
echo =========================
 
cd docs-scraper
git clone https://github.com/meilisearch/docs-scraper
cd docs-scraper
pip install pipenv
pipenv install
ls
pipenv run ./docs-scraper ../myapi.json
echo =========================
echo docs scraping
echo =========================