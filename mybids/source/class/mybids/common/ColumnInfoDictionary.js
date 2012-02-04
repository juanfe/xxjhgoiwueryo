qx.Class.define("mybids.common.ColumnInfoDictionary",{
  extend: qx.core.Object,
  construct: function(columnInfoArray) {
    this.names = [];
    this.types = {};
    if(columnInfoArray) {
      for(var i = 0; i < columnInfoArray.length; i++) {
        this.add(columnInfoArray[i]);
      }
    }
  },
  members: {
    names : null,
    types : null,
    add : function(columnInfo) {
      var name = columnInfo.name,
          type = columnInfo.type;
      this.names.push(name);
      this.types[name] = type;
    },
    getNames : function() {
      return this.names;
    },
    getType : function(columnName) {
      return this.types[columnName];
    }
  }
});