## Fruit Loops

It may surprise you to realize that programming languages exist that do not include loops! That's right, no for loop, no while loop and, certainly no do ... while loop. If you are just hearing that for the first time, it might throw you for a loop. Yes, you can definitely groan. Although it seems necessary to have loops in a language, it is most certainly not. In fact, you can express solutions for just as many computational problems in languages without loops as you can in languages with loops ... provided that you have 

### Recursion

I think that recursion is one of the neatest tricks in computer science. When we use recursion, it really seems like we are pulling one over on the computer. When I write a recursive solution, it always seems like no one is actually doing the work and then, at the end, bang! Everything comes together and we have a solution. A recursive solution to a computational problem is one that is written in terms of itself. A recursive solution relies on itself to find the answer.

Wait a second. If I am expected to answer a question, it seems a little rich of me to pawn off responsibility on someone else for generating an answer. It also seems a little ridiculous that we would take someone seriously if, in real life, we asked them a question and they attempted to answer it by muttering to themselves.

The key is that a recursive solution only invokes itself on _smaller_ versions of the problems that it was asked to solve. Without this key restriction on how a recursive solution is able to use itself, we run the risk of building never-ending programs. Even I know that when someone asks a question we can only stall for so long before they get very agitated.

### List Length

Before we start to think about recursive solutions, let's solve a common problem and in a familiar way. Let's try to determine the length of a list. In order to better simulate the way that we will be able to work with lists in a functional programming language like Haskell, let's assume that we are not able to do _all_ the things that we are normally able to do with lists in a language like Python. Instead, let's assume that we are only able to perform three operations on lists:

1. Split the first element from the list so that we have access to that element and then rest of the elements.
2. Determine whether the list has *any* elements at all.
3. Build a new list from a single element and an existing list.

These operations are fundamental in functional programming and even have names: [car, cdr](https://en.wikipedia.org/wiki/CAR_and_CDR) and cons. We will learn about the origin of those odd names during the module on functional programming languages.

In Python, we can approximate these operations in the following way. Let's assume that there is a list named `seasons` and that it has elements as we would expect:

```Python
seasons = ['winter', 'spring', 'summer', 'fall']
```

If we wanted to split the `seasons` list into the `first` element and the `rest` of the elements, we could do this:

```Python
first, *rest = seasons
```

and if we printed `first`, we would get

```
'winter'
```

and if we printed `rest`, we would get

```
['spring', 'summer', 'fall']
```

How cool is that?


What about determining whether a list is empty? Well, we'll have to cheat a little. I know that our goal here is to write a function that calculates the length of a list. So, using a function from Python that already does that seems odd, but stay with me. To make the illusion stick, let's write an `is_empty` function that will hide our use of `len`:

```Python
def is_empty(lst):
    if len(lst) == 0:
        return True
    return False
```

To make sure it works, let's check out what happens when we run the following code:

```Python
seasons = ['winter', 'spring', 'summer', 'fall']
if is_empty(seasons):
    print("There is only emptiness.")
else:
    print("Happy day!")
```

```
Happy Day!
```

But, what about when we run:

```Python
seasons = ['winter', 'spring', 'summer', 'fall']
if is_empty([]):
    print("There is only emptiness.")
else:
    print("Happy day!")
```

```
There is only emptiness.
```

Given only those tools, let's write our own length function. Wait, what? Yes, I agree: we should think about how we are going to attack the problem before we get started. I think that it seems like a good idea to peel one element off the list at a time (a power we have - (1) from above), increment a counter, and repeat that process until there are no more elements left in the list (a check we can make - power (2)). At that point, the value that we have in the counter will be the length of the list! Let's make a chart and see whether it works:

| `counter` | `first` | `rest` |
| -- | -- | -- |
| 0 | | `['winter', 'spring', 'summer', 'fall']` |
| 1 | `'winter'` | `['spring', 'summer', 'fall']` |
| 2 | `'spring'` | `['summer', 'fall']` |
| 3 | `'summer'` | `['fall']` |
| 4 | `'fall'` | `[]` |

And, voila! Now that we know it works, let's write some code:

```Python
def length(lst):
    list_length = 0
    while not is_empty(lst):
        first, *lst = lst
        list_length += 1
    return list_length
```
Awesome! The cool part happens right there in the middle of the loop:

```Python
        first, *lst = lst
```

where we are overwriting `lst` with the values of `lst` leftover after pulling out the first element.

How cool are we? _Very_ is the answer!

### List Length List Length List Length List Length ...

Our solution is already impressive because we wrote something that worked and we used only those three list operations (and we didn't even really use that third one at all, did we?). However, we did cheat a little -- we were able to use loops. So, let's up our degree of difficulty and see whether we can write our function without a loop. 

In order to see the solution grow from nothing (the way that recursive solutions often do), let's start with a simple case and work backwards. The easiest list for which to calculate the length is the list that is ... I'll wait ... That's right: _empty_. If we are given an empty list, what is its length? 

Bingo: $0$. 

So, let's start by writing that little bit of code:

```Python
def recursive_length(lst):
    if is_empty(lst):
        return 0
    pass
```

Okay, we are obviously not done, but let's see if what we have so far works:

```Python
print(f"{recursive_length([])=}")
```

And we get

```
recursive_length([])=0
```

YES!

Now, slightly harder, but not by much, let's think about what happens if we are given a list that is _not_ empty. How could we calculate its length? Well, we really only have a few tools at our disposal. When all you have is a hammer, everything looks like a nail!

What if we did this: First, we'll peel off an element from the given list. Because we peeled off that element, we know that the length of the list that we were given is 1 more than the length of the list of the remaining elements. Great! But, how do we know the length of the list with the remaining elements? 

_If only we had a function that returned the length of a list._

Oh, wait, we do! It's ourselves!

> Will this even work? Well, let's just try it -- YOLO.

```Python
def recursive_length(lst):
    if is_empty(lst):
        return 0
    first, *rest = lst
    return 1 + recursive_length(rest)
```

And now we can use it:

```Python
print(f"{recursive_length(seasons)=}")
```

will give

```
recursive_length(seasons)=4
```

Unbelievable.

### But, Does It Work?

We know _that_ it works, but let's diagram an invocation and see _why_ it works.

| Depth |  | | | | | |
| -- | -- | -- | -- | -- | -- | -- |
| 0. | `recursive_length(['winter', 'spring', 'summer', 'fall'])` | | | | | |
| 1. |  | `1 + recursive_length(['spring', 'summer', 'fall'])` | | | | | |
| 2. |  |  | `1 + recursive_length(['summer', 'fall'])` | | | |
| 3. |  |  |  | `1 + recursive_length(['fall'])` | | |
| 4. |  |  |  | | `1 + recursive_length([])` | |
| 5. |  |  |  | | | `recursive_length([])`  |
| 5. |  |  |  | | | `0` |
| 4. |  |  |  | | `1 + 0` | |
| 3. |  |  |  | `1 + 1` | |  |
| 2. |  |  | `1 + 2` | | |  |
| 1. |  | `1 + 3` | | | | |  |
| 0. | `4` | | | | | |  |

What can we see? Well, what we see is that the recursion eventually hits the bottom of the abyss. Because we remove one from `lst` every time, we are destined to reach the case where we call ourselves and `lst` is empty! At that point, the function does not call itself any more and we can unwind! Notice how our key assumption from before comes back to help us out: The fact that we are only invoking ourselves recursively on problems that are smaller means that we are inexorably making progress toward the base case. That is a really, really critical assumption: That our recursive invocations lead, 100% of the time, to the base case.

This is just one example of how you can use recursion to replace loops. There are many, many others. Before you start getting too excited, let's see if we can make this solution a little better.

### The Tail Wags The Dog

When we find ourselves at _Depth 5_ and we have finally called ourselves with an empty list, is that the end of the story? Well, no, not exactly. There are still the $5$ invocations of `recursive_length` that are yet to complete. They are waiting for the response from their recursive invocation. And, until that recursive invocation completes, their job is not done. 

Why is this ["not great, Dan"](https://www.adweek.com/media/crooked-media-brews-more-than-just-podcasts-with-new-branded-coffee-line/)? Well, what would happen if we had a very long list. In that case, we would have the situation where a ton of invocations are waiting to complete and our stack could overflow!

Let's try to write `recursive_length` a little differently and see whether it makes a difference. Let's name this version `do_recursive_length`. It will look very similar to the `recursive_length` that we wrote before but it will take an additional parameter. That parameter will represent the length of the list _to this point_. So, the first time that `do_recursive_length` is called, the argument for the second parameter will be `0`. The second time, `1`. And so on. In other words, the value of the second parameter at every invocation is how many elements have been peeled off the front of the original list in previous recursive invocations. Does this trick really buy us anything?

```Python
def do_recursive_length(lst, yet):
    if is_empty(lst):
        return yet
    first, *rest = lst
    return do_recursive_length(rest, yet + 1)
```

We will have to use this function a little differently, but I think that we can manage:

```Python
print(f"{do_recursive_length(seasons, 0)=}")
```

```
do_recursive_length(seasons, 0)=4
```

Okay, great job, Will: You made us write more code and nothing changed.

Or did it? Let's investigate with a chart:

| Depth |  | | | | | |
| -- | -- | -- | -- | -- | -- | -- |
| 0. | `do_recursive_length(['winter', 'spring', 'summer', 'fall'], 0)` | | | | | |
| 1. |  | `do_recursive_length(['spring', 'summer', 'fall'], 1)` | | | | | |
| 2. |  |  | `do_recursive_length(['summer', 'fall'], 2)` | | | |
| 3. |  |  |  | `do_recursive_length(['fall'], 3)` | | |
| 4. |  |  |  | | `do_recursive_length([], 4)` | |

What do you notice? Exactly! When we are at _Depth 4_, you can see that the previous invocations of the function no longer need to hang around ... the final invocation of `do_recursive_length` has all the information that it needs to answer the question _entirely_. The recursive invocations do not need to unwind in order to calculate the ultimate answer.

How cool is that?

Well, it's only cool if the language can see that is the case and do something like:

| Depth |  |
| -- | -- |
| 0. | `do_recursive_length(['winter', 'spring', 'summer', 'fall'], 0)` |
| 0. | `do_recursive_length(['spring', 'summer', 'fall'], 1)` |
| 0. | `do_recursive_length(['summer', 'fall'], 2)` |
| 0. | `do_recursive_length(['fall'], 3)` |
| 0. | `do_recursive_length([], 4)` |

And, _most_ can! What you just did was optimize a recursive function using something called _tail recursion_. The second solution is tail recursive and the first one is not. If we can write tail recursive functions, we _definitely_ want to do that.

However, there's one problem: `do_recursive_length` is not quite as ergonomic as `recursive_length`, is it? Well, I bet that we can get around that. Python lets us write nested functions so we could nest `do_recursive_length` inside `recursive_length` and the users of `recursive_length` will be none the wiser:


```Python
def recursive_length(lst):
    def do_recursive_length(lst, yet):
        if is_empty(lst):
            return yet
        first, *rest = lst
        return do_recursive_length(rest, yet + 1)
    return do_recursive_length(lst, 0)
```

And now we are right back where we started:

```Python
print(f"{recursive_length(seasons)=}")
```

```
recursive_length(seasons)=4
```

but with code that runs _so_ much faster!

### Conclusion

It is an amazing thing that we really do not need loops to write code that repeats. Recursion is a great alternative to writing loops. What's more, although most people think that recursion is slower than an iterative solution, if we can write tail recursive functions, that is just not the case. 

During the lesson we also saw how a few primitives on lists give us all the power that we need to start writing higher-level functionality. That, too, is really powerful. While you are thinking about the three operations that we assumed to be able to use on lists, think about how you would implement a list data structure so that those operations were really, _really_ fast. Hint: It rhymes with the past tense of a type of [pickleball shot](https://primetimepickleball.com/what-is-a-dink-shot-in-pickleball/) and a [retired soda](https://en.wikipedia.org/wiki/Sierra_Mist).