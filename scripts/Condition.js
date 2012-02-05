dojo.provide('ls.Condition');


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


