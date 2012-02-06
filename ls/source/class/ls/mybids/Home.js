qx.Class.define("ls.mybids.Home",
{
  extend : qx.ui.window.Window,
  
  construct : function()
  {
    this.base(arguments, "Liquidity Exchange");
    this.setShowClose(false);
    this.setShowMaximize(false);
    this.setShowMinimize(false);
    this.maximize();
    var layout = new qx.ui.layout.Grid(10, 0);
    this.setLayout(layout);
    var mybidsButton = this.mybidsButton = new qx.ui.form.Button("My Bids");
    var searchButton = this.searchButton = new qx.ui.form.Button("Search");
    //var saveButton = this.saveButton = new qx.ui.form.Button("Save Test");
    this.add(searchButton, {row:0, column:0});
    this.add(mybidsButton, {row:0, column:1});
    //this.add(saveButton, {row:0, column:2});
  },
  
  members :
  {
    searchButton : null,
    mybidsButton : null,
    saveButton : null
  }
});