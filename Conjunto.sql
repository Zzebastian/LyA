DROP DATABASE IF EXISTS catalogo;
CREATE DATABASE catalogo;
USE catalogo;
CREATE TABLE conjunto (
	id_conjunto	INTEGER NOT NULL AUTO_INCREMENT,
	conjunto	TEXT,
	cod_conjunto	TEXT,
	PRIMARY KEY(id_conjunto)
);
CREATE TABLE cod1 (
	id_cod1	INTEGER NOT NULL AUTO_INCREMENT,
	cod1	TEXT,
	cod_cod1	TEXT,
	PRIMARY KEY(id_cod1)
);
CREATE TABLE cod2 (
	id_cod2	INTEGER NOT NULL AUTO_INCREMENT,
	cod2	TEXT,
	cod_cod2	TEXT,
	PRIMARY KEY(id_cod2)
);
CREATE TABLE cod3 (
	id_cod3	INTEGER NOT NULL AUTO_INCREMENT,
	cod3	TEXT,
	cod_cod3	TEXT,
	PRIMARY KEY(id_cod3)
);
CREATE TABLE cod4 (
	id_cod4	INTEGER NOT NULL AUTO_INCREMENT,
	cod4	TEXT,
	cod_cod4	TEXT,
	PRIMARY KEY(id_cod4)
);
CREATE TABLE cod5 (
	id_cod5	INTEGER NOT NULL AUTO_INCREMENT,
	cod5	TEXT,
	cod_cod5	TEXT,
	PRIMARY KEY(id_cod5)
);
CREATE TABLE cod6 (
	id_cod6	INTEGER NOT NULL AUTO_INCREMENT,
	cod6	TEXT,
	cod_cod6	TEXT,
	PRIMARY KEY(id_cod6)
);
CREATE TABLE producto (
	id_producto	INTEGER NOT NULL AUTO_INCREMENT,
	producto	TEXT,
	cod_producto	TEXT,
	PRIMARY KEY(id_producto)
);

INSERT INTO `catalogo`.`producto` (`producto`, `cod_producto`) VALUES ('prod1', 'p1');