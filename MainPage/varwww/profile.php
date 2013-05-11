<?php
session_start();
	require_once('libs/Smarty.class.php');
	$smarty = new Smarty();

	include('db/profileInfo.php');
	$smarty->assign("LNE",$entityRow['name']);
	$smarty->assign("FOE",$entityRow['form']);
	$smarty->assign("EIN",$entityRow['ein']);
	$smarty->assign("BADD",$entityRow['business_address']);
	$smarty->assign("MADD",$entityRow['mail_address']);
	$smarty->assign("Contact",$contactRow['name']);
	$smarty->assign("Owner",$contactRow['acc_name']);
	$smarty->assign("Name",$contactRow['name']);
	$smarty->assign("AccName",$contactRow['acc_name']);
	$smarty->assign("Title",$contactRow['title']);
	$smarty->assign("Phone",$contactRow['phone']);
	$smarty->assign("Mobile",$contactRow['mobile']);
	$smarty->assign("email",$contactRow['email']);

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
	$smarty->display('profile.tpl');
?>
