<?php
header('Access-Control-Allow-Origin: *');

$x = 0;
$y = 0;
$R = 0;
$G = 0;
$B = 0;
$C = 0;

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    if ((bool)isset($_POST["x"])) $x = $_POST["x"];
    if ((bool)isset($_POST["y"])) $y = $_POST["y"];
    if ((bool)isset($_POST["R"])) $R = $_POST["R"];
    if ((bool)isset($_POST["G"])) $G = $_POST["G"];
    if ((bool)isset($_POST["B"])) $B = $_POST["B"];
    if ((bool)isset($_POST["C"])) $C = $_POST["C"];
    $response = shell_exec("python led_matrix_set.py -x $x -y $y -R $R -G $G -B $B -C $C");
    echo $response;
}

if ($_SERVER["REQUEST_METHOD"] == "GET"){
    $response = shell_exec("python led_matrix_get.py");
    echo $response;
}
 