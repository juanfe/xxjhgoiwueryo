{config_load file="menu.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>Liquidity Spot - Sign up</title>
	
	<link href="../css/main.css" rel="stylesheet" type="text/css" />
	<link href="../css/screen.css" rel="stylesheet" type="text/css" />
	
	
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

	// validate the comment form when it is submitted
	$("#form3").validate({
		rules:{
			susername: {
				required: true,
				minlength: 5,
				maxlength: 15,
				userDoesNotExist: true,
				noSpace: true
			},
			spassword: {
				required: true,
				minlength: 5,
				maxlength: 15
			},
			password2: {
				required: true,
				minlength: 5,
				maxlength: 15,
				passwordsMatch: true
			},
			cName: {
				required: true			
			},
			fName: {
				required: true
			},
			lName: {
				required: true
			},
			sTitle: {
				required: false
			},
			phone: {
				required: true,
				number: true
			},
			mobile: {
				required: false,
				number: true
			},
			email: {
				required: true,
				email: true
			}
		},
		messages: {
			susername: {
				minlength: "Your username must be at least 5 characters long",
				maxlength: "Your username must have less than 15 characters"
			},
			spassword: {
				minlength: "Your password must be at least 5 characters long",
				maxlength: "Your password must have less than 15 characters"
			},
			password2: {
				minlength: "Your password must be at least 5 characters long",
				maxlength: "Your password must have less than 15 characters"
			}
		}	
	});
});

jQuery.validator.addMethod( 
	  "passwordsMatch", 
	  function(value, element) { 
	  if ($("#spassword").val()!= $("#password2").val()){ 
		      return false; 
	  } 	   
	  else return true; 	  
	  }, 
	  "Passwords should match"
	);

jQuery.validator.addMethod(
	"noSpace",
	function(value, element) {
		return $("#susername").val().indexOf(" ") < 0;
	},
	"Username should not have any space"
	);

var userglobalvar=true;
jQuery.validator.addMethod(
        "userDoesNotExist",
        function(value,element){
		return userglobalvar;
	},
        "Username is already taken, please choose a different one."
        );
function setUserGlobalVar(msg){
	if(msg == "true"){
		userglobalvar = false;
	}
	else if(msg == "false"){
		userglobalvar = true;
	}
}

function checkUser(){
	var user = $("#susername").val();
	$.ajax({
                        type: "POST",
                        url: "../db/checkUser.php",
                        data: "checkUsername="+user,
                        dataType: "text",
                        success: function(msg)
                        {
                                setUserGlobalVar(msg);
                        }
        });

}

</script>

<style type="text/css">
#form3 { width: 600px; }
#form3 label { width: 250px; }
#form3 label.error, #form3 input.submit { margin-left: 253px; }
</style>
	
</head>
<body>
	<div id="header">
		<h1><a href="../index.php"><img src="../images/logo.jpg"></img></a></h1>
		<ul id="menu">
			<li><a href="../index.php">{#home#}</a></li>
			<li><a href="../what.php">{#what#}</a></li>
			<li><a href="../how.php">{#how#}</a></li>
			{if $sessionStarted eq 1}
			<li><a href="../sweetSpot.php">{#spot#}</a></li>
			{/if}
			<li><a href="../who.php">{#who#}</a></li>
			<li><a href="../contactUs.php">{#contact#}</a></li>
			{if $sessionStarted eq 1}<li><a href="../logoff.php">{#logout#}</a></li>
			{else}<li class="active"><a href="../login.php">{#login#}</a></li>
			{/if}
		</ul>
		{if $sessionStarted eq 1}<br><br><br><br><br>
                <a tabindex="0" href="#search-engines" class="fg-button fg-button-icon-right ui-widget ui-state-default ui-corner-all" id="flat"><span class="ui-icon ui-icon-triangle-1-s"></span><font color="white">Welcome, {$user}</font></a>
                <div id="search-engines" class="hidden">
                <ul>
                        <li><a href="../profile.php">Profile</a></li>
                        {if $admin eq 1}<li><a href="../adminPanel.php">Admin Panel</a></li>{/if}
                        {if $companyAdmin eq 1}<li><a href="../companyAdminPanel.php">Company Admin Panel</a></li>{/if}
                </ul>
                </div>
                {/if}
	</div>

	<div id="title">
		<div id="wrap">
			<div class="titlebox">
				<h2>Sign up form</h2>
			</div>
		</div>
	</div>

	{if $companyAdmin eq 1}
	<div id="container">
	<form id="form3" action="addUser2.php" method="post">
			<fieldset><legend>Sign up form</legend>
				<p class="first">
					<label for"susername">New Username *</label>
					<input type="text" name="susername" id="susername" size="25" onChange="checkUser()"/>
				</p>
				<p>
					<label for="spassword">Password *</label>
					<input type="password" name="spassword" id="spassword" size="25" />
				</p>
				<p>
					<label for="password2">Password Again *</label>
					<input type="password" name="password2" id="password2" size="25" />
				</p>
				<p>
					<label for="fname">First Name *</label>
					<input type="text" name="fName" id="fName" size="25" />
				</p>
				<p>
					<label for="lname">Last Name *</label>
					<input type="text" name="lName" id="lName" size="25" />
				</p>
				<p>
					<label for="title">Title</label>
					<input type="text" name="sTitle" id="sTitle" size="25" />
				</p>
				<p>
					<label for="phone">Phone Number *</label>
					<input type="text" name="phone" id="phone" size="25" />
				</p>
				<p>
					<label for="mobile">Mobile Number</label>
					<input type="text" name="mobile" id="mobile" size="25" />
				</p>
				<p>
					<label for="email">Email *</label>
					<input type="text" name="email" id="email" size="25" />
				</p>
			</fieldset>
			<p class="submit"><button type="submit">Create</button></p>
		</form>
	</div>
	{else}
		<h1>You are not authorized to see this page.</h1>
	{/if}
		
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="../index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
