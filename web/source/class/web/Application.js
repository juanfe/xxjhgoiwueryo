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

  construct : function()
  {
	  this.Filter = {};
  },

  /*
  *****************************************************************************
     MEMBERS
  *****************************************************************************
  */

  members :
  {

	Filter : null, 

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

      //var windowManager = new qx.ui.window.Manager();
      //var desktop = new qx.ui.window.Desktop(windowManager);

      //root.add(desktop);

	  var WinTbl = new web.Table();
	  root.add(WinTbl);

	  var WinCtl = new web.Control();
      //WinCtl.BtnCancel.addListener("execute", WinCtl.close, WinCtl);
      WinCtl.BtnCancel.addListener("execute", function(e){
		WinCtl.close();
	});
      WinCtl.addListener("changeData",function(e)
      {
		  WinTbl.TableModel.resetHiddenRows();
		  WinTbl.TableModel.hideRows(0,1);        
		  var data = e.getData();
          WinTbl.TableModel.addNumericFilter(">", data.SLCorLogFraudRiskScore, "CoreLogic Fraud Risk Score");
          WinTbl.TableModel.addNumericFilter(">", data.SLCorLogCollRiskScore, "CoreLogic Collateral Risk Score");
          WinTbl.TableModel.addNumericFilter(">", data.SLAcceptableFICO + 300, "FICO Score");

          WinTbl.TableModel.addNumericFilter("<", data.SPMinLoanAmount, "Current UPB");
          WinTbl.TableModel.addNumericFilter(">", data.SPMaxLoanAmount, "Current UPB");
          WinTbl.TableModel.addNumericFilter(">", data.SPMaxLoanToValue, "Original LTV");
          WinTbl.TableModel.addNumericFilter(">", data.SPMaxComLoanToValue, "Original CLTV");
          WinTbl.TableModel.addNumericFilter(">", data.SPMaxAdvance, "Advance %");

		  if (data.CBLienType == "First")
		      WinTbl.TableModel.addNumericFilter("!=", 1, "Lien Position"); 
	      else if (data.CBLienType == "Second")
		      WinTbl.TableModel.addNumericFilter("!=", 2, "Lien Position"); 
		  else if (data.CBLienType == "First & Second")
	      {
		      WinTbl.TableModel.addNumericFilter("<", 1, "Lien Position"); 
		      WinTbl.TableModel.addNumericFilter(">", 2, "Lien Position"); 
		  }

		  if (data.GBLoanType != null)
			  WinTbl.TableModel.addNumericFilter("!=", data.GBLoanType, "Is Adjustable");

		  if (data.GBPropertyType != null)
			  WinTbl.TableModel.addNumericFilter("!=", data.GBPropertyType, "Property Type Code");

		  if (data.GBAcceptState != null)
			  WinTbl.TableModel.addNumericFilter("!=", data.GBAcceptState, "State");
		  
          WinTbl.TableModel.applyFilters();
          WinTbl.Tbl.setAdditionalStatusBarText(", Filtered.");
		  WinCtl.close();
      }); 
      WinCtl.setModal(true);
	  root.add(WinCtl);

	  WinTbl.open();
	  WinTbl.moveTo(10, 10);

	  WinCtl.moveTo(10, 10);
      WinTbl.BtnFilter.addListener("execute", WinCtl.open, WinCtl);

    }
  }
});
