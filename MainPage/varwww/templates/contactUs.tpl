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

	<script src="js/jquery.js" type="text/javascript"></script>
	<script src="js/jquery.validate.js" type="text/javascript"></script>

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

	<script type="text/javascript">
	$().ready(function() {
		$("#formContact").validate({
			rules:{
				name: {
					required: true
				},
				lastName: {
					required: true
				},
				companyName: {
					required: false
				},
				email: {
					required: true,
					email: true
				},
				phone: {
					required: false
				},	
				comments: {
					required: true
				}	
			}
		});
	});
	</script>

	<style type="text/css">
	#formContact label { width: 250px; }
	#formContact label.error, #formContact input.submit { margin-left: 25px; }
	</style>
	
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
			<li class="active"><a href="contactUs.php">{#contact#}</a></li>
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
				<h2>Contact Us</h2>
			</div>
		</div>
	</div>
	
	<div class="wrap2">
	<table border="0" width="100%" style="table-layout:fixed">
		<tr>
			<td width="50%">
				Liquidity Spot</br>
				4607 Lakeview Canyon Rd.,</br>
				Suite 231</br>
				Westlake Village, CA 91361</br>
				Tel: 805.870.5646</br>
				email: contact@liquidityspot.com
				<br></br>
				<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=4607+Lakeview+Canyon+Road&amp;aq=&amp;sll=37.0625,-95.677068&amp;sspn=36.368578,86.572266&amp;vpsrc=6&amp;ie=UTF8&amp;hq=&amp;hnear=4607+Lakeview+Canyon+Rd,+Westlake+Village,+California+91361&amp;ll=34.14755,-118.819393&amp;spn=0.004644,0.010568&amp;t=m&amp;z=14&amp;output=embed"></iframe><br /><small><a href="http://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=4607+Lakeview+Canyon+Road&amp;aq=&amp;sll=37.0625,-95.677068&amp;sspn=36.368578,86.572266&amp;vpsrc=6&amp;ie=UTF8&amp;hq=&amp;hnear=4607+Lakeview+Canyon+Rd,+Westlake+Village,+California+91361&amp;ll=34.14755,-118.819393&amp;spn=0.004644,0.010568&amp;t=m&amp;z=14" style="color:#0000FF;text-align:left">View Larger Map</a></small>
			</td>
			<td width="50%" align="left">
				<div id="container2">
					<form id="formContact" action="mail.php" method="post">
						<fieldset><legend></legend>
							<p class="first">
								<label>* Required</label>
								<label for"firstName">First Name * </label>
								<input type="text" name="name" id="name" size="30" />
							</p>
							<p>
								<label for="lastName">Last Name * </label>
								<input type="text" name="lastName" id="lastName" size="30" />
							</p>
							<p>
								<label for="company">Company Name </label>
								<input type="text" name="companyName" id="companyName" size="30" />
							</p>
							<p>
								<label for="email">Email Address *</label>
								<input type="text" name="email" id="email" size="30" />
							</p>
							<p>
								<label for="phone">Phone Number </label>
								<input type="text" name="phone" id="phone" size="30" />
							</p>
							<p>
								<label for="comments">Comments/Questions *</label>
								<textarea name="comments" cols=40 rows=6 id="comments"></textarea>
							</p>
						</fieldset>
					    <p class="submit"><button type="submit">Submit</button></p>
			 		</form>
				</div>
			</td>
		</tr>
	</table>
	</div>
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
