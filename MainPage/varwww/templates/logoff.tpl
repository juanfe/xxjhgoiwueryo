{config_load file="menu.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Liquidity Spot</title>
	<meta name="description" content="Web Application" />
	<meta name="keywords" content="web, application" />
	<link href="css/main.css" rel="stylesheet" type="text/css" />
	<link href="css/screen.css" rel="stylesheet" type="text/css" />
</head>
<body>
	<div id="header">
		<h1><a href="redirector.php?page=index.php&logout=1"><img src="images/logo.jpg"></img></a></h1>
		<ul id="menu">
			<li><a href="redirector.php?page=index.php&logout=1">{#home#}</a></li>
			<li><a href="redirector.php?page=what.php&logout=1">{#what#}</a></li>
			<li><a href="redirector.php?page=how.php&logout=1">{#how#}</a></li>
			{if $sessionStarted eq 1}
			<li><a href="redirector.php?page=sweetSpot.php&logout=1">{#spot#}</a></li>
			{/if}
			<li><a href="redirector.php?page=who.php&logout=1">{#who#}</a></li>
			<li><a href="redirector.php?page=contactUs.php&logout=1">{#contact#}</a></li>
			{if $sessionStarted eq 1}<li><a href="redirector.php?page=logoff.php&logout=1">{#logout#}</a></li>
			{else}<li class="active"><a href="redirector.php?page=login.php&logout=1">{#login#}</a></li>
			{/if}
		</ul>
	</div>

	<div id="title">
		<div id="wrap">
			<div class="titlebox">
				<h2>Log off</h2>
			</div>
		</div>
	</div>

	<div id="container">
		<form id="form1" action="redirector.php?page=index.php&logout=1" method="post">
			<fieldset><legend></legend>
				<p class="first">
					<label for"login">Thank you for using the system.</label>
				</p>
			</fieldset>
			<p class="submit"><button type="submit">go Home</button></p>
		</form>
	</div>
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
