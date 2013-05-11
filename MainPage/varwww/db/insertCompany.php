<?php
$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"iCompany",'INSERT INTO entities (name,business_address,form,email,city,state,country,ein,mail_address,side) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10) ');

$result = pg_execute($db,"iCompany",array($eName,$bAdd,$eForm,$eemail,$city,$state,$country,$EIN,$mAdd,$side));
?>
