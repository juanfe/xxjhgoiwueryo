qx.Class.define("ls.common.Cookie",
{
  type :  "static",
  
  statics: {
    // cookie key for the user:
    userKey : "com.liquidityspot.user",
    // user accesors
    getUser : function() {
      return qx.bom.Cookie.get(this.userKey);
    },
    setUser : function(user) {
      qx.bom.Cookie.set(this.userKey, user);
    }
  }
});