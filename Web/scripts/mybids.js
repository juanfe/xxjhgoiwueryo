dojo.require("dijit.TitlePane");
dojo.require("dojo.data.ItemFileReadStore");
dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("dijit.form.Button");
dojo.require("dojox.grid.EnhancedGrid");
dojo.require("dojo.number");
dojo.require("dojo.on");

//application namespace
var ls={};

dojo.addOnLoad(function() {
	ls.dataStore = new dojo.data.ItemFileReadStore({
    identifier:'Collateral',
    url : "/dojobids"
  });
	createGrid(ls.dataStore)
	ls.dataStore.fetch({
		query: {'Collateral':'*'}
	})
});

function extractField(item){
	return item[this.field][0];
}


function createGrid(dataStore) {
	// set the layout structure:
	var layout = [ [ {
    'name' : 'Loan #',
    'field' : 'Collateral',
    'width' : 'auto',
    'cellStyles' : 'text-align: center;',
    'headerStyles': 'text-align: center;'
  },{
    'name' : 'Participation %',
    'field' : 'participation',
    'width' : 'auto',
    'cellStyles' : 'text-align: center;',
    'headerStyles': 'text-align: center;',
    'formatter': function(item){
      return dojo.number.format(item,{pattern: "#0.0"});
      },
  }, {
    'name' : 'Bid Rate',
    'field' : 'bidrate',
    'width' : 'auto',
    'formatter': '',
    'cellStyles' : 'text-align: center;',
    'headerStyles': 'text-align: center;',
    'formatter': function(item){
      return dojo.number.format(item,{pattern: "#0.0"});
      },
  }, {
    'name' : 'Status',
    'field' : 'status',
    'width' : 'auto',
    'formatter': '',
    'cellStyles' : 'text-align: center;',
    'headerStyles': 'text-align: center;',
  } ] ];

	ls.grid = new dojox.grid.EnhancedGrid({
		query: {'Collateral':'*'},
		store : dataStore,
		clientSort : true,
		rowSelector : '20px',
		structure : layout,
	}, document.createElement('div'));

	// append the new grid to the div "grid":
	dojo.byId("grid").appendChild(ls.grid.domNode);

	// Call startup, in order to render the grid:
	ls.grid.startup();
}