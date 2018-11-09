all: build run

build:
	cd lib/games_catcher && make deps && make
	mv lib/games_catcher/games_catcher.so lib/

run:
	python3 server.py

clean:
	cd lib/games_catcher
	make clean

docker:
	docker build --build-arg vitrine_key=${VITRINE_KEY} -t vitrine-server .
	docker run -p 80:8000 vitrine-server
