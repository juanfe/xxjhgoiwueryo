{config_load file="statistics.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<link href="../css/main.css" rel="stylesheet" type="text/css" />
	<link href="../css/screen.css" rel="stylesheet" type="text/css" />
	<link href="../css/table.css" rel="stylesheet" type="text/css" />
	
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
</head>

<body>
	{if $companyAdmin eq 1}
	<div id="container">
	Select the User You Want To Delete
	<form id="form2" action="compAdminSureDeleteUser.php" method="post">
			<fieldset><legend>Modify Company</legend>
			<p>
				<label for="mUser">Select the User</label>
				<select name="mUser" style="width:260px">
					{foreach $users as $us}
						{if $us neq $user}
						<option value="{$us['name']}">{$us['name']}</option>
						{/if}
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

