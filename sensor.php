<?php

// rest api to read sense-hat sensor values
$r = true;
$p = true;
$y = true;
$u = "deg";
$P = "hPa";
$T = "C";
$H = "%";

if ($_SERVER["REQUEST_METHOD"] == "GET"){
    if (isset($_POST["r"])) $r = $_POST["r"];
    if (isset($_POST["p"])) $p = $_POST["p"];
    if (isset($_POST["y"])) $y = $_POST["y"];
    if (isset($_POST["u"])) $u = $_POST["u"];
    if (isset($_POST["P"])) $P = $_POST["P"];
    if (isset($_POST["T"])) $T = $_POST["T"];
    if (isset($_POST["H"])) $H = $_POST["H"];
    $cmd = "py read_sensors.py -r $r -p $p -y $y -u $u -P $P -T $T -H $H";
    echo shell_exec($cmd);
    }

?>
