{config_load file="statistics.conf"}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
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
	{if $updatedOk eq 1}
	<div id="container">
	<form id="form2" action="#" method="post">
			<fieldset><legend>Modify Company</legend>
				<p class="first">
                                        <label for"login">Company Successfully Updated</label>
                                </p>
			</fieldset>
	</form>
	</div>
	{else}
	<div id="container">
        <form id="form2" action="#" method="post">
                        <fieldset><legend>Modify Company</legend>
                                <p class="first">
                                        <label for"login">An Error Ocurred While Updating the Company. Please Try Again.</label>
                                </p>
                        </fieldset>
        </form>
        </div>
        {/if}
	{/if}
		
	<div id="footer">
	</div>
</body>
</html>

