dojo.require("dijit.TitlePane");
dojo.require("dojo.data.ItemFileReadStore");
dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("dijit.form.Button");
dojo.require("dojox.grid.EnhancedGrid");
dojo.require("dojo.on");

//application namespace
var ls={};

dojo.addOnLoad(function() {
	ls.dataStore = new dojo.data.ItemFileReadStore({
		identifier:'collateral_key',
		url : "../data/FundingData.json"
	});
	createGrid(ls.dataStore)
	dataStore.fetch({
		query: {'collateral_key':'*'},
		onComplete:function(items){
			var states = items.map(extractField,{field:'state'});
			var propertyType = items.map(extractField,{field:'property_type_code'});
			var loanType = items.map(extractField,{field:'is_adjustable'});
			var lienType = items.map(extractField,{field:'lien_position'});
			var maxLTV = items.map(extractField,{field:'original_ltv'});
			var maxCLTV = items.map(extractField,{field:'original_cltv'});
			var loanAmount = items.map(extractField,{field:'curr_upb'});
			var coreLogicCollateralRisk = items.map(extractField,{field:'CoreLogic Collateral Risk Score'});
			var coreLogicFraudRisk = items.map(extractField,{field:'CoreLogic Fraud Risk Score'});
			var fico = items.map(extractField,{field:'fico_score'});
		}
	})
});

function extractField(item){
	return item[this.field][0];
}


function createGrid(dataStore) {
	// set the layout structure:
	var layout = [ [ {
		'name' : 'Collateral Key',
		'field' : 'collateral_key',
		'width' : 'auto'
	}, {
		'name' : 'Property Type',
		'field' : 'property_type_code',
		'width' : 'auto'
	}, {
		'name' : 'State',
		'field' : 'state',
		'width' : 'auto'
	}, {
		'name' : 'Loan Type',
		'field' : 'is_adjustable',
		'width' : 'auto'
	},{
		'name' : 'Lien Type',
		'field' : 'lien_position',
		'width' : 'auto'
	},{
		'name' : 'Max LTV',
		'field' : 'original_ltv',
		'width' : 'auto'
	},{
		'name' : 'Max CLTV',
		'field' : 'original_cltv',
		'width' : 'auto'
	},
	{
		'name' : 'Loan Amount',
		'field' : 'curr_upb',
		'width' : 'auto'
	},{
		'name' : 'CoreLogic Collateral Risk',
		'field' : 'CoreLogic Collateral Risk Score',
		'width' : 'auto'
	},{
		'name' : 'CoreLogic Fraud Risk',
		'field' : 'CoreLogic Fraud Risk Score',
		'width' : 'auto'
	},{
		'name' : 'FICO',
		'field' : 'fico_score',
		'width' : 'auto'
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
