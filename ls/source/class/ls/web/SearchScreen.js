qx.Class.define("ls.web.SearchScreen",
{
  extend: qx.core.Object,
  
  construct : function(root)
  {
    var WinTbl = this.WinTbl = new ls.web.Table();
    root.add(WinTbl);

    var WinCtl = new ls.web.Control();
    //WinCtl.BtnCancel.addListener("execute", WinCtl.close, WinCtl);
    WinCtl.BtnCancel.addListener("execute", function(e){
      WinCtl.close();
    });
    WinCtl.addListener("changeData",function(e)
    {
      WinTbl.TableModel.resetHiddenRows();
      WinTbl.TableModel.applyFilters();
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

    //WinTbl.open();
    WinTbl.moveTo(10, 10);

    WinCtl.moveTo(10, 10);
    WinTbl.BtnFilter.addListener("execute", WinCtl.open, WinCtl);
  },
  
  members :
  {
    WinTbl : null,
    open : function() {
      this.WinTbl.open();
    }
  }
});