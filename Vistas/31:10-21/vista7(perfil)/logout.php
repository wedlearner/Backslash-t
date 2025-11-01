<?php
session_start();
session_destroy(); #Eliminar datos del login
header("Location: login.html"); 
exit;
?>
