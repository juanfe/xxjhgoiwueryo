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

if(isset($_POST['mUser'])){
	$smarty->assign("user",$_POST['mUser']);
	$smarty->assign("company",$_GET['company']);
}

$smarty->display('adminSureDeleteUser.tpl');

?>
