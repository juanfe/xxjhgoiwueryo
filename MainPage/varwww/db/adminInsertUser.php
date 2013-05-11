<?php
$db = pg_connect('host=127.0.0.1 port=5432 dbname=LiquiditySpot user=admin password=LSpot');

$result = pg_prepare($db,"adminEntId",'SELECT id FROM entities WHERE name=$1');
$result = pg_prepare($db,"contactExists","SELECT id FROM contacts WHERE name=$1");
$result = pg_prepare($db,"iContact",'INSERT INTO contacts (name,acc_name,title,phone,mobile,email)VALUES($1,$2,$3,$4,$5,$6)');
$result = pg_prepare($db,"cId",'SELECT id FROM contacts WHERE name=$1 AND acc_name=$2 AND phone=$3 AND email=$4');
$result = pg_prepare($db,"iUser","INSERT INTO users (username,password,contact_id,entity_id,company_admin) VALUES ($1,crypt($2,gen_salt('md5')),$3,$4,$5)");

$result = pg_execute($db,"adminEntId",array($company));
$row = pg_fetch_assoc($result);
$eid = $row['id'];

$result = pg_execute($db,"contactExists",array("$fName $lName"));
$row = pg_fetch_assoc($result);
$cid = $row['id'];

if($cid == null || $cid == '' || $cid < 0){

$result = pg_execute($db,"iContact",array("$fName $lName",$susername,isset($sTitle) ? $sTitle : null,intval($phone),isset($mobile) ? intval($mobile) : null, $email ));

$result = pg_execute($db,"cId",array("$fName $lName",$susername,intval($phone),$email));
$row = pg_fetch_assoc($result);
$cid = $row['id'];
}
$result = pg_execute($db,"iUser",array($susername,$spassword,$cid,$eid,$userAdmin));
?>
