/* ************************************************************************

   Copyright: 2012, Vichara Right Reserved

   License: Under Vichara License

   Authors: Juan Fernando Jaramillo Botero

************************************************************************ */

/* ************************************************************************

#asset(web/*)

************************************************************************ */

/**
 * This is the main application class of your custom application "web"
 */
qx.Class.define("web.Application",
{
  extend : qx.application.Standalone,



  /*
  *****************************************************************************
     MEMBERS
  *****************************************************************************
  */

  members :
  {
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

      var root = this.getRoot();

      var windowManager = new qx.ui.window.Manager();
      var desktop = new qx.ui.window.Desktop(windowManager);

      root.add(desktop);

	  var WinTbl = new web.Table();
	  desktop.add(WinTbl);

	  var WinCtl = new web.Control(/*WinTbl.__tableModel, WinTbl.__tbl*/);
          WinCtl.__BtnCancel.addListener("execute", WinCtl.close, WinCtl);
          WinCtl.__BtnOk.addListener("execute",function(e)
          {
              WinTbl.__tableModel.addNumericFilter("!=", 3, "Occupancy Code");
              WinTbl.__tableModel.applyFilters();
              WinTbl.__tbl.setAdditionalStatusBarText(", Filteres by State.");
              WinCtl.close();
          }); 
          WinCtl.setModal(true);
	  desktop.add(WinCtl);

	  WinTbl.open();
	  WinTbl.moveTo(10, 10);

          WinTbl.__BtnFilter.addListener("execute", WinCtl.open, WinCtl);
          WinTbl.__BtnFilter.addListener("execute", WinCtl.open, WinCtl);
          WinTbl.__BtnFilter.addListener("execute", WinCtl.open, WinCtl);
    }
  }
});
