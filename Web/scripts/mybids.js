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
	//addGridEventHandlers(ls.grid);
	ls.addGridTooltip({
		grid:ls.grid,
		column:'Status',
		defaultMessage:'Hey',
		gridSection: 'cell',
		messages: {
			'Accepted' : 'The bid is already placed',
			'Active' : 'There active bids for this loan',
			'Cancelled' : 'The bid was cancelled by the user',
		}
	});
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

// parameters is an object with the following fields:
//   grid: A dojox.grid.EnhancedGrid instance where the tooltip
//     will be added.
//   column: The name of the column where this toolip is appliable 
//   defaultMessage: The text of the tooltip if there isn't
//     text specific for that cell value.
//   gridSection (optional, 'both' by default): can be 'header'
//     or 'cell' according to which part of the table is going
//     to display the tooltip.
//   messages (optional) : is an object with properties as possible
//     values of the cells with the corresponding message, to be
//     shown in the tooltip, as value.
ls.addGridTooltip = function(parameters) {
	function notEmptySameType(variable, type) {
		var typeByName = typeof type === 'string';
		if (typeByName) {
			type = type.toLowerCase();
		}
		switch (typeof variable)
		{
			case 'undefined':
				return false;
			case 'boolean':
				return type === (typeByName ? 'boolean' : Boolean);
			case 'number':
				return type === (typeByName ? 'number' : Number);
			case 'string':
				return type === (typeByName ? 'string' : String)
					&& variable;
			case 'object':
				if(variable && variable instanceof type){
					for (var prop in variable) {
						if (variable.hasOwnProperty(prop)) {
							return true;
						}
					}
				}
				return false;
			case 'function':
				return type === (typeByName ? 'function' : Function);			
		}
		if (typeof variable !== "undefined") {
			if (variable instanceof type) {
				if (variable) {
					return true;
				}
			}
		}
		return false;
	}
	if (notEmptySameType(parameters, Object)) {
		var grid = parameters.grid,
			defaultMessage = parameters.defaultMessage,
			column = parameters.column;
		if(notEmptySameType(grid, dojox.grid.EnhancedGrid)
			&& notEmptySameType(defaultMessage, String)
			&& notEmptySameType(column, String))
		{
			// Checking and managing grid section option
			var gridSection = parameters.gridSection,
				messages = parameters.messages,
				headerTooltip = true,
				cellTooltip = true;
			if(notEmptySameType(gridSection, String)) {
				switch (gridSection) {
					case 'header':
						cellTooltip = false;
						break;
					case 'cell':
						headerTooltip = false;
						break;
				}
			}
			// Checking and managing specific messages option
			if (!notEmptySameType(messages, Object)) {
				messages = {};
			}
			// Event handlers
			var showTooltip = function(e) {
				if (e.cell.name === column) { 
					var msg = headerTooltip ? column : '';
					if (cellTooltip && e.rowIndex >= 0) {
        				var item = e.grid.getItem(e.rowIndex); 
        				cellValue = e.grid.store.getValue(item, e.cell.field);
        				msg = cellValue;        				
        			}
        			msg += ': ' + (messages[msg] || defaultMessage);
        			dijit.showTooltip(msg, e.cellNode);
				}
			}; 
    		var hideTooltip = function(e) { 
				dijit.hideTooltip(e.cellNode); 
			};
			// Header event connections
			if (headerTooltip) { 
				grid.on("HeaderCellMouseOver", showTooltip); 
				grid.on("HeaderCellMouseOut", hideTooltip);
			}
			// Cells events connection
			if (cellTooltip) {
				grid.on("CellMouseOver", showTooltip); 
				grid.on("CellMouseOut", hideTooltip);
			}  
		}
	}
}

function addGridEventHandlers(grid){
	var showTooltip = function(e) {
		if (e.cell.name === 'Status') { 
        	var item = e.grid.getItem(e.rowIndex), 
        		msg = e.grid.store.getValue(item, e.cell.field); 
        	if (msg) { 
            	dijit.showTooltip(msg + ': Lorem ipsum', e.cellNode); 
        	}
		}
	}; 
    var hideTooltip = function(e) { 
		dijit.hideTooltip(e.cellNode); 
	}; 
	grid.on("CellMouseOver", showTooltip); 
	grid.on("CellMouseOut", hideTooltip);  
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

