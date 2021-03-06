<?php
/*
 * Copyright 2007-2011 Charles du Jeu <contact (at) cdujeu.me>
 * This file is part of AjaXplorer.
 *
 * AjaXplorer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * AjaXplorer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with AjaXplorer.  If not, see <http://www.gnu.org/licenses/>.
 *
 * The latest code can be found at <http://www.ajaxplorer.info/>.
 *
 */
defined('AJXP_EXEC') or die( 'Access not allowed');
include_once(AJXP_INSTALL_PATH."/plugins/access.smb/smb.php");

/**
 * @package info.ajaxplorer.plugins
 * AJXP_Plugin to access a samba server
 */
class smbAccessDriver extends fsAccessDriver
{
	/**
	* @var Repository
	*/
	public $repository;
	public $driverConf;
	protected $wrapperClassName;
	protected $urlBase;
		
	function initRepository(){
		if(is_array($this->pluginConf)){
			$this->driverConf = $this->pluginConf;
		}else{
			$this->driverConf = array();
		}

		$create = $this->repository->getOption("CREATE");
		$recycle = $this->repository->getOption("RECYCLE_BIN");
		
		$wrapperData = $this->detectStreamWrapper(true);
		$this->wrapperClassName = $wrapperData["classname"];
		$this->urlBase = $wrapperData["protocol"]."://".$this->repository->getId();
		if(!is_dir($this->urlBase)){
			//throw new AJXP_Exception("Cannot find base path ($this->urlBase) for your repository! Please check the configuration!");
		}/*
		if($recycle != ""){
			if(!is_dir($this->urlBase."/".$recycle)){
				@mkdir($this->urlBase."/".$recycle);
				if(!is_dir($this->urlBase."/".$recycle)){
					throw new AJXP_Exception("Cannot create recycle bin folder. Please check repository configuration or that your folder is writeable!");
				}
			}
			RecycleBinManager::init($this->urlBase, "/".$recycle);
		}*/
	}
	
	/**
	 * Parse 
	 * @param DOMNode $contribNode
	 */
	protected function parseSpecificContributions(&$contribNode){
		parent::parseSpecificContributions($contribNode);
		if($contribNode->nodeName != "actions") return ;
		$this->disableArchiveBrowsingContributions($contribNode);
	}	
	
}	

?>