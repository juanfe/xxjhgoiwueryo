/* ************************************************************************
 *
 * #asset(web/FundingData.json)
 *
 * ************************************************************************ */
qx.Class.define("mybids.BaseTable",
{
  extend : qx.ui.window.Window,

  construct : function(jsonFilepath, columnsInfo, keysToFilter)
  {
    this.base(arguments, "Loans")
    this.setShowClose(false);
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.maximize();
    
    var regExpStr = this.self(arguments).__matchAll(keysToFilter);
    
    // add layout
    var layout = new qx.ui.layout.Grid(0, 0);
    this.setLayout(layout);

    layout.setRowFlex(0, 1);
    layout.setColumnFlex(0,1);

    var tableModel = this.__tableModel = new qx.ui.table.model.Filtered();
    
    var columnInfoDict = new mybids.common.ColumnInfoDictionary(columnsInfo);
    
    tableModel.setColumns(columnInfoDict.getNames());
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
	     	  var type = columnInfoDict.getType(key);
				  if (type == "string" || type == "date"){
            row.push(value);
				  }
				  else if (type == "int"){
            row.push(parseInt(value));
				  }
				  else if (type == "float"){
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
      alert("populating");
      tableModel.setData(rows);
      alert("before Filter");
      tableModel.addNotRegex(regExpStr, "Collateral", true);
      tableModel.applyFilters();
    });
    req.send();

    for (var i = 0; i < columnsInfo.length; i++){
      tableModel.setColumnEditable(i, false);
    }

    var tbl = this.__tbl = new qx.ui.table.Table(tableModel);

    tbl.getSelectionModel().setSelectionMode(qx.ui.table.selection.Model.MULTIPLE_INTERVAL_SELECTION);

    var tcm = tbl.getTableColumnModel();

    tcm.setDataCellRenderer(3, new qx.ui.table.cellrenderer.Boolean());
    tcm.setHeaderCellRenderer(5, new qx.ui.table.headerrenderer.Icon("icon/16/apps/office-calendar.png", "A date"));

    this.add(tbl, {row: 0, column: 0});
  },
  
  statics :
  {
    __matchAll : function(array) {
      var i,
          regExpString = "";
      if(array) {
        for(i = 0; i<array.length; i++ ) {
          regExpString += ((i == 0 ? '' : '|') + array[i]); 
        }
      }
      return regExpString;
    }
  },
  
  members :
  {
    __tableModel : null,
    __tbl : null,
    BtnFilter : null
  }
});
