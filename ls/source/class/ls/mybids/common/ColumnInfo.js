qx.Class.define("ls.mybids.common.ColumnInfo",{
  extend: qx.core.Object,
  construct: function(name, type) {
    this.name = name;
    this.type = type;
  },
  members: {
    name : "",
    type : "int"
  }
});
