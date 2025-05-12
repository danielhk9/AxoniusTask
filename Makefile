build:
	docker build -t axonius-tests .

run:
	docker run --rm axonius-tests

repeat:
	docker run --rm axonius-tests --count=10