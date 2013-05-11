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
				form:{
					required: true
				},
				EIN:{
					required: true
				},
				country:{
					required: true
				},
				state:{
					required: true
				},
				city:{
					required: true
				},
				email:{
					required: true,
					email: true
				},
				bAddress:{
					required: true
				},
				cSide:{
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
	<form id="form2" action="modifyCompany2.php" method="post">
			<fieldset><legend>Modify Company</legend>
			<table border="0">
			<tr>
				<table id="table-3" >
					<tr>
					<td>
						<label for="name">Name*: </label>
						<input type="text" name="name" id="name" size="10" value="{$company['name']}" />
					</td>
					<td>
						<label for="form">Form*: </label>
                                                <input type="text" name="form" id="form" size="10" value="{$company['form']}" />
					</td>
					<td>
						<label for="EIN">E.I.N*:</label>
                                                <input type="text" name="EIN" id="EIN" size="10" value="{$company['ein']}" />
					</td>
					</tr>
				</table>
			</tr>
			<tr>
				<br>
				<table id="table-3">
					<tr>
					<td>
						<label for="name">Country*: </label>
                                                <input type="text" name="country" id="country" size="10" value="{$company['country']}" />
					</td>
					<td>
                                                <label for="form">State*: </label>
                                                <input type="text" name="state" id="state" size="10" value="{$company['state']}" />
					</td>
					<td>
						<label for="EIN">City*: </label>
                                                <input type="text" name="city" id="city" size="10" value="{$company['city']}" />
					</td>
					</tr>
				</table>
			</tr>
			<tr>
				<br>
				<table id="table-3">
					<tr>
					<td>
						<label for="name">Contact Email*: </label>
                                                <input type="text" name="email" id="email" size="10" value="{$company['email']}" />
					</td>
					<td>
						<label for="form">Business Address*: </label>
                                                <input type="text" name="bAddress" id="bAddress" size="10" value="{$company['business_address']}" />
					</td>
					<td>
						<label for="EIN">Mail Address: </label>
                                                <input type="text" name="mAddress" id="mAddress" size="10" value="{$company['mail_address']}" />
					</td>
					</tr>
				</table>
			</tr>
			<tr>
				<table id="table-3">
					<tr>
					<td>
						<label for="cSide">Company Side*: </label>
						<select name="cSide" style="width: 260px">
                                	                <option value=""></option>
                        	                        <option value="Supply Side" {if $company['side'] eq "Supply Side"}selected="selected"{/if}>Supply Side</option>
                	                                <option value="Demand Side" {if $company['side'] eq "Demand Side"}selected="selected"{/if}>Demand Side</option>
        	                                        <option value="Corp" {if $company['side'] eq "Corp"}selected="selected"{/if}>Corp</option>
	                                        </select>
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

