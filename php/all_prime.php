<?php
$n = 15;
$a = [2];
for($i=1;$i<=$n;$i++){


    for($j=2;$j<=$i;$j++){
        if($i%$j ==0){
            break;
        }elseif ($j == $i-1){
            array_push($a,$i);
            break;
        }
    }
}
print_r($a);

?>