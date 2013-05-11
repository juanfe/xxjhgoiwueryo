<?php

/*
 * Description : This script search for a user in the database. if it exists return true and false otherwise. This script is called in the validation of the creation of a new normal user aswell as in the creation of a new company/company admin user.
 *
 * Requires : Name of the user to check.
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$user = $_POST['checkUsername'];

$query = "SELECT * FROM users WHERE username='$user'";

$result = pg_query($query);
if (!$result) { 
            echo "Problem with query " . $query . "<br/>"; 
            echo pg_last_error(); 
            exit(); 
        } 

$row = pg_fetch_assoc($result);
$id = $row['id'];
$username = $row['username'];
if(sizeof($row)>0 && $id!=0) { 
      echo "true";
      exit();
}
else{

echo "false";
exit();
}

?>
