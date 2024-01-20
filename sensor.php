<?php
header('Access-Control-Allow-Origin: *');

$r = true;
$p = true;
$y = true;
$u = "deg";
$P = "hPa";
$T = "C";
$H = "%";

if ($_SERVER["REQUEST_METHOD"] == "GET"){
	$r = $_GET["r"];
    $p = $_GET["p"];
    $y = $_GET["y"];
    $u = $_GET["u"];
    $P = $_GET["P"];
    $T = $_GET["T"];
    $H = $_GET["H"];
    $cmd = "python read_sensors.py -r $r -p $p -y $y -u $u -P $P -T $T -H $H";
    echo shell_exec($cmd);
    }

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $r = $_POST["r"];
    $p = $_POST["p"];
    $y = $_POST["y"];
    $u = $_POST["u"];
    $P = $_POST["P"];
    $T = $_POST["T"];
    $H = $_POST["H"];
    $cmd = "python read_sensors.py -r $r -p $p -y $y -u $u -P $P -T $T -H $H";
    echo shell_exec($cmd);
    }

?>
