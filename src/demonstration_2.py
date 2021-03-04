"""
You're a new author working on your first book. You've written a
series of drafts, each subsequent draft based on the previous draft. The latest draft
of your book has a serious typo. Since each new draft is based on the
previous draft, every draft that comes after the initial typo draft also includes
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find the draft
that first contained the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo.

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""
def firstDraftWithTypo(n):
    # Your code here

