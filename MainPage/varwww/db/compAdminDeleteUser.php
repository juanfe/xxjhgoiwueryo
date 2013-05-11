<?php

/*
 * Description : This script allows a Liquidity SPOT Admin to delete a company.
 * 
 * Requires : Name of the company to be deleted. 
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"userID","SELECT id FROM contacts WHERE name=$1");
$result = pg_prepare($db,"entityID","SELECT entity_id FROM users WHERE username=$1 ");
$result = pg_prepare($db,"CAdelUser","DELETE FROM users WHERE contact_id=$1 AND entity_id=$2");

$pResult = true;
$result = pg_execute($db,"userID",array($user));
$row = pg_fetch_assoc($result);
$cid = $row['id'];

$result = pg_execute($db,"entityID",array($admin));
$row = pg_fetch_assoc($result);
$eid = $row['entity_id'];

echo "cid: $cid eid: $eid";

$result = pg_execute($db,"CAdelUser",array($cid,$eid));
if(!$result)
	$pResult = false;

if(!$pResult)
	$result = $pResult;
?>
