dojo.require("dijit.TitlePane");
dojo.require("dijit.Tooltip");
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
    identifier:'collateral_key',
    url : "/bids"
  });
	createGrid(ls.dataStore);
	addGridEventHandlers(ls.grid);
	ls.dataStore.fetch({
		query: {'collateral_key':'*'}
	})
});

function createGrid(dataStore) {
	// set the layout structure:
	var layout = [ [ {
    'name' : 'Loan #',
    'field' : 'collateral_key',
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
		query: {'collateral_key':'*'},
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

function addGridEventHandlers(grid){
	ls.grid.on("CellMouseOver", function(evt) {
		value = evt.cellNode.firstChild.data;
		if(evt.cell.name === 'Status'){
			tooltip = new dijit.Tooltip({
				connectId : evt.cellNode,
				label : value + ": Lorem ipsum",
				showDelay: 250
			});
			//alert(value);
		}
	});
}

function cleanBidsClick(){
	var xhrArgs = {
            url: "/clean",
            handleAs: "json",
            load: function(data) {
            	console.log(data);
            },
            error: function(error) {
            	console.log(error);
            }
        };
        //Call the asynchronous xhrPost
        var deferred = dojo.xhrPost(xhrArgs);
}

