qx.Class.define("ls.common.RequestAdapter",
{
  type :  "static",
  
  statics: {
    // url to save the bids json:
    bidsJsonUrl : "/save",
    saveJson : function(obj, url) {
      var jsonUrl = url || this.bidsJsonUrl;
      var req = new qx.io.remote.Request(jsonUrl,"POST");
      req.setParameter("bids", qx.lang.Json.stringify(obj)); 
      req.send();
    }
  }
});