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
    // Defining the buttons
    var mybidsButton = this.mybidsButton = new qx.ui.form.Button("My Bids");
    var searchButton = this.searchButton = new qx.ui.form.Button("Search");
    var logoutButton = this.saveButton = new qx.ui.form.Button("Logout");
    // Placing them
    this.add(searchButton, {row:0, column:0});
    this.add(mybidsButton, {row:0, column:1});
    this.add(logoutButton, {row:0, column:2});
    // Adding proper listeners
    logoutButton.addListener("execute", function() {
        var logoutUrl = "/logout",
            frm = document.forms["dummyForm"];
        frm.action = logoutUrl;
        //ls.common.Cookie.deleteUser();
        frm.submit();
    });
  },
  
  members :
  {
    searchButton : null,
    mybidsButton : null,
    saveButton : null
  }
});