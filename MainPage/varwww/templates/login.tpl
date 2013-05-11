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
		<h1><a href="index.php"><img src="images/logo.jpg"></img></a></h1>
		<ul id="menu">
			<li><a href="index.php">{#home#}</a></li>
			<li><a href="what.php">{#what#}</a></li>
			<li><a href="how.php">{#how#}</a></li>
			{if $sessionStarted eq 1}
			<li><a href="sweetSpot.php">{#spot#}</a></li>
			{/if}
			<li><a href="who.php">{#who#}</a></li>
			<li><a href="contactUs.php">{#contact#}</a></li>
			{if $sessionStarted eq 1}<li><a href="logoff.php">{#logout#}</a></li>
			{else}<li class="active"><a href="login.php">{#login#}</a></li>
			{/if}
		</ul>
	</div>

	<div id="title">
		<div id="wrap">
			<div class="titlebox">
				<h2>Log in</h2>
			</div>
		</div>
	</div>

	<div id="container">
		<form id="form1" action="http://www.liquidityspot.com/logon2.php" method="post">
			<fieldset><legend>Please log in</legend>
				<p class="first">
					<label for"login">Login</label>
					<input type="text" name="login" id="login" size="30" />
				</p>
				<p>
					<label for="password">Password</label>
					<input type="password" name="password" id="password" size="30" />
				</p>
			</fieldset>
			<p class="submit"><button type="submit">Log In</button></p>
		</form>
	</div>
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
