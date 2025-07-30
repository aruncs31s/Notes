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

The `=>` operator is used to assign values to keys in arrays.

```php
<?php
// Associative arrays (key => value pairs)
$person = [
    "name" => "John",
    "age" => 25,
    "city" => "New York"
];

// Numeric arrays with explicit keys
$colors = [
    0 => "red",
    1 => "green", 
    2 => "blue"
];

// Mixed keys
$mixed = [
    "string_key" => "value1",
    42 => "value2",
    "another" => "value3"
];

// Accessing values
echo $person["name"]; // outputs: John
echo $colors[1]; // outputs: green

// In foreach loops
foreach ($person as $key => $value) {
    echo "$key: $value\n";
}
// outputs:
// name: John
// age: 25  
// city: New York
?>
```

**Note**: In your comments above, `# =>` is just showing expected output, not using the array operator.