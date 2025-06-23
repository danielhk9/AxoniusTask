IMAGE_NAME=airbnb-e2e

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -v $(PWD)/temp:/app/temp $(IMAGE_NAME)

repeat:
	docker run --rm $(IMAGE_NAME) --count=10
