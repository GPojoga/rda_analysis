
# module.json format

```
{
	"extractors" : {
		"module_name" : {
			"type" : "module" | "library",
			<Optional> "input" : <list of arguments>,
			<Optional> "output" : <output filename | saved at ./extractors/module_name>,
			<Optional> "dependencies" : [
				{
					"stage" : <stage name>,
					"module_name" : <module name>
				}
			],
			<Optional> "libraries" : [
				{
					"stage" : <stage name>,
					"module_name" : <module name>
				}
			]
		}
	},
	"pre_processors" : {
		"module_name" : {
			"type" : "module" | "library"
			<Optional> "input" : <list of arguments>
			<Optional> "output" : <output filename | saved at ./pre_processors/module_name>
			<Optional> "dependency" : <list of dependencies>
		}
	},
	"processors": {
		"module_name" : {
			"type" : "module" | "library"
			<Optional> "input" : <list of arguments>
			<Optional> "output" : <output filename | saved at ./processors/module_name>
			<Optional> "dependency" : <list of dependencies>
		}
	},
	"post_processors": {
		"module_name" : {
			"type" : "module" | "library"
			<Optional> "input" : <list of arguments>
			<Optional> "output" : <output filename | saved at ./post_processors/module_name>
			<Optional> "dependency" : <list of dependencies>
		}
	}
}
```
