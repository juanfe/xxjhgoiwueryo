<?php

/*
 * Description : This script allows a Liquidity SPOT General Admin to create a Company Admin. This is done when a General Admin wants to create a new company.
 *		 First, the contact is inserted in the system (contacts table). Second, they system finds the contact_id and entity_id. Third, the user is inserted using these previous values and a default TRUE in the company_admin field of the table.
 *
 * Requires : All the required fields in the contacts table of the LiquiditySpot database. (name,acc_name,title,phone,mobile,email)
 * 	      All the required fileds in the users table of the LiquiditySpot database. (username,password,contact_id,entity_id)
 */

$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"iContact",'INSERT INTO contacts (name,acc_name,title,phone,mobile,email)VALUES($1,$2,$3,$4,$5,$6)');
$result = pg_prepare($db,"cId",'SELECT id FROM contacts WHERE name=$1 AND acc_name=$2 AND title=$3 AND phone=$4 AND email=$5');
$result = pg_prepare($db,"eId",'SELECT id FROM entities WHERE name=$1');
$result = pg_prepare($db,"iUser","INSERT INTO users (username,password,contact_id,entity_id,company_admin) VALUES ($1,crypt($2,gen_salt('md5')),$3,$4,$5)");

$result = pg_execute($db,"iContact",array("$eName Admin","$eName Admin","Company Admin",isset($compPhone) ? intval($compPhone) : null,null,$eemail));

$result = pg_execute($db,"cId",array("$eName Admin","$eName Admin","Company Admin",isset($compPhone) ? intval($compPhone) : null,$eemail));
$row = pg_fetch_assoc($result);
$cid = $row['id'];

$result = pg_execute($db,"eId",array($eName));
$row = pg_fetch_assoc($result);
$eid = $row['id'];

$result = pg_execute($db,"iUser",array($compAdminUser,$compAdminPass,$cid,$eid,TRUE));

?>
