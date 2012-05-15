dojo.require("dojox.grid.EnhancedGrid");
dojo.require("dojo.data.ItemFileWriteStore");

var ls={};

function createGrid(dataStore) {
    var label = function(field) {
        return ls.FieldLabel.label(field);
    };
    var fields = {
        collateral: 'collateral_key',
        participation: 'participation',
        bidRate: 'bidrate',
        status: 'status',
        creation: 'createdAt',
        expiration: 'expiresAt'
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
                //name: label(fields.collateral),
                name: fields.collateral,
                field: fields.collateral,
                datatype: 'string'
            }, {
                //name: label(fields.participation),
                name: fields.participation,
                field: fields.participation,
                datatype: 'number',
                /*formatter: function(item){
                    return dojo.number.format(item,{pattern: "#0.0"});
                }*/
            }, {
                //name: label(fields.bidRate),
                name: fields.bidRate,
                field: fields.bidRate,
                datatype: 'number',
                /*formatter: function(item){
                    return dojo.number.format(item,{pattern: "#0.0"});
                }*/
            }, {
                //name: label(fields.status),
                name: fields.status,
                field: fields.status,
                datatype: 'string'
            }, {
                //name: label(fields.creation),
                name: fields.creation,
                field: fields.creation,
                datatype: 'date',
                dataTypeArgs: {
                    datePattern: "yyyy/M/d H:m:s"
                }
            }, {
                //name: label(fields.expiration),
                name: fields.expiration,
                field: fields.expiration,
                datatype: 'date',
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

    var data_list = [
      { collateral_key: "normal",
		participation : 3, 
		bidrate: 0.3, 
        status: 29.91,
		createdAt: "01/01/2012",
		expiresAt: "01/01/2012"
		},
      { collateral_key: "important",
		participation : 4,
		bidrate: 0.5, 
        status: 9.33,
		createdAt: "01/01/2012",
		expiresAt: "01/01/2012"
        },
      { collateral_key: "important",
		/*col2: false,*/
		participation: 5,
		bidrate: 0.23,
        status: 19.34,
		createdAt: "01/01/2012",
		expiresAt: "01/01/2012"
        }
    ];
    var rows = 60;
    for(var i=0, l=data_list.length; i<rows; i++){
      data.items.push(dojo.mixin({ id: i+1 }, data_list[i%l]));
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
    var bids = {};
    for (var i=0; i< selectedBids.length; i++){
        bids[selectedBids[i].collateral_key] =
        {
            'collateral_key': selectedBids[i].collateral_key[0]
        };
    }
    var xhrArgs = {
        url: "/bids",
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
} 
