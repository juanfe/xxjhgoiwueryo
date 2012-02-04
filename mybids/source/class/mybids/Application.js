/* ************************************************************************

   Copyright:

   License:

   Authors:

************************************************************************ */

/* ************************************************************************

#asset(mybids/*)

************************************************************************ */

/**
 * This is the main application class of your custom application "mybids"
 */
qx.Class.define("mybids.Application",
{
  extend : qx.application.Standalone,

  /*
  *****************************************************************************
     MEMBERS
  *****************************************************************************
  */

  members :
  {
    /**
     * This method contains the initial application code and gets called 
     * during startup of the application
     * 
     * @lint ignoreDeprecated(alert)
     */
    main : function()
    {
      // Call super class
      this.base(arguments);

      // Enable logging in debug variant
      if (qx.core.Environment.get("qx.debug"))
      {
        // support native logging capabilities, e.g. Firebug for Firefox
        qx.log.appender.Native;
        // support additional cross-browser console. Press F7 to toggle visibility
        qx.log.appender.Console;
      }

      /*
      -------------------------------------------------------------------------
        Below is your actual application code...
      -------------------------------------------------------------------------
      */
      
      var root = this.getRoot();

      //var windowManager = new qx.ui.window.Manager();
      //var desktop = new qx.ui.window.Desktop(windowManager);

      //root.add(desktop);
      
      qx.bom.Cookie.set(this.self(arguments).userCookie, "cmartinez");
      var user = qx.bom.Cookie.get(this.self(arguments).userCookie);
      // Getting the bids to filter by
      var bidsJsonFile = this.self(arguments).bidsJson,
          bidsJsonUrl = qx.util.ResourceManager.getInstance().toUri(bidsJsonFile),
          req = new qx.io.request.Xhr(bidsJsonUrl);
      req.addListener("success", function(e) {
        var req = e.getTarget(),
            bidsObject = qx.lang.Json.parse(req.getResponse()),
            bids = bidsObject[user];
        var WinTbl = new mybids.Table(bids);
        root.add(WinTbl);
    
        WinTbl.open();
        WinTbl.moveTo(10, 10);
      }, this);

      // Send request
      req.send(); 
    }
  },
  
  // Configuration related variables
  statics : 
  {
    // bids source file relative to <applicationName>/source/resource folder
    bidsJson : "mybids/bids.json",
    // cookie key for the user:
    userCookie : "com.liquidityspot.user"
  }
});
