-- pwd2025.productos definition

CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) DEFAULT NULL,
  `precio` float(10,2) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `marca_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productos_marcas_FK` (`marca_id`),
  CONSTRAINT `productos_marcas_FK` FOREIGN KEY (`marca_id`) REFERENCES `marcas` (`id`)
) 