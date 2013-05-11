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
			eName: {
				required: true
			},
			EIN: {
				required: true
			},
			eForm: {
				required: true
			},
			country: {
				required: true
			},
			side: {
				required: true
			},
			state: {
				required: true
			},
			city: {
				required: true
			},
			bAdd: {
				required: true
			},
			mAdd: {
				required: true
			},	
			eemail: {
				required: true,
				email: true	
			},
			compPhone: {
				required: false
			},
			compAdminUser: {
				required: true,
				minlength: 5,
				maxlength: 15,
				noSpace: true
			},
			compAdminPass: {
				required: true,
				minlength: 5,
				maxlength: 15
			}
		}	
	});
});

jQuery.validator.addMethod(
	"noSpace",
	function(value, element){
		return $("#compAdminUser").val().indexOf(" ") < 0;
	},
	"Username should not have any space"
);

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
				<h2>Add a Company to Our List</h2>
			</div>
		</div>
	</div>
	
	{if $admin eq 1}
	<div id="container">
	<form id="form3" action="addCompany2.php" method="post">
			<fieldset><legend>Add Company</legend>
				<p class="first">
					<label for"eName">Name of entity *</label>
					<input type="text" name="eName" id="eName" size="25" />
				</p>
				<p>
					<label for="EIN">E.I.N. # *</label>
					<input type="text" name="EIN" id="EIN" size="25" />
				</p>
				<p>
					<label for="eForm">Form of Entity (c corp, LLC, etc) *</label>
					<input type="text" name="eForm" id="eForm" size="25" />
				</p>
				<p>
					<label for="side">Select the company side *</label>
					<select name="side" style="width: 260px">
						<option value=""></option>
						<option value="Supply Side">Supply Side</option>
						<option value="Demand Side">Demand Side</option>
						<option value="Corp">Corp</option>
					</select>
				</p>
				<p>
					<label for="country">Country *</label>
					<select name="country" style="width: 260px">
						<option value=""></option>
						<option value="Afganistan">Afghanistan</option>
						<option value="Albania">Albania</option>
						<option value="Algeria">Algeria</option>
						<option value="American Samoa">American Samoa</option>
						<option value="Andorra">Andorra</option>
						<option value="Angola">Angola</option>
						<option value="Anguilla">Anguilla</option>
						<option value="Antigua &amp; Barbuda">Antigua &amp; Barbuda</option>
						<option value="Argentina">Argentina</option>
						<option value="Armenia">Armenia</option>
						<option value="Aruba">Aruba</option>
						<option value="Australia">Australia</option>
						<option value="Austria">Austria</option>
						<option value="Azerbaijan">Azerbaijan</option>
						<option value="Bahamas">Bahamas</option>
						<option value="Bahrain">Bahrain</option>
						<option value="Bangladesh">Bangladesh</option>
						<option value="Barbados">Barbados</option>
						<option value="Belarus">Belarus</option>
						<option value="Belgium">Belgium</option>
						<option value="Belize">Belize</option>
						<option value="Benin">Benin</option>
						<option value="Bermuda">Bermuda</option>
						<option value="Bhutan">Bhutan</option>
						<option value="Bolivia">Bolivia</option>
						<option value="Bonaire">Bonaire</option>
						<option value="Bosnia &amp; Herzegovina">Bosnia &amp; Herzegovina</option>
						<option value="Botswana">Botswana</option>
						<option value="Brazil">Brazil</option>
						<option value="British Indian Ocean Ter">British Indian Ocean Ter</option>
						<option value="Brunei">Brunei</option>
						<option value="Bulgaria">Bulgaria</option>
						<option value="Burkina Faso">Burkina Faso</option>
						<option value="Burundi">Burundi</option>
						<option value="Cambodia">Cambodia</option>
						<option value="Cameroon">Cameroon</option>
						<option value="Canada">Canada</option>
						<option value="Canary Islands">Canary Islands</option>
						<option value="Cape Verde">Cape Verde</option>
						<option value="Cayman Islands">Cayman Islands</option>
						<option value="Central African Republic">Central African Republic</option>
						<option value="Chad">Chad</option>
						<option value="Channel Islands">Channel Islands</option>
						<option value="Chile">Chile</option>
						<option value="China">China</option>
						<option value="Christmas Island">Christmas Island</option>
						<option value="Cocos Island">Cocos Island</option>
						<option value="Colombia">Colombia</option>
						<option value="Comoros">Comoros</option>
						<option value="Congo">Congo</option>
						<option value="Cook Islands">Cook Islands</option>
						<option value="Costa Rica">Costa Rica</option>
						<option value="Cote DIvoire">Cote D'Ivoire</option>
						<option value="Croatia">Croatia</option>
						<option value="Cuba">Cuba</option>
						<option value="Curaco">Curacao</option>
						<option value="Cyprus">Cyprus</option>
						<option value="Czech Republic">Czech Republic</option>
						<option value="Denmark">Denmark</option>
						<option value="Djibouti">Djibouti</option>
						<option value="Dominica">Dominica</option>
						<option value="Dominican Republic">Dominican Republic</option>
						<option value="East Timor">East Timor</option>
						<option value="Ecuador">Ecuador</option>
						<option value="Egypt">Egypt</option>
						<option value="El Salvador">El Salvador</option>
						<option value="Equatorial Guinea">Equatorial Guinea</option>
						<option value="Eritrea">Eritrea</option>
						<option value="Estonia">Estonia</option>
						<option value="Ethiopia">Ethiopia</option>
						<option value="Falkland Islands">Falkland Islands</option>
						<option value="Faroe Islands">Faroe Islands</option>
						<option value="Fiji">Fiji</option>
						<option value="Finland">Finland</option>
						<option value="France">France</option>
						<option value="French Guiana">French Guiana</option>
						<option value="French Polynesia">French Polynesia</option>
						<option value="French Southern Ter">French Southern Ter</option>
						<option value="Gabon">Gabon</option>
						<option value="Gambia">Gambia</option>
						<option value="Georgia">Georgia</option>
						<option value="Germany">Germany</option>
						<option value="Ghana">Ghana</option>
						<option value="Gibraltar">Gibraltar</option>
						<option value="Great Britain">Great Britain</option>
						<option value="Greece">Greece</option>
						<option value="Greenland">Greenland</option>
						<option value="Grenada">Grenada</option>
						<option value="Guadeloupe">Guadeloupe</option>
						<option value="Guam">Guam</option>
						<option value="Guatemala">Guatemala</option>
						<option value="Guinea">Guinea</option>
						<option value="Guyana">Guyana</option>
						<option value="Haiti">Haiti</option>
						<option value="Hawaii">Hawaii</option>
						<option value="Honduras">Honduras</option>
						<option value="Hong Kong">Hong Kong</option>
						<option value="Hungary">Hungary</option>
						<option value="Iceland">Iceland</option>
						<option value="India">India</option>
						<option value="Indonesia">Indonesia</option>
						<option value="Iran">Iran</option>
						<option value="Iraq">Iraq</option>
						<option value="Ireland">Ireland</option>
						<option value="Isle of Man">Isle of Man</option>
						<option value="Israel">Israel</option>
						<option value="Italy">Italy</option>
						<option value="Jamaica">Jamaica</option>
						<option value="Japan">Japan</option>
						<option value="Jordan">Jordan</option>
						<option value="Kazakhstan">Kazakhstan</option>
						<option value="Kenya">Kenya</option>
						<option value="Kiribati">Kiribati</option>
						<option value="Korea North">Korea North</option>
						<option value="Korea Sout">Korea South</option>
						<option value="Kuwait">Kuwait</option>
						<option value="Kyrgyzstan">Kyrgyzstan</option>
						<option value="Laos">Laos</option>
						<option value="Latvia">Latvia</option>
						<option value="Lebanon">Lebanon</option>
						<option value="Lesotho">Lesotho</option>
						<option value="Liberia">Liberia</option>
						<option value="Libya">Libya</option>
						<option value="Liechtenstein">Liechtenstein</option>
						<option value="Lithuania">Lithuania</option>
						<option value="Luxembourg">Luxembourg</option>
						<option value="Macau">Macau</option>
						<option value="Macedonia">Macedonia</option>
						<option value="Madagascar">Madagascar</option>
						<option value="Malaysia">Malaysia</option>
						<option value="Malawi">Malawi</option>
						<option value="Maldives">Maldives</option>
						<option value="Mali">Mali</option>
						<option value="Malta">Malta</option>
						<option value="Marshall Islands">Marshall Islands</option>
						<option value="Martinique">Martinique</option>
						<option value="Mauritania">Mauritania</option>
						<option value="Mauritius">Mauritius</option>
						<option value="Mayotte">Mayotte</option>
						<option value="Mexico">Mexico</option>
						<option value="Midway Islands">Midway Islands</option>
						<option value="Moldova">Moldova</option>
						<option value="Monaco">Monaco</option>
						<option value="Mongolia">Mongolia</option>
						<option value="Montserrat">Montserrat</option>
						<option value="Morocco">Morocco</option>
						<option value="Mozambique">Mozambique</option>
						<option value="Myanmar">Myanmar</option>
						<option value="Nambia">Nambia</option>
						<option value="Nauru">Nauru</option>
						<option value="Nepal">Nepal</option>
						<option value="Netherland Antilles">Netherland Antilles</option>
						<option value="Netherlands">Netherlands (Holland, Europe)</option>
						<option value="Nevis">Nevis</option>
						<option value="New Caledonia">New Caledonia</option>
						<option value="New Zealand">New Zealand</option>
						<option value="Nicaragua">Nicaragua</option>
						<option value="Niger">Niger</option>
						<option value="Nigeria">Nigeria</option>
						<option value="Niue">Niue</option>
						<option value="Norfolk Island">Norfolk Island</option>
						<option value="Norway">Norway</option>
						<option value="Oman">Oman</option>
						<option value="Pakistan">Pakistan</option>
						<option value="Palau Island">Palau Island</option>
						<option value="Palestine">Palestine</option>
						<option value="Panama">Panama</option>
						<option value="Papua New Guinea">Papua New Guinea</option>
						<option value="Paraguay">Paraguay</option>
						<option value="Peru">Peru</option>
						<option value="Phillipines">Philippines</option>
						<option value="Pitcairn Island">Pitcairn Island</option>
						<option value="Poland">Poland</option>
						<option value="Portugal">Portugal</option>
						<option value="Puerto Rico">Puerto Rico</option>
						<option value="Qatar">Qatar</option>
						<option value="Republic of Montenegro">Republic of Montenegro</option>
						<option value="Republic of Serbia">Republic of Serbia</option>
						<option value="Reunion">Reunion</option>
						<option value="Romania">Romania</option>
						<option value="Russia">Russia</option>
						<option value="Rwanda">Rwanda</option>
						<option value="St Barthelemy">St Barthelemy</option>
						<option value="St Eustatius">St Eustatius</option>
						<option value="St Helena">St Helena</option>
						<option value="St Kitts-Nevis">St Kitts-Nevis</option>
						<option value="St Lucia">St Lucia</option>
						<option value="St Maarten">St Maarten</option>
						<option value="St Pierre &amp; Miquelon">St Pierre &amp; Miquelon</option>
						<option value="St Vincent &amp; Grenadines">St Vincent &amp; Grenadines</option>
						<option value="Saipan">Saipan</option>
						<option value="Samoa">Samoa</option>
						<option value="Samoa American">Samoa American</option>
						<option value="San Marino">San Marino</option>
						<option value="Sao Tome & Principe">Sao Tome &amp; Principe</option>
						<option value="Saudi Arabia">Saudi Arabia</option>
						<option value="Senegal">Senegal</option>
						<option value="Seychelles">Seychelles</option>
						<option value="Sierra Leone">Sierra Leone</option>
						<option value="Singapore">Singapore</option>
						<option value="Slovakia">Slovakia</option>
						<option value="Slovenia">Slovenia</option>
						<option value="Solomon Islands">Solomon Islands</option>
						<option value="Somalia">Somalia</option>
						<option value="South Africa">South Africa</option>
						<option value="Spain">Spain</option>
						<option value="Sri Lanka">Sri Lanka</option>
						<option value="Sudan">Sudan</option>
						<option value="Suriname">Suriname</option>
						<option value="Swaziland">Swaziland</option>
						<option value="Sweden">Sweden</option>
						<option value="Switzerland">Switzerland</option>
						<option value="Syria">Syria</option>
						<option value="Tahiti">Tahiti</option>
						<option value="Taiwan">Taiwan</option>
						<option value="Tajikistan">Tajikistan</option>
						<option value="Tanzania">Tanzania</option>
						<option value="Thailand">Thailand</option>
						<option value="Togo">Togo</option>
						<option value="Tokelau">Tokelau</option>
						<option value="Tonga">Tonga</option>
						<option value="Trinidad &amp; Tobago">Trinidad &amp; Tobago</option>
						<option value="Tunisia">Tunisia</option>
						<option value="Turkey">Turkey</option>
						<option value="Turkmenistan">Turkmenistan</option>
						<option value="Turks &amp; Caicos Is">Turks &amp; Caicos Is</option>
						<option value="Tuvalu">Tuvalu</option>
						<option value="Uganda">Uganda</option>
						<option value="Ukraine">Ukraine</option>
						<option value="United Arab Erimates">United Arab Emirates</option>
						<option value="United Kingdom">United Kingdom</option>
						<option value="United States of America">United States of America</option>
						<option value="Uraguay">Uruguay</option>
						<option value="Uzbekistan">Uzbekistan</option>
						<option value="Vanuatu">Vanuatu</option>
						<option value="Vatican City State">Vatican City State</option>
						<option value="Venezuela">Venezuela</option>
						<option value="Vietnam">Vietnam</option>
						<option value="Virgin Islands (Brit)">Virgin Islands (Brit)</option>
						<option value="Virgin Islands (USA)">Virgin Islands (USA)</option>
						<option value="Wake Island">Wake Island</option>
						<option value="Wallis &amp; Futana Is">Wallis &amp; Futana Is</option>
						<option value="Yemen">Yemen</option>
						<option value="Zaire">Zaire</option>
						<option value="Zambia">Zambia</option>
						<option value="Zimbabwe">Zimbabwe</option>
					</select>
				</p>
				<p>
					<label for="state">State *</label>
					<input type="text" name="state" id="state" size="25" />
				</p>
				<p>
					<label for="city">City *</label>
					<input type="text" name="city" id="city" size="25" />
				</p>
				<p>
					<label for="bAdd">Business Address *</label>
					<input type="text" name="bAdd" id="bAdd" size="25" />
				</p>
				<p>
					<label for="mAdd">Mailing Address *</label>
					<input type="text" name="mAdd" id="mAdd" size="25" />
				</p>
				<p>
					<label for="eemail">Contact Email *</label>
					<input type="text" name="eemail" id="eemail" size="25" />
				</p>
				<p>
					<label for="compPhone">Phone Number</label>
					<input type="text" name="compPhone" id="compPhone" size="25" />
				</p>
				<p>
					<label for="compAdminUser">Company Admin Username *</label>
					<input type="text" name="compAdminUser" id="compAdminUser" size="25" />
				</p>
				<p>
					<label for="compAdminPass">Company Admin Password *</label>
					<input type="text" name="compAdminPass" id="compAdminPass" size="25" />
				</p>
			</fieldset>
			<p class="submit"><button type="submit">Add Company</button></p>
		</form>
	</div>
	{else}
		<div id="container">
			<h1> You are not authorized to see this page.</h1>
		</div>
	{/if}	
	<div id="footer">
		<p class="right">Design: Vichara Technologies, <a title="Vichara Technologies" href="http://www.vichara.com/">Vichara Technologies</a></p>
		<p>&copy; Copyright 2011 <a href="../index.html">Liquidity Spot</a> &middot; All Rights Reserved</p>
	</div>
</body>
</html>
