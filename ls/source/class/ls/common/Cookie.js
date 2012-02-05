qx.Class.define("ls.common.Cookie",
{
  extend: qx.core.Object,
  
  statics: {
    // cookie key for the user:
    userKey : "com.liquidityspot.user",
    // user accesors
    getUser : function() {
      return qx.bom.Cookie.get(this.constructor.userKey);
    },
    setUser : function(user) {
      qx.bom.Cookie.set(this.constructor.userKey, user);
    }
  }
});