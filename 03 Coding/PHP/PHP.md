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

## Object Operator (->)

The `->` operator is used to access properties and methods of objects.

**Syntax**: `$object->property` or `$object->method()`

```php
<?php
class User {
    public $name;
    public $email;
    private $groups = ['admin', 'user'];
    
    public function __construct($name, $email) {
        $this->name = $name;
        $this->email = $email;
    }
    
    public function isInGroup($group) {
        return in_array($group, $this->groups);
    }
    
    public function getName() {
        return $this->name;
    }
}

// Create an object
$user = new User("John Doe", "john@example.com");

// Access properties with ->
echo $user->name;    // outputs: John Doe
echo $user->email;   // outputs: john@example.com

// Call methods with ->
echo $user->getName();           // outputs: John Doe
echo $user->isInGroup('admin');  // outputs: 1 (true)
echo $user->isInGroup('guest');  // outputs: (false/empty)

// $user->isInGroup means: call the isInGroup method on the $user object
?>
```

**Think of it as**: `$object->something` means "access something from this object"

## Class Constants (::)

The `::` operator (scope resolution operator) is used to access class constants and static properties/methods.

**Syntax**: `ClassName::CONSTANT` or `ClassName::staticMethod()`

```php
<?php
class User {
    // Class constants
    const USER_TYPE_STUDENT = 'student';
    const USER_TYPE_TEACHER = 'teacher';
    const USER_TYPE_ADMIN = 'admin';
    
    private $userType;
    private $groups = [];
    
    public function __construct($userType) {
        $this->userType = $userType;
        $this->groups = [$userType];
    }
    
    public function isInGroup($group) {
        return in_array($group, $this->groups);
    }
}

// Create objects
$user = new User(User::USER_TYPE_TEACHER);

// Breaking down: 'expression'=>'$user->isInGroup(User::USER_TYPE_TEACHER)'
$expression = [
    'expression' => '$user->isInGroup(User::USER_TYPE_TEACHER)'
];

// What each part means:
// User::USER_TYPE_TEACHER  -> gets constant 'teacher'
// $user->isInGroup(...)    -> calls method on $user object
// 'expression' => '...'    -> array key-value pair

// Actual execution:
echo User::USER_TYPE_TEACHER;                    // outputs: teacher
echo $user->isInGroup(User::USER_TYPE_TEACHER);  // outputs: 1 (true)
?>
```

**Complete meaning**: 
- `'expression'=>'...'` creates an array with key 'expression'
- `$user->isInGroup(User::USER_TYPE_TEACHER)` calls the isInGroup method on $user object, passing the constant value 'teacher'
- It's checking if the user belongs to the teacher group