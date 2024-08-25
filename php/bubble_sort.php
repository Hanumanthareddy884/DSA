<?php
$array = [2,85,1,95,76,2,9];

print_r(array_values($array));

for($i=0;$i<sizeof($array);$i++){

    for($j=0;$j<sizeof($array);$j++){
        if($array[$j]>$array[$i]){
            $temp = $array[$i];
            $array[$i] = $array[$j];
            $array[$j] = $temp;
        }
    }
}

print_r($array);

?>