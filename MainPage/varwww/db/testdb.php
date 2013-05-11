<?php
echo "starting...";
$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$query = "SELECT * FROM contacts";
echo "about to start: ";
$result = pg_query($query);
if (!$result) { 
            echo "Problem with query " . $query . "<br/>"; 
            echo pg_last_error(); 
            exit(); 
        } 

        while($myrow = pg_fetch_assoc($result)) { 
             echo $myrow['name'];
        }

?>
