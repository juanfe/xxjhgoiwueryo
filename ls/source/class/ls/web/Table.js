/* ************************************************************************
 *
 * #asset(ls/web/FundingData.json)
 * #asset(ls/web/16/Collateral.png)
 * #asset(ls/web/16/Zip.png)
 * #asset(ls/web/16/Adjustable.png)
 * #asset(ls/web/16/Current_UPB.png)
 * #asset(ls/web/16/Max_Advance.png)
 * #asset(ls/web/16/Investor_Code.png)
 * #asset(ls/web/16/Property_Type.png)
 * #asset(ls/web/16/Max_LTV.png)
 * #asset(ls/web/16/Max_CLTV.png)
 * #asset(ls/web/16/FICO.png)
 * #asset(ls/web/16/Purpose_Code.png)
 * #asset(ls/web/16/Occupancy_Code.png)
 * #asset(ls/web/16/Doc_Level_Code.png)
 * #asset(ls/web/16/Debt_Service_Ratio.png)
 * #asset(ls/web/16/Current_Rate.png)
 * #asset(ls/web/16/CoreLogic_Collateral_Risk_Score.png)
 * #asset(ls/web/16/CoreLogic_Fraud_Risk_Score.png)
 *
 * ************************************************************************ */
qx.Class.define("ls.web.Table", {
	extend : qx.ui.window.Window,

	construct : function(root) {
		this.base(arguments, "Loans")
		this.setShowClose(false);
		this.setShowMaximize(false);
		this.setShowMinimize(false);
		this.maximize();

		// add layout
		var layout = new qx.ui.layout.Grid(0, 0);
		this.setLayout(layout);

		//toolbar
		var toolbar = new qx.ui.toolbar.ToolBar();
		this.add(toolbar, {
			row : 0,
			column : 0,
			colSpan : 2
		});

		var TBPart1 = new qx.ui.toolbar.Part();
		var BtnPlaceBids = new qx.ui.toolbar.Button("Place bids");
		var BtnSubmitBids = new qx.ui.toolbar.Button("Submit bids");
		
		var BtnReturn = new qx.ui.toolbar.Button("Return");
		var BtnHome = new qx.ui.toolbar.Button("Home");
		BtnPlaceBids.setWidth(100);
		BtnSubmitBids.setWidth(0);
		BtnReturn.setWidth(0);
		
		TBPart1.add(BtnPlaceBids);
		TBPart1.add(BtnSubmitBids);
		TBPart1.add(BtnReturn);
		TBPart1.add(BtnHome);
		TBPart1.add(new qx.ui.toolbar.Separator());
		toolbar.add(TBPart1);

		var TBPart2 = new qx.ui.toolbar.Part();
		var BtnFilter = this.BtnFilter = new qx.ui.toolbar.Button("Filter");
		TBPart2.add(BtnFilter);
		toolbar.add(TBPart2);

		toolbar.addSpacer();
		//var helpButton = new qx.ui.toolbar.Button("Help", "icon/22/actions/help-contents.png");
		var helpButton = new qx.ui.toolbar.Button("Help");
		toolbar.add(helpButton);
		this.setContentPadding(0);

		layout.setRowFlex(1, 1);
		layout.setColumnFlex(0, 1);

		//var CapColmNames = ["Sel", "Collateral", "State", "Zip", "Original UPB", "Current UPB",  "Origination Date", "Is Adjustable", "Advance %", "Investor Code", "Property Type Code", "Lien Position", "Original LTV", "Original CLTV", "FICO Score", "Purpose Code", "Occupancy Code", "Doc Level Code", "Debt Service Ratio", "Cur Note Rate", "CoreLogic Fraud Risk Score", "CoreLogic Collateral Risk Score"];
		var CapColmNames = ["Selected", "Collateral", "State", "Zip", "Orig Loan Amount", "Curr Loan Amount", "Origination Date", "Is Adjustable", "Advance %", "Investor Code", "Property Type Code", "Lien Position", "Original LTV", "Original CLTV", "FICO Score", "Purpose Code", "Occupancy Code", "Doc Level Code", "Debt Service Ratio", "Cur Note Rate", "CoreLogic Fraud Risk Score", "CoreLogic Collateral Risk Score", "Participation %", "Bid rate"];
		var colTypes = {
			"Collateral" : "string",
			"State" : "string",
			"Zip" : "string",
			"Original UPB" : "int",
			"Current UPB" : "int",
			"Origination Date" : "date",
			"Is Adjustable" : "string",
			"Advance %" : "float",
			"Investor Code" : "string",
			"Property Type Code" : "string",
			"Lien Position" : "int",
			"Original LTV" : "float",
			"Original CLTV" : "float",
			"FICO Score" : "int",
			"Purpose Code" : "string",
			"Occupancy Code" : "string",
			"Doc Level Code" : "int",
			"Debt Service Ratio" : "float",
			"Cur Note Rate" : "float",
			"CoreLogic Fraud Risk Score" : "int",
			"CoreLogic Collateral Risk Score" : "int"
		};

		var tableModel = this.TableModel = new qx.ui.table.model.Filtered();

		tableModel.setColumns(CapColmNames);
		var url = qx.util.ResourceManager.getInstance().toUri("ls/web/FundingData.json");

		var req = new qx.io.remote.Request(url, "GET", "text/plain");
		var rows = [];

		var row = new Array(CapColmNames.length);
		row[0] = false;
		row[1] = "All Collaterals: ";
		rows.push(row);

		req.addListener("completed", function(e) {
			var data = e.getContent();
			var pdata = new qx.data.Array();
			var row = [false];
			var header = [];
			var flag = 0;
			pdata = qx.lang.Json.parse(data, function(key, value) {
				//	if (key == "Collateral")
				//		row.push(1);
				if(isNaN(parseInt(key))) {
					if(colTypes[key] == "string" || colTypes[key] == "date") {
						row.push(value);
					} else if(colTypes[key] == "int") {
						row.push(parseInt(value));
					} else if(colTypes[key] == "float") {
						row.push(parseFloat(value));
					}
				} else {
					rows.push(row);
					row = [false];
					flag = 1;
				}
				if(flag == 0) {
					header.push(key);
				}
			});
			tableModel.setData(rows);
			tableModel.hideRows(0, 1);
		});
		req.send();

		var tbl = this.Tbl = new qx.ui.table.Table(tableModel);
		var tcm = tbl.getTableColumnModel();
		var tsm = tbl.getSelectionModel();

		for(var i = 0; i < CapColmNames.length; i++) {
			tableModel.setColumnEditable(i, false);
			if(i >= CapColmNames.length - 2) {
				tcm.setColumnVisible(i, false);
			}
		}

		var selectColumnName = "Selected";
		var selectColumnId = tableModel.getColumnIndexById(selectColumnName);
		var loanAmountName = "Curr Loan Amount";
		var loanAmountId = tableModel.getColumnIndexById(loanAmountName);

		tcm.setDataCellRenderer(0, new qx.ui.table.cellrenderer.Boolean());
		tbl.addListener("cellClick", function(e) {
			if(e.getColumn() == selectColumnId) {
				var bValue = ((tableModel.getValue(selectColumnId, e.getRow()) == true ) ? false : true );
				// if(e.getRow() != 0) {
					tableModel.setValue(selectColumnId, e.getRow(), bValue);
				// } 
				// else {
					// var dataToPost = tableModel.getData();
					// for(var i = 0; i < dataToPost.length; i++) {
						// for(var j = 0; j < rows.length; j++) {
							// if(dataToPost[i][1] == rows[j][1]) {
								// tableModel.setValue(selectColumnId, j, bValue);
							// }
						// }
					// }
				// }
			}
		}, this);

		tbl.set({
			width : 900,
			height : 500,
			decorator : null
		});

		BtnPlaceBids.addListener("execute", function(evt) {
			var i = 2;
			for(i; i < CapColmNames.length - 2; i++) {
				tcm.setColumnVisible(i, false);
			}
			tcm.setColumnVisible(loanAmountId, true);
			for(i; i < CapColmNames.length; i++) {
				tableModel.setColumnEditable(i, true);
				tcm.setColumnVisible(i, true);
			}
			tableModel.resetHiddenRows();
			tableModel.addNumericFilter("!=", true, selectColumnName);
			tableModel.applyFilters();
			BtnSubmitBids.setWidth(BtnPlaceBids.getWidth());
			BtnReturn.setWidth(BtnPlaceBids.getWidth());
			BtnPlaceBids.setWidth(0);
		}, this);

		BtnReturn.addListener("execute", function(evt) {
			var i = 2;
			for(i; i < CapColmNames.length - 2; i++) {
				tcm.setColumnVisible(i, true);
			}
			for(i; i < CapColmNames.length; i++) {
				tableModel.setColumnEditable(i, false);
				tcm.setColumnVisible(i, false);
			}
			tableModel.resetHiddenRows();
			BtnPlaceBids.setWidth(BtnReturn.getWidth());
			BtnSubmitBids.setWidth(0);
			BtnReturn.setWidth(0);
		}, this);

		BtnHome.addListener("execute", function(evt) {
			var i = 2;
			for(i; i < CapColmNames.length - 2; i++) {
				tcm.setColumnVisible(i, true);
			}
			for(i; i < CapColmNames.length; i++) {
				tableModel.setColumnEditable(i, false);
				tcm.setColumnVisible(i, false);
			}
			tableModel.resetHiddenRows();
			BtnPlaceBids.setWidth(BtnReturn.getWidth());
			BtnSubmitBids.setWidth(0);
			BtnReturn.setWidth(0);
			this.homeClicked();
		}, this);

		BtnSubmitBids.addListener("execute", function(evt) {
			var dataToPost = tableModel.getData();
			var sentRow = [];
			var sentRows = [];
			for(var i = 1; i < dataToPost.length; i++) {
				if(dataToPost[i][0] == true && dataToPost.length == 24 && dataToPost[i][22].length > 0 && dataToPost[i][23].length > 0) {
					sentRow.push(dataToPost[i][1]);
					sentRow.push(dataToPost[i][22]);
					sentRow.push(dataToPost[i][23]);
					sentRow.push("Accepted");
					sentRows.push(sentRow);
					sentRow = [];
				}
			}
			ls.common.RequestAdapter.saveJson(sentRows);
			this.submissionSuccesful();
		}, this);

		tbl.getSelectionModel().setSelectionMode(qx.ui.table.selection.Model.NO_SELECTION);

		var tcm = tbl.getTableColumnModel();

		//tcm.setDataCellRenderer(0, new qx.ui.table.cellrenderer.Boolean());
		//TODO add the popups messages in the setHeaderCellRenderer last parameter
		tcm.setHeaderCellRenderer(1, new qx.ui.table.headerrenderer.Icon("ls/web/16/Collateral.png", "Identifier of the Collateral."));
		tcm.setHeaderCellRenderer(3, new qx.ui.table.headerrenderer.Icon("ls/web/16/Zip.png", "Identifier of the Collateral."));
		tcm.setHeaderCellRenderer(4, new qx.ui.table.headerrenderer.Icon("ls/web/16/Original_UPB.png", ""));
		tcm.setHeaderCellRenderer(5, new qx.ui.table.headerrenderer.Icon("ls/web/16/Current_UPB.png", ""));
		tcm.setHeaderCellRenderer(6, new qx.ui.table.headerrenderer.Icon("icon/16/apps/office-calendar.png", "A date"));
		tcm.setHeaderCellRenderer(7, new qx.ui.table.headerrenderer.Icon("ls/web/16/Adjustable.png", ""));
		tcm.setHeaderCellRenderer(8, new qx.ui.table.headerrenderer.Icon("ls/web/16/Max_Advance.png", ""));
		tcm.setHeaderCellRenderer(9, new qx.ui.table.headerrenderer.Icon("ls/web/16/Investor_Code.png", ""));
		tcm.setHeaderCellRenderer(10, new qx.ui.table.headerrenderer.Icon("ls/web/16/Property_Type.png", ""));
		tcm.setHeaderCellRenderer(12, new qx.ui.table.headerrenderer.Icon("ls/web/16/Max_LTV.png", ""));
		tcm.setHeaderCellRenderer(13, new qx.ui.table.headerrenderer.Icon("ls/web/16/Max_CLTV.png", ""));
		tcm.setHeaderCellRenderer(14, new qx.ui.table.headerrenderer.Icon("ls/web/16/FICO.png", ""));
		tcm.setHeaderCellRenderer(15, new qx.ui.table.headerrenderer.Icon("ls/web/16/Purpose_Code.png", ""));
		tcm.setHeaderCellRenderer(16, new qx.ui.table.headerrenderer.Icon("ls/web/16/Occupancy_Code.png", ""));
		tcm.setHeaderCellRenderer(17, new qx.ui.table.headerrenderer.Icon("ls/web/16/Doc_Level_Code.png", ""));
		tcm.setHeaderCellRenderer(18, new qx.ui.table.headerrenderer.Icon("ls/web/16/Debt_Service_Ratio.png", ""));
		tcm.setHeaderCellRenderer(19, new qx.ui.table.headerrenderer.Icon("ls/web/16/Current_Rate.png", ""));
		tcm.setHeaderCellRenderer(20, new qx.ui.table.headerrenderer.Icon("ls/web/16/CoreLogic_Fraud_Risk_Score.png", ""));
		tcm.setHeaderCellRenderer(21, new qx.ui.table.headerrenderer.Icon("ls/web/16/CoreLogic_Collateral_Risk_Score.png", ""));
		this.add(tbl, {
			row : 2,
			column : 0
		});
	},
	members : {
		TableModel : null,
		Tbl : null,
		BtnFilter : null,
		submissionSuccesful : null,
		homeClicked : null
	}
});
