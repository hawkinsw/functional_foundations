# The Tropic of Capricorn

## Introduction

Now that you are an expert at understanding how loops can be rewritten using recursion and how higher-order functions can give us a tremendous amount of power to customize an otherwise dreary, plain function, we are ready to tackle a task (football season is starting this weekend, after all!) that will combine the two.

In this particular Functional Foundation we are going to focus on the latter (higher-order functions) and in the next one we will rely on our expertise about the former.

Okay, enough generalities, let's get down to writing some code!

## There's Just So Many Friends: An Application of Map

As we said before, although the idea of being able to pass functions as parameters to other functions is not something that may immediately strike you as revolutionary, I promise that what we are about to do is going to change the way you see code forever. You cannot unsee what you are about to learn! So, buckle up. 

As you know, the University is on a mission to educate as many people as possible. That's a laudable goal, but the college's technology is a little, well, dated and the IT department is running into a bit of a problem. In particular, the format of student M Numbers has limited the school's ability to enroll new students. Right now (at hypothetical UC), there are only 6 digits in the M Number. That means that we are limited to enrolling (in all of history, if we want each student to have a unique M Number for eternity) $6^{10}$ students.

The IT staff has commissioned us to write some code that will go through an array of M Numbers in their current format and adjust each one so that:

1. It has a total of 12 digits (all existing M Numbers will grow to 12 digits by prepending $6$ `0`s) and
2. It starts with a capital `M` -- the new Catalyst software requires that all userids start with a letter, and not a number (progress, right?).

### One At A Time

Just to get a sense of our task, here are a few examples of existing M Numbers:

- `020982`
- `041485`
- `091749`

Although they are comprised of nothing but numbers, let's assume that they are actually stored in the UC database as strings.

What would the skeleton of a Python function look like that accepts one of these old M Numbers and returns a new one? Well, we can't _really_ encode the length of the string in the type, so the best that we can probably do is something like:

```Python
def upgrade_m_number(existing: str) -> str:
    return ""
```

Great. So, have a function named `upgrade_m_number` that takes a single parameter (with the type `str`) and returns a value whose type is also `str`.

Just to be on the safe side, before the function upgrades an M Number, it should check that the given M Number is only 6 digits. That's just a little error handling. Then, if the given M Number is only 6 digits long, we will do the upgrade. Nothing fancy, then:

```Python
def upgrade_m_number(existing: str) -> str:
    new = existing
    if len(new) == 6:
        new = "000000" + new
    return "M" + new
```

Let's just give this a spin and see whether it works. 

```Python
old_m_number = "020982"
new_m_number = upgrade_m_number(old_m_number)
print(f"{new_m_number=}")
```

will print

```
new_m_number='M000000020982'
```

And,

```Python
old_m_number = "041485"
new_m_number = upgrade_m_number(old_m_number)
print(f"{new_m_number=}")
```

will print

```
new_m_number='M000000041485'
```

### On Repeat

Well, that's great! If we wanted job security, then we would be all set. We could ask the University for a list of existing M Numbers, then copy-and-paste each one into the `old_m_number` assignment statement in 

```Python
def upgrade_m_number(existing: str) -> str:
    new = existing
    if len(new) == 6:
        new = "000000" + new
    return "M" + new

if __name__=="__main__":
    old_m_number = "041485"
    new_m_number = upgrade_m_number(old_m_number)
    print(f"{new_m_number=}")
```

and record the output.

But, well, we know that we can do better. And, the best part? We don't have to tell anyone that we automated the process and that we are just loafing while while we pretend to do all that ardous manual data manipulation.

So, the University has given us the data in an array and they have named it `existing_m_numbers`. They want the results to be put into a list named `updated_m_numbers`. Okay, I think we all know what is going to come next ... loop!

```Python
def upgrade_m_number(existing: str) -> str:
    new = existing
    if len(new) == 6:
        new = "000000" + new
    return "M" + new

if __name__=="__main__":
    existing_m_numbers = ['020982', '041485', '091749']
    updated_m_numbers = []
    for existing_m_number in existing_m_numbers:
        updated_m_numbers.append(upgrade_m_number(existing_m_number))
    print(f"{updated_m_numbers=}")
```

And, voila:

```
updated_m_numbers=['M000000020982', 'M000000041485', 'M000000091749']
```

### So. Much. Typing.

You all know that I hate one thing more than anything else: Too much typing. So, I think that we should explore a way that we could accomplish the same thing without having to write a loop.

But first, let's think about what we are really doing here. We are taking a function (i.e., `upgrade_m_number`), applying it to each element in an existing list and building up a new list with the results. Pretty neat!

Let's take our analysis one step further: The types of things in each of the lists (the one with the existing elements and the one with the updated elements) have a remarkable similarity to the types of the function that we are using over and over. 

The items in the existing list have the same type as the input type to the function! And the items in the updated list have the same time as the output of the function! That's really neat. Hold that thought closely -- we will return to it before the end of this Functional Foundation.

What would be really cool is if there were a function in Python that _mapped_ a given function over all the elements in a list that we provide! If that were the case, then we could (maybe!) remove that for loop and replace it with a single line of code!

Don't make say I told you so ... but, Python delivers the goods: [`map`](https://docs.python.org/3/library/functions.html#map). 

Before we get too excited, let's look at the documentation for `map` and see if we can figure out what goes where. Remember, we will need to give `map` two things:

1. The function to repeatedly apply; and
2. The list of elements.

Bonus quiz: Because `map` will need to take a function as a parameter, that makes it a ...? That's right, a higher-order function!

Okay, back to that documentation:

```
 map(function, iterable, *iterables)
 ```

 The Python documentation goes on to say:

 > Return an iterator that applies function to every item of iterable, yielding the results. 

 It goes on from there to talk about that magical `iterables` at the end, but we'll just assume it's not necessary for us.

 Okay, so, when we want to use `map`, the first argument will be the function to apply to the list of elements, which we will give as the second argument.

 I think that it will make much more sense when we see how we can reduce the for loop to a single line of code:

 ```Python
    existing_m_numbers = ['020982', '041485', '091749']
    updated_m_numbers = []
    for existing_m_number in existing_m_numbers:
        updated_m_numbers.append(upgrade_m_number(existing_m_number))
    print(f"{updated_m_numbers=}")
`
 ```

 to

 ```Python
    existing_m_numbers = ['020982', '041485', '091749']
    updated_m_numbers = map(upgrade_m_number, existing_m_numbers)
    print(f"{updated_m_numbers=}")
 ```

### Uhm, What?

Even though we should have supreme confidence in ourselves, I think it would be wise to make sure that we see whether our code works. We expect identical results with our new, improved version. Let's remember what that result was:

```
updated_m_numbers=['M000000020982', 'M000000041485', 'M000000091749']
```

But, if we run our updated code, we get

```
updated_m_numbers=<map object at 0x70968d87ba20>
```

What in the world? What's happening is that Python is trying to be, well, "helpful". Python thinks that maybe, just maybe, you won't actually access each of the elements in the updated list. So, Python stashes away the function that we gave as an argument and the list into an object. Then, just at the time that we access the elements in the list, Python will invoke the function on a single element and return that updated element. Python is gambling that we will not access all (or even many) of the elements. And if that gamble pays off, then there will be a huge savings!

But, we can force Python's hand (these Vegas references are getting tired) by putting the result inside `list`. That will make Python apply the function to every element immediately. With a small change


```Python
    existing_m_numbers = ['020982', '041485', '091749']
    updated_m_numbers = list(map(upgrade_m_number, existing_m_numbers))
    print(f"{updated_m_numbers=}")
```

we are back to getting the output we want:
```
updated_m_numbers=['M000000020982', 'M000000041485', 'M000000091749']
```

## Conclusion

What a whirlwind tour of the `map` function. Like I said, now that you have seen it, I bet that you will never see a for loop the same way. While I was doing my PhD I worked with a person who refused to write for loops. That would be strange enough if we were writing code in a functional programming language, but we were writing code in C++!!

In the next edition of the Functional Foundations, we will take a look at how to implement `map`. If you remember earlier, I asked you to hold on to a thought about how the types "match up". Let's say that the function we gave to `map` takes a type named `A` and returns a type named `B`. With just that information, we should be able to write out the type of the function `map`. (We will use `List[X]` to indicate a list of things, each of which has type `X`. We will use `Func[X,Y]` to indicate a function that takes a single parameter with the type `X` that returns a single value with the type `Y`.) 

```Python
def map(Func[A, B], List[A]) -> List[B]:
```

The caller of `map` can give us a list of _any_ type, as long as it matches the type of the elements in the given list! As the implementer of `map`, then, we cannot make _any_ assumptions about the type of `A` or the type of `B`. 

Let's think about that for a second. We could use `map` to multiply every number in a list by $2$:

```Python
def multiply_by_2(input: int) -> int:
    return input * 2

print(f"{list(map(multiply_by_2, [2,4,6]))=}")
```

Or, we could make each character in a list uppercase:

```Python
def upper(input: str) -> str:
    return input.upper()

print(f"{list(map(upper, ['s', 'c', 'r', 'e', 'a', 'm']))=}")
```

(Note: We _had_ to use `str` as the types in this example because Python doesn't have a real character type -- at least I don't think!)

So, because the caller can use `map` to do all those operations (and more), as the implementer we are really limited in the assumptions that we are able to make about the types `A` and `B`. In fact, if you think about it hard enough, there is really only one way to implement `map` that will be right _in all_ cases. 

What we have here is the first example of how a language that allows us to be very precise with the types of our variables can (almost) force us into writing code that is correct _in all cases_. I don't think that it gets cooler than that

