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
	ls.dataStore.fetch({
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
	var layout = [ {
		defaultCell: { width: 'auto' },
		cells : [
		         { name : 'Collateral key', field : 'collateral_key' },
		         { name : 'Property type', field : 'property_type_code' },
		         { name : 'State', field : 'state' },
		         { name : 'Loan type', field : 'is_adjustable'},
		         { name : 'Lien Type', field : 'lien_position' },
		         { name : 'Max LTV', field : 'original_ltv' },
		         { name : 'Max CLTV', field : 'original_cltv' },
		         { name : 'Loan Amount', field : 'curr_upb' },
		         { name : 'CoreLogic Collateral Risk', field : 'CoreLogic Collateral Risk Score' },
		         { name : 'CoreLogic Fraud Risk', field : 'CoreLogic Fraud Risk Score' },
		         { name : 'FICO', field : 'fico_score' },
		        ]
	} ];

	ls.grid = new dojox.grid.EnhancedGrid({
		query: {'collateral_key':'201149912'},
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