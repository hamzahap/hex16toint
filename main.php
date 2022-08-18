<?php

function twoscomp($bin) {
    $out = "";
    $mode = "init";
    for($x = strlen($bin)-1; $x >= 0; $x--) {
        if ($mode != "init")
            $out = ($bin[$x] == "0" ? "1" : "0").$out;
        else {
            if($bin[$x] == "1") {
                $out = "1".$out;
                $mode = "invert";
            }
            else
                $out = "0".$out;
        }
    }
    return $out;
}

function smartbindec($bin, $a) {
    if($a[0] <= 7)
    return (int) bindec($bin);
    else return -1 * bindec(twoscomp($bin));
}

$a = readline('Enter a string: ');
$b = base_convert($a, 16, 2);
echo $b;
echo "\r\n";
//$a for checking if the first digit of the initial hex was 0 since base_convert doesn't consider 0s
$c = smartbindec($b, $a);
echo $c;  

?>