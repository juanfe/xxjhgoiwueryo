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

	if(isset($_GET['company'])){
		$company = $_GET['company'];
		$smarty->assign("company",$company);
		if(isset($_POST['susername'])){
			$susername = $_POST['susername'];
	       		$spassword = $_POST['spassword'];
        		$fName = $_POST['fName'];
		        $lName = $_POST['lName'];
			$userAdmin = $_POST[''];

	        	if(isset($_POST['sTitle'])){
                		$sTitle = $_POST['sTitle'];
	        	}

        		$phone = $_POST['phone'];

		        if(isset($_POST['mobile'])){
        	        	$mobile = $_POST['mobile'];
	        	}

        		$email = $_POST['email'];
			$userAdmin = 'f';
			if($_POST['userAdmin'] == "YES")
				$userAdmin = 't';

			echo "userAdmin: $userAdmin company: $company";
			$smarty->assign("adminuAddSuccess",0);
			include("../db/adminInsertUser.php");
			if($result)
				$smarty->assign("adminuAddSuccess",1);
		}
	}
	$smarty->display('adminAddUser2.tpl');
?>
