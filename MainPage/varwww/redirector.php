<?php
session_start();
require_once('libs/Smarty.class.php');
$smarty = new Smarty();

if(isset($_GET["logout"])){
	unset($_SESSION['user']);
	unset($_SESSION['started']);
	if(isset($_SESSION['compAdmin'])){
		unset($_SESSION['compAdmin']);
	}
}
else{
	$_SESSION['started'] = 1;
	$_SESSION['user'] = $_GET['user'];
	$_SESSION['compAdmin'] = $_GET['compAdmin'];
}

$smarty->assign("page",$_GET['page']);
	
$smarty->display('redirector.tpl');
?>
