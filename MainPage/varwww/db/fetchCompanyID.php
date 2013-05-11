<?php

/*
 * Description : This script allows a Liquidity SPOT Admin to delete a company.
 * 
 * Requires : Name of the company to be deleted. 
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"entID","SELECT id FROM entities WHERE name=$1");

$result = pg_execute($db,"entID",array($company));
$row = pg_fetch_assoc($result);
$eid = $row['id'];

?>
