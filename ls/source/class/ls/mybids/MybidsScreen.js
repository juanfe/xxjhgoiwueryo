qx.Class.define("ls.mybids.MybidsScreen",
{
  extend: qx.core.Object,
  
  construct : function(root)
  {
    var user = ls.common.Cookie.getUser();
    // Creating the mybids window
    var WinTbl = this.WinTbl = new ls.mybids.Table(user);
    root.add(WinTbl);
  },
  
  members :
  {
    WinTbl : null,
    open : function() {
      this.WinTbl.open();
    }
  }
});