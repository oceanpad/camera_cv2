build:
	docker build -t camera_yolov5 .

dev:
	docker-compose -f docker/development.yml -p camera_yolov5 up

prod:
	docker-compose -f docker/prod.yml -p dr up --no-deps -d


