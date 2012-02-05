/* ************************************************************************
 *
 * #asset(web/FundingData.json)
 * #asset(web/16/Collateral.png)
 * #asset(web/16/Zip.png)
 *
 * ************************************************************************ */
qx.Class.define("web.Table",
{
  extend : qx.ui.window.Window,

  construct : function()
  {
    this.base(arguments, "Loans")
    this.setShowClose(false);
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.setWidth(950);
    this.setHeight(400);
	
    // add layout
    var layout = new qx.ui.layout.Grid(0, 0);
    this.setLayout(layout);

    //toolbar
    var toolbar = new qx.ui.toolbar.ToolBar();
    this.add(toolbar, {row: 0, column: 0, colSpan: 2});

	var TBPart1 = new qx.ui.toolbar.Part();
	var BtnPlaceBids = new qx.ui.toolbar.Button("Place bids");
	var BtnRtrnToMySpot = new qx.ui.toolbar.Button("Return to My Spot");

	TBPart1.add(BtnPlaceBids);
	TBPart1.add(BtnRtrnToMySpot);
	TBPart1.add(new qx.ui.toolbar.Separator());
	toolbar.add(TBPart1);

	var TBPart2 = new qx.ui.toolbar.Part();
	var BtnFilter = this.BtnFilter = new qx.ui.toolbar.Button("Filter");
	var BtnLogout = new qx.ui.toolbar.Button("Logout");
    TBPart2.add(BtnFilter);
	TBPart2.add(BtnLogout);
	toolbar.add(TBPart2);

	toolbar.addSpacer();
	//var helpButton = new qx.ui.toolbar.Button("Help", "icon/22/actions/help-contents.png");
	var helpButton = new qx.ui.toolbar.Button("Help");
	toolbar.add(helpButton);
    this.setContentPadding(0);

    layout.setRowFlex(1, 1);
    layout.setColumnFlex(0,1);

    //var CapColmNames = ["Sel", "Collateral", "State", "Zip", "Original UPB", "Current UPB",  "Origination Date", "Is Adjustable", "Advance %", "Investor Code", "Property Type Code", "Lien Position", "Original LTV", "Original CLTV", "FICO Score", "Purpose Code", "Occupancy Code", "Doc Level Code", "Debt Service Ratio", "Cur Note Rate", "CoreLogic Fraud Risk Score", "CoreLogic Collateral Risk Score"]; 
    var CapColmNames = ["Collateral", "State", "Zip", "Original UPB", "Current UPB",  "Origination Date", "Is Adjustable", "Advance %", "Investor Code", "Property Type Code", "Lien Position", "Original LTV", "Original CLTV", "FICO Score", "Purpose Code", "Occupancy Code", "Doc Level Code", "Debt Service Ratio", "Cur Note Rate", "CoreLogic Fraud Risk Score", "CoreLogic Collateral Risk Score", "%Bid", "%Interest "]; 
	var colTypes = { "Collateral":"string",
		"State":"string",
		"Zip":"int",
		"Original UPB":"int",
		"Current UPB":"int",
		"Origination Date":"date",
		"Is Adjustable":"string",
		"Advance %":"float",
		"Investor Code":"string",
		"Property Type Code":"string",
		"Lien Position":"int",
		"Original LTV":"float",
		"Original CLTV":"float",
		"FICO Score":"int",
		"Purpose Code":"string",
		"Occupancy Code":"string",
		"Doc Level Code":"int",
		"Debt Service Ratio":"float",
		"Cur Note Rate":"float",
		"CoreLogic Fraud Risk Score":"int",
		"CoreLogic Collateral Risk Score":"int"};

    var tableModel = this.TableModel = new qx.ui.table.model.Filtered();

	tableModel.setColumns(CapColmNames);
	var url = qx.util.ResourceManager.getInstance().toUri("web/FundingData.json");
	
	var req = new qx.io.remote.Request(url, "GET", "text/plain"); 
	var rows = [];
	req.addListener("completed", function(e) { 
		var data = e.getContent();

		var pdata = new qx.data.Array();
		var row = [];
		var header = [];
		var flag = 0;
		pdata = qx.lang.Json.parse(data, function(key, value)
		{
		//	if (key == "Collateral")
		//		row.push(1);
			if (isNaN(parseInt(key)))
	     	{
				if (colTypes[key] == "string" || colTypes[key] == "date"){
 				  row.push(value);
				}
				else if (colTypes[key] == "int"){
				  row.push(parseInt(value));//}
				}
				else if (colTypes[key] == "float"){
				  row.push(parseFloat(value));
				}
			}
			else
	      	{
				rows.push(row);
				row = [];
				flag = 1;
			}
			if (flag == 0)
			{
				header.push(key);
			}
		});
        tableModel.setData(rows);
	});
	req.send();

    var tbl = this.Tbl = new qx.ui.table.Table(tableModel);
  	var tcm = tbl.getTableColumnModel();

	for (var i = 0; i < CapColmNames.length; i++){
      tableModel.setColumnEditable(i, false);
      if (i >= CapColmNames.length - 2)
	      tcm.setColumnVisible(i, false);      	
	}

    tbl.set({
        width: 900,
        height: 430,
        decorator : null
    });

	BtnPlaceBids.addListener("execute", function(evt)
      {
      	var i = 1
		for (i; i < CapColmNames.length - 2; i++){
	      tcm.setColumnVisible(i, false);
		}
		for (i; i < CapColmNames.length; i++){
	      tableModel.setColumnEditable(i, true);
	      tcm.setColumnVisible(i, true);
		}
		tbl.getSelectionModel().iterateSelection(function(ind) {
          //selection.push(ind + "");
          tableModel.hideRows(ind,1);
        });
        //this.showDialog("Selected rows:<br>" + selection.join(", "));
      }, this);

    tbl.getSelectionModel().setSelectionMode(qx.ui.table.selection.Model.MULTIPLE_INTERVAL_SELECTION_TOGGLE);

    var tcm = tbl.getTableColumnModel();

    //tcm.setDataCellRenderer(0, new qx.ui.table.cellrenderer.Boolean
    tcm.setHeaderCellRenderer(5, new qx.ui.table.headerrenderer.Icon("icon/16/apps/office-calendar.png", "A date"));
    tcm.setHeaderCellRenderer(0, new qx.ui.table.headerrenderer.Icon("web/16/Collateral.png", "Identifier of the Collateral."));
    tcm.setHeaderCellRenderer(2, new qx.ui.table.headerrenderer.Icon("web/16/Zip.png", "Identifier of the Collateral."));

    this.add(tbl, {row: 2, column: 0});
  },

  members :
  {
    TableModel : null,
    Tbl : null,
    BtnFilter : null
  }
});
