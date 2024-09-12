cd mysql

docker build -t mysql_db .

docker run mysql_db

abrir novo terminal

cd mysql

docker container ls

pegar novo CONTAINER ID

docker exec -it 43826440000a /bin/bash

bash(terminal sql):

cd docker-entrypoint-initdb.d

ls

cd ..

mysql -proot

dentro do mysql:

show databases;

use AiCommerceTables;

show tables;

select * from cliente;

select * from pedido;

FECHAR TERMINAIS!

tirar "CREATE DATABASE AiCommerceTables;" do database_tables.sql.

e tirar "ENV MYSQL_ROOT_PASSWORD=root" do Dockerfile(sql)

novo terminal:

docker-compose up

docker-compose up
