qx.Class.define("mybids.Home",
{
  extend : qx.ui.window.Window,
  
  construct : function()
  {
    this.base(arguments, "Liquidity Exchange");
    this.setShowClose(false);
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.maximize();
    var layout = new qx.ui.layout.Grid(0, 0);
    this.setLayout(layout);
    var button = this.mybidsButton = new qx.ui.toolbar.Button("My Bids");
    //button.addListener("execute", WinTbl.open, WinTbl);
    this.add(button, {row:0, column:0});
    //this.open();
  },
  
  members :
  {
    searchButton : null,
    mybidsButton : null
  }
});