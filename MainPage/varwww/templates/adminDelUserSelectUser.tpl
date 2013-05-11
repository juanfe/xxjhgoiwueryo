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
	
	<script src="../js/jquery.js" type="text/javascript"></script>
        <script src="../js/jquery.validate.js" type="text/javascript"></script>

	<script type="text/javascript">
	$().ready(function() {
		$("#form2").validate({
			rules:{
				mUser:{
					required: true
				}
			}
		});
	});
	</script>

<body>

	{if $admin eq 1}
	<div id="container">
	Please Select the User you want to modify
	<form id="form2" action="adminSureDeleteUser.php?company={$company}" method="post">
			<fieldset><legend>Modify Company</legend>
			<p>
				<label for="mUser">Select the User</label>
				<select name="mUser" style="width:260px">
					{foreach $users as $user}
						<option value="{$user['name']}">{$user['name']}</option>
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

