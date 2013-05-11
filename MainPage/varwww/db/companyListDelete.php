<?php

/*
 * Description : This script fetches all the information in the entities table.
 *
 * Requires : nothing.
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"eIDdelete","SELECT entity_id FROM users WHERE username=$1");
$result = pg_prepare($db,"AdminSelDelete","SELECT * FROM entities WHERE id!=$1");

$result = pg_execute($db,"eIDdelete",array($user));
$row = pg_fetch_assoc($result);
$eid = $row['entity_id'];

$result = pg_execute($db,"AdminSelDelete",array($eid));
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
