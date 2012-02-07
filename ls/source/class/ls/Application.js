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
      
      // For debugging it is not using app engine
      if (qx.core.Environment.get("qx.debug")) {
        ls.common.Cookie.setUser("cmartinez");
      } else {
        // Add any app engine required code
      }
      
      //var user = qx.bom.Cookie.get(this.self(arguments).userCookie);
      // Creating the search window
      var mybidsScreen = new ls.mybids.MybidsScreen(root);
      var searchScreen = new ls.web.SearchScreen(root);
      var WinHome = new ls.mybids.Home();
      WinHome.mybidsButton.addListener("execute", mybidsScreen.open, mybidsScreen);
      WinHome.searchButton.addListener("execute", searchScreen.open, searchScreen);
      searchScreen.setSubmitHandler(function() {
        searchScreen.close();
        mybidsScreen.open();
      });
      searchScreen.setHomeHandler(function() {
        searchScreen.close();
        WinHome.open();
      });
      WinHome.open();
    }
  }
});