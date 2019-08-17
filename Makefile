pack:
	cd function; \
	mkdir build; \
	cp main.py build; \
	mkdir build/lib; \
	pip3 install -r requirements.txt -t build/lib; \
	cd build; zip -9qr build.zip .;

apply:
	terraform apply

update: pack
	terraform apply
