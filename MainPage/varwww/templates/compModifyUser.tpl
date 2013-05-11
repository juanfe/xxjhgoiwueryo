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
				name:{
					required: true
				},
				accName:{
					required: true
				},
				uTitle:{
					required: true
				},
				phone:{
					required: true,
					number: true
				},
				mobile:{
					required: false,
					number: true
				},
				email:{
					required: true,
					email: true
				}
			}
		});
	});
	</script>
</head>

<body>
	{if $companyAdmin eq 1}
	<div id="container">
	<form id="form2" action="compModifyUser2.php?origUser={$user['name']}" method="post">
			<fieldset><legend>Modify User</legend>
			<table border="0">
			<tr>
				<table id="table-3" >
					<tr>
					<td>
						<label for="name">Name*: </label>
						<input type="text" name="name" id="name" size="10" value="{$user['name']}" />
					</td>
					<td>
						<label for="accName">Account Name*: </label>
                                                <input type="text" name="accName" id="accName" size="10" value="{$user['acc_name']}" />
					</td>
					<td>
						<label for="uTitle">Title*: </label>
                                                <input type="text" name="uTitle" id="uTitle" size="10" value="{$user['title']}" />
					</td>
					</tr>
				</table>
			</tr>
			<tr>
				<br>
				<table id="table-3">
					<tr>
					<td>
						<label for="phone">Phone*: </label>
                                                <input type="text" name="phone" id="phone" size="10" value="{$user['phone']}" />
					</td>
					<td>
                                                <label for="mobile">Mobile: </label>
                                                <input type="text" name="mobile" id="mobile" size="10" value="{$user['mobile']}" />
					</td>
					<td>
						<label for="email">Email*: </label>
                                                <input type="text" name="email" id="email" size="10" value="{$user['email']}" />
					</td>
					</tr>
				</table>
			</tr>
			</fieldset>
			<p class="submit"><button type="submit">Modify</button></p>
	</form>
	</div>
	{else}
        Unauthorized access.
        {/if}
		
	<div id="footer">
	</div>
</body>
</html>

