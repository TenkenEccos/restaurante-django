USE restaurante;

-- se usa la palabra delimiter, que sirve para indicar donde empieza y termina el procedimiento
DELIMITER //
CREATE PROCEDURE DevolverTodosLosUsuarios()
BEGIN
	SELECT * FROM usuarios;
    -- El procedimiento almacenado son un conjunto de operaciones repetitivas(stored procedure)
    -- INSERT---
    -- DELETE---
END //

DELIMITER ;

-- AHORA UN SP CON PARAMETROS
-- en este caso declaramos un parametro de entrada (IN) y a su vez le ponemos un nombre al delimitador
-- para indicar parametro de salida (OUT)
DROP PROCEDURE IF EXISTS DevolverUsuariosSegunTipo;

DELIMITER //
CREATE PROCEDURE DevolverUsuariosSegunTipo(IN tipo VARCHAR(40), OUT usuarioID INT)
BEGIN
	-- 	Funciones de agregacion (count, sum ,avg,max,min, etc..)
    -- https://www.mysqltutorial.org/mysql-aggregate-functions.aspx
    -- COUNT → contabiliza cuantos usuarios hay de ese tipo
	SELECT COUNT(id) INTO usuarioID FROM usuarios WHERE tipo_usuario = tipo;
END //

DELIMITER ;

-- para eliminar procedimiento " DROP PROCEDURE nombredeprocedimiento "
-- para llamar los procedimientos CALL DevolverTodosLosUsuarios();

CALL DevolverTodosLosUsuarios();
CALL DevolverUsuariosSegunTipo('ADMIN' , @usuarioId);
SELECT @usuarioId;

CALL DevolverUsuariosSegunTipo('USER', @usuarioUser );
SELECT @usuarioUser;

