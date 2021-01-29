There are many people that thought [my recent OO-bashing post](https://leontrolski.github.io/mostly-pointless.html) was wrong in various ways.

> It’s very badly done OO

> The reason why bad code is bad is not because it's OO, it's because it's bad code.

> Pointing to someone's bad code example and saying "This is why all OO is pointless", is truly a lazy effort.

> I think OO caught on because it encourages people to organize their thoughts, and good structure alone brings a tremendous improvement in code.

> The example given in the article is not compelling.

> How about file-like objects?

> This guy makes a simple concept too complicated.

> Please, post your clickbait bullshit somewhere else.

Etc. Really, what I'd like to do is to test my conjecture - `all OO code can be refactored into equivalent non-OO code that's as easy or more easy to understand` - to acheive that, I'm issuing:

# A call to arms for Python OO enthusiasts

As per this [example](arms), submit a PR to this repo with the most idiomatic OO you can think of, least refactorable into data + functions. I'll have a shot at refactoring, the mob can decide the outcome.

## Rules

- Max 500 lines - I don't have all the time. _(Sorry if you think this simply makes it an unfair test 😞)_.
- You can use the stdlib + commonly used libraries, but it would be nice if the examples were relatively self contained.
- No operator overloading specific stuff (I get that `pathlib` is really cute).
- If you want the code I write to be runnable, provide some tests alongside the code.
