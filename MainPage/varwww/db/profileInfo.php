<?php
$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"fIds",'SELECT contact_id, entity_id FROM users WHERE username=$1 ');
$result = pg_prepare($db,"fEntity",'SELECT * FROM entities WHERE id=$1');
$result = pg_prepare($db,"fContact",'SELECT * FROM contacts WHERE id=$1');

$result = pg_execute($db,"fIds",array($_SESSION['user']));
$row = pg_fetch_assoc($result);
$eid = $row['entity_id'];
$cid = $row['contact_id'];

$result = pg_execute($db,"fEntity",array($eid));
$entityRow = pg_fetch_assoc($result);

$result = pg_execute($db,"fContact",array($cid));
$contactRow = pg_fetch_assoc($result);
?>
