<?php
	require_once('libs/Smarty.class.php');
	$smarty = new Smarty();
	
	
	session_start();

      	// Necessary to make "connection" with the glueCode
      	define("AJXP_EXEC", true);
      	$glueCode = "/var/www/html/sweetSpot/plugins/auth.remote/glueCode.php";
      	$secret = "vichara";
	
	global $AJXP_GLUE_GLOBALS;
	$AJXP_GLUE_GLOBALS = array();
	$AJXP_GLUE_GLOBALS["secret"] = $secret;
	$AJXP_GLUE_GLOBALS["plugInAction"] = "logout";
	include($glueCode);
	unset($_SESSION['started']);

	$smarty->assign("admin",0);
	if(isset($_SESSION['started'])){
		$smarty->assign("sessionStarted",$_SESSION['started']);
		$smarty->assign("user",$_SESSION['user']);
		$smarty->assign("companyAdmin",$_SESSION['compAdmin']);
		if($_SESSION['user'] == "admin"){
			$smarty->assign("admin",1);
		}
	}
	else {
		$smarty->assign("sessionStarted",0);
	}
	$smarty->display('logoff.tpl');
?>
