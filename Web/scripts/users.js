//application namespace
var ls={};

function createGrid(dataStore) {
    var label = function(field) {
        return ls.FieldLabel.label(field);
    };
    var fields = {
        account: 'account',
        fundsAvailable: 'fundsAvailable',
        group: 'group'
    };
    // set the layout structure:
    var layout = 
    {
        defaultCell:
        {
            width: 'auto',
            cellStyles: 'text-align: center;',
            headerStyles: 'text-align: center;'
        }, 
        cells: 
        [ 
            {
                name: label(fields.account),
                field: fields.account,
                datatype: 'string'
            },{
                name: label(fields.fundsAvailable),
                field: fields.fundsAvailable,
                datatype: 'number',
                /*formatter: function(item){
                    return dojo.number.format(item,{pattern: "#0.0"});
                }*/
            },{
                name: label(fields.group),
                field: fields.group,
                datatype: 'string'
            }
        ]
    };

    ls.grid = new dojox.grid.EnhancedGrid({
        //query: {'collateral_key':'*'},
        store : dataStore,
        clientSort : true,
        rowSelector : '20px',
        structure : layout,
        plugins: {
            filter: {
                itemsName: 'users'
            }
        }
    }, document.createElement('div'));

    // append the new grid to the div "grid":
    dojo.byId("grid").appendChild(ls.grid.domNode);

    // Call startup, in order to render the grid:
    ls.grid.startup();
}

dojo.ready(function () {
	ls.dataStore = new dojo.data.ItemFileReadStore({
        identifier: 'collateral_key',
        url: "/users"
    });
	createGrid(ls.dataStore);
	ls.addGridTooltip({
		grid:ls.grid,
		column:'Status',
		defaultMessage:'Hey',
		gridSection: 'cell',
		messages: {
			'Accepted' : 'The bid is already placed',
			'Active' : 'There active bids for this loan',
			'Cancelled' : 'The bid was cancelled by the user'
		}
	});
	/*ls.dataStore.fetch({
		query: {'collateral_key':'*'}
	});*/
});



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
/*ls.addGridTooltip = function(parameters) {
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
				return type === (typeByName ? 'string' : String) &&
				    variable;
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
		if(notEmptySameType(grid, dojox.grid.EnhancedGrid) &&
		  notEmptySameType(defaultMessage, String) &&
		  notEmptySameType(column, String))
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
                        var item = e.grid.getItem(e.rowIndex),
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
				dojo.connect(grid, "onHeaderCellMouseOver", showTooltip); 
				dojo.connect(grid, "onHeaderCellMouseOut", hideTooltip);
			}
			// Cells events connection
			if (cellTooltip) {
				dojo.connect(grid, "onCellMouseOver", showTooltip); 
				dojo.connect(grid, "onCellMouseOut", hideTooltip);
			}  
		}
	}
};*/

/*function cleanBidsClick(){
	var selectedBids = ls.grid.selection.getSelected();
	var bids = {};
	for (var i=0; i< selectedBids.length; i++){
		bids[selectedBids[i].collateral_key] =
		{
			'collateral_key': selectedBids[i].collateral_key[0]
		};
	}
	var xhrArgs = {
        url: "/users",
        content: {'bids':dojo.toJson(bids)},
        handleAs: "json",
        load: function(data) {
            console.log(data);
        },
        error: function(error) {
            console.log(error);
        }
    };
    //Call the asynchronous xhrDelete
    var deferred = dojo.xhrDelete(xhrArgs);
    deferred.then(
		function(data){
		    location.href="/mybids";
		},
		function(error){
			alert("An unexpected error occurred: " + error);
		}
	);
}*/

