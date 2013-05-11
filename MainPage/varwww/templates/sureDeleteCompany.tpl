<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<link href="../css/main.css" rel="stylesheet" type="text/css" />
	<link href="../css/screen.css" rel="stylesheet" type="text/css" />
	<link href="../css/table.css" rel="stylesheet" type="text/css" />
	
	<script src="../js/jquery.js" type="text/javascript"></script>
        <script src="../js/jquery.validate.js" type="text/javascript"></script>
</head>

<body>
	{if $admin eq 1}
	<div id="container">
	Confirm that you want to delete {$mCompany}
	<form id="form2" action="deleteCompany.php?delete=true&eid={$entityID}" method="post">
			<fieldset><legend>Modify Company</legend>
			<p>
				<label for="mCompany">Please confirm that you want to delete {$mCompany} and all its users. If you don't want to delete it please close the window.</label>
			</p>
			</fieldset>
			<p class="submit"><button type="submit" >Confirm</button></p>
	</form>
	</div>
	{else}
        Unauthorized access.
        {/if}
		
	<div id="footer">
	</div>
</body>
</html>

