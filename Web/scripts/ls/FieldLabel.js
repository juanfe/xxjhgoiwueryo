dojo.provide("ls.FieldLabel");
// initializing labels source
// and providing accesors
var labels;
dojo.xhrGet({
	url : "/labels",
	handleAs : "json",
	load : function(obj) {
		labels = obj;
	},
	error : function(err) {
	},
	sync : true
});
// Accesor for the label
ls.FieldLabel.label = function(field) {
	return labels[field];
};
