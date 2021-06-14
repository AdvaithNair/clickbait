up:
	docker-compose up -d
up-log:
	docker-compose up
rebuild:
	docker-compose up --build
down:
	docker-compose down
prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
ls:
	docker-compose ps