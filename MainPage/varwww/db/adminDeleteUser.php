<?php

/*
 * Description : This script allows a Liquidity SPOT General Admin to delete a user in a given company.
 * 
 * Requires : Name of the user and name of the company the user belongs to. 
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"userID","SELECT id FROM contacts WHERE name=$1");
$result = pg_prepare($db,"entityID","SELECT id FROM entities WHERE name=$1");
$result = pg_prepare($db,"CAdelUser","DELETE FROM users WHERE contact_id=$1 AND entity_id=$2");

$pResult = true;
$result = pg_execute($db,"userID",array($user));
$row = pg_fetch_assoc($result);
$cid = $row['id'];

$result = pg_execute($db,"entityID",array($company));
$row = pg_fetch_assoc($result);
$eid = $row['id'];

$result = pg_execute($db,"CAdelUser",array($cid,$eid));
if(!$result)
	$pResult = false;

if(!$pResult)
	$result = $pResult;
?>
