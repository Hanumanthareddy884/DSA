

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

$ab = [
    // ['name' => 'Reddy', 'age' => '27'],
    // ['name' => 'Tr', 'age' => '23'],
    // ['name' => 'pk', 'age' => '26']
];

// for($i =0;$i<count($ab); $i++){
//         echo $ab[$i]['name'];
//         print("<br>");
//     }

//    echo $ab[0]['name'];

   foreach($ab as $key => $value) {
        echo $value['name'];
        echo $key;
        echo "</br>";
   }
?>
</body>
</html>
