<?php

/*
 * Description : This script allows a Liquidity SPOT Admin to delete a company.
 * 
 * Requires : Name of the company to be deleted. 
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"delUsers","DELETE FROM users WHERE entity_id=$1");
$result = pg_prepare($db,"delCompany","DELETE FROM entities WHERE id=$1 ");

$pResult = true;
$result = pg_execute($db,"delUsers",array($eid));
if(!$result)
	$pResult = false;

$result = pg_execute($db,"delCompany",array($eid));
if(!$result)
	$pResult = false;

if(!$pResult)
	$result = $pResult;

?>
