build:
	cd function; \
	zip -9qr build.zip .;

apply:
	terraform apply

update: build
	terraform apply
