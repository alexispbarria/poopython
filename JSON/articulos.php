<?php
header('Content-Type: application/json');

$server = "localhost";
$user = "root";
$clave = "";
$base = "articulos";
$conexion = mysqli_connect($server, $user, $clave, $base) or die("problema de conexion");
mysqli_set_charset($conexion, 'utf8');

$datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos");
$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
echo json_encode ($resultado);

?>