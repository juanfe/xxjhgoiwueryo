/* ************************************************************************
 *
 * #asset(web/FundingData.json)
 *
 * ************************************************************************ */
qx.Class.define("mybids.BaseTable",
{
  extend : qx.ui.window.Window,

  construct : function(columnsName)
  {
    this.base(arguments, "My Bids")
    this.setShowClose(false);
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.maximize();
    
    // add layout
    var layout = new qx.ui.layout.Grid(0, 0);
    this.setLayout(layout);
    layout.setRowFlex(0, 1);
    layout.setRowFlex(1, 1);
    layout.setColumnFlex(0,1);
    //toolbar
    var toolbar = this.__toolbar = new qx.ui.toolbar.ToolBar();
    this.add(toolbar, {row: 0, column: 0});

    // Setting tableModel
    var tableModel = this.__tableModel = new qx.ui.table.model.Filtered();
    tableModel.setColumns(columnsName);
    for (var i = 0; i < columnsName.length; i++){
      tableModel.setColumnEditable(i, false);
    }
    // Setting table   
    var tbl = this.__tbl = new qx.ui.table.Table(tableModel);
    tbl.getSelectionModel().setSelectionMode(qx.ui.table.selection.Model.MULTIPLE_INTERVAL_SELECTION);
    //var tcm = tbl.getTableColumnModel();
    //tcm.setDataCellRenderer(3, new qx.ui.table.cellrenderer.Boolean());
    //tcm.setHeaderCellRenderer(5, new qx.ui.table.headerrenderer.Icon("icon/16/apps/office-calendar.png", "A date"));
    this.add(tbl, {row: 1, column: 0});
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
      if(regExpString === "") {
        regExpString = " ";
      }
      return regExpString;
    }
  },
  
  members :
  {
    __tableModel : null,
    __tbl : null,
    __toolbar : null,
    setData : function(rows) {
      this.__tableModel.setData(rows);
    },
    addButton : function(button) {
      this.__toolbar.add(button);
    },
    // Is going to hide all the columns that don't match the regular expression
    filterCollateralBy : function(regExpStr) {
      this.__tableModel.addNotRegex(regExpStr, "Collateral", true);
      this.__tableModel.applyFilters();
    }
  }
});
