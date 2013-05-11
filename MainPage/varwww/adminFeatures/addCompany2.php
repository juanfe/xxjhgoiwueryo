<?php
session_start();
require_once('../libs/Smarty.class.php');
$smarty = new Smarty();

$smarty->setTemplateDir('/var/www/html/templates/');
$smarty->setCompileDir('/var/www/html/templates_c/');
$smarty->setConfigDir('/var/www/html/configs/');
$smarty->setCacheDir('/var/www/html/cache/');

$smarty->assign("admin",0);	
if(isset($_SESSION['started'])){
	$smarty->assign("sessionStarted",1);
	$smarty->assign("user",$_SESSION['user']);
	$smarty->assign("companyAdmin",$_SESSION['compAdmin']);
	if($_SESSION['user'] == "admin"){
		$smarty->assign("admin",1);
	}
}
else {
	$smarty->assign("sessionStarted",0);
}

if(isset($_POST['eName'])){
        $eName = $_POST['eName'];
        $EIN = $_POST['EIN'];
        $eForm = $_POST['eForm'];
	$side = $_POST['side'];
        $country = $_POST['country'];
        $state = $_POST['state'];
        $city = $_POST['city'];
        $bAdd = $_POST['bAdd'];
        $mAdd = $_POST['mAdd'];
        $eemail = $_POST['eemail'];
	$compPhone = $_POST['compPhone'];
	$compAdminUser = $_POST['compAdminUser'];
	$compAdminPass = $_POST['compAdminPass'];
        include('../db/insertCompany.php');
	include('../db/insertAdminUser.php');
	if($result){
		$smarty->assign("cAddSuccess",1);
	}
}

$smarty->display('addCompany2.tpl');
?>
