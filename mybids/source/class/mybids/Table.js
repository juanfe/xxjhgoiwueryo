/* ************************************************************************
 *
 * #asset(web/FundingData.json)
 *
 * ************************************************************************ */
qx.Class.define("mybids.Table",
{
  extend : mybids.BaseTable,
  
  construct : function(keysToFilter)
  {
    this.base(arguments, this.self(arguments).jsonFilepath, this.self(arguments).columnsInfo, keysToFilter);
  },

  statics : {
    // Configuration related variables
    // json source file relative to <applicationName>/source/resource folder
    jsonFilepath :  "mybids/FundingData.json",
    // Column name and type of each column of the table
    columnsInfo : [
      new mybids.common.ColumnInfo("Collateral","int"),
      new mybids.common.ColumnInfo("State","string"),
      new mybids.common.ColumnInfo("Zip","int"),
      new mybids.common.ColumnInfo("Original UPB","int"),
      new mybids.common.ColumnInfo("Current UPB","int"),
      new mybids.common.ColumnInfo("Origination Date","date"),
      new mybids.common.ColumnInfo("Is Adjustable","int"),
      new mybids.common.ColumnInfo("Max Advance","int"),
      new mybids.common.ColumnInfo("Investor Code","string"),
      new mybids.common.ColumnInfo("Property Type Code","string"),
      new mybids.common.ColumnInfo("Lien Position","int"),
      new mybids.common.ColumnInfo("Original LTV","float"),
      new mybids.common.ColumnInfo("Original CLTV","float"),
      new mybids.common.ColumnInfo("FICO Score","int"),
      new mybids.common.ColumnInfo("Purpose Code","string"),
      new mybids.common.ColumnInfo("Occupancy Code","string"),
      new mybids.common.ColumnInfo("Doc Level Code","int"),
      new mybids.common.ColumnInfo("Debt Service Ratio","float"),
      new mybids.common.ColumnInfo("Cur Note Rate","float"),
      new mybids.common.ColumnInfo("CoreLogic Fraud Risk Score","int"),
      new mybids.common.ColumnInfo("CoreLogic Collateral Risk Score","int")
    ]
  }
});
