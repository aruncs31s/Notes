# Mock Testing
In Go, the `go test` command identifies test files based on their filename pattern: any file that ends with `_test.go` is considered a test file. These files typically contain test functions (which must start with `Test` and take a `*testing.T` parameter), benchmark functions (starting with `Benchmark`), and other testing-related code

>- any file that ends with `_test.go` is considered a test file
>- test functions (which must start with `Test`
>	- take a `*testing.T` parameter


FILE: main_test.go



```go
func TestGetUserId(t *testing.T) {
}
```


## In Go
> - "github.com/stretchr/testify/assert"
```go
import (
	"net/http"
	"net/http/httptest"
	"net/url"
	"strconv"
	"testing"
	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
)
```


```go
w := httptest.NewRecorder()
ctx := GetTestGinContext(w)
```

- Add Parameters.
```go
//configure path params
params := []gin.Param{
	{
		Key:   "id",
		Value: "1",
	},
```
- configure query params
```go
u := url.Values{}
u.Add("foo", "bar")
```


```go
MockJsonGet(ctx, params, u)
GetUserId(ctx)
assert.EqualValues(t, http.StatusOK, w.Code)
got, _ := strconv.Atoi(w.Body.String())
assert.Equal(t, 1, got)
```

1. **`MockJsonGet(ctx, params, u)`**:
    - Calls the helper function `MockJsonGet` to configure the mock Gin context (`ctx`) with the simulated HTTP request details.
    - It sets up the request as a GET method, adds path parameters (e.g., [id=1](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)), query parameters (e.g., `foo=bar`), and other mock data. This prepares the context as if a real request to `/user/1?foo=bar` was made.
2. **GetUserId(ctx)**:
    - Invokes the actual [GetUserId](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) handler function (from [main.go](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)) with the mocked context.
    - The handler reads the path param ([id=1](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)), query param (`foo=bar`), converts the ID to an integer, and writes a JSON response (e.g., `{"value": 1}` or just `1` as the body) with status 200 OK.
    - The response is captured by the `httptest.ResponseRecorder` (`w`), not sent over the network.
3. **`assert.EqualValues(t, http.StatusOK, w.Code)`**:
    
    - Uses the `testify/assert` library to check that the HTTP response status code (`w.Code`) is `200` (which is [http.StatusOK](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)).
    - `EqualValues` compares values regardless of type (e.g., int vs. int). If the status isn't 200, the test fails with an error message.
4. **`got, _ := strconv.Atoi(w.Body.String())`**:
    
    - Retrieves the response body from the recorder (`w.Body.String()`), which is a string (e.g., `"1"`).
    - [strconv.Atoi](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) converts the string to an integer (`got`). The [_](vscode-file://vscode-app/c:/Users/arunc/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) ignores any conversion error (since we expect it to succeed in this test).
    - This extracts the actual value returned by the handler for comparison.
5. **`assert.Equal(t, 1, got)`**:
    
    - Asserts that the parsed response body (`got`) equals `1` (the expected ID from the path param).
    - If `got` isn't `1`, the test fails. This verifies the handler correctly processed the input and returned the right output.

```go
// mock getrequest
func MockJsonGet(c *gin.Context, params gin.Params, u url.Values) {
	c.Request.Method = "GET"
	c.Request.Header.Set("Content-Type", "application/json")
	c.Set("user_id", 1)

	// set path params
	c.Params = params

	// set query params
	c.Request.URL.RawQuery = u.Encode()
}
```