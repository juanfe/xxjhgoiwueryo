{config_load file="menu.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Liquidity Spot</title>
	<meta name="description" content="Web Application" />
	<meta name="keywords" content="web, application" />
	<link href="css/main.css" rel="stylesheet" type="text/css" />
	<link href="css/table.css" rel="stylesheet" type="text/css" />

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
        .fg-button-icon-solo { display:block; width:8px; text-indent: -9999px; }         /* solo icon buttons must have block properties for the text-indent to work */

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
			{else}<li><a href="login.php">{#login#}</a></li>
			{/if}
		</ul>
		{if $sessionStarted eq 1}<br><br><br><br><br>
		<a tabindex="0" href="#search-engines" class="fg-button fg-button-icon-right ui-widget ui-state-default ui-corner-all" id="flat"><span class="ui-icon ui-icon-triangle-1-s"></span><font color="white">Welcome, {$user}</font></a>
                <div id="search-engines" class="hidden">
                <ul>
                        <li><a href="profile.php">Profile</a></li>
                        {if $admin eq 1}<li><a href="adminPanel.php">Admin Panel</a></li>{/if}
                        {if $companyAdmin eq 1}<li><a href="companyAdminPanel.php">Company Admin Panel</a></li>{/if}
                </ul>
                </div>
		{/if}
	</div>

	<div id="title">
		<div id="wrap">
			<div class="titlebox">
				<h2>Profile</h2>
			</div>
		</div>
	</div>

	<div class="wrap2">
		<table border="0">
			<tr>
				<h3>Entity Information</h3>
				<table id="table-3">
					<tr><td>Legal name of entity: {$LNE}</td><td>Form of entity (c corp, s corp, LLC, LLP, etc): {$FOE}	</td></tr>
					<tr><td>E.I.N.#: {$EIN}</td><td></td></tr>
					<tr><td>Business address: {$BADD}</td><td>Mailing Address: {$MADD}</td></tr>
				</table>
			</tr>
			<tr>
				<br><br><br>
				<h3>Contact Information</h3>
				<table id="table-3">
					<tr><td>Contact<br><span class="boldbig">{$Contact}</span></td><td>User Name<br><span class="boldbig">{$user}</span></td></tr>
				</table>
			</tr>
			<tr>
				<br><br>
				<table id="table-3">
					<tr><td>Contact Owner: {$Owner}</td><td>Phone Number: {$Phone}</td></tr>
					<tr><td>Name: {$Contact}</td><td>Mobile Number: {$Mobile}</td></tr>
					<tr><td>Account Name: {$AccName}</td><td>Email: {$email}</td></tr>
					<tr><td>Title: {$Title}</td><td></td></tr>
				</table>
			</tr>
		</table>
	</div>
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
