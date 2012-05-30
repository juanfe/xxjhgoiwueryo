dojo.provide("scripts.show");

dojo.require("dojo.parser");
dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("dojox.layout.ContentPane");
dojo.require("dojox.grid.DataGrid");

// used for cropping the biography of an actor
dojo.require("dojox.dtl.filter.strings")

dojo.ready(function(){
	var grid = dijit.byId("movieGrid");
	//grid.setStore(scripts.show.movieStore);
	grid.connect(grid, "onRowClick", function(el){
		var item = this.getItem(el.rowIndex);
		scripts.show.showDetails(item);
	});
	window.setTimeout(function(){ // would require a separate parse process!
		dijit.byId("mainBC").resize();
	}, 100);
});

