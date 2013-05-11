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

if(isset($_POST['cSide'])){
	$name = $_POST['name'];
	$form = $_POST['form'];
	$EIN = $_POST['EIN'];
	$country = $_POST['country'];
	$state = $_POST['state'];
	$city = $_POST['city'];
	$email = $_POST['email'];
	$bAddress = $_POST['bAddress'];
	if(isset($_POST['mAddress'])){
		$mAddress = $_POST['mAddress'];
	}
	$cSide = $_POST['cSide'];
	$smarty->assign("updatedOk",0);
	include("../db/modifyCompany.php");
	if($result)
		$smarty->assign("updatedOk",1);	
}

$smarty->display('modifyCompany2.tpl');
?>
