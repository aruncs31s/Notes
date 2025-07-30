# PHP 


```php
<?php // begin with a PHP open tag.

echo "php\n";
print("php");

?>
```

```php
# => '$String'
$sgl_quotes = '$String';

echo $sgl_quotes; // outputs: $String
# => 'This is a $String.'
$dbl_quotes = "This is a $sgl_quotes.";
echo $dbl_quotes; // outputs: This is a $String.

# => a 	 tab character.
$escaped   = "a \t tab character.";
echo $escaped; // outputs: a 	 tab character.
# => a slash and a t: \t

$unescaped = 'a slash and a t: \t';
echo $unescaped; // outputs: a slash and a t: \t

// Complete output:
// php
// php$StringThis is a $String.a 	 tab character.a slash and a t: \t
?>
```

## Array Operator (=>)

The `=>` operator creates **key-value pairs** in PHP arrays. It means "assign this value to this key".

**Syntax**: `key => value`

```php
<?php
// This means: assign "John" to the key "name"
"name" => "John"

// Breaking it down:
$person = [
    "name" => "John",     // key: "name", value: "John"
    "age" => 25,          // key: "age", value: 25
    "city" => "New York"  // key: "city", value: "New York"
];

// Without => (indexed array - PHP assigns numeric keys automatically)
$fruits = ["apple", "banana", "orange"]; // keys: 0, 1, 2

// With => (associative array - you specify the keys)
$fruits = [
    0 => "apple",    // explicitly assign "apple" to key 0
    1 => "banana",   // explicitly assign "banana" to key 1  
    2 => "orange"    // explicitly assign "orange" to key 2
];

// Real-world example
$user = [
    "id" => 123,
    "username" => "john_doe", 
    "email" => "john@example.com",
    "is_active" => true
];

echo $user["username"]; // outputs: john_doe
?>
```

**Think of it as**: `key => value` means "the key points to this value"

**Note**: In your comments above, `# =>` is just showing expected output, not using the array operator.