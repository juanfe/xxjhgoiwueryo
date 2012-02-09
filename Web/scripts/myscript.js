
//application namespace
var ls={};
ls.conditions={};
ls.convertFunctions={};
ls.fullData=[];
ls.selectedLoanType = {};
ls.selectedPropertyType = {};
ls.checkboxGroups = {};

ls.Condition = function(configObj)
{
	//internal variables
	var obj = configObj;
	var userSatisfy;

	this.setSatisfy = function(func){
		userSatisfy = func;
	}
	    	    	
	this.satisfy = function(item){
		return userSatisfy(item,obj);
	}
};

dojo.addOnLoad(function() {
	ls.dataStore = new dojo.data.ItemFileReadStore({
		identifier:'Collateral',
		url : "../data/FundingData.json"
	});
	ls.dataStore.fetch({
		query: {'Collateral':'*'},
		onComplete:function(items){
			//Adjust data types
			ls.convertFunctions['CoreLogic Collateral Risk Score'] = parseInt;
			ls.convertFunctions['CoreLogic Fraud Risk Score'] = parseInt;
			ls.convertFunctions['Original LTV'] = parseFloat;
			ls.convertFunctions['Original CLTV'] = parseFloat;
			ls.convertFunctions['Current UPB'] = parseFloat;
			ls.convertFunctions['FICO Score'] = parseInt;
			ls.convertFunctions['Advance'] = parseFloat;
			ls.fullData = items.map(adjustDataType,ls.convertFunctions);
			//Create grid
			createGrid(ls.dataStore);
			//extract columns for filters
			ls.states = items.map(extractField,{field:'State'});
			ls.propertyType = items.map(extractField,{field:'Property Type Code'});
			ls.loanType = items.map(extractField,{field:'Is Adjustable'});
			ls.lienType = items.map(extractField,{field:'Lien Position'});
			ls.maxLTV = items.map(extractField,{field:'Original LTV'});
			ls.maxCLTV = items.map(extractField,{field:'Original CLTV'});
			ls.loanAmount = items.map(extractField,{field:'Current UPB'});
			ls.coreLogicCollateralRisk = items.map(extractField,{field:'CoreLogic Collateral Risk Score'});
			ls.coreLogicFraudRisk = items.map(extractField,{field:'CoreLogic Fraud Risk Score'});
			ls.fico = items.map(extractField,{field:'FICO Score'});
			ls.advancePercentage = items.map(extractField,{field:'Advance'});
			//Filters
			initFilters();
			//init palcebids dialog
		    ls.bidDialog = new dijit.Dialog({
		    	id: "bidDialog",
		        autofocus: false	
		    }); 
		    var html = "<div style='width: 500px; height: 500px;'dojoType='dijit.layout.ContentPane'><button dojoType='dijit.form.Button' id='submitBids' onClick='submitBidsClick'>Place bids</button><div id='bidGrid'></div></div>";							
		    ls.bidDialog.set("content",html);
		    ls.bidDialog.set("title", 'Place Bids');
		    initBidsGrid();

		}
	})
});

//this is mapped into the imported items. The "this" holds information on the data types that should be applied. 
function adjustDataType(item){
	for (field in item){
		if(item.hasOwnProperty(field)){
			if (this[field]){
				item[field] = [this[field](item[field])]; //replace old with new type
			}
		}
	}
	return item;
}

//This is 'mapped' into an array. Additional information (conditions) accessible in "this"
function filterFunc(item){
	var selected = true;
	for (var condition in this){
		selected = selected && this[condition].satisfy(item);
	}
	return selected;
}

function findMyAssetsClick(){
	dijit.byId('filters').toggle();
	applyFilters();
}

function placeBidsClick() {
	var selectedLoans = ls.grid.selection.getSelected();
	updateBidGrid(selectedLoans);
	ls.bidDialog.resize();
	ls.bidDialog.show();
}

function downloadDetailsClick() {
	var selectedLoans = ls.grid.selection.getSelected(),
		loansData = extractLoansData(selectedLoans),
		loansDataJson = dojo.toJson(loansData),
		dummyForm = dojo.byId('downloadForm'),
		keysPlaceHolder = dojo.byId('downloadInfo');
	dummyForm.action = '/download';
	keysPlaceHolder.value = loansDataJson;
	dummyForm.submit();
}

/*function loansDataToJson(loansData) {
	var rows = [],
		loansDataJson,
		i;
	for(i = 0; i < loansData.length; i++) {
		rows.push(dojo.toJson(loansData[i].slice(0,loansData[i].length - 2)));
	}
	loansDataJson = "[";
	for(i = 0; i < rows.length; i++) {
		loansDataJson += rows[i];
	}
	loansDataJson += "]";
	return loansDataJson;
}*/

function extractLoansData(selectedLoans) {
	var headers = [],
		firstLoan = true,
		loanData,
		loansData = [];
	if(selectedLoans.length){
		dojo.forEach(selectedLoans, function(selectedLoan){
			if(selectedLoan !== null){
				loanData = []
				dojo.forEach(ls.grid.store.getAttributes(selectedLoan), function(attribute){
					var value = ls.grid.store.getValue(selectedLoan, attribute);
					if(firstLoan) {
						headers.push(attribute);
					}
					loanData.push(value);				
				});
				if(firstLoan) {
					loansData.push(headers);
					firstLoan = false;
				}
				loansData.push(loanData);
			}
		});
	}
	// removing some dojo internal attributes
	for(var i = 0; i<loansData.length; i++){
		loansData[i].length -= 2;
	}
	return loansData;
}

function updateBidGrid(selectedLoans){
	for(var i=0; i < selectedLoans.length; i++){
		dojo.mixin(selectedLoans[i],{'participation':[0.0], 'bidrate':[0.0]});
	}
	// Create new datastore with selected items only
	var bidStore = new dojo.data.ItemFileWriteStore(
			{data: {	
				identifier: 'Collateral',
				items: selectedLoans}
			});
	
	ls.bidGrid.setStore(bidStore);
}

function initBidsGrid(){
	bidData = {	items: []};
	var bidStore = new dojo.data.ItemFileWriteStore({data: bidData});
	// set the layout structure:
	var layout = [ [ {
		'name' : 'Loan #',
		'field' : 'Collateral',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	}, {
		'name' : 'Loan Amount',
		'field' : 'Current UPB',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;',
		'formatter': function(item){
			return dojo.number.format(item,{pattern:'#,##0.##'});
			},
	},{
		'name' : 'Participation %',
		'field' : 'participation',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;',
		'editable':'true',
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
		'editable':'true',
		'formatter': function(item){
			return dojo.number.format(item,{pattern: "#0.0"});
			},
	}	] ];
		
	ls.bidGrid = new dojox.grid.EnhancedGrid({
		store : bidStore,
		clientSort : true,
		rowSelector : '20px',
		structure : layout,
		selectionMode: 'multiple'
	}, 'bidGrid');
	ls.bidGrid.startup();
}

function submitBidsClick(){
	var selectedBids = ls.bidGrid.selection.getSelected();
	var bids = {};
	for (var i=0; i< selectedBids.length; i++){
		bids[selectedBids[i]['Collateral']] =
		{
			'Collateral': selectedBids[i]['Collateral'][0],
			'participation': selectedBids[i]['participation'][0],
			'bidrate' : selectedBids[i]['bidrate'][0]
		};
	}
	dijit.byId('bidDialog').hide();
	
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
        //Call the asynchronous xhrPost
        var deferred = dojo.xhrPost(xhrArgs);
}


function applyFilters(){
	//Find selected items
	var selected = ls.fullData.filter(filterFunc, ls.conditions);

	// Create new datastore with selected items only
	var newStore = new dojo.data.ItemFileReadStore(
			{data: { 
				identifier: 'Collateral',
				items: selected}
			});

	//update grid
	ls.grid.setStore(newStore);
}

function initFilters() {
	// Core Logic Fraud Risks
	var min = Array.min(ls.coreLogicFraudRisk);
	var max = Array.max(ls.coreLogicFraudRisk);
	var CoreLogicFraudRiskRangeSlider = new dojox.form.HorizontalRangeSlider({
		name : "CoreLogic Fraud Risk",
		value : [ min, max ],
		minimum : min,
		maximum : max,
		intermediateChanges : true,
		style : "width:300px;",
		onChange : function(value) {
			var func = function(item, obj) {
				var val = item[obj.field][0];
				return (val > obj.min) && (val < obj.max);
			};
			var condition = new ls.Condition({
				field : 'CoreLogic Fraud Risk Score',
				min : value[0],
				max : value[1]
			});
			condition.setSatisfy(func);
			ls.conditions['CoreLogic Fraud Risk'] = condition;
			dojo.byId("CoreLogicFraudRiskRange").innerHTML = "[" + dojo.number.format(value[0],{fractional:false,type:'decimal'}) + " - " +
			 dojo.number.format(value[1],{fractional:false,type:'decimal'}) + "]";
		}
	}, "CoreLogicFraudRiskRangeSlider");

	// Core Logic Collateral Risk
	var min = Array.min(ls.coreLogicCollateralRisk);
	var max = Array.max(ls.coreLogicCollateralRisk);
	var CoreLogicCollateralRiskRangeSlider = new dojox.form.HorizontalRangeSlider(
			{
				name : "CoreLogic Collateral Risk",
				value : [ min, max ],
				minimum : min,
				maximum : max,
				intermediateChanges : true,
				style : "width:300px;",
				onChange : function(value) {
					var func = function(item, obj) {
						var val = item[obj.field][0];
						return (val > obj.min) && (val < obj.max);
					};
					var condition = new ls.Condition({
						field : 'CoreLogic Collateral Risk Score',
						min : value[0],
						max : value[1]
					});
					condition.setSatisfy(func);
					ls.conditions['CoreLogic Collateral Risk Score'] = condition;
					dojo.byId("CoreLogicCollateralRiskRange").innerHTML = "[" + dojo.number.format(value[0],{fractional:false,type:'decimal'}) + " - " +
					 dojo.number.format(value[1],{fractional:false,type:'decimal'}) + "]";
				}
			}, "CoreLogicCollateralRiskRangeSlider");
	
	// Acceptable FICO range
	var min = Array.min(ls.fico);
	var max = Array.max(ls.fico);
	var ficoRangeSlider = new dojox.form.HorizontalRangeSlider(
			{
				name : "Acceptable FICO range",
				value : [ min, max ],
				minimum : min,
				maximum : max,
				intermediateChanges : true,
				style : "width:300px;",
				onChange : function(value) {
					var func = function(item, obj) {
						var val = item[obj.field][0];
						return (val > obj.min) && (val < obj.max);
					};
					var condition = new ls.Condition({
						field : 'FICO Score',
						min : value[0],
						max : value[1]
					});
					condition.setSatisfy(func);
					ls.conditions['FICO Score'] = condition;
					dojo.byId("ficoRange").innerHTML = "[" + dojo.number.format(value[0],{fractional:false,type:'decimal'}) + " - " +
															 dojo.number.format(value[1],{fractional:false,type:'decimal'}) + "]";
					
				}
			}, "ficoRangeSlider");
	// Loan Amount (minimum)
	var props = {
            name: "minLoanAmount",
            style: 'width:100px;',
            label :"Loan Amount (minimum)",
            constraints: {pattern: "#,##0.##"},
			onChange: function(value){
				if (this.State == 'Error') return;
				if (!value){
					delete ls.conditions['Current UPB_min'];
					return;
				}
				var func = function(item, obj) {
					var val = item[obj.field][0];
					return (val > obj.value);
				};
				var condition = new ls.Condition({
					field : 'Current UPB',
					value: value
				});
				condition.setSatisfy(func);
				ls.conditions['Current UPB_min'] = condition;
			}
        };
	var minLoanAmount = new dijit.form.NumberTextBox(props,"minLoanAmount");
	
	// Loan Amount (maximum)
	var props = {
            name: "maxLoanAmount",
            style: 'width:100px;',
            label :"Loan Amount (maximum)",
            constraints: {pattern: "#,##0.##"},
    		onChange: function(value){
				if (this.State == 'Error') return;
				if (!value){
					delete ls.conditions['Current UPB_max'];
					return;
				}

				var func = function(item, obj) {
					var val = item[obj.field][0];
					return (val < obj.value);
				};
				var condition = new ls.Condition({
					field : 'Current UPB',
					value: value
				});
				condition.setSatisfy(func);
				ls.conditions['Current UPB_max'] = condition;
			}
        };
	var maxLoanAmount = new dijit.form.NumberTextBox(props,"maxLoanAmount");
	
	// Maximum Loan to Value(LTV)
	var props = {
            name: "maxLTV",
            style: 'width:100px;',
            label :"Maximum LTV",
            constraints: {pattern: "#00.00"},
    		onChange: function(value){
				if (this.State == 'Error') return;
				if (!value){
					delete ls.conditions['Original LTV'];
					return;
				}
				var func = function(item, obj) {
					var val = item[obj.field][0];
					return (val < obj.value);
				};
				var condition = new ls.Condition({
					field : 'Original LTV',
					value: value
				});
				condition.setSatisfy(func);
				ls.conditions['Original LTV_max'] = condition;
			}
        };
	var maxLTV = new dijit.form.NumberTextBox(props,"maxLTV");

	// Maximum Combined Loan to Value(CLTV)
	var props = {
            name: "maxCLTV",
            style: 'width:100px;',
            label :"Maximum Combined LTV",
            constraints: {pattern: "#00.00"},
    		onChange: function(value){
				if (this.State == 'Error') return;
				if (!value){
					delete ls.conditions['Original CLTV_max'];
					return;
				}
				var func = function(item, obj) {
					var val = item[obj.field][0];
					return (val < obj.value);
				};
				var condition = new ls.Condition({
					field : 'Original CLTV',
					value: value
				});
				condition.setSatisfy(func);
				ls.conditions['Original CLTV_max'] = condition;
			}
        };
	var maxLTV = new dijit.form.NumberTextBox(props,"maxCLTV");

	// Maximum Advance %
	var props = {
            name: "maxAdvance",
            style: 'width:100px;',
            label :"Max Advance %",
            constraints: {pattern: "#00.00"},
    		onChange: function(value){
				if (this.State == 'Error') return;
				if (!value){
					delete ls.conditions['Advance'];
					return;
				}
				var func = function(item, obj) {
					var val = item[obj.field][0];
					return (val < obj.value);
				};
				var condition = new ls.Condition({
					field : 'Advance',
					value: value/100
				});
				condition.setSatisfy(func);
				ls.conditions['Advance'] = condition;
			}
        };
	var maxAdvPercentace = new dijit.form.NumberTextBox(props,"maxAdv");
	
	// Lien Type
	var labels = {'1':'First','2':'Second'};
	var lienTypes = distinct(ls.lienType);
	var lienOptions = lienTypes.map(function(item){
		return {value : item, label : labels[item] }
	});
	lienOptions.push({value: '3', label:'First and Second'});
    var select = new dijit.form.Select({
        name: "lienType",
        options: lienOptions,
        style: "width: 170px;",
        value: '3',
        onChange: function(value){
			var func = function(item, obj) {
				var val = item[obj.field][0];
				if (obj.value == '3'){
					return true;
				}else{
					return (val == obj.value);					
				}

			};
			var condition = new ls.Condition({
				field : 'Lien Position',
				value: value
			});
			condition.setSatisfy(func);
			ls.conditions['Lien Position'] = condition;        	
        }
    }, "lienType");
    select.startup();
    
    //Loan Types
    createCheckboxGroup('Is Adjustable',["0","1"],'loanType',{'0':'FIXED', '1':'ARM'});
    
    //Property Types
    createCheckboxGroup('Property Type Code',["SFR","PUD","CONDO","TOWNHOUSE","MANUFACTURED"],'propertyType');
    
    //States
    createCheckboxGroup('State', 
    		["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    		 "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    		 "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"],
    		 'states');
        
}

function createCheckboxGroup(name,options,parentNode,labelMap){
	var node = dojo.create("div", { id:name},parentNode);
	ls.checkboxGroups[name]={};
	for (var i=0; i<options.length; i++){
		createCheckbox(name,options[i],(labelMap ? labelMap[options[i]] : undefined));
	}
}

function createCheckbox(group,option, label){
	var name = (label ? label : option);
	var node = dojo.create("span", { innerHTML:'&nbsp;' + name + '&nbsp;'},dojo.byId(group));
	var node = dojo.create("div", { id:option},dojo.byId(group));
	var checkBox = new dijit.form.CheckBox({
        name: option,
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.checkboxGroups[group][option]=true;
        	else{
        		delete ls.checkboxGroups[group][option];
        		if (isEmpty(ls.checkboxGroups[group])){
	        		delete ls.conditions[group];
	        		return;
	        	}
        	}
			var func = function(item, obj) {
				var val = item[group][0];
				if(ls.checkboxGroups[group][val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions[group] = condition;        	
        }
      },node);
}


function extractField(item){
	return item[this.field][0];
}

function distinct(items) {
	var check = {};
	return items.filter(function(item) {
		var id = item[0];
		if (check[id])
			return false;
		return check[id] = true;
	});
}


//filterFunc has to apply all the conditions that determine if item should be filtered.
//An "apply filter" button will call filterGrid
//need to write a function that will create filterFunc based on the various filter selections.

//function updateGride(datastore){
//	var newStore = new dojo.data.ItemFileReadStore({data: {... some data ...});
//	var grid = dijit.byId("gridId");
//	grid.setStore(newStore);
//}

function createGrid(dataStore) {
	// set the layout structure:
	var layout = [ [ {
		'name' : 'Collateral Key',
		'field' : 'Collateral',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	}, {
		'name' : 'Property Type',
		'field' : 'Property Type Code',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	}, {
		'name' : 'State',
		'field' : 'State',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	}, {
		'name' : 'Loan Type',
		'field' : 'Is Adjustable',
		'width' : 'auto',
		'formatter': function(item){
			var names = {'0':'FIXED','1':'ARM'};
			return names[item];
			},
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},{
		'name' : 'Lien Type',
		'field' : 'Lien Position',
		'width' : 'auto',
		'formatter': function(item){
			var names = {'1':'FIRST','2':'SECOND'};
			return names[item];
			},		
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},{
		'name' : 'Max LTV',
		'field' : 'Original LTV',
		'width' : 'auto',
		'formatter': function(item){
			return dojo.number.format(item,{pattern: "#00.00"});
			},
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},{
		'name' : 'Max CLTV',
		'field' : 'Original CLTV',
		'width' : 'auto',
		'formatter': function(item){
			return dojo.number.format(item,{pattern: "#00.00"});
			},
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},
	{
		'name' : 'Loan Amount',
		'field' : 'Current UPB',
		'width' : 'auto',
		'formatter': function(item){
			return dojo.number.format(item,{pattern:'#,##0.##'});
			},
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},
	{
		'name' : 'Advance %',
		'field' : 'Advance',
		'width' : 'auto',
		'formatter': function(item){
			return dojo.number.format(item,{pattern:'#%'});
			},		
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},
	{
		'name' : 'CoreLogic Collateral Risk',
		'field' : 'CoreLogic Collateral Risk Score',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},{
		'name' : 'CoreLogic Fraud Risk',
		'field' : 'CoreLogic Fraud Risk Score',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	},{
		'name' : 'FICO',
		'field' : 'FICO Score',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles': 'text-align: center;'
	} ] ];
	
	
//	/*programmatic menus*/
//    var menusObject = {
//        rowMenu: new dijit.Menu(),
//    };
//
//    menusObject.rowMenu.addChild(new dijit.MenuItem({label: "Show loan details"}));
//    menusObject.rowMenu.addChild(new dijit.MenuItem({label: "Select loan"}));
//    menusObject.rowMenu.startup();	
	
	ls.grid = new dojox.grid.EnhancedGrid({
		query: {'Collateral':'*'},
		store : dataStore,
		clientSort : true,
		rowSelector : '20px',
		structure : layout,
		columnReordering: true,
		selectionMode: 'multiple',
		onRowContextMenu: showLoanDetails
//		plugins: {menus: menusObject},
	}, document.createElement('div'));
	
	dojo.connect(ls.grid, "onRowContextMenu", showLoanDetails);

	// append the new grid to the div "grid":
	dojo.byId("grid").appendChild(ls.grid.domNode);

	// Call startup, in order to render the grid:
	ls.grid.startup();
}

function showLoanDetails(e){
	var item = e.grid.getItem(e.rowIndex);
	dijit.showTooltip(tooltipMarkup(item),e.srcElement);
	
	if (dijit.byId('closeButton'))
		dijit.byId('closeButton').destroy();
	
	var button = new dijit.form.Button({
	        label: "Close",
	        onClick: function(){
	        	dijit.byId('dijit__MasterTooltip_0').domNode.style.cssText = '';//Ugly, should be better way!
	        }
	    }, "closeButton");
}


function tooltipMarkup(item){
	var html = "<button id='closeButton'></button>";
	html += "<table>";
	for (prop in item){
		if (item.hasOwnProperty(prop) && (prop.search("^_.*") == -1)){
			html += "<tr><td>" + prop + ": " + item[prop] + "</td></tr>";
		}
	}
	html += "</table>";
	return html;
}


Array.max = function( array ){
    return Math.max.apply( Math, array );
};
Array.min = function( array ){
    return Math.min.apply( Math, array );
};

function isEmpty(map) {
	for(var key in map) {
		if (map.hasOwnProperty(key)) {
			return false;
		}
		return true;
	}
	return true;
}