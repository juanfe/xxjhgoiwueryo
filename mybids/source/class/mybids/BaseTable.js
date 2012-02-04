/* ************************************************************************
 *
 * #asset(web/FundingData.json)
 *
 * ************************************************************************ */
qx.Class.define("mybids.BaseTable",
{
  extend : qx.ui.window.Window,

  construct : function(jsonFilepath)
  {
    this.base(arguments, "Loans")
    this.setShowClose(false);
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.maximize();
	
    // add layout
    var layout = new qx.ui.layout.Grid(0, 0);
    this.setLayout(layout);

    layout.setRowFlex(0, 1);
    layout.setColumnFlex(0,1);

    var CapColmNames = ["Collateral", "State", "Zip", "Original UPB", "Current UPB",  "Origination Date", "Is Adjustable", "Max Advance", "Investor Code", "Property Type Code", "Lien Position", "Original LTV", "Original CLTV", "FICO Score", "Purpose Code", "Occupancy Code", "Doc Level Code", "Debt Service Ratio", "Cur Note Rate", "CoreLogic Fraud Risk Score", "CoreLogic Collateral Risk Score"]; 
    var colTypes = { "Collateral":"int",
		  "State":"string",
		  "Zip":"int",
		  "Original UPB":"int",
		  "Current UPB":"int",
      "Origination Date":"date",
      "Is Adjustabl":"int",
      "Max Advance":"int",
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

    var tableModel = this.__tableModel = new qx.ui.table.model.Filtered();

    tableModel.setColumns(CapColmNames);
    var url = qx.util.ResourceManager.getInstance().toUri(jsonFilepath);
	
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
        //if (isNaN(parseInt(key)) || key == "1st_adj_max_initial_rate" || key == "1st_adj_min_initial_rate")
        if (isNaN(parseInt(key)))
	     	{
				  if (colTypes[key] == "string" || colTypes[key] == "date"){
            row.push(value);
				  }
				  else if (colTypes[key] == "int"){
            row.push(parseInt(value));
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

    for (var i = 0; i < CapColmNames.length; i++){
      tableModel.setColumnEditable(i, false);
    }

    var tbl = this.__tbl = new qx.ui.table.Table(tableModel);

    tbl.set({
        width: 900,
        height: 430,
        decorator : null
    });

    tbl.getSelectionModel().setSelectionMode(qx.ui.table.selection.Model.MULTIPLE_INTERVAL_SELECTION);

    var tcm = tbl.getTableColumnModel();

    tcm.setDataCellRenderer(3, new qx.ui.table.cellrenderer.Boolean());
    tcm.setHeaderCellRenderer(5, new qx.ui.table.headerrenderer.Icon("icon/16/apps/office-calendar.png", "A date"));

    this.add(tbl, {row: 0, column: 0});
  },

  members :
  {
    __tableModel : null,
    __tbl : null,
    BtnFilter : null
  }
});
