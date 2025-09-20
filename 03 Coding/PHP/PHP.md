---
id: PHP
aliases: []
tags:
  - coding
  - php
dg-publish: true
---
# PHP

> [!info] PHP Overview
> PHP is a server-side scripting language designed for web development. All PHP code must be enclosed within `<?php` and `?>` tags.

## Basic Syntax

```php
<?php // begin with a PHP open tag

echo "php\n";
print("php");
?>

```

> [!tip] Echo vs Print
> - `echo` can output multiple parameters and has no return value
> - `print` only takes one parameter and always returns 1

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

> [!warning] String Quotes Matter
> - **Single quotes**: Variables and escape sequences are treated literally
> - **Double quotes**: Variables are interpolated and escape sequences work

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

> [!note] Array Types
> - **Associative**: Use string keys (`"name" => "John"`)
> - **Indexed**: Use numeric keys (automatically assigned or explicit)

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

> [!example] Object Access
> Use `->` to access anything that belongs to an object instance:
> - Properties: `$user->name`
> - Methods: `$user->isInGroup('admin')`

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

> [!important] Class vs Instance
> - `::` accesses class-level items (constants, static methods)
> - `->` accesses instance-level items (properties, methods)
> - Use `self::` inside the class to reference its own constants

