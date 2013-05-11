<?php

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"updateCompany","UPDATE entities SET name=$1, form=$2, ein=$3, country=$4, state=$5, city=$6, email=$7, business_address=$8, mail_address=$9, side=$10 WHERE name=$11");

$result = pg_execute($db,"updateCompany",array($name,$form,$EIN,$country,$state,$city,$email,$bAddress,isset($mAddress)? $mAddress: "",$cSide,$name));

?>
