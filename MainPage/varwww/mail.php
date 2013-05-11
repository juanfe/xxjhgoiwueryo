<?php
	require_once('libs/Smarty.class.php');
	$smarty = new Smarty();
	
	
	session_start();
	
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

	if(isSet($_POST["name"])){
		$to = "contact@liquidityspot.com";
		$name = $_POST["name"];
		$lastname = $_POST["lastname"];
		$company = $_POST["companyName"];
		$mail = $_POST["email"];
		$phone = $_POST["phone"];
		$subject = "Contact: $name  $lastname from $company";
		$comments = $_POST["comments"];
		$headers = "MIME-Version: 1.0\r\n";
		$headers .="Content-type: text/html; charset=iso-8859-1\r\n";
		$title = "Contact from $name $lastname from $colombia";
		$body = "<html> <head> <title> $title </title> </head> <body> <br> <UL><LI>Name: $name</LI><LI>Lastname: $lastname</LI><LI>Company: $company</LI><LI>Email: $mail</LI><LI>Phone number: $phone</LI><br><br>Comments/Questions:<br>$comments</body></html>";

		if (mail($to, $subject, $body,$headers)) {
			$smarty->assign("success",1);
			$smarty->assign("user",$_SESSION['user']);
		} 
		else {
			$smarty->assign("success",0);
			echo "0";
		}
	}
	else{
		$smarty->assign("success",2);
		echo "2";
	}	
	$smarty->display('mail.tpl');
?>
