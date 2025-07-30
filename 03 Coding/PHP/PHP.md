# PHP

## Basic Syntax

```php
<?php // begin with a PHP open tag

echo "php\n";
print("php");
?>
```

## String Handling

```php
<?php
// Single quotes - literal strings (no variable interpolation)
$sgl_quotes = '$String';
echo $sgl_quotes; // outputs: $String

// Double quotes - interpolated strings
$dbl_quotes = "This is a $sgl_quotes.";
echo $dbl_quotes; // outputs: This is a $String.

// Escape sequences work in double quotes
$escaped = "a \t tab character.";
echo $escaped; // outputs: a 	 tab character.

// Escape sequences are literal in single quotes
$unescaped = 'a slash and a t: \t';
echo $unescaped; // outputs: a slash and a t: \t
?>
```

## Array Operator (=>)

Creates **key-value pairs** in PHP arrays.

```php
<?php
// Associative arrays
$person = [
    "name" => "John",
    "age" => 25,
    "city" => "New York"
];

// Indexed arrays (explicit keys)
$colors = [
    0 => "red",
    1 => "green", 
    2 => "blue"
];

echo $person["name"]; // outputs: John
?>
```

## Object Operator (->)

Accesses properties and methods of objects.

```php
<?php
class User {
    public $name;
    private $groups = ['admin', 'user'];
    
    public function __construct($name) {
        $this->name = $name;
    }
    
    public function isInGroup($group) {
        return in_array($group, $this->groups);
    }
}

$user = new User("John");
echo $user->name; // outputs: John
echo $user->isInGroup('admin'); // outputs: 1 (true)
?>
```

## Scope Resolution Operator (::)

Accesses class constants and static members.

```php
<?php
class User {
    const USER_TYPE_TEACHER = 'teacher';
    const USER_TYPE_STUDENT = 'student';
    
    public function isInGroup($group) {
        return $group === self::USER_TYPE_TEACHER;
    }
}

echo User::USER_TYPE_TEACHER; // outputs: teacher

// Complete expression example:
// 'expression' => '$user->isInGroup(User::USER_TYPE_TEACHER)'
// This checks if $user is in the teacher group using the class constant
?>
```