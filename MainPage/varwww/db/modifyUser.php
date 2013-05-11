<?php

/*
 * Description : This script allows a Liquidity SPOT Company Admin to update information of a user within its company.
 * 
 * Requires : All the required fields in the contacts table of the LiquiditySpot database. (name,acc_name,title,phone,mobile,email)
 *	      The original name. 
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"updateUser","UPDATE contacts SET name=$1, acc_name=$2, title=$3, phone=$4, mobile=$5, email=$6 WHERE name=$7");

$result = pg_execute($db,"updateUser",array($name,$accName,$uTitle,$phone,isset($mobile)? intVal($mobile): null,$email,$origUser));

?>
