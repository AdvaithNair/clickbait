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
prod-log:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
prod-rebuild:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
ls:
	docker-compose ps