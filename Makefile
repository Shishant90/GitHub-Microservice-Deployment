.PHONY: install test build run docker-run ansible-run k8s-deploy clean

install:
	pip install -r requirements.txt

test:
	cd ci-cd-pipeline-project && pytest tests/  # cSpell:ignore pytest

build:
	cd ci-cd-pipeline-project && docker build -t github-microservice .

run:
	cd ci-cd-pipeline-project && python src/app.py

docker-run:
	cd ci-cd-pipeline-project && docker-compose up

ansible-run:
	cd ci-cd-pipeline-project && ansible-playbook -i inventory ansible/playbook.yml

k8s-deploy:
	cd ci-cd-pipeline-project && kubectl apply -f k8s/

clean:
	docker system prune -f