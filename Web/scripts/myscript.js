//application namespace
var ls = {};
ls.conditions = {};
ls.convertFunctions = {};
ls.fullData = [];
ls.selectedLoanType = {};
ls.selectedPropertyType = {};
ls.checkboxGroups = {};

dojo.addOnLoad(function() {
	//Get field labels
	initFieldLabels();
	//Get data
	ls.dataStore = new dojo.data.ItemFileReadStore({
		identifier : 'Collateral',
		url : "/jsonLoans"
	});
	ls.dataStore.fetch({
		query : {
			'collateral_key' : '*'
		},
		onComplete : function(items) {
			ls.fullData = items;
			//Create grid
			createGrid(ls.dataStore);
			//extract columns for filters
			ls.states = items.map(extractField, {
				field : 'state'
			});
			ls.propertyType = items.map(extractField, {
				field : 'property_type_code'
			});
			ls.loanType = items.map(extractField, {
				field : 'is_adjustable'
			});
			ls.lienType = items.map(extractField, {
				field : 'lien_position'
			});
			ls.maxLTV = items.map(extractField, {
				field : 'original_ltv'
			});
			ls.maxCLTV = items.map(extractField, {
				field : 'original_cltv'
			});
			ls.loanAmount = items.map(extractField, {
				field : 'curr_upb'
			});
			ls.coreLogicCollateralRisk = items.map(extractField, {
				field : 'CoreLogic Collateral Risk Score'
			});
			ls.coreLogicFraudRisk = items.map(extractField, {
				field : 'CoreLogic Fraud Risk Score'
			});
			ls.fico = items.map(extractField, {
				field : 'fico_score'
			});
			ls.advanceAmount = items.map(extractField, {
				field : 'advance_amt'
			});
			//Filters
			initFilters();
			initBidsDialog();
			initBidsGrid();
			//init loand details dialog
			ls.loanDetailsDialog = new dijit.Dialog({
				id : "loanDetailsDialog",
				autofocus : false
			});
			var html = "<div style='width: 350px; height: 500px;'dojoType='dijit.layout.ContentPane'><div id='loanDetailsGrid'></div></div>";
			ls.loanDetailsDialog.set("content", html);
			ls.loanDetailsDialog.set("title", 'Loan Details');
			initLoanDetailsGrid();
		}
	});
});
function initBidsDialog() {
	ls.bidDialog = new dijit.Dialog({
		id : "bidDialog",
		autofocus : false
	});
	var html = "<div style='width: 850px; height: 900px;overflow:hidden;'dojoType='dijit.layout.ContentPane'>" + "<div id='bidGrid'></div></br>" + "<div id='globalbid' style='margin:auto; text-align: center; width:800px; background-color: #EBF1F6;padding: 5px; border-color: #DBDBDB; border-style: solid; border-width: 5px;'>" + "&nbsp;&nbsp;&nbsp;&nbsp;Participation %&nbsp;<div id = 'globalParticipationTxBx'></div>&nbsp;&nbsp;" + "Bid Rate&nbsp;<div id = 'globalBidRateTxBx'></div>" + "&nbsp;&nbsp;&nbsp;&nbsp;" + "<button dojoType='dijit.form.Button' id='submitBids' onClick='submitBidsClick'>Place bids</button>" + "</div>" + "</div>"; "</div>";
	ls.bidDialog.set("content", html);
	ls.bidDialog.set("title", 'Place Bids');
	genericCreateCheckbox('globalbidChkBx', 'Apply to All', 'globalbid', 'first', function(value) {
		var grid = dijit.byId("bidGrid");
		if(value) {
			applyGlobalBid();
			for(var row = 0; row < grid.rowCount; row++) {
				grid.selection.setSelected(row, true);
			}
		} else
			grid.selection.clear();
	});
	var props = {
		style : 'width:100px;',
		label : "Participation",
		constraints : {
			pattern : "#0.0"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			dijit.byId('globalbidChkBx').set('checked', true);
			applyGlobalBid(value);
		}
	};
	var bidRateTxtBox = new dijit.form.NumberTextBox(props, "globalParticipationTxBx");

	var props = {
		style : 'width:100px;',
		label : "Bid Rate",
		constraints : {
			pattern : "#0.0"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			dijit.byId('globalbidChkBx').set('checked', true);
			applyGlobalBid(value);
		}
	};
	var bidRateTxtBox = new dijit.form.NumberTextBox(props, "globalBidRateTxBx");
}

function applyGlobalBid() {
	var globalParticipation = dijit.byId('globalParticipationTxBx').get("value");
	var globalBidRate = dijit.byId('globalBidRateTxBx').get("value");

	var store = ls.bidGrid.store;
	store.fetch({
		onComplete : function(items) {
			for(var i = 0; i < items.length; i++) {
				if(globalParticipation)
					store.setValue(items[i], 'participation', globalParticipation);
				if(globalBidRate)
					store.setValue(items[i], 'bidrate', globalBidRate);
			}
		}
	});
}

function initBidsGrid() {
	bidData = {
		items : []
	};
	var bidStore = new dojo.data.ItemFileWriteStore({
		data : bidData
	});
	// set the layout structure:
	var layout = [[{
		'name' : ls.labels['collateral_key'],
		'field' : 'collateral_key',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['curr_upb'],
		'field' : 'curr_upb',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;',
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : '#,##0.##'
			});
		}
	}, {
		'name' : 'Participation %',
		'field' : 'participation',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;',
		'editable' : 'true',
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : "#0.0"
			});
		}
	}, {
		'name' : 'Bid Rate',
		'field' : 'bidrate',
		'width' : 'auto',
		'formatter' : '',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;',
		'editable' : 'true',
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : "#0.0"
			});
		}
	}]];

	ls.bidGrid = new dojox.grid.EnhancedGrid({
		store : bidStore,
		clientSort : true,
		rowSelector : '20px',
		structure : layout,
		selectionMode : 'multiple',
		height : '400px'
	}, 'bidGrid');
	ls.bidGrid.startup();
	dojo.connect(ls.bidGrid, "onApplyCellEdit", function(val, row, col) {
		ls.bidGrid.selection.setSelected(row, true);
	});
}

function submitBidsClick() {
	var selectedBids = ls.bidGrid.selection.getSelected();
	var bids = {};
	for(var i = 0; i < selectedBids.length; i++) {
		bids[selectedBids[i]['collateral_key']] = {
			'collateral_key' : selectedBids[i]['collateral_key'][0],
			'participation' : selectedBids[i]['participation'][0],
			'bidrate' : selectedBids[i]['bidrate'][0]
		};
	}
	dijit.byId('bidDialog').hide();

	var xhrArgs = {
		url : "/bids",
		content : {
			'bids' : dojo.toJson(bids)
		},
		handleAs : "json",
		load : function(data) {
			console.log(data);
		},
		error : function(error) {
			console.log(error);
		}
	};
	//Call the asynchronous xhrPost
	var deferred = dojo.xhrPost(xhrArgs);
}

//this is mapped into the imported items. The "this" holds information on the data types that should be applied.
function adjustDataType(item) {
	for(field in item) {
		if(item.hasOwnProperty(field)) {
			if(this[field]) {
				item[field] = [this[field](item[field])];
				//replace old with new type
			}
		}
	}
	return item;
}

//This is 'mapped' into an array. Additional information (conditions) accessible in "this"
function filterFunc(item) {
	var selected = true;
	for(var condition in this) {
		selected = selected && this[condition].satisfy(item);
	}
	return selected;
}

function findMyAssetsClick() {
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
	var selectedLoans = ls.grid.selection.getSelected();	
	if (selectedLoans.length){
		var loansData = extractLoansData(selectedLoans),
			loansDataJson = dojo.toJson(loansData),
			dummyForm = dojo.byId('downloadForm'),
			keysPlaceHolder = dojo.byId('downloadInfo');
		dummyForm.action = '/download';
		keysPlaceHolder.value = loansDataJson;
		dummyForm.submit();
		keysPlaceHolder.value = '';
	} else {
		new dijit.Dialog({
    			title: "No loans selected",
    			content: "You did not select any loan"
		}).show();
	}
}

function extractLoansData(selectedLoans) {
	var headers = [], firstLoan = true, loanData, loansData = [];
	if(selectedLoans.length) {
		dojo.forEach(selectedLoans, function(selectedLoan) {
			if(selectedLoan !== null) {
				loanData = []
				dojo.forEach(ls.grid.store.getAttributes(selectedLoan), function(attribute) {
					var value = ls.grid.store.getValue(selectedLoan, attribute),
						label = ls.labels[attribute];
					if(firstLoan) {
						headers.push(label ? label : attribute);
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
		// removing some dojo internal attributes
		for(var i = 0; i < loansData.length; i++) {
			loansData[i].length -= 2;
		}
	}
	return loansData;
}

function updateBidGrid(selectedLoans) {
	for(var i = 0; i < selectedLoans.length; i++) {
		dojo.mixin(selectedLoans[i], {
			'participation' : [0.0],
			'bidrate' : [0.0]
		});
	}
	// Create new datastore with selected items only
	var bidStore = new dojo.data.ItemFileWriteStore({
		data : {
			items : selectedLoans
		}
	});

	ls.bidGrid.setStore(bidStore);
}

function applyFilters() {
	//Find selected items
	var selected = ls.fullData.filter(filterFunc, ls.conditions);
	dojo.byId('loanCount').innerHTML = selected.length + ' loans match your criteria.';

	// Create new datastore with selected items only
	var newStore = new dojo.data.ItemFileReadStore({
		data : {
			items : selected
		}
	});

	//update grid
	ls.grid.setStore(newStore);
}

function initFilters() {
	// Core Logic Fraud Risks
	var min = Array.min(ls.coreLogicFraudRisk);
	var max = Array.max(ls.coreLogicFraudRisk);
	var CoreLogicFraudRiskRangeSlider = new dojox.form.HorizontalRangeSlider({
		name : ls.labels["CoreLogic Fraud Risk"],
		value : [min, max],
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
			dojo.byId("CoreLogicFraudRiskRange").innerHTML = "[" + dojo.number.format(value[0], {
				fractional : false,
				type : 'decimal'
			}) + " - " + dojo.number.format(value[1], {
				fractional : false,
				type : 'decimal'
			}) + "]";
		}
	}, "CoreLogicFraudRiskRangeSlider");

	// Core Logic Collateral Risk
	var min = Array.min(ls.coreLogicCollateralRisk);
	var max = Array.max(ls.coreLogicCollateralRisk);
	var CoreLogicCollateralRiskRangeSlider = new dojox.form.HorizontalRangeSlider({
		name : ls.labels["CoreLogic Collateral Risk"],
		value : [min, max],
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
			dojo.byId("CoreLogicCollateralRiskRange").innerHTML = "[" + dojo.number.format(value[0], {
				fractional : false,
				type : 'decimal'
			}) + " - " + dojo.number.format(value[1], {
				fractional : false,
				type : 'decimal'
			}) + "]";
		}
	}, "CoreLogicCollateralRiskRangeSlider");

	// Acceptable FICO range
	var min = Array.min(ls.fico);
	var max = Array.max(ls.fico);
	var ficoRangeSlider = new dojox.form.HorizontalRangeSlider({
		name : "Acceptable FICO range",
		value : [min, max],
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
				field : 'fico_score',
				min : value[0],
				max : value[1]
			});
			condition.setSatisfy(func);
			ls.conditions['fico_score'] = condition;
			dojo.byId("ficoRange").innerHTML = "[" + dojo.number.format(value[0], {
				fractional : false,
				type : 'decimal'
			}) + " - " + dojo.number.format(value[1], {
				fractional : false,
				type : 'decimal'
			}) + "]";

		}
	}, "ficoRangeSlider");
	// Loan Amount (minimum)
	var props = {
		name : "minLoanAmount",
		style : 'width:100px;',
		label : "Loan Amount (minimum)",
		constraints : {
			pattern : "#,##0.##"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			if(!value) {
				delete ls.conditions['curr_upb_min'];
				return;
			}
			var func = function(item, obj) {
				var val = item[obj.field][0];
				return (val > obj.value);
			};
			var condition = new ls.Condition({
				field : 'curr_upb',
				value : value
			});
			condition.setSatisfy(func);
			ls.conditions['curr_upb_min'] = condition;
		}
	};
	var minLoanAmount = new dijit.form.NumberTextBox(props, "minLoanAmount");

	// Loan Amount (maximum)
	var props = {
		name : "maxLoanAmount",
		style : 'width:100px;',
		label : "Loan Amount (maximum)",
		constraints : {
			pattern : "#,##0.##"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			if(!value) {
				delete ls.conditions['curr_upb_max'];
				return;
			}

			var func = function(item, obj) {
				var val = item[obj.field][0];
				return (val < obj.value);
			};
			var condition = new ls.Condition({
				field : 'curr_upb',
				value : value
			});
			condition.setSatisfy(func);
			ls.conditions['curr_upb_max'] = condition;
		}
	};
	var maxLoanAmount = new dijit.form.NumberTextBox(props, "maxLoanAmount");

	// Maximum Loan to Value(LTV)
	var props = {
		name : "maxLTV",
		style : 'width:100px;',
		label : "Maximum LTV",
		constraints : {
			pattern : "#00.00"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			if(!value) {
				delete ls.conditions['original_ltv'];
				return;
			}
			var func = function(item, obj) {
				var val = item[obj.field][0];
				return (val < obj.value);
			};
			var condition = new ls.Condition({
				field : 'original_ltv',
				value : value
			});
			condition.setSatisfy(func);
			ls.conditions['original_ltv_max'] = condition;
		}
	};
	var maxLTV = new dijit.form.NumberTextBox(props, "maxLTV");

	// Maximum Combined Loan to Value(CLTV)
	var props = {
		name : "maxCLTV",
		style : 'width:100px;',
		label : "Maximum Combined LTV",
		constraints : {
			pattern : "#00.00"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			if(!value) {
				delete ls.conditions['original_cltv_max'];
				return;
			}
			var func = function(item, obj) {
				var val = item[obj.field][0];
				return (val < obj.value);
			};
			var condition = new ls.Condition({
				field : 'original_cltv',
				value : value
			});
			condition.setSatisfy(func);
			ls.conditions['original_cltv_max'] = condition;
		}
	};
	var maxLTV = new dijit.form.NumberTextBox(props, "maxCLTV");

	// Maximum Advance %
	var props = {
		name : "maxAdvance",
		style : 'width:100px;',
		label : "Max Advance %",
		constraints : {
			pattern : "#00.00"
		},
		onChange : function(value) {
			if(this.State == 'Error')
				return;
			if(!value) {
				delete ls.conditions['advance_amt'];
				return;
			}
			var func = function(item, obj) {
				var val = item['advance_amt'][0]/item['curr_upb'][0];
				return (val < obj.value);
			};
			var condition = new ls.Condition({
				field : 'advance_amt',
				value : value / 100
			});
			condition.setSatisfy(func);
			ls.conditions['advance_amt'] = condition;
		}
	};
	var maxAdvPercentace = new dijit.form.NumberTextBox(props, "maxAdv");

	// Lien Type
	var labels = {
		'1' : 'First',
		'2' : 'Second'
	};
	var lienTypes = distinct(ls.lienType);
	var lienOptions = lienTypes.map(function(item) {
		return {
			value : item,
			label : labels[item]
		}
	});
	lienOptions.push({
		value : '3',
		label : 'First and Second'
	});
	var select = new dijit.form.Select({
		name : "lienType",
		options : lienOptions,
		style : "width: 170px;",
		value : '3',
		onChange : function(value) {
			var func = function(item, obj) {
				var val = item[obj.field][0];
				if(obj.value == '3') {
					return true;
				} else {
					return (val == obj.value);
				}

			};
			var condition = new ls.Condition({
				field : 'lien_position',
				value : value
			});
			condition.setSatisfy(func);
			ls.conditions['lien_position'] = condition;
		}
	}, "lienType");
	select.startup();

	//Loan Types
	createCheckboxGroup('is_adjustable', ["0", "1"], 'loanType', {
		'0' : 'FIXED',
		'1' : 'ARM'
	});

	//Property Types
	createCheckboxGroup('property_type_code', ["SFR", "PUD", "CONDO", "TOWNHOUSE", "MANUFACTURED"], 'propertyType');

	//States
	createCheckboxGroup('state', ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"], 'states');

}

function createCheckboxGroup(name, options, parentNode, labelMap) {
	var node = dojo.create("div", {
		id : name
	}, parentNode);
	var table = dojo.create("table", {}, node);
	var tr = dojo.create("tr", {}, table);
	var maxColsPerRow = 12;
	var colsPerRow = 0;
	ls.checkboxGroups[name] = {};
	for(var i = 0; i < options.length; i++) {
		if(colsPerRow < maxColsPerRow) {
			colsPerRow++;
			var td = dojo.create("td", {
				'style' : 'text-align:right;'
			}, tr);
			createCheckbox(name, options[i], ( labelMap ? labelMap[options[i]] : undefined), td);
		} else {
			colsPerRow = 0;
			tr = dojo.create("tr", {}, table);
		}
	}
}

function genericCreateCheckbox(option, label, parentNode, position, onchange) {
	var name = ( label ? label : option);
	if(position) {
		var label = dojo.create("span", {
			innerHTML : '&nbsp;' + name + '&nbsp;'
		}, parentNode, position);
		var chkboxdiv = dojo.create("div", {
			id : option
		}, parentNode, position);
	} else {
		var label = dojo.create("span", {
			innerHTML : '&nbsp;' + name + '&nbsp;'
		}, parentNode);
		var chkboxdiv = dojo.create("div", {
			id : option
		}, parentNode);
	}
	var checkBox = new dijit.form.CheckBox({
		name : option,
		checked : false,
		onChange : onchange
	}, option);
}

function createCheckbox(group, option, label, parentNode, position, onchange) {
	var name = ( label ? label : option);
	if(position) {
		var label = dojo.create("span", {
			innerHTML : '&nbsp;' + name + '&nbsp;'
		}, parentNode, position);
		var chkboxdiv = dojo.create("div", {
			id : option
		}, parentNode, position);
	} else {
		var label = dojo.create("span", {
			innerHTML : '&nbsp;' + name + '&nbsp;'
		}, parentNode);
		var chkboxdiv = dojo.create("div", {
			id : option
		}, parentNode);
	}
	var checkBox = new dijit.form.CheckBox({
		name : option,
		checked : false,
		onChange : function(value) {
			if(value)
				ls.checkboxGroups[group][option] = true;
			else {
				delete ls.checkboxGroups[group][option];
				if(isEmpty(ls.checkboxGroups[group])) {
					delete ls.conditions[group];
					return;
				}
			}
			var func = function(item, obj) {
				var val = item[group][0];
				if(ls.checkboxGroups[group][val]) {
					return true;
				}
			};
			var condition = new ls.Condition();
			condition.setSatisfy(func);
			ls.conditions[group] = condition;
		}
	}, chkboxdiv);
}

function extractField(item) {
	return item[this.field][0];
}

function distinct(items) {
	var check = {};
	return items.filter(function(item) {
		var id = item[0];
		if(check[id])
			return false;
		return check[id] = true;
	});
}

function createGrid(dataStore) {
	// set the layout structure:
	var layout = [[{
		'name' : ls.labels['collateral_key'],
		'field' : 'collateral_key',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['property_type_code'],
		'field' : 'property_type_code',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['state'],
		'field' : 'state',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['is_adjustable'],
		'field' : 'is_adjustable',
		'width' : 'auto',
		'formatter' : function(item) {
			var names = {
				'0' : 'FIXED',
				'1' : 'ARM'
			};
			return names[item];
		},
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['lien_position'],
		'field' : 'lien_position',
		'width' : 'auto',
		'formatter' : function(item) {
			var names = {
				'1' : 'FIRST',
				'2' : 'SECOND'
			};
			return names[item];
		},
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['original_ltv'],
		'field' : 'original_ltv',
		'width' : 'auto',
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : "#00.00"
			});
		},
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['original_cltv'],
		'field' : 'original_cltv',
		'width' : 'auto',
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : "#00.00"
			});
		},
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['curr_upb'],
		'field' : 'curr_upb',
		'width' : 'auto',
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : '#,##0.##'
			});
		},
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : 'Advance %',
		'field' : 'advance_amt',
		'width' : 'auto',
		'get' : getAdvancePercent,
		'formatter' : function(item) {
			return dojo.number.format(item, {
				pattern : '#%'
			});
		},
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['CoreLogic Collateral Risk Score'],
		'field' : 'CoreLogic Collateral Risk Score',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['CoreLogic Fraud Risk Score'],
		'field' : 'CoreLogic Fraud Risk Score',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}, {
		'name' : ls.labels['fico_score'],
		'field' : 'fico_score',
		'width' : 'auto',
		'cellStyles' : 'text-align: center;',
		'headerStyles' : 'text-align: center;'
	}]];

	ls.grid = new dojox.grid.EnhancedGrid({
		query : {
			'collateral_key' : '*'
		},
		store : dataStore,
		clientSort : true,
		structure : layout,
		columnReordering : true
	}, document.createElement('div'));

	dojo.connect(ls.grid, "onRowContextMenu", showLoanDetails);

	// append the new grid to the div "grid":
	dojo.byId("grid").appendChild(ls.grid.domNode);

	// Call startup, in order to render the grid:
	ls.grid.startup();

}

function getAdvancePercent(rowIndex, item) {
	if(item != null) {
		return item.advance_amt / item.curr_upb;
	}
}

function initLoanDetailsGrid() {
	/* set up layout */
	var layout = [[{
		'name' : 'Field',
		'field' : 'field',
		'width' : 'auto',
		'formatter' : function(field) {
			return ls.labels[field];
		}
	}, {
		'name' : 'Value',
		'field' : 'value',
		'width' : 'auto'
	}]];

	/* create a new grid: */
	ls.loanDetailsGrid = new dojox.grid.DataGrid({
		structure : layout
	}, 'loanDetailsGrid');
	ls.loanDetailsGrid.startup();
}

function updateLoanDetails(item) {
	var fields = [];
	for(prop in item) {
		if(item.hasOwnProperty(prop) && (prop.search("^_.*") == -1)) {
			fields.push({
				field : prop,
				value : item[prop]
			});
		}
	}

	// Create new datastore with selected items only
	var store = new dojo.data.ItemFileWriteStore({
		data : {
			items : fields
		}
	});

	ls.loanDetailsGrid.setStore(store);
}

function showLoanDetails(e) {
	var item = e.grid.getItem(e.rowIndex);
	updateLoanDetails(item);
	ls.loanDetailsDialog.resize();
	ls.loanDetailsDialog.show();
}

ls.Condition = function(configObj) {
	//internal variables
	var obj = configObj;
	var userSatisfy;

	this.setSatisfy = function(func) {
		userSatisfy = func;
	}

	this.satisfy = function(item) {
		return userSatisfy(item, obj);
	}
};
function initFieldLabels() {
	dojo.xhrGet({
		url : "../data/labels.json",
		handleAs : "json",
		load : function(obj) {
			ls.labels = obj;
		},
		error : function(err) {
		}
	});
}

Array.max = function(array) {
	return Math.max.apply(Math, array);
};
Array.min = function(array) {
	return Math.min.apply(Math, array);
};
function isEmpty(map) {
	for(var key in map) {
		if(map.hasOwnProperty(key)) {
			return false;
		}
		return true;
	}
	return true;
}