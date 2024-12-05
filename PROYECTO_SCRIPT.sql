CREATE DATABASE IF NOT EXISTS crucero_proyecto;
USE crucero_proyecto;

CREATE TABLE Cabina(
	idCabina INT PRIMARY KEY,
	capacidad INT NOT NULL,
	disponibilidad BOOLEAN NOT NULL,
	tamanho VARCHAR(50) NOT NULL,
	precio FLOAT NOT NULL
);

CREATE TABLE Rol(
	idRol INT PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	descripcion VARCHAR(100) NOT NULL,
	departamento VARCHAR(100) NOT NULL,
	salario FLOAT NOT NULL
);

CREATE TABLE Servicio(
	idServicio INT PRIMARY KEY,
	tipo VARCHAR(100) NOT NULL,
	descripcion VARCHAR(100) NOT NULL,
	precio FLOAT NOT NULL
);

CREATE TABLE Pasajero(
	idPasajero VARCHAR(150) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	apell_1 VARCHAR(100) NOT NULL,
	apell_2 VARCHAR(100) NOT NULL,
	anho_nacimiento YEAR NOT NULL,
	genero VARCHAR(100) NOT NULL,
	activo BOOLEAN NOT NULL
);

CREATE TABLE Trabajador(
	idTrabajador VARCHAR(150) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	apell_1 VARCHAR(100) NOT NULL,
	apell_2 VARCHAR(100) NOT NULL,
	anho_nacimiento YEAR NOT NULL,
	genero VARCHAR(100) NOT NULL,
	activo BOOLEAN NOT NULL,
	idRol INT,
	FOREIGN KEY (idRol) REFERENCES Rol(idRol) ON DELETE SET NULL 
);

CREATE TABLE Registro (
    idRegistro INT PRIMARY KEY AUTO_INCREMENT, 
    idCabina INT NOT NULL,                    
    idPasajero VARCHAR(150) NOT NULL,        
    fechaEntrada DATE NOT NULL,               
    fechaSalida DATE NOT NULL,                 
    FOREIGN KEY (idCabina) REFERENCES Cabina(idCabina) ON DELETE CASCADE,
    FOREIGN KEY (idPasajero) REFERENCES Pasajero(idPasajero) ON DELETE CASCADE
);

CREATE TABLE SolicitudServicio (
    idSolicitud INT PRIMARY KEY AUTO_INCREMENT, 
    idRegistro INT NOT NULL,  		
    idServicio INT NOT NULL,        
    idTrabajador VARCHAR(150),       
    fecha DATE NOT NULL,             
    hora TIME NOT NULL,          
    FOREIGN KEY (idRegistro) REFERENCES Registro(idRegistro) ON DELETE CASCADE,
    FOREIGN KEY (idServicio) REFERENCES Servicio(idServicio) ON DELETE CASCADE,
    FOREIGN KEY (idTrabajador) REFERENCES Trabajador(idTrabajador) ON DELETE SET NULL
);

-- Insertar datos en la tabla Cabina
INSERT INTO Cabina (idCabina, capacidad, disponibilidad, tamanho, precio) VALUES
(1, 2, TRUE, 'Pequeña', 150.00),
(2, 4, TRUE, 'Mediana', 300.00),
(3, 6, TRUE, 'Grande', 450.00),
(4, 2, TRUE, 'Pequeña', 120.00),
(5, 8, TRUE, 'Grande', 800.00);

-- Insertar datos en la tabla Rol
INSERT INTO Rol (idRol, nombre, descripcion, departamento, salario) VALUES
(1, 'Capitán', 'Operación del barco', 'Navegación', 5000.00),
(2, 'Chef', 'Preparación de alimentos', 'Cocina', 2000.00),
(3, 'Mecánico', 'Mantenimiento de maquinaria', 'Técnico', 2500.00),
(4, 'Camarero', 'Atención al cliente', 'Servicio', 1500.00),
(5, 'Recepcionista', 'Recepción y asistencia', 'Atención', 1800.00);

-- Insertar datos en la tabla Servicio
INSERT INTO Servicio (idServicio, tipo, descripcion, precio) VALUES
(1, 'Spa', 'Tratamientos relajantes', 100.00),
(2, 'Restaurante', 'Comida gourmet', 50.00),
(3, 'Bar', 'Bebidas y cocteles', 30.00),
(4, 'Tour', 'Visitas guiadas', 75.00),
(5, 'Piscina', 'Acceso a la piscina', 20.00);

-- Insertar datos en la tabla Pasajero
INSERT INTO Pasajero (idPasajero, nombre, apell_1, apell_2, anho_nacimiento, genero, activo) VALUES
('P001', 'Luis', 'García', 'López', 1985, 'Masculino', TRUE),
('P002', 'Ana', 'Martínez', 'Jiménez', 1990, 'Femenino', TRUE),
('P003', 'Carlos', 'Sánchez', 'Ruiz', 1978, 'Masculino', TRUE),
('P004', 'María', 'Pérez', 'Torres', 2000, 'Femenino', TRUE),
('P005', 'Javier', 'Morales', 'Hernández', 1995, 'Masculino', TRUE);

-- Insertar datos en la tabla Trabajador
INSERT INTO Trabajador (idTrabajador, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idRol) VALUES
('T001', 'Juan', 'Ramírez', 'Cordero', 1980, 'Masculino', TRUE, 1),
('T002', 'Pedro', 'Castro', 'Vargas', 1975, 'Masculino', TRUE, 3),
('T003', 'Sofía', 'Rojas', 'Durán', 1992, 'Femenino', TRUE, 2),
('T004', 'Miguel', 'Vega', 'Salas', 1988, 'Masculino', TRUE, 4),
('T005', 'Carla', 'Fernández', 'Solano', 1990, 'Femenino', TRUE, 5);

select * from rol;
select * from cabina;
select * from registro;
select * from trabajador;
select * from SolicitudServicio;

SELECT 
    p.idPasajero AS id_pasajero, 
    p.nombre, 
    CONCAT(p.apell_1, ' ', p.apell_2) AS apellidos_completos,
    c.idCabina AS numero_cabina, 
    r.fechaEntrada AS fecha_entrada, 
    r.fechaSalida AS fecha_salida
FROM 
    Registro r
JOIN 
    Pasajero p ON r.idPasajero = p.idPasajero
JOIN 
    Cabina c ON r.idCabina = c.idCabina;
    
 SELECT 
CONCAT(p.nombre, ' ', p.apell_1, ' ', p.apell_2) AS "Nombre del pasajero",
p.idPasajero AS "Identificación del pasajero",
c.idCabina AS "Número de cabina",
c.tamanho AS "Tamaño de la cabina",
reg.fechaEntrada AS "Fecha de entrada",
reg.fechaSalida AS "Fecha de salida"
FROM 
Registro reg
JOIN 
Pasajero p ON reg.idPasajero = p.idPasajero
JOIN 
Cabina c ON reg.idCabina = c.idCabina	
ORDER BY 
p.nombre, p.apell_1, p.apell_2;    