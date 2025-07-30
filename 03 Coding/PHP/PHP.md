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
```