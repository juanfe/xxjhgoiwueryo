<?php

/*
 * Description : This script allows a Liquidity SPOT Company Admin to see the users its company has registered.
 *	         First the system finds the entityID of the user and then fetches the contacts information that matches the entity_id.
 *
 * Requires : All the required fields in the contacts table of the LiquiditySpot database. (name,acc_name,title,phone,mobile,email)
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"eId",'SELECT entity_id FROM users WHERE username=$1');
$result = pg_prepare($db,"uList",'SELECT c.name, c.acc_name, c.title, c.phone, c.mobile, c.email FROM users as u, contacts as c WHERE u.entity_id=$1 AND c.id=u.contact_id');

$result = pg_execute($db,"eId",array($suser));
$row = pg_fetch_assoc($result);
$eid = $row['entity_id'];

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
