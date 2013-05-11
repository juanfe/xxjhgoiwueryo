{config_load file="menu.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Liquidity Spot</title>
	<meta name="description" content="Web Application" />
	<meta name="keywords" content="web, application" />
	<link href="css/main.css" rel="stylesheet" type="text/css" />
	
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
			<li class="active"><a href="who.php">{#who#}</a></li>
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
				<h2>Who we are</h2>
			</div>
		</div>
	</div>
	
	<div class="wrap">
		<table border="0" width="100%">
			<tr>
				<br><br><h1>John duHadway</h1><a href="mailto:john.duhadway@liquidityspot.com"><img src="images/mail.png"></img></a><br><br><br>
				<h3>Founder</h3><br>
				John has more than 25 years of financial services experience. He led several entrepreneur and early-stage companies in the technology and financial services sectors that, under his leadership, resulted in significant exits for the investors. He negotiated and closed numerous key strategic partnerships, resulting in significant franchise value enhancements. He was a pioneer in the securitization of non agency mortgage assets and has been an industry leader and speaker.  He has authored industry guidance and has represented or assisted various constituencies in formulating industry, accounting and regulatory guidance and regulations, including the Financial Accounting Standards Board, the Mortgage Bankers Association of America, the Department of Housing and Urban Development and the Government National Mortgage Association.  In his mortgage industry positions, John led and was responsible for capital markets, accounting, finance, credit, human resources, facilities and product development. John holds a BS degree in Accounting and is a Certified Public Accountant.
			</tr>
			<tr>
				<br><br><h1>Rich Gupta</h1><a href="mailto:rich.gupta@liquidityspot.com"><img src="images/mail.png"></img></a><br><br><br>
				<h3>Co-founder</h3><br>
				Rich co-founded ASCENT and is the firm’s Risk Manager and Compliance Officer. Prior to joining ASCENT, Rich was a member of the teams that created both Countrywide Alternative Investments and CapitalFusion Partners. Prior to that, he managed the transaction and operational risk management function related to the multi-billion dollar trading books of structured products for Prudential Securities. Rich helped build and manage the infrastructure and operational framework used to originate and manage structured product transactions. Rich holds a B. Com. from University of Allahabad, India. He also holds a MBA in Finance from Long Island University, New York.
			</tr>
			<tr>
				<br><br><h1>Atul Jain</h1><a href="mailto:atul.jain@liquidityspot.com"><img src="images/mail.png"></img></a><br><br><br>
				<h3>Co-founder</h3><br>
				Atul is recognized as a leading consultant and software designer in the Wall Street technology community, where he continues to be an innovator in trading and risk management technology. The enterprise-class systems and the quantitative analysis software that he designed for Citigroup, Nomura, IXIS Real Estate Capital (formerly CDC), Clinton Group, Goldman Sachs, Telerate, Reuters, and many other financial firms have been used to manage multi-billion dollar portfolios across markets, including fixed income, derivatives, equities, FX, and commodities. Prior to founding Vichara, he was CEO of TechHackers, a quantitative financial technology firm that he founded, and Managing Director at Unisys, where he headed the capital markets technology business after Unisys acquired TechHackers. Earlier in his career, he was a management consultant at PriceWaterhouseCoopers and research engineer at HP. Atul holds MS and BS degrees in computer science from MIT, has taught at MIT, and currently serves on the board of the MIT India Program.
			</tr>
		</table>
	</div>
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
