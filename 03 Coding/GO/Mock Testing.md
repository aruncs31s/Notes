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