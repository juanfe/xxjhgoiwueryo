<?php

/*
 * Description : This script allows a Liquidity SPOT General Admin to see the users of a selected company.
 *	         First the system finds the entityID of the selected company and then fetches the contacts information that matches the entity_id.
 *
 * Requires : Company name.
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"entId",'SELECT id FROM entities WHERE name=$1');
$result = pg_prepare($db,"uList",'SELECT name FROM users as u, contacts as c WHERE u.entity_id=$1 AND c.id=u.contact_id');

$result = pg_execute($db,"entId",array($company));
$row = pg_fetch_assoc($result);
$eid = $row['id'];

$result = pg_execute($db,"uList",array($eid));
if (!$result){
	echo "Problem with query " . $result . "<br/>";
	echo pg_last_error();
	exit();
}
$usersArray = array('');
while($row = pg_fetch_assoc($result)){
	$usersArray[] = $row;
}
?>
