<?php
$year = 2027;
if($year %400 ==0 && $year % 100 || $year % 4 ==0){
    echo "$year is leap year";
}else{
    echo "This is not leap year";
}


?>