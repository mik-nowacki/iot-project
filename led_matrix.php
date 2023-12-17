<?php
header('Access-Control-Allow-Origin: *');

$x = 0;
$y = 0;
$R = 0;
$G = 0;
$B = 0;
$C = 0;

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    if (isset($_POST["x"])) $x = $_POST["x"];
    if (isset($_POST["y"])) $y = $_POST["y"];
    if (isset($_POST["R"])) $R = $_POST["R"];
    if (isset($_POST["G"])) $G = $_POST["G"];
    if (isset($_POST["B"])) $B = $_POST["B"];
    if (isset($_POST["C"])) $C = $_POST["C"];
    $cmd = "py led_matrix_set.py -x $x -y $y -R $R -G $G -B $B -C $C";
    echo shell_exec($cmd);
}

if ($_SERVER["REQUEST_METHOD"] == "GET"){
    $response = shell_exec("py led_matrix_get.py");
    echo $response;
}
 