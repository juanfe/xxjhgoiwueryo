<?php

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"sUser","SELECT * FROM contacts WHERE name=$1");

$result = pg_execute($db,"sUser",array($user));;

if (!$result){
	echo "Problem with query " . $result . "<br/>";
	echo pg_last_error();
	exit();
}
$userInfo = pg_fetch_assoc($result);
?>
