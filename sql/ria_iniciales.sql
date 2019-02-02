CREATE DATABASE ria_iniciales;
USE ria_iniciales;

CREATE TABLE clientes(
    id_cliente  varchar(13) NOT NULL PRIMARY KEY,
    nombre_cliente varchar(50)  NOT NULL,
    apellido_paterno_cliente    varchar(50) NOT NULL,
    apellido_materno_cliente    varchar(50) NOT NULL,
    telefono_cliente    varchar(10) NOT NULL,
    email_cliente   varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes(id_cliente, nombre_cliente, apellido_paterno_cliente, apellido_materno_cliente, telefono_cliente, email_cliente)
VALUES('0000000000001', 'Jose', 'Ramon', 'Fernandez', '7751234567', 'ramon@gmail.com'),
('0000000000002', 'Jose', 'Hernandez', 'Gonzales', '7751234568', 'jose@gmail.com'),
('0000000000003', 'Rubi', 'Vargas', 'Romero', '7751234569', 'Rubi@gmail.com');

CREATE TABLE productos(
    id_producto    varchar(13) NOT NULL PRIMARY KEY,
    nombre_producto varchar(50) NOT NULL,
    lote_producto   varchar(5) NOT NULL,
    existencia_producto int NOT NULL,
    fecha_caducida_producto date NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO productos(id_producto, nombre_producto, lote_producto, existencia_producto, fecha_caducida_producto)
VALUES('0000000000001', 'Gansito', '12345', 20, '2020-01-29'),
('0000000000002', 'Cerveza XX', '12346', 6, '2019-06-06'),
('0000000000003', 'Panque de nuez', '12347', 40, '2021-10-18');

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;

