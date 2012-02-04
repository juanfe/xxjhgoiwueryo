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
      
      // Configuration related variables
      // json source file relative to <applicationName>/source/resource folder
      var loansJson = "mybids/FundingData.json";
      
      var root = this.getRoot();

      //var windowManager = new qx.ui.window.Manager();
      //var desktop = new qx.ui.window.Desktop(windowManager);

      //root.add(desktop);

      var WinTbl = new mybids.Table(loansJson);
      root.add(WinTbl);
	  
      WinTbl.open();
      WinTbl.moveTo(10, 10);
    }
  }
});
