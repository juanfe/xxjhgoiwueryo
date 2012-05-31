dojo.require("dojox.grid.EnhancedGrid");
dojo.require("dojo.data.ItemFileWriteStore");

var ls={};

function createGrid(dataStore) {
    var label = function(field) {
        return ls.FieldLabel.label(field);
    };
	var lbs = {
		collateral: 'Collateral',
		property_type_code: "Property Type Code",
		customer_account_key: "Customer Account Key",
		original_upb: "Original UPB",
		current_upb: "Current UPB",
		origination_date: "Origination Date",
		is_adjustable: "Is Adjustable",
	};
    var fields = {
		collateral: 'collateral_key',
		property_type_code: "property_type_code",
		customer_account_key: "customer_account_key",
		original_upb: 'orig_upb',
		current_upb: 'curr_upb',
        origination_date: 'origination_date',
		is_adjustable: 'is_adjustable',
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
		[{
                //name: label(fields.collateral),
                name: lbs.collateral,
                field: fields.collateral,
                datatype: 'string'
            }, {
				//name: label(fields.property_type_code),
				name: lbs.property_type_code,
				field: fields.property_type_code,
                datatype: 'string'
			}, {
				//name: label(fields.customer_account_key),
				name: lbs.customer_account_key,
				field: fields.customer_account_key,
                datatype: 'string'
			}, {
                //name: label(fields.original_upb),
				name: lbs.original_upb,
                field: fields.original_upb,
                datatype: 'number',
                /*formatter: function(item){
                    return dojo.number.format(item,{pattern: "#0.0"});
                }*/
            }, {
                //name: label(fields.current_upb),
				name: lbs.current_upb,
                field: fields.current_upb,
                datatype: 'number',
                /*formatter: function(item){
                    return dojo.number.format(item,{pattern: "#0.0"});
                }*/
            }, {
                //name: label(fields.origination_date),
                name: lbs.origination_date,
                field: fields.origination_date,
                datatype: 'date',
                dataTypeArgs: {
                    datePattern: "yyyy/M/d H:m:s"
                }
            }, {
                //name: label(fields.is_adjustable),
                name: lbs.is_adjustable,
                field: fields.is_adjustable,
                datatype: 'boolean',
                dataTypeArgs: {
                    datePattern: "yyyy/M/d H:m:s"
                }
            }
    ]};
 
    /*create a new grid:*/
    ls.grid = new dojox.grid.EnhancedGrid({
        id: 'grid',
		query: {'collateral_key':'*'},
        store: dataStore,
		clientSort : true,
        rowSelector: '20px',
        structure: layout,
		/*plugins: {
		    filter: {
			    itemsName: 'bids'
		    }
		}*/
	}, document.createElement('div'));
 
	ls.grid.height = 200;
    /*append the new grid to the div*/
    dojo.byId("gridDiv").appendChild(ls.grid.domNode);

    /*Call startup() to render the grid*/
    ls.grid.startup();
}

dojo.ready(function(){
    /*ls.dataStore = new dojo.data.ItemFileReadStore({
        identifier: 'collateral_key',
        url: "/bids"
    });*/
    /*set up data store*/
    var data = {
      identifier: 'id',
      items: []
    };

	var data_list = loans;
	var rows = 60;
	for(var i=0; i<data_list.length; i++){
      data.items.push(dojo.mixin({ id: i+1 }, data_list[i]));
    }
    ls.dataStore = new dojo.data.ItemFileWriteStore({data: data});
  
    createGrid(ls.dataStore);
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
};

function cleanBidsClick(){
    var selectedBids = ls.grid.selection.getSelected();
    var loans = {};
    for (var i=0; i< selectedBids.length; i++){
        loans[selectedBids[i].collateral_key] =
        {
            'collateral_key': selectedBids[i].collateral_key[0]
        };
    }
    var xhrArgs = {
        url: "loans",
        content: {'loans':dojo.toJson(loans)},
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
            location.href="/loans";
        },
        function(error){
            alert("An unexpected error occurred: " + error);
        }
    );
} 
