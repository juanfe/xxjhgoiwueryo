/* ************************************************************************
 *
 * #asset(web/FundingData.json)
 *
 * ************************************************************************ */
qx.Class.define("mybids.Table",
{
  extend : mybids.BaseTable,
  
  construct : function(jsonFilepath)
  {
    this.base(arguments, jsonFilepath);
  },

  members :
  {
    
  }
});
