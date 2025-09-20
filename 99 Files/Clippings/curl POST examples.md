---
id: curl POST examples
aliases: []
tags:
  - clippings
title: curl POST examples
url: https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
dg-publish: true
---
curl POST examples

> [!summary]- #### Common Options
> `-#, --progress-bar` Make curl display a simple progress bar instead of the more informational standard meter.
> 
> `-b, --cookie <name=data>` Supply cookie with request. If no `=`, then specifies the cookie file to use (see `-c`).
> 
> `-c, --cookie-jar <file name>` File to save response cookies to.
> 
> `-d, --data <data>` Send specified data in POST request. Details provided below.
> 
> `-f, --fail` Fail silently (don't output HTML error form if returned).
> 
> `-F, --form <name=content>` Submit form data.
> 
> `-H, --header <header>` Headers to supply with request.
> 
> `-i, --include` Include HTTP headers in the output.
> 
> `-I, --head` Fetch headers only.
> 
> `-k, --insecure` Allow insecure connections to succeed.
> 
> `-L, --location` Follow redirects.
> 
> `-o, --output <file>` Write output to. Can use `--create-dirs` in conjunction with this to create any directories specified in the `-o` path.
> 
> `-O, --remote-name` Write output to file named like the remote file (only writes to current directory).
> 
> `-s, --silent` Silent (quiet) mode. Use with `-S` to force it to show errors.
> 
> `-v, --verbose` Provide more information (useful for debugging).
> 
> `-w, --write-out <format>` Make curl display information on stdout after a completed transfer. See man page for more details on available variables. Convenient way to force curl to append a newline to output: `-w "\n"` (can add to `~/.curlrc`).
> 
> `-X, --request` The request method to use.
> 

## POST

When sending data via a POST or PUT request, two common formats (specified via the `Content-Type` header) are:
(mimetype)
- `application/json`
- `application/x-www-form-urlencoded`

Many APIs will accept both formats, so if you're using `curl` at the command line, it can be a bit easier to use the form urlencoded format instead of json because

- the json format requires a bunch of extra quoting
- curl will send form urlencoded by default, so for json the `Content-Type` header must be explicitly set

This gist provides examples for using both formats, including how to use sample data files in either format with your `curl` requests.

## curl usage

For sending data with POST and PUT requests, these are common `curl` options:

- request type
	- `-X POST`
	- `-X PUT`
- content type header
- `-H "Content-Type: application/x-www-form-urlencoded"`
- `-H "Content-Type: application/json"`
- data
	- form urlencoded: `-d "param1=value1&param2=value2"` or `-d @data.txt`
	- json: `-d '{"key1":"value1", "key2":"value2"}'` or `-d @data.json`

## Examples

### POST application/x-www-form-urlencoded

`application/x-www-form-urlencoded` is the default:

```

curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data

```

explicit:

```

curl -d "param1=value1&param2=value2" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:3000/data

```

with a data file

```

curl -d "@data.txt" -X POST http://localhost:3000/data

```

### POST application/json

```

curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:3000/data

```

```bash
curl -vX POST  http://127.0.0.1:5000/api/register \
-H "Content-Type: application/json" \
-d '{"name": "aruncs", "password": "simplepass", "email": "test@gmail.com"}' 

```

^00546a

with a data file

```

curl -d "@data.json" -X POST http://localhost:3000/data

```

```

{
	"Content-Type": "application/json",
	"key1":"value1",
	"key2":"value2"
}

```

```

param1=value1&param2=value2

```

```

{
        

            "name": "postdemo",
        
        
          

            "version": "1.0.0",
        
        
          

            "scripts": {
        
        
          

              "start": "node server.js"
        
        
          

            },
        
        
          

            "dependencies": {
        
        
          

              "body-parser": "^1.15.0",
        
        
          

              "express": "^4.13.4"
        
        
          

            }
        
        
          

          }

```

```

var app = require('express')();
  var bodyParser = require('body-parser');
  app.use(bodyParser.json()); // for parsing application/json
  app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded
  app.post('/data', function (req, res) {
  console.log(req.body);
  res.end();
});
 app.listen(3000);

```

### POST Form Encoded Data

```bash
curl -X POST http://127.0.0.1:5000/register \
-F "name=arunc" \
-F "password=simplepass" \
-F "email=test@gmail.com"

```
