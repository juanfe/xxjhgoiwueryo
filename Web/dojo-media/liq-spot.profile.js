dependencies = {
        layers: [
                {
                        name: "../scripts/show.js",
                        layerDependencies: [
                        ],
                        dependencies: [
                                "scripts.show"
                        ]
                }
        ],

        prefixes: [
                [ "dijit", "../dijit" ],
                [ "dojox", "../dojox" ],
                [ "dojango", "../../../dojango/dojo-media/dojango" ],
                [ "scripts", "../../../../engine/dojo-media/scripts"]
        ]
}
