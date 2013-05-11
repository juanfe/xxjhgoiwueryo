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
				mCompany:{
					required: true
				}
			}
		});
	});
	</script>
</head>

<body>
	{if $admin eq 1}
	<div id="container">
	Select the Company You Want To Modify
	<form id="form2" action="modifyCompany.php" method="post">
			<fieldset><legend>Modify Company</legend>
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

