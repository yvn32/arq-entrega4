create table producto (
	id BIGSERIAL,
	nombre VARCHAR(90),
	descripcion VARCHAR(500),
	precio INTEGER,
	preciodcto INTEGER,
	stock INTEGER,
	idempresa INTEGER,
	rutaimg VARCHAR(500),
	PRIMARY KEY (id)
);

-- Producto 1
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'Acer Nitro 5 AN515-54-59UV',
'Procesador: Intel Core i5-9300H; RAM: 16 GB DDR4, Pantalla: LED 15.6"; Almacenamiento: HDD 500GB, SSD 250GB; Tarjetas de video: Intel UHD Graphics 630 (Integrada), NVIDIA GeForce GTX',
520000, 499990, 4, 1, 'https://media.solotodo.com/media/cache/39/54/3954e556f84edcccce8363da73511242.png'
);

-- Producto 2
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'Lenovo IdeaPad Gaming 3 15ARH05 [82EY0017CL]',
'Procesador: AMD Ryzen 5 4600H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 512GB; Tarjetas de video: AMD Radeon RX Vega 6 (Integrada), NVIDIA GeForce GTX 1650 (4 GB)',
520000, 489990, 3, 1, 'https://media.solotodo.com/media/cache/0d/be/0dbe0b8c0f460367cb613c731c99373b.png'
);

-- Producto 3
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'ASUS VivoBook Pro N580GD-E4201T',
'Procesador: Intel Core i7-8750H; RAM: 16 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: HDD 1TB; Tarjetas de video: Intel UHD Graphics 630 (Integrada), NVIDIA GeForce GTX 1050 (4 GB)',
580000, 559990, 3, 1, 'https://media.solotodo.com/media/cache/bb/e6/bbe61a3f7e8f5aa15a1e35b760b86ec3.png'
);

-- Producto 4
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'HP Pavilion Gaming 15 (i5-9300H)',
'Procesador: Intel Core i5-9300H; RAM: 16 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: HDD 500GB; Tarjetas de video: Intel UHD Graphics 630 (Integrada), NVIDIA GeForce GTX 1650 (4 GB)',
590000, 579990, 2, 2, 'https://media.solotodo.com/media/cache/a2/00/a200bdab2a2c512481dd1634c697b150.png'
);

-- Producto 5
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'HP Pavilion Gaming 15-EC1024LA',
'Procesador: AMD Ryzen 7 4800H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 512GB; Tarjetas de video: AMD Radeon RX Vega 7 (Integrada), NVIDIA GeForce GTX 1650 (4 GB)',
719990, 699990, 1, 2, 'https://media.solotodo.com/media/cache/04/0c/040c1c66ce71ba271c22f3e14bd0f430.png'
);

-- Producto 6
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'Dell G5 15 Gaming 5510 [G5510_NI582561650]',
'Procesador: Intel Core i5-10500H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 256GB; Tarjetas de video: Intel UHD Graphics 630 (Integrada), NVIDIA GeForce GTX 1650 (4 GB)',
759990, 739990, 1, 2, 'https://media.solotodo.com/media/cache/f0/88/f088f00edd25a58b8d0e33ed595a1524.png'
);

-- Producto 7
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'Lenovo Legion 5 15ARH05 [82B50094CL]',
'Procesador: AMD Ryzen 5 4600H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 512GB; Tarjetas de video: AMD Radeon RX Vega 6 (Integrada), NVIDIA GeForce GTX 1650 (4 GB)',
829990, 799990, 1, 2, 'https://media.solotodo.com/media/cache/2a/a6/2aa67cb33a226e66846a2b5b05eb8c34.png'
);

-- Producto 8
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'Dell G15 Gaming 5515 [DVVC7]',
'Procesador: AMD Ryzen 5 5600H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 256GB; Tarjetas de video: AMD Radeon RX Vega 6 (Integrada), NVIDIA GeForce GTX 3050 (4 GB)',
889277, 859990, 1, 2, 'https://media.solotodo.com/media/cache/ab/51/ab51a331024fb26073983f543c8b8586.png'
);

-- Producto 9
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'MSI GF63 Thin 10SC-222 [9S7-16R512-022]',
'Procesador: Intel Core i5-10500H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 256GB; Tarjetas de video: Intel UHD Graphics 630 (Integrada), NVIDIA GeForce 1650 Max-Q (4 GB)',
899990, 859990, 4, 3, 'https://media.solotodo.com/media/cache/02/e3/02e3eb34c55dd867763037df662cf635.png'
);

-- Producto 10
insert into producto (nombre, descripcion, precio, precioDcto, stock, idEmpresa, rutaImg) values (
'MSI Bravo 15 B5DD (Ryzen 5 5600H)',
'Procesador: AMD Ryzen 5 5600H; RAM: 8 GB DDR4; Pantalla: LED 15.6"; Almacenamiento: SSD 512GB; Tarjetas de video: AMD Radeon RX Vega 6 (Integrada), AMD Radeon RX 5500M (4 GB)',
1123970, 1099990, 3, 3, 'https://media.solotodo.com/media/cache/7b/db/7bdb0c0ee943b57bc535476565ae7f70.png'
);