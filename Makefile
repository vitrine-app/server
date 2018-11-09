all: build run

build:
	cd lib/games_catcher && make deps && make
	mv lib/games_catcher/games_catcher.so lib/

run:
	python server.py

clean:
	cd lib/games_catcher
	make clean
