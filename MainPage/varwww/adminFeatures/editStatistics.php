<?php
require_once('../libs/Smarty.class.php');
$smarty = new Smarty();

$smarty->setTemplateDir('/var/www/html/templates/');
$smarty->setCompileDir('/var/www/html/templates_c/');
$smarty->setConfigDir('/var/www/html/configs/');
$smarty->setCacheDir('/var/www/html/cache/');
	
$smarty->display('editStatistics.tpl');

?>
