# High Order Functions

Now that we have learned about the common choices made by designers of languages that fit into the functional paradigm, it's time that we start exploring how those choices effect the way that we write programs in those languages. Obviously the fact that functional programming languages (usually) eschew loops for recursion will have an impact on how we write our code. And, for programs coded in _pure_ functional programming languages, the fact that the programs will have no state will also cause us to code differently than we would in a language that supported the creation of programs that contain state.

Those characteristics make functional programming languages very different from their imperative and object-oriented kin. However, because the paradigm is named "functional", let's start with one of the other characteristics that make functional programming languages unique: the fact that functions are _first-class_ values.

The idea of being able to pass functions as parameters to other functions is not something that may sit well with you at first. That's only because most of us learn programming by starting with either imperative or object-oriented programming languages, where functions are not given the same respect as other entities (e.g., variables). That said, the idea of passing functions as parameters to other functions is really cool. Once you see the power you can gain by constructing _higher-order functions_, functions that take other functions as parameters, you will never want to work in a language without it! To repeat, functions in a functional programming language hold the same status as every other type of entity because they can be passed as arguments to functions and given alternate names. 

> Note: Just because a program written in a pure functional programming language has no state and, therefore, no variables, does _not_ mean that we programmers cannot assign names to values. The purity of the language only means that the names cannot be used as a means to change the the data to which they refer. That's the reason for the tortured grammar in the final sentence of the paragraph above. It would have been incorrect to say that (again, in a pure functional programming language) we can assign functions to variables. However, we can give functions additional names!

## Passing Functions As Parameters

That's all well and good. But, why would a language want to provide the programmer the power to use functions in this odd way? Well, there are many reasons, but let's examine one use case that is really common and I believe will help you see the power of the flexibility provided when you can use functions as arguments to other functions.

Let's say that we are writing an operation that needs to sort a list of numbers. Although there are myriad ways to actually implement a sort (some faster than others), ultimately the algorithm will need to compare two members of the list, $a$ and $b$ where $a$ is temporarily before $b$, and determine whether $a$ goes before $b$ in the final sorted list. The sorting algorithm will use that determination (which it may have to recompute multiple times) to, eventually, put the list in order. We could write some pseudocode for a sort function and it might look like:

```python
def sort(list_of_numbers):
    while (not is_ordered(list_of_numbers)):
        ...
        if b < a:
            swap(a, b)
        ...
```

Great! The little block way down in the middle of the function says, essentially, "At the current stage of our computation of the sorted list $a$ is before $b$. But if $b$ is less than $a$, then $b$ should come before $a$. In that case, we will _swap_ them." 

But, let's think about something: Is the best name of that function really `sort`? Or, is it really `sort_ascending`? Yes, sad trombone. Our `sort` function is really limited to being able to sort the numbers in ascending order. So, let's fix our pseudocode:

```python
def sort_ascending(list_of_numbers):
    while (not is_ordered(list_of_numbers)):
        ...
        if b < a:
            swap(a, b)
        ...
```

If our list consisted of

```python
[8, 4, 1, 3, 7]
```

we could use 

```python
sort_ascending([8,4,1,3,7])
```

to get

```python
[1,3,4,7,8]
```

And, we would have to do lots of copy/paste if we wanted to write a `sort_descending` function:

```python
def sort_descending(list_of_numbers):
    while (not is_ordered(list_of_numbers)):
        ...
        if b > a:
            swap(a, b)
        ...
```
The little block way down in the middle of the `sort_descending` function says, this time, "At the current stage of our computation of the sorted list $a$ is before $b$. But if $b$ is greater than $a$, then $b$ should come before $a$. In that case, we will _swap_ them." 
Again, if our list consisted of

```python
[8, 4, 1, 3, 7]
```

we could use 

```python
sort_descending([8,4,1,3,7])
```

to get

```python
[8,7,4,3,1]
```

What would be really cool, however, is if there was a way to abstract the little bit of the pieces of `sort_ascending` and `sort_descending` that determines whether items $a$ and $b$, where $a$ is before $b$ in the in-process-of-being-sorted list, should stay in the order in the sorted list. Let's assume that there is a little function named `less_than` and all it does is determine whether the value of its first parameter is less than the value of its second parameter: 

```python
def less_than(left, right):
    return left < right
```

Simple, right (pun _definitely_ intended)? Okay, let's rewrite our `sort_ascending` pseudocode to use that function:

```python
def sort_ascending(list_of_numbers):
    while (not is_ordered(list_of_numbers)):
        ...
        if less_than(b,a):
            swap(a, b) # b is less than a, so we should swap!
        ...
```

If one is good, two is better: Let's assume that there is another little function named `greater_than` and all it does is determine whether the value of its first parameter is greater than the value of its second parameter: 

```python
def greater_than(left, right):
    return left > right
```

Let's rewrite our `sort_descending` pseudocode to use that function:

```python
def sort_descending(list_of_numbers):
    while (not is_ordered(list_of_numbers)):
        ...
        if greater_than(b, a):
            swap(a, b) # b is greater than a, so we should swap!
        ...
```

Because we are well versed at _abstraction_ as users we do not care that the internals of `sort_ascending` and `sort_descending` are written and we do not have to change the code that we wrote to use the functions!

```Python
print(sort_ascending([8,4,1,3,7]))
print(sort_descending([8,4,1,3,7]))
```

would output

```
[1,3,4,7,8]
[8,7,4,3,1]
```

But, if we _do_ look at the implementation of the two functions, there is something really strange and magical here, isn't there? Let's blank out a few pieces of the algorithm:

```python
def sort_________(list_of_numbers):
    while (not is_ordered(list_of_numbers)):
        ...
        if _______(b, a):
            swap(a, b)
        ...
```

Wow! Because `less_than` and `greater_than` take the same types of inputs and give the same type of output, they can really be used interchangeably in that second `______`, can't they? 

All we need now is a way to write the `sort_______` function to accept another argument that we could use to fill in the blank! If we could do that, we could consolidate `sort_ascending` and `sort_descending` into a single, short-named `sort` function. Boom! And, in a language with high-order functions, we could do exactly that! 

We'll stick with pseudocode at this point, and rewrite `sort` to take a user-specified comparison function which could be invoked in order to determine whether two consecutive elements from a list need to be swapped in order to make progress toward constructing a sorted list:

```python
def sort(list_of_numbers, comparer):
    while (not is_ordered(list_of_numbers)):
        ...
        if comparer(b, a):
            swap(a, b)
        ...
```

Okay, that's wild. But, because there has been a change to the interface of the `sort` function with respect to the `sort_ascending` and `sort_descending` functions, just how is it used? Well, let's remember that we have `less_than` and `greater_than`.

As before, if our list consisted of

```python
[8, 4, 1, 3, 7]
```

we could use 

```python
sort([8,4,1,3,7], less_than)
```

to get

```python
[1, 3, 4, 7, 8]
```

and

```python
sort([8,4,1,3,7], greater_than)
```

to get

```python
[8, 7, 4, 3, 1]
```

_Woah_!


### Practice: Passing Functions As Parameters

Before you get worked up and think that I am teaching you something that is not usable in real Python, let me show you that the language's tools for sorting actually work just ... like ... this. We can explore this corner of Python's functionality and get some practice using high-order functions at the same time.

In the sorting function defined by Python, the comparison function that Python expects as a parameter works _slightly_ differently than the comparison functions that we just created in our pseudocode-- but not much.

Python's sort function expects that the user-specified comparison function takes two parameters, $\mathit{left}$ and $\mathit{right}$, and

1. Returns $-1$ if $\mathit{left}$ is $<$ $\mathit{right}$;
2. Returns $0$ if $\mathit{left}$ is $=$ $\mathit{right}$;
1. Returns $1$ if $\mathit{left}$ is $>$ $\mathit{right}$;

Let's convert our pseudocode from above for `less_than` into real Python code according to the specification that we just defined:

```Python
def less_than(left, right):
    if left < right:
        return -1
    elif left == right:
        return 0
    return 1
```

The way that we actually invoke the Python machinery to sort a list and specify our comparison function is a little, well, _odd_, but give this code a try:

```Python
    list = [8,4,1,3,7]
    result = sorted(list, key=functools.cmp_to_key(less_than))
    print(f"{result=}")
```

And, voila ... the output of the program is:

```
result=[1,3,4,7,8]
```

Just how cool is that?

Take some time and play with the code in [`code/high_order_functions.py`](./code/high_order_functions.py) (or run it on Compiler Explorer [here](https://godbolt.org/z/oj4bT1a4E)) and see if you can develop some muscle memory for using functions as parameters! Try modifying the `less_than` function so that `sorted` returns the list sorted in the opposite direction. What happens if `less_than` returns `0` in every case? The more you work with this new technique of passing functions as parameters, the more comfortable you will feel.

> Note: If you would like to know more about the need for wrapping `less_than` in `functtools.cmp_to_key` and why the parameter to `sorted` is named `key`, you can check out the Python documentation for [sorting](https://docs.python.org/3/howto/sorting.html).