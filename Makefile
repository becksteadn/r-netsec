pack:
	cd function; \
	zip -9qr build.zip .;

apply:
	terraform apply

update: pack
	terraform apply
