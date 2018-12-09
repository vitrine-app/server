all: build run

build:
	cd lib/games_catcher && make deps && make
	mv lib/games_catcher/games_catcher.so lib/

run: build
	gunicorn -w 4 -b 0.0.0.0:8000 server:app

clean:
	cd lib/games_catcher && make clean

install:
	docker exec vitrine-server pip3 install -r requirements.txt

migrate:
	docker exec vitrine-server python3 manage.py db migrate

upgrade:
	docker exec vitrine-server python3 manage.py db upgrade

downgrade:
	docker exec vitrine-server python3 manage.py db downgrade

encrypt:
	@gpg -ca --batch --passphrase ${VITRINE_KEY} .env

decrypt:
	@gpg -d --batch --yes --passphrase ${VITRINE_KEY} -o .env .env.asc
