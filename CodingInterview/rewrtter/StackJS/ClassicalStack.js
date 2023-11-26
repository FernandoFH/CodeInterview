// List of Operations on Stack
//
// push():  Adds a single or multiple items to the top of the Stack.
// pop():   Removes and Returns the top item of the Stack.
// peek():  Returns the top item of the Stack.
// isEmpty(): Returns True if Stack is empty, False otherwise.
// clear(): Removes all the items from the Stack.
// size(): Returns the length of the stack.

// Creating a Stack

// Classical

function Stack()
        {   var items = [];   
            var top = 0;   

        // Push an item in the Stack
        this.push = function(element){ items[top++] = element }

        //Pop an item from the Stack 
        this.pop = function(){  return items[--top] }

        //Peek an item in the Stack
        this.peek = function(){   return items[top - 1]; }

        //Check if Stack is empty
        this.isEmpty = function(){   return top === 0; }

        //Clear the Stack
        this.clear= function(){   top = 0; }

        //Size of the Stack
        this.size = function(){   return top; }

        }

var stack = new Stack(); 

// Test Stack 
stack.push(1); 
stack.push(2); 
stack.push(3); 
console.log(stack.peek()); 
console.log(stack.isEmpty()); 
console.log(stack.size()); 
console.log(stack.pop()); 
console.log(stack.size()); 
stack.clear(); 
console.log(stack.isEmpty()); 

/* Output: 
3
false
3
3
2
true */