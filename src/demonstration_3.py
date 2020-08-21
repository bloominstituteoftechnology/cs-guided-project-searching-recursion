"""
Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a
jar of cookies with `n` cookies inside of it, how many ways could he eat all
`n` cookies in the cookie jar? Implement a function `eating_cookies` that
counts the number of possible ways Cookie Monster can eat all of the cookies in
the jar.

For example, for a jar of cookies with n = 3 (the jar has 3 cookies inside it),
there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

He can eat 1 cookie at a time 3 times
He can eat 1 cookie, then 2 cookies
He can eat 2 cookies, then 1 cookie
He can eat 3 cookies all at once.
Thus, eating_cookies(3) should return an answer of 4.

Can you implement a solution that has a O(n) time complexity and a O(n) space
complexity?

*Note: Since this question is asking you to generate a bunch of possible
permutations, you'll probably want to use recursion for this. Think about base
cases that we would want our recursive function to stop recursing on (when do
you know you've found a "way" to eat the cookies versus when you have not?).*
"""
def eating_cookies(n, cache = None):
    # Your code here

