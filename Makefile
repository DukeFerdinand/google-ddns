install:
	yarn

dev: install
	yarn dev

ready:
    docker run --rm --privileged linuxkit/binfmt:v0.8

tag:
	docker tag google-ddns registry.dougflynn.dev/google-ddns .

build-arm: ready
	docker buildx build --platform linux/arm64 --push \
		-t registry.dougflynn.dev/google-ddns \
		.

publish: build-arm
	echo Waiting a few seconds for docker image to process...
	sleep 10
	kubectl apply -f kube-job.yml