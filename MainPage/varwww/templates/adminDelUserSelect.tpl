{config_load file="menu.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title>Liquidity Spot</title>
	<meta name="description" content="Web Application" />
        <meta name="keywords" content="web, application" />
	<link href="../css/main.css" rel="stylesheet" type="text/css" />
	<link href="../css/screen.css" rel="stylesheet" type="text/css" />
	<link href="../css/table.css" rel="stylesheet" type="text/css" />
	
	<script src="../js/jquery.js" type="text/javascript"></script>
        <script src="../js/jquery.validate.js" type="text/javascript"></script>
	<script type="text/javascript" src="../js/fg.menu.js"></script>

	<link type="text/css" href="../css/fg.menu.css" media="screen" rel="stylesheet" />
        <link type="text/css" href="../images/dropdown/ui.all.css" media="screen" rel="stylesheet" />

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
	$().ready(function() {
		$("#form2").validate({
			rules:{
				mCompany:{
					required: true
				}
			}
		});
	});
	</script>

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

                $(".button2").colorbox({
                        iframe:true,
                        width:"80%",
                        height:"80%"
                });
        });
        </script>
	
</head>

<body>

	{if $admin eq 1}
	<div id="container">
	Please Select the Company you want to delete a user
	<form id="form2" action="adminDelUserSelectUser.php" method="post">
			<fieldset><legend>Select Company</legend>
			<p>
				<label for="mCompany">Select the Company</label>
				<select name="mCompany" style="width:260px">
					{foreach $companies as $company}
						<option value="{$company['name']}">{$company['name']}</option>
					{/foreach}
				</select>
			</p>
			</fieldset>
			<p class="submit"><button type="submit">Select</button></p>
	</form>
	</div>
	{else}
        Unauthorized access.
        {/if}

	<div id="footer">
        </div>
		
</body>
</html>

