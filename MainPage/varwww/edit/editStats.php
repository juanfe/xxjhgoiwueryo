<?php

$loans = $_POST['loans'];
$loans7 = $_POST['loans7'];
$loans30 = $_POST['loans30'];
$PAmount = $_POST['PAmount'];
$PAmount7 = $_POST['PAmount7'];
$PAmount30 = $_POST['PAmount30'];
$WAdemand = $_POST['WAdemand'];
$WAdemand7 = $_POST['WAdemand7'];
$WAdemand30 = $_POST['WAdemand30'];
$WAsupply = $_POST['WAsupply'];
$WAsupply7 = $_POST['WAsupply7'];
$WAsupply30 = $_POST['WAsupply30'];
$WAduration = $_POST['WAduration'];
$WAduration7 = $_POST['WAduration7'];
$WAduration30 = $_POST['WAduration30'];

$fname = "../configs/statistics.conf";
$fh = fopen($fname,'w');

fwrite($fh,"numLoansToday = $loans\n");
fwrite($fh,"numLoans7 = $loans7\n");
fwrite($fh,"numLoans30 = $loans30\n");

fwrite($fh,"pAmountToday = $PAmount\n");
fwrite($fh,"pAmount7 = $PAmount7\n");
fwrite($fh,"pAmount30 = $PAmount30\n");

fwrite($fh,"WAdemandSideRateToday = $WAdemand\n");
fwrite($fh,"WAdemandSideRate7 = $WAdemand7\n");
fwrite($fh,"WAdemandSideRate30 = $WAdemand30\n");

fwrite($fh,"WAsupplySideYieldToday = $WAsupply\n");
fwrite($fh,"WAsupplySideYield7 = $WAsupply7\n");
fwrite($fh,"WAsupplySideYield30 = $WAsupply30\n");

fwrite($fh,"WAdurationToday = $WAduration\n");
fwrite($fh,"WAduration7 = $WAduration7\n");
fwrite($fh,"WAduration30 = $WAduration30\n");

fclose($fh);
?>
<html>

<body>
Configuration file saved.<br>Reload Page to see the changes.
</body>

</html>
