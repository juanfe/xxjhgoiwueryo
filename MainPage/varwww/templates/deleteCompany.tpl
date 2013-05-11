<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<link href="../css/main.css" rel="stylesheet" type="text/css" />
	<link href="../css/screen.css" rel="stylesheet" type="text/css" />
	<link href="../css/table.css" rel="stylesheet" type="text/css" />
	
	<script src="../js/jquery.js" type="text/javascript"></script>
</head>

<body>
	{if $admin eq 1}
	{if $deleteOK eq 1}
		<div id="container">
		Company deleted
		<form id="form2" action="#" method="post">
			<fieldset><legend>Modify Company</legend>
			<p>
				<label for="mCompany">The company was succesfully deleted.</label>
			</p>
			</fieldset>
		</form>
		</div>
	{else}
		<div id="container">
                ERROR
                <form id="form2" action="deleteCompany.php" method="post">
                        <fieldset><legend>Modify Company</legend>
                        <p>
                                <label for="mCompany">An error ocurred while deleting the company. Please Try again.</label>
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

