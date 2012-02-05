
//application namespace
var ls={};
ls.conditions={};
ls.convertFunctions={};
ls.fullData=[];
ls.selectedLoanType = {};
ls.selectedPropertyType = {};
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
            constraints: {pattern: "#00.00%"},
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
					value: value
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
    
    //Loan Type
    var loanTypeFixedCheckBox = new dijit.form.CheckBox({
        name: "fixed",
        value: "fixed",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['0']=true;
        	else
        		delete selectedLoanType['0'];
        	
			var func = function(item, obj) {
				var val = item['Is Adjustable'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Is Adjustable'] = condition;        	
        }
    }, "fixed");
    
    var loanTypeARMCheckBox = new dijit.form.CheckBox({
        name: "ARM",
        value: "ARM",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['1']=true;
        	else
        		delete selectedLoanType['1'];
        	
			var func = function(item, obj) {
				var val = item['Is Adjustable'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Is Adjustable'] = condition;        	
        }
      }, "ARM");
    
    var loanTypeHybridCheckBox = new dijit.form.CheckBox({
        name: "hybrid",
        value: "hybrid",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['2']=true;
        	else
        		delete selectedLoanType['2'];
        	
			var func = function(item, obj) {
				var val = item['Is Adjustable'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Is Adjustable'] = condition;        	
        }
      }, "hybrid");
    
    //Property Type
    var propertyTypeSFRCheckBox = new dijit.form.CheckBox({
        name: "sfr",
        value: "SFR",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['SFR']=true;
        	else
        		delete selectedLoanType['SFR'];
        	
			var func = function(item, obj) {
				var val = item['Property Type Code'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Property Type Code'] = condition;        	
        }
      }, "sfr");
    
    var propertyTypeHUDCheckBox = new dijit.form.CheckBox({
        name: "PUD",
        value: "pud",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['PUD']=true;
        	else
        		delete selectedLoanType['PUD'];
        	
			var func = function(item, obj) {
				var val = item['Property Type Code'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Property Type Code'] = condition;        	
        }
      }, "pud");
    
    var propertyTypeCondoCheckBox = new dijit.form.CheckBox({
        name: "condo",
        value: "condo",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['CONDO']=true;
        	else
        		delete selectedLoanType['CONDO'];
        	
			var func = function(item, obj) {
				var val = item['Property Type Code'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Property Type Code'] = condition;        	
        }
      }, "condo");
    var propertyTypeTownhouseCheckBox = new dijit.form.CheckBox({
        name: "townhouse",
        value: "townhouse",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['TOWNHOUSE']=true;
        	else
        		delete selectedLoanType['TOWNHOUSE'];
        	
			var func = function(item, obj) {
				var val = item['Property Type Code'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Property Type Code'] = condition;        	
        }
      }, "townhouse");
    var propertyTypeManufacturedCheckBox = new dijit.form.CheckBox({
        name: "manufactured",
        value: "manufactured",
        checked: false,
        onChange: function(value){
        	if (value)
        		ls.selectedLoanType['MANUFACTURED']=true;
        	else
        		delete selectedLoanType['MANUFACTURED'];
        	
			var func = function(item, obj) {
				var val = item['Property Type Code'][0];
				if(ls.selectedLoanType[val]){
					return true;
				}					
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions['Property Type Code'] = condition;        	
        }
      }, "manufactured");
    
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
		'width' : 'auto'
	}, {
		'name' : 'Property Type',
		'field' : 'Property Type Code',
		'width' : 'auto'
	}, {
		'name' : 'State',
		'field' : 'State',
		'width' : 'auto'
	}, {
		'name' : 'Loan Type',
		'field' : 'Is Adjustable',
		'width' : 'auto'
	},{
		'name' : 'Lien Type',
		'field' : 'Lien Position',
		'width' : 'auto'
	},{
		'name' : 'Max LTV',
		'field' : 'Original LTV',
		'width' : 'auto'
	},{
		'name' : 'Max CLTV',
		'field' : 'Original CLTV',
		'width' : 'auto'
	},
	{
		'name' : 'Loan Amount',
		'field' : 'Current UPB',
		'width' : 'auto'
	},
	{
		'name' : 'Advance %',
		'field' : 'Advance',
		'width' : 'auto'
	},
	{
		'name' : 'CoreLogic Collateral Risk',
		'field' : 'CoreLogic Collateral Risk Score',
		'width' : 'auto'
	},{
		'name' : 'CoreLogic Fraud Risk',
		'field' : 'CoreLogic Fraud Risk Score',
		'width' : 'auto'
	},{
		'name' : 'FICO',
		'field' : 'FICO Score',
		'width' : 'auto'
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

Array.max = function( array ){
    return Math.max.apply( Math, array );
};
Array.min = function( array ){
    return Math.min.apply( Math, array );
};
function stringArrayToIntArray(array){
	return array.map(function(item){return parseInt(item);});
}

function stringArrayToFloatArray(array){
	return array.map(function(item){return parseFloat(item);});
}
