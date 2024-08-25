<?php
$a=5;

for($i=0;$i<$a;$i++){
    for($j=0;$j<$a;$j++){
        if($i==$j){
            echo "0 ";
        }else{
            echo "1 ";
        }
    }
    echo "</br>";
}



?>