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
 * @class AJXP_Plugin
 * The basic concept of plugin. Only needs a manifest.xml file.
 */
class AJXP_Plugin implements Serializable{
	protected $baseDir;
	protected $id;
	protected $name;
	protected $type;
	/**
	 * XPath query
	 *
	 * @var DOMXPath
	 */
	protected $xPath;
	protected $manifestLoaded = false;
    protected $enabled;
	protected $actions;
	protected $registryContributions = array();
	protected $options; // can be passed at init time
	protected $pluginConf; // can be passed at load time
	protected $pluginConfDefinition;
	protected $dependencies;
	protected $mixins = array();
	public $loadingState = "";
	/**
	 * The manifest.xml loaded
	 *
	 * @var DOMDocument
	 */
	protected $manifestDoc;
	
	/**
	 * Internally store XML during serialization state.
	 *
	 * @var string
	 */
	private $manifestXML;
	
	private $serializableAttributes = array(
		"baseDir", 
		"id", 
		"name", 
		"type", 
		"manifestLoaded",
        "enabled",
		"actions", 
		"registryContributions", 
		"mixins",
		"options", "pluginConf", "pluginConfDefinition", "dependencies", "loadingState", "manifestXML");
	
	/**
	 * Construction method
	 *
	 * @param string $id
	 * @param string $baseDir
	 */	
	public function __construct($id, $baseDir){
		$this->baseDir = $baseDir;
		$this->id = $id;
		$split = explode(".", $id);
		$this->type = $split[0];
		$this->name = $split[1];
		$this->actions = array();
		$this->dependencies = array();
	}
	public function init($options){
		$this->options = $options;
		$this->loadRegistryContributions();
	}
	/**
	 * Perform initialization checks, and throw exception if problems found.
	 * @throws Exception
	 */
	public function performChecks(){
		
	}
    /**
     * @return bool
     */
    public function isEnabled(){
        if(isSet($this->enabled)) return $this->enabled;
        $this->enabled = true;
        if($this->manifestLoaded){
            $l = $this->xPath->query("@enabled", $this->manifestDoc->documentElement);
            if($l->length && $l->item(0)->nodeValue === "false"){
                $this->enabled = false;
            }
        }
        return $this->enabled;
    }

	protected function loadRegistryContributions(){		
		$regNodes = $this->xPath->query("registry_contributions/*");
		for($i=0;$i<$regNodes->length;$i++){
			$regNode = $regNodes->item($i);
			if($regNode->nodeType != XML_ELEMENT_NODE) continue;
			if($regNode->nodeName == "external_file"){
				$data = $this->nodeAttrToHash($regNode);
				$filename = $data["filename"] OR "";
				$include = $data["include"] OR "*";
				$exclude = $data["exclude"] OR "";			
				if(!is_file(AJXP_INSTALL_PATH."/".$filename)) continue;			
				if($include != "*") {
					$include = explode(",", $include);
				}else{
					$include = array("*");
				}
				if($exclude != "") {
					$exclude = explode(",", $exclude);			
				}else{
					$exclude = array();
				}
				$this->initXmlContributionFile($filename, $include, $exclude);
			}else{
				$this->registryContributions[]=$regNode;
				$this->parseSpecificContributions($regNode);
			}
		}
		// add manifest as a "plugins" (remove parsed contrib)
		$pluginContrib = new DOMDocument();
		$pluginContrib->loadXML("<plugins uuidAttr='name'></plugins>");
		$manifestNode = $pluginContrib->importNode($this->manifestDoc->documentElement, true);
		$pluginContrib->documentElement->appendChild($manifestNode);
		$xP=new DOMXPath($pluginContrib);
		$regNodeParent = $xP->query("registry_contributions", $manifestNode);
		if($regNodeParent->length){
			$manifestNode->removeChild($regNodeParent->item(0));
		}
		$this->registryContributions[]=$pluginContrib->documentElement;
		$this->parseSpecificContributions($pluginContrib->documentElement);
	}
	
	protected function initXmlContributionFile($xmlFile, $include=array("*"), $exclude=array()){
		$contribDoc = new DOMDocument();
		$contribDoc->load(AJXP_INSTALL_PATH."/".$xmlFile);
		if(!is_array($include) && !is_array($exclude)){
			$this->registryContributions[] = $contribDoc->documentElement;
			$this->parseSpecificContributions($contribDoc->documentElement);
			return;
		}
		$xPath = new DOMXPath($contribDoc);
		$excluded = array();
		foreach($exclude as $excludePath){
			$children = $xPath->query($excludePath);
			foreach($children as $child){
				$excluded[] = $child;
			}
		}
		$selected = array();
		foreach($include as $includePath){
			$incChildren = $xPath->query($includePath);
			if(!$incChildren->length) continue;
			$parentNode = $incChildren->item(0)->parentNode;
			if(!isSet($selected[$parentNode->nodeName])){
				$selected[$parentNode->nodeName]=array("parent"=>$parentNode, "nodes"=>array());
			}
			foreach($incChildren as $incChild){
				$foundEx = false;
				foreach($excluded as $exChild){
					if($this->nodesEqual($exChild, $incChild)) {
						$foundEx = true;break;
					}
				}
				if($foundEx) continue;
				$selected[$parentNode->nodeName]["nodes"][] = $incChild;
			}
			if(!count($selected[$parentNode->nodeName]["nodes"])){
				unset($selected[$parentNode->nodeName]);
			}
		}
		if(!count($selected)) return;
		foreach($selected as $parentNodeName => $data){
			$node = $data["parent"]->cloneNode(false);
			foreach($data["nodes"] as $childNode){
				$node->appendChild($childNode);
			}
			$this->registryContributions[] = $node;
			$this->parseSpecificContributions($node);			
		}		
	}
	protected function parseSpecificContributions(&$contribNode){
		//Append plugin id to callback tags
		$callbacks = $contribNode->getElementsByTagName("serverCallback");
		foreach($callbacks as $callback){
			$attr = $callback->ownerDocument->createAttribute("pluginId");
			$attr->value = $this->id;
			$callback->appendChild($attr);
		}
		if($contribNode->nodeName == "actions"){
			$actionXpath=new DOMXPath($contribNode->ownerDocument);
			foreach($contribNode->childNodes as $actionNode){
				if($actionNode->nodeType!=XML_ELEMENT_NODE) continue;
				$actionData=array();
				$actionData["XML"] = $contribNode->ownerDocument->saveXML($actionNode);			
				$names = $actionXpath->query("@name", $actionNode);
				$callbacks = $actionXpath->query("processing/serverCallback/@methodName", $actionNode);
				if($callbacks->length){
					$actionData["callback"] = $callbacks->item(0)->value;
				}
				$rightContextNodes = $actionXpath->query("rightsContext",$actionNode);
				if($rightContextNodes->length){
					$rightContext = $rightContextNodes->item(0);
					$actionData["rights"] = $this->nodeAttrToHash($rightContext);
				}
				$actionData["node"] = $actionNode;
				$names = $actionXpath->query("@name", $actionNode);
				$name = $names->item(0)->value;
				$this->actions[$name] = $actionData;
			}
		}
	}
	public function loadManifest(){
		$file = $this->baseDir."/manifest.xml";
		if(!is_file($file)) {
			return;
		}
		$this->manifestDoc = new DOMDocument();
		try{
			$this->manifestDoc->load($file);
		}catch (Exception $e){
			throw $e;
		}
		$this->xPath = new DOMXPath($this->manifestDoc);
		$this->loadMixins();
		$this->manifestLoaded = true;
		$this->loadDependencies();
	}
	
	public function getManifestLabel(){
		$l = $this->xPath->query("@label", $this->manifestDoc->documentElement);
		if($l->length) return $l->item(0)->nodeValue;
		else return $this->id;
	}
	
	public function getManifestDescription(){
		$l = $this->xPath->query("@description", $this->manifestDoc->documentElement);
		if($l->length) return $l->item(0)->nodeValue;
		else return "";
	}
	
	public function serialize(){
		if($this->manifestDoc != null){
			$this->manifestXML = base64_encode($this->manifestDoc->saveXML());
		}
		$serialArray = array();
		foreach ($this->serializableAttributes as $attr){
			$serialArray[$attr] = serialize($this->$attr);
		}
		return serialize($serialArray);
	}
	
	public function unserialize($string){
		$serialArray = unserialize($string);
		foreach ($serialArray as $key => $value){
			$this->$key = unserialize($value);
		}
		if($this->manifestXML != NULL){			
			$this->manifestDoc = DOMDocument::loadXML(base64_decode($this->manifestXML));
			$this->reloadXPath();			
			unset($this->manifestXML);
		}
		//var_dump($this);
	}
	
	public function getManifestRawContent($xmlNodeName = "", $format = "string"){
		if($xmlNodeName == ""){
			if($format == "string"){
				return $this->manifestDoc->saveXML($this->manifestDoc->documentElement);
			}else{
				return $this->manifestDoc->documentElement;
			}
		}else{
			$nodes = $this->xPath->query($xmlNodeName);
			if($format == "string"){
				$buffer = "";
				foreach ($nodes as $node){
					$buffer .= $this->manifestDoc->saveXML($node);
				}
				return $buffer;
			}else{
				return $nodes;
			}
		}
	}
	public function getRegistryContributions(){
		return $this->registryContributions;
	}
	protected function loadDependencies(){
		$depPaths = "dependencies/*/@pluginName";
		$nodes = $this->xPath->query($depPaths);
		foreach ($nodes as $attr){
			$value = $attr->value;
			$this->dependencies = array_merge($this->dependencies, explode("|", $value));
		}
	}
	public function updateDependencies($pluginService){
		$append = false;
		foreach ($this->dependencies as $index => $dependency){
			if($dependency == "access.AJXP_STREAM_PROVIDER"){
				unset($this->dependencies[$index]);
				$append = true;
			}
		}
		if($append){
			$this->dependencies = array_merge($this->dependencies, $pluginService->getStreamWrapperPlugins());
		}
	}
	
	public function dependsOn($pluginName){
		return in_array($pluginName, $this->dependencies);
	}
	/**
	 * Get dependencies
	 *
	 * @param AJXP_PluginsService $pluginService
	 * @return array
	 */
	public function getActiveDependencies($pluginService){
		if(!$this->manifestLoaded) return array();
		$deps = array();
		$nodes = $this->xPath->query("dependencies/activePlugin/@pluginName");
		foreach ($nodes as $attr) {
			$value = $attr->value;
			if($value == "access.AJXP_STREAM_PROVIDER"){
				$deps = array_merge($deps, $pluginService->getStreamWrapperPlugins());
			}else{
				$deps = array_merge($deps, explode("|", $value));
			}
		}
		return $deps;
	}
	
	protected function loadConfigsDefinitions(){
		$params = $this->xPath->query("//server_settings/global_param");
		$this->pluginConf = array();
		foreach ($params as $xmlNode){
			$paramNode = $this->nodeAttrToHash($xmlNode);
			$this->pluginConfDefinition[$paramNode["name"]] = $paramNode;
			if(isset($paramNode["default"])){
                if($paramNode["type"] == "boolean"){
                    $paramNode["default"] = ($paramNode["default"] === "true" ? true: false);
                }else if($paramNode["type"] == "integer"){
                    $paramNode["default"] = intval($paramNode["default"]);
                }
				$this->pluginConf[$paramNode["name"]] = $paramNode["default"];
			}
		}					
	}
	
	public function getConfigsDefinitions(){
		return $this->pluginConfDefinition;
	}
	
	public function loadConfigs($configData){
		// PARSE DEFINITIONS AND LOAD DEFAULT VALUES
		if(!isSet($this->pluginConf)) {
			$this->loadConfigsDefinitions();
		}
		// MERGE WITH PASSED CONFIGS
		$this->pluginConf = array_merge($this->pluginConf, $configData);
		
		// PUBLISH IF NECESSARY
		foreach ($this->pluginConf as $key => $value){
			if(isSet($this->pluginConfDefinition[$key]) && isSet($this->pluginConfDefinition[$key]["expose"]) && $this->pluginConfDefinition[$key]["expose"] == "true"){
				$this->exposeConfigInManifest($key, $value);
			}
		}

        // ASSIGN SPECIFIC OPTIONS TO PLUGIN KEY
        if(isSet($this->pluginConf["AJXP_PLUGIN_ENABLED"])){
            $this->enabled = $this->pluginConf["AJXP_PLUGIN_ENABLED"];
        }
	}
			
	public function getConfigs(){
		$core = AJXP_PluginsService::getInstance()->findPlugin("core", $this->type);
		if(!empty($core)){
			$coreConfs = $core->getConfigs();
			return array_merge($coreConfs, $this->pluginConf);
		}else{
			return $this->pluginConf;
		}
	}
	
	public function getClassFile(){
		$files = $this->xPath->query("class_definition");
		if(!$files->length) return false;
		return $this->nodeAttrToHash($files->item(0));
	}
	public function manifestLoaded(){
		return $this->manifestLoaded;
	}
	public function getId(){
		return $this->id;
	}
	public function getName(){
		return $this->name;
	}
	public function getType(){
		return $this->type;
	}
	public function getBaseDir(){
		return $this->baseDir;
	}
	public function getDependencies(){
		return $this->dependencies;
	}
	
	public function detectStreamWrapper($register = false){
		$files = $this->xPath->query("class_stream_wrapper");
		if(!$files->length) return false;
		$streamData = $this->nodeAttrToHash($files->item(0));
		if(!is_file(AJXP_INSTALL_PATH."/".$streamData["filename"])){
			return false;
		}
		include_once(AJXP_INSTALL_PATH."/".$streamData["filename"]);
		if(!class_exists($streamData["classname"])){
			return false;
		}
		if($register){
			$pServ = AJXP_PluginsService::getInstance();
			if(!in_array($streamData["protocol"], stream_get_wrappers())){
				stream_wrapper_register($streamData["protocol"], $streamData["classname"]);
				$pServ->registerWrapperClass($streamData["protocol"], $streamData["classname"]);
			}
		}
		return $streamData;
	}
	    
	protected function exposeConfigInManifest($configName, $configValue){
		$confBranch = $this->xPath->query("plugin_configs");		
		if(!$confBranch->length){			
			$configNode = $this->manifestDoc->importNode(new DOMElement("plugin_configs", ""));
			$this->manifestDoc->documentElement->appendChild($configNode);			
		}else{
			$configNode = $confBranch->item(0);
		}
		$prop = $this->manifestDoc->createElement("property");
		$propValue = $this->manifestDoc->createCDATASection(json_encode($configValue));
		$prop->appendChild($propValue);
		$attName = $this->manifestDoc->createAttribute("name");
		$attValue = $this->manifestDoc->createTextNode($configName);
		$attName->appendChild($attValue);
		$prop->appendChild($attName);
		$configNode->appendChild($prop);
		$this->reloadXPath();
	}

	public function reloadXPath(){
		// Relaunch xpath
		$this->xPath = new DOMXPath($this->manifestDoc);		
	}
	
	public function hasMixin($mixinName){
		return (in_array($mixinName, $this->mixins));
	}
	
	protected function loadMixins(){
		
		$attr = $this->manifestDoc->documentElement->getAttribute("mixins");
		if($attr != ""){
			$this->mixins = explode(",", $attr);
			foreach ($this->mixins as $mixin){
				AJXP_PluginsService::getInstance()->patchPluginWithMixin($this, $this->manifestDoc, $mixin);
			}
		}
	}
	
	/**
	 * Transform a simple node and its attributes to a hash
	 *
	 * @param DOMNode $node
	 */
	protected function nodeAttrToHash($node){
		$hash = array();
		$attributes  = $node->attributes;
		if($attributes!=null){
			foreach ($attributes as $domAttr){
				$hash[$domAttr->name] = $domAttr->value;
			}
		}
		return $hash;
	}
	/**
	 * Compare two nodes at first level (nodename and attributes)
	 *
	 * @param DOMNode $node
	 */
	protected function nodesEqual($node1, $node2){
		if($node1->nodeName != $node2->nodeName) return false;
		$hash1 = $this->nodeAttrToHash($node1);
		$hash2 = $this->nodeAttrToHash($node2);
		foreach($hash1 as $name=>$value){
			if(!isSet($hash2[$name]) || $hash2[$name] != $value) return false;
		}
		return true;
	}
}
?>