{config_load file="menu.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Liquidity Spot</title>
	<meta name="description" content="Web Application" />
	<meta name="keywords" content="web, application" />
	<link href="css/main.css" rel="stylesheet" type="text/css" />

	<link media="screen" rel="stylesheet" href="css/colorbox.css" />
        <script type="text/javascript" src="js/jquery.js"></script>
        <script src="js/jquery.colorbox.js"></script>
	
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

		$(".button").colorbox({
                        iframe:true,
                        width:"80%",
                        height:"90%",
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
			<li class="active"><a href="how.php">{#how#}</a></li>
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
				<h2>The Liquidity SPOT Exchange Solution</h2>
			</div>
		</div>
	</div>
	
	<div class="wrap2">	
	<div id="howContent">
		<table border="0" width="720" style="table-layout:fixed">
		<tr>
		<td width="650">
			<div class="hContent">
				<h5>High yielding, secured assets;<br>short term duration and commitment</h5>
				<br></br>
				<h1>The process is robust yet simple</h1><br><br><br>
				Approved Mortgage Originators submit an electronic file detailing specific loan level information and their desired advance.  Supply Side Investors can either search criteria and identify loans or prescribe a rate sheet which will auto bid to keep the investor's funds invested subject to the parameters dictated by the investor.  Winning bids are identified and when accepted, funds are moved by the Trustee from the investor's trust account to a loan funding trust account.  Separately, the Mortgage Originator transfers required documents to the Document Custodian.  Real time reports are uploaded from the Document Custodian to the exchange platform.  Upon verification, the Trustee releases funds as instructed.  Once the Mortgage Originator completes the sale, the Custody Documents are released to the Takeout Buyer.  Upon receipt of the funds by the Trustee, the Trustee disburses the funds to the appropriate Supply Side Investor(s).<br><br>
				<h4>
				Supply side investments are collateralized and secured by:
				<UL>
					<LI>Fannie Mae and Freddie eligible paper</LI>
					<LI>Institutional loan purchaser credit</LI>
					<LI>Mortgage originator credit</LI>
					<LI>Real estate property (originated concurrently)</LI>
					<LI>Mortgage borrower credit and cash equity in transaction</LI>
					<LI>Mortgage originator cash equity</LI>
					<LI>Third party secured mortgage and legal documentation</LI>
					<LI>Diversification</LI>
				</UL>
				</h4>
				<br><br><br><br>
				<span style="cursor: pointer;"><a href="images/Overview.jpg" class="button" title="Overview">Overview of our platform</a></span>
                <br></br><br>
		<span style="cursor: pointer;"><a href="images/LSExchangePlatform.jpg" class="button" title="The Platform">The Liquidity SPOT Exchange Platform</a></span>                
			</div>
		</td>
		<td width="300" cellpadding="20">
		<img src="images/how1.png" align="top"><br></br><br></br><br></br><br></br>
		<span style="cursor: pointer;"><a href="https://docs.google.com/spreadsheet/ccc?key=0Aq2jSF1IA0DBdGlTdDFPai03LVI5dUx6dElRNEFVTVE&hl=en_US" class="button" title="Click here to see assets currently available for investment">Assets currently available</a></span>
		<br></br><br></br>
		</td>
		</tr>
		</table>
	<br><br><br>
	</div>
	</div>
	
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
