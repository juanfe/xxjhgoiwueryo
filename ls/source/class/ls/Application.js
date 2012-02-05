/* ************************************************************************

   Copyright: Copyright (C) 2012 Vichara Technologies Inc.

   License: All rights reserved.
            Permission to use, copy, modify, distribute, and sell the source code for any purpose is not permitted 
            without a written authorization from  Vichara Technologies Inc.

   Authors: Eduardo Zea,
            Juan Jaramillo,
            Leonardo Zuniga,
            Camilo Martínez

************************************************************************ */

/* ************************************************************************

#asset(ls/*)

************************************************************************ */

/**
 * This is the main application class of your custom application "ls"
 */
qx.Class.define("ls.Application",
{
  extend : qx.application.Standalone,
   
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
      // Creating the mybids window
      var WinTbl = new ls.mybids.Table(user);
      root.add(WinTbl);
      // Creating the search window
      var searchScreen = new ls.web.SearchScreen(root);
      var WinHome = new ls.mybids.Home();
      WinHome.mybidsButton.addListener("execute", WinTbl.open, WinTbl);
      WinHome.searchButton.addListener("execute", searchScreen.open, searchScreen);
      WinHome.open();
    }
  },
  
  // Configuration related variables
  statics : 
  {
    // cookie key for the user:
    userCookie : "com.liquidityspot.user"
  }
});