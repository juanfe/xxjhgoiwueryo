from scenario0 import scenario as scenario0
from scenario1 import scenario as scenario1
from scenario2 import scenario as scenario2
from scenario3 import scenario as scenario3
from scenario4 import scenario as scenario4
from scenario5 import scenario as scenario5
from scenario0 import argument as argument0
from scenario1 import argument as argument1
from scenario2 import argument as argument2
from scenario3 import argument as argument3
from scenario4 import argument as argument4
from scenario5 import argument as argument5

Scenario = {
	'test_init' : [{'arg': argument0, 'p': scenario0['test_init']},],
	'test_LoadMortgageOperators' : [{'arg': argument0,
		'p': scenario0['test_LoadMortgageOperators']},
		{'arg': argument1, 'p': scenario1['test_LoadMortgageOperators']}
		],
	'test_addLoans' : [{'arg': argument0,
		 'p': scenario0['test_addLoans']['p'],
		 'q': scenario0['test_addLoans']['q'],
		 'r': scenario0['test_addLoans']['r']},
		{'arg': argument1,
		 'p': scenario1['test_addLoans']['p'],
		 'q': scenario1['test_addLoans']['q'],
		 'r': scenario1['test_addLoans']['r']},
		],
	'test_LoadLoans' : [{'arg': argument0, 'p': scenario0['test_LoadLoans']},
		{'arg': argument1, 'p': scenario1['test_LoadLoans']},
		],
	'test_LoadBids' : [{'arg': argument0,
		'p': scenario0['test_LoadBids']['p'],
		'q': scenario0['test_LoadBids']['q'],
		'r': scenario0['test_LoadBids']['r']},
		{'arg': argument1,
		'p': scenario1['test_LoadBids']['p'],
		'q': scenario1['test_LoadBids']['q'],
		'r': scenario1['test_LoadBids']['r']},
		],
	'test_LoadExceptions' : [{'arg': argument0,}],
	'test_SpecifiedAssetAssignation' : [{'arg': argument0,
		 'p': scenario0['test_SpecifiedAssetAssignation']},
		{'arg': argument1, 'p': scenario1['test_SpecifiedAssetAssignation']}
		],
	'test_WARateSC' : [{'arg': argument0, 'p': scenario0['test_WARateSC'],},
		{'arg': argument1, 'p': scenario1['test_WARateSC']},
		],
	'test_CalcRemaing' : [{'arg': argument0, 'p': scenario0['test_CalcRemaing'],},
		{'arg': argument1, 'p': scenario1['test_CalcRemaing'],},
		],
	'test_WARateSNC' : [{'arg': argument0, 'p': scenario0['test_WARateSNC'],},
		{'arg': argument1, 'p': scenario1['test_WARateSNC'],},
		],
	'test_WARateS' : [{'arg': argument0,
			'p': scenario0['test_WARateS']['p'],
			'q': scenario0['test_WARateS']['q']},
		{'arg': argument1,
			'p': scenario1['test_WARateS']['p'],
			'q': scenario1['test_WARateS']['q']},
		{'arg': argument3,
			'p': scenario3['test_WARateS']['p'],
			'q': scenario3['test_WARateS']['q']},
		],
	'test_CalcRateAwarded' : [{'arg': argument0, 'p': scenario0['test_CalcRateAwarded'],}, 
			{'arg': argument1, 'p': scenario1['test_CalcRateAwarded'],}, 
		],
	'test_WARateTot' : [{'arg': argument0, 'p': scenario0['test_WARateTot'],},
			{'arg': argument1, 'p': scenario1['test_WARateTot'],},
		],
	'test_Summary' : [{'arg': argument0, 'p': scenario0['test_Summary'],},
			{'arg': argument1, 'p': scenario1['test_Summary'],},
			{'arg': argument2, 'p': scenario2['test_Summary'],},
			{'arg': argument3, 'p': scenario3['test_Summary'],},
			{'arg': argument4, 'p': scenario4['test_Summary'],},
			{'arg': argument5, 'p': scenario5['test_Summary'],},
		],
	'test_SumRateAllocation' : [{'arg': argument0, 'p': scenario0['test_SumRateAllocation'],},
			{'arg': argument1, 'p': scenario1['test_SumRateAllocation'],},
			{'arg': argument2, 'p': scenario2['test_SumRateAllocation'],},
			{'arg': argument3, 'p': scenario3['test_SumRateAllocation'],},
			{'arg': argument4, 'p': scenario4['test_SumRateAllocation'],},
			{'arg': argument5, 'p': scenario5['test_SumRateAllocation'],},
		],
}

