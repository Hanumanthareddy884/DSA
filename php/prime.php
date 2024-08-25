<?php
$n=7;

for($i=2;$i<=$n;$i++){
    if($n%$i==0){
        echo "Not Prime";
        break;
    }elseif ($i==$n-1){
        echo "Prime number";
        break;
    }
}


?>