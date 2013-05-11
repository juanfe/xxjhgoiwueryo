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
	{if $deletionOK eq 1}
	<div id="container">
	User deleted
	<form id="form2" action="compAdminDeleteUser.php?user={$user}" method="post">
			<fieldset><legend>Delete User</legend>
			<p>
				<label for="mUser">The user was succesfully deleted.</label>
			</p>
			</fieldset>
	</form>
	</div>
	{else}
	<div id="container">
        ERROR
        <form id="form2" action="compAdminDeleteUser.php?user={$user}" method="post">
                        <fieldset><legend>Delete User</legend>
                        <p>
                                <label for="mUser">Error deleting user. Please try again.</label>
                        </p>
                        </fieldset>
        </form>
        </div>
	{/if}
	{else}
        Unauthorized access.
        {/if}
		
	<div id="footer">
	</div>
</body>
</html>

