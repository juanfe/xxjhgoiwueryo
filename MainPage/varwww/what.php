<?php
session_start();
	require_once('libs/Smarty.class.php');
	$smarty = new Smarty();

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
	$smarty->display('what.tpl');
?>
