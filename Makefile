
start:
	uvicorn src.main:app --host localhost --port 8083 --reload


local-start:
	 docker-compose -f ./docker/local/docker-compose.yaml --env-file .env up -d --build

deploy-start:
	 docker-compose -f ./docker/deploy/docker-compose.yaml --env-file .env up -d --build
