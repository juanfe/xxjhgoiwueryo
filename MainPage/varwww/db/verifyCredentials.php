<?php
$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$user = $_POST["login"];
$pass = $_POST["password"];

$result = pg_prepare($db,"verify",'SELECT u.id, u.company_admin, side FROM users as u, entities as e  WHERE u.username=$1 AND u.password=crypt($2,password) AND u.entity_id=e.id');
$result = pg_execute($db,"verify",array($user,$pass));
if (!$result) { 
            echo "There was a problem executing the query. " . $query . "<br/>"; 
            echo pg_last_error(); 
} 
$row = pg_fetch_assoc($result);
$okCredentials = false;	
if(sizeof($row)>0 && $row['id'] != 0) { 
	$verifiedSide = $row['side'];
	$okCredentials = true;
}

?>
