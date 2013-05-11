<?php

/*
 * Description : This script fetches all the information in the entities table.
 *
 * Requires : nothing.
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$query = "SELECT * FROM entities";

$result = pg_query($query);

if (!$result){
	echo "Problem with query " . $result . "<br/>";
	echo pg_last_error();
	exit();
}
$entitiesArray = array('');
while($row = pg_fetch_assoc($result)){
	$entitiesArray[] = $row;
}


?>
