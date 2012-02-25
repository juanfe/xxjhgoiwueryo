from scenario0 import scenario as scenario0
from scenario1 import scenario as scenario1
from scenario0 import argument as argument0
from scenario1 import argument as argument1

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
}

