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
 */
defined('AJXP_EXEC') or die( 'Access not allowed');
/**
 * @package info.ajaxplorer.core
 * @class Repository
 * The basic abstraction of a data server
 */
class Repository {

	var $uuid;
	var $id;
	var $path;
	var $display;
	var $displayStringId;
	var $accessType = "fs";
	var $recycle = "";
	var $create = true;
	var $writeable = false;
	var $enabled = true;
	var $options = array();
	var $slug;
    public $isTemplate = false;
	
	private $owner;
	private $parentId;
	private $uniqueUser;
	private $inferOptionsFromParent = false;
	/**
	 * @var Repository
	 */
	private $parentTemplateObject;
	
	public $streamData;
	
	function Repository($id, $display, $driver){
		$this->setAccessType($driver);
		$this->setDisplay($display);
		$this->setId($id);
		$this->uuid = md5(time());
		$this->slug = AJXP_Utils::slugify($display);
	}
	
	function createSharedChild($newLabel, $newOptions, $parentId = null, $owner = null, $uniqueUser = null){
		$repo = new Repository(0, $newLabel, $this->accessType);
		$newOptions = array_merge($this->options, $newOptions);
		$repo->options = $newOptions;
		if($parentId == null){
			$parentId = $this->id;
		}
		$repo->setOwnerData($parentId, $owner, $uniqueUser);
		return $repo;
	}
	
	function createTemplateChild($newLabel, $newOptions, $owner = null, $uniqueUser = null){
		$repo = new Repository(0, $newLabel, $this->accessType);
		$repo->options = $newOptions;
		$repo->setOwnerData($this->id, $owner, $uniqueUser);
		$repo->inferOptionsFromParent = true;
		return $repo;
	}
	
	function upgradeId(){
		if(!isSet($this->uuid)) {
			$this->uuid = md5(serialize($this));
			//$this->uuid = md5(time());
			return true;
		}
		return false;
	}
	
	function getUniqueId($serial=false){
		if($serial){
			return md5(serialize($this));
		}
		return $this->uuid;
	}
	
	function getSlug(){
		return $this->slug;
	}
	
	function setSlug($slug = null){
		if($slug == null){
			$this->slug = AJXP_Utils::slugify($this->display);
		}else{
			$this->slug = $slug;
		}
	}
	
	function getClientSettings(){
		$fileName = AJXP_INSTALL_PATH."/plugins/access.".$this->accessType."/manifest.xml";
		$settingLine = "";
		if(is_readable($fileName)){
			$lines = file($fileName);	
			$inside = false;		
			foreach ($lines as $line){
				$compareLine = strtolower($line);				
				if(preg_match('/\<client_settings/', trim($compareLine)) > 0){
					$settingLine = trim($line);
					if(preg_match("/\/\>/", trim($compareLine))>0 || preg_match("/\<\/client_settings\>/", trim($compareLine)>0)){
						return $settingLine;
					}
					$inside = true;					
				}else{
					if($inside) $settingLine.=trim($line);
					if(preg_match("/\<\/client_settings\>/", trim(strtolower($line)))>0) return $settingLine;
				}
			}
		}
		return $settingLine;
	}
	
	function detectStreamWrapper($register = false, &$streams=null){
		$plugin = AJXP_PluginsService::findPlugin("access", $this->accessType);
		if(!$plugin) return(false);
		$streamData = $plugin->detectStreamWrapper($register);
		if(!$register && $streamData !== false && is_array($streams)){
			$streams[$this->accessType] = $this->accessType;
		}
		if($streamData !== false) $this->streamData = $streamData;
		return ($streamData !== false);
	}
	

	function addOption($oName, $oValue){
		if(strpos($oName, "PATH") !== false){
			$oValue = str_replace("\\", "/", $oValue);
		}
		$this->options[$oName] = $oValue;
	}
	
	function getOption($oName, $safe=false){
		if(isSet($this->options[$oName])){
			$value = $this->options[$oName];			
			if(!$safe) $value = AJXP_VarsFilter::filter($value);
			return $value;
		}
		if($this->inferOptionsFromParent){
			if(!isset($this->parentTemplateObject)){
				$this->parentTemplateObject = ConfService::getRepositoryById($this->parentId);
			}
			if(isSet($this->parentTemplateObject)){
				return $this->parentTemplateObject->getOption($oName, $safe);
			}
		}
		return "";
	}
	
	function getOptionsDefined(){
		$keys = array();
		foreach($this->options as $key => $value){
			if(!empty($value)) $keys[] = $key;
		}
		return $keys;
	}
	
	function getDefaultRight(){
		$opt = $this->getOption("DEFAULT_RIGHTS");
		return (isSet($opt)?$opt:"");
	}
	
	
	/**
	 * @return String
	 */
	function getAccessType() {
		return $this->accessType;
	}
	
	/**
	 * @return String
	 */
	function getDisplay() {
		if(isSet($this->displayStringId)){
			$mess = ConfService::getMessages();
			if(isSet($mess[$this->displayStringId])){
				return SystemTextEncoding::fromUTF8($mess[$this->displayStringId]);
			}
		}
		return $this->display;
	}
	
	/**
	 * @return int
	 */
	function getId() {
		return $this->id;
	}
	
	/**
	 * @return boolean
	 */
	function getCreate() {
		return $this->getOption("CREATE");
	}
	
	/**
	 * @param boolean $create
	 */
	function setCreate($create) {
		$this->options["CREATE"] = $create;
	}

	
	/**
	 * @param String $accessType
	 */
	function setAccessType($accessType) {
		$this->accessType = $accessType;
	}
	
	/**
	 * @param String $display
	 */
	function setDisplay($display) {
		$this->display = $display;
	}
	
	/**
	 * @param int $id
	 */
	function setId($id) {
		$this->id = $id;
	}
	
	function isWriteable(){
		return $this->writeable;
	}
	
	function setWriteable($w){
		$this->writeable = $w;
	}
	
	function isEnabled(){
		return $this->enabled;
	}
	
	function setEnabled($e){
		$this->enabled = $e;
	}
	
	function setDisplayStringId($id){
		$this->displayStringId = $id;
	}
	
	function setOwnerData($repoParentId, $ownerUserId = null, $childUserId = null){
		$this->owner = $ownerUserId;
		$this->uniqueUser = $childUserId;
		$this->parentId = $repoParentId;
	}
	
	function getOwner(){
		return $this->owner;
	}
	
	function getParentId(){
		return $this->parentId;
	}
	
	function getUniqueUser(){
		return $this->uniqueUser;
	}
	
	function hasOwner(){
		return isSet($this->owner);
	}
		
	function hasParent(){
		return isSet($this->parentId);
	}
		
}

?>