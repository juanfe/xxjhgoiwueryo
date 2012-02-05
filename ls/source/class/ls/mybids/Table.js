qx.Class.define("ls.mybids.Table",
{
  extend : ls.mybids.BaseTable,
  
  construct : function(user)
  {
    var columnInfoDict = new ls.mybids.common.ColumnInfoDictionary(this.self(arguments).columnsInfo);
    this.base(arguments, columnInfoDict.getNames());
    this.user = user;
    this.self(arguments).loadJson(this.self(arguments).getJsonUrl(), this.self(arguments).extractDataTo, this);
    var homeButton = new qx.ui.toolbar.Button("Home");
    homeButton.addListener("execute", this.close, this);
    this.addButton(homeButton);
  },
  
  members : {
    sourceData : null,
    user : "",
    button : null
  },
  
  statics : {
    // Configuration related variables
    // json source file relative to <applicationName>/source/resource folder
    jsonFilepath :  "ls/mybids/bids.json",
    getJsonUrl : function() {
      return this.constructor.toResourceUrl(this.constructor.jsonFilepath);
    },
    // Column name and type of each column of the table
    columnsInfo : [
      new ls.mybids.common.ColumnInfo("Collateral","int"),
      new ls.mybids.common.ColumnInfo("Percentage owned (%)","float"),
      new ls.mybids.common.ColumnInfo("Bid rate (%)","float"),
      new ls.mybids.common.ColumnInfo("Status","string")
    ],
    // wrapper for the resource manager
    toResourceUrl : function(filepath) {
      return qx.util.ResourceManager.getInstance().toUri(filepath);
    },
    // the complete handler must acept an object as parameter 
    loadJson : function(url, completeHandler, instance) {
      var req = new qx.io.remote.Request(url, "GET", "text/plain");
      req.addListener("completed", function(response) {
        var responseContent = response.getContent();
        var jsObj = qx.lang.Json.parse(responseContent);
        completeHandler(jsObj, instance);
      });
      req.send();
    },
    extractDataTo : function(data, instance) {
      var sourceData = instance.sourceData = data[instance.user] || [];
      //sourceData.push(userData);
      instance.setData(sourceData);
    }
  }
});
