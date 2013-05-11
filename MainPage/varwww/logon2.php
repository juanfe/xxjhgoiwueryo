<?php
session_start();
require_once('libs/Smarty.class.php');
$smarty = new Smarty();

if(isSet($_POST["login"]) && isSEt($_POST["password"])){
	$user = $_POST["login"];
	include('db/verifyCredentials.php');
	if($okCredentials){
	define("AJXP_EXEC", true);
      	$glueCode = "/var/www/html/sweetSpot/plugins/auth.remote/glueCodeLiquiditySpot.php";
      	$secret = "vichara";
	$side = $verifiedSide;
      	// Initialize the "parameters holder"
      	global $AJXP_GLUE_GLOBALS;
      	$AJXP_GLUE_GLOBALS = array();
      	$AJXP_GLUE_GLOBALS["secret"] = $secret;
      	$AJXP_GLUE_GLOBALS["plugInAction"] = "login";
      	$AJXP_GLUE_GLOBALS["autoCreate"] = true;
	
      	$AJXP_GLUE_GLOBALS["login"] = array("name" => $_POST["login"], "password" => md5($_POST["password"]));

 	// NOW call glueCode!
      	include($glueCode);

	if($AJXP_GLUE_GLOBALS["result"] == 1){
        	$_SESSION['started'] = 1;
		$_SESSION['user'] = $user;
		if($row['company_admin'] == 't'){
			$smarty->assign("companyAdmin",1);
		}
		else{
			$smarty->assign("companyAdmin",0);
		}
	}
	}
	else{
		unset($_SESSION['started']);
		unset($_SESSION['user']);
	}

}

$smarty->assign("admin",0);
if(isset($_SESSION['started'])){
	$smarty->assign("sessionStarted",1);
	$smarty->assign("user",$_SESSION['user']);
	if($_SESSION['user'] == "admin"){
		$smarty->assign("admin",1);
	}
}
else {
	$smarty->assign("sessionStarted",0);
}
$smarty->display('logon2.tpl');
?>
