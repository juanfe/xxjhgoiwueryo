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

	<script type="text/javascript" src="js/jquery.js"></script>
    	<script type="text/javascript" src="js/fg.menu.js"></script>
    
        <link type="text/css" href="css/fg.menu.css" media="screen" rel="stylesheet" />
	<link type="text/css" href="images/dropdown/ui.all.css" media="screen" rel="stylesheet" />

	<style type="text/css">
	#menuLog { font-size:1.4em; margin:20px; }
	.hidden { position:absolute; top:0; left:-9999px; width:1px; height:1px; overflow:hidden; }
	
	.fg-button { clear:both; margin:0 0px -30px 0px; padding: .1em 1em; text-decoration:none !important; cursor:pointer; position: relative; text-align: center; zoom: 1}
	.fg-button .ui-icon { position: absolute; top: 50%; margin-top: -8px; left: 50%; margin-left: -8px; }
	a.fg-button { float:right;  }
	button.fg-button { width:auto; overflow:visible; } /* removes extra button width in IE */
	
	.fg-button-icon-left { padding-left: 2.1em; }
	.fg-button-icon-right { padding-right: 2.1em; }
	.fg-button-icon-left .ui-icon { right: auto; left: .2em; margin-left: 0; }
	.fg-button-icon-right .ui-icon { left: auto; right: .2em; margin-left: 0; }
	.fg-button-icon-solo { display:block; width:8px; text-indent: -9999px; }	 /* solo icon buttons must have block properties for the text-indent to work */	
	
	.fg-button.ui-state-loading .ui-icon { background: url(spinner_bar.gif) no-repeat 0 0; }
	</style>
	
	<script type="text/javascript">    
    $(function(){
    	// BUTTONS
    	$('.fg-button').hover(
    		function(){ $(this).removeClass('ui-state-default').addClass('ui-state-focus'); },
    		function(){ $(this).removeClass('ui-state-focus').addClass('ui-state-default'); }
    	);
    	
    	// MENUS    	
		$('#flat').menu({ 
			content: $('#flat').next().html(), // grab content from this page
			showSpeed: 400 
		});
    });
    </script>
</head>
<body>
	<div id="header">
		<h1><a href="redirector.php?page=index.php&user={$user}"><img src="images/logo.jpg"></img></a></h1>
		<ul id="menu">
		{if $sessionStarted eq 1}
			<li><a href="redirector.php?page=index.php&user={$user}&compAdmin={$companyAdmin}">{#home#}</a></li>
			<li><a href="redirector.php?page=what.php&user={$user}&compAdmin={$companyAdmin}">{#what#}</a></li>
			<li><a href="redirector.php?page=how.php&user={$user}&compAdmin={$companyAdmin}">{#how#}</a></li>
			<li><a href="redirector.php?page=sweetSpot.php&user={$user}&compAdmin={$companyAdmin}">{#spot#}</a></li>
			<li><a href="redirector.php?page=who.php&user={$user}&compAdmin={$companyAdmin}">{#who#}</a></li>
			<li><a href="redirector.php?page=contactUs.php&user={$user}&compAdmin={$companyAdmin}">{#contact#}</a></li>
			<li class="active"><a href="redirector.php?page=logoff.php&user={$user}&compAdmin={$companyAdmin}">{#logout#}</a></li>
		{else}
			<li><a href="index.php">{#home#}</a></li>
                        <li><a href="what.php">{#what#}</a></li>
                        <li><a href="how.php">{#how#}</a></li>
                        <li><a href="who.php">{#who#}</a></li>
                        <li><a href="contactUs.php">{#contact#}</a></li>
                        <li class="active"><a href="login.php">{#login#}</a></li>
		{/if}
		</ul>
		{if $sessionStarted eq 1}<br><br><br><br>
		<a tabindex="0" href="#search-engines" class="fg-button fg-button-icon-right ui-widget ui-state-default ui-corner-all" id="flat"><span class="ui-icon ui-icon-triangle-1-s"></span><font color="white">Welcome, {$user}</font></a>
		<div id="search-engines" class="hidden">
		<ul>
			<li><a href="redirector.php?page=profile.php&user={$user}&compAdmin={$companyAdmin}">Profile</a></li>
			{if $admin eq 1}<li><a href="redirector.php?page=adminPanel.php&user={$user}&compAdmin={$companyAdmin}">Admin Panel</a></li>{/if}
			{if $companyAdmin eq 1}<li><a href="redirector.php?page=companyAdminPanel.php&user={$user}&compAdmin={$companyAdmin}">Company Admin Panel</a></li>{/if}
		</ul>
		</div>
		{/if}
	</div>

	<div id="title">
		<div id="wrap">
			<div class="titlebox">
				<h2></h2>
			</div>
		</div>
	</div>

	<div id="container">
		{if 1 eq $sessionStarted}
		<form id="form1" action="redirector.php?page=sweetSpot.php&user={$user}&compAdmin={$companyAdmin}" method="post">
			<fieldset><legend></legend>
				<p class="first">
					<label for"login">Successful log in</label>
				</p>
			</fieldset>
			<p class="submit"><button type="submit">go to the sweet spot</button></p>
		</form>
		{else}
		<form id="form1" action="login.php" method="post">
			<fieldset><legend></legend>
                                <p class="first">
                                        <label for"login">Username/password are not correct. Please try again.</label>
                                </p>
                        </fieldset>
                        <p class="submit"><button type="submit">go to login</button></p>
		</form>
		{/if}
	</div>
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
