{config_load file="menu.conf"}
{config_load file="statistics.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Liquidity Spot</title>
	<meta name="description" content="Web Application" />
	<meta name="keywords" content="web, application" />
	
	<link href="css/main.css" rel="stylesheet" type="text/css" />
	<link href="css/table.css" rel="stylesheet" type="text/css" />
	
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
	
	<link rel="icon" href="favicon.ico" type="image/x-icon" />
	<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
</head>
<body>
	<div id="header">
		<h1><a href="index.php"><img src="images/logo.jpg"></img></a></h1>
		<ul id="menu">
			<li class="active"><a href="index.php">{#home#}</a></li>
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

	<div id="teaser">
		<div class="wrap">
			<div id="image"></div>
			<div class="box">
				<h2>Welcome to the SPOT!</em></h2>
				<h4><p><UL><LI>Investors can invest short term cash in high yielding, collateralized assets.</LI><LI>Mortgage originators can obtain customized warehouse financing for their mortgage loans.</LI><LI>We employ social media technology to provide for a transparent, reputation economy.</Li></UL></p></h4>
			</div>
		</div>
	</div>

	<div class="wrap3">
	<div class="col" align="center">
                        <h3>Exchange <span class="orange">Statistics</span></h3>
                        <table id="table-3">
                                <thead>
                                        <th></th>
                                        <th>Today</th>
                                        <th>Last 7 days</th>
                                        <th>Last 30 days</th>
                                </thead>
                        <tbody>
                        <tr><td># of loans</td><td>{#numLoansToday#}</td><td>{#numLoans7#}</td><td>{#numLoans30#}</td>
                        </tr>
                        <tr><td>Principal amount</td><td>{#pAmountToday#}</td><td>{#pAmount7#}</td><td>{#pAmount30#}</td>
                        </tr>
                        <tr><td>WA demand side rate</td><td>{#WAdemandSideRateToday#}</td><td>{#WAdemandSideRate7#}</td><td>{#WAdemandSideRate30#}</td>
                        </tr>
                        <tr><td>WA supply side yield</td><td>{#WAsupplySideYieldToday#}</td><td>{#WAsupplySideYield7#}</td><td>{#WAsupplySideYield30#}</td>
                        </tr>
                        <tr><td>WA duration (days)</td><td>{#WAdurationToday#}</td><td>{#WAduration7#}</td><td>{#WAduration30#}</td>
                        </tr>
                        </tbody>
                        </table>
                        {if $admin eq 1}
                        <br><span style="cursor: pointer;"><a href="adminFeatures/editStatistics.php" class="button" title="Click here to modify statistics">EDIT</a></span>
                        {/if}
         </div>
		<div class="col" align="center">
			<h3>What's hot at the <span class="orange">SPOT</span></h3>
			<!-- Feedzilla Widget BEGIN -->

<div class="feedzilla-news-widget feedzilla-9021723826881498" style="width:250px; padding: 0; text-align: center; font-size: 11px; border: 0;">
<script type="text/javascript" src="http://widgets.feedzilla.com/news/iframe/js/widget.js"></script>
<script type="text/javascript">
new FEEDZILLA.Widget({
	style: 'slide-left-to-right',
		culture_code: 'en_us',
			q: 'Bloomberg',
				headerBackgroundColor: '#013b4f',
					footerBackgroundColor: '#013b4f',
						title: 'Bloomberg',
							order: 'relevance',
								count: '20',
									w: '250',
										h: '300',
											timestamp: 'true',
												scrollbar: 'false',
													theme: 'ui-lightness',
														className: 'feedzilla-9021723826881498'
														});
														</script><br />
														</div>

<!-- Feedzilla Widget END -->
		</div>
		<div class="col last" align="center">
			<h3>About <span class="orange">Liquidity Spot</span></h3>
			<h6><p align="justify">Liquidity <span class="orange">SPOT</span> brings a fresh approach and perspective to mortgage warehouse financing. Our warehouse exchange platform enables the supply side and demand side to seamlessly price and fulfill warehouse advance transactions in a clear, transparent, reputation and data based ecosystem.<br>Traditionally, only banks with warehouse lending infrastructures could participate - and thereby reap the returns of warehouse financing. Our exchange platform disrupts the barriers and allows investors big and small to compete and earn above market short term secured returns. Institutions can identify their own customer on the demand side and support them by bidding on their loans, perhaps being more aggressive than those in the general population. We enable community banks to outsource the infrastructure, yet maintain the local community activity and investment that they desire.</p></h6>
		</div>
	<iframe src="//www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.liquidityspot.com&amp;send=false&amp;layout=standard&amp;width=450&amp;show_faces=false&amp;action=like&amp;colorscheme=light&amp;font&amp;height=35" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:450px; height:35px;" allowTransparency="true"></iframe>
	</div>

	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
