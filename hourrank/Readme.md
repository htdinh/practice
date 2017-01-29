## Introduction
This is code to solve the past Hackerrank coding [**competition**] (https://www.hackerrank.com/contests/hourrank-16/challenges/leonardo-and-lucky-numbers). The solution here is refined after consulting the Editorial solution. However, I want to introduce clearer analysis in the Markup file.

## General problem
Given two number a, b (for simplification, assume a < b i.e. a = 4, b = 7). For an integer number n, the question asks to check whether n can be decomposed into n = ax + by where x, y are non-negative integer numbers. For example, 11 = 7*1 + 4*1. While this can be solved as a coin change problem using dynamic programming ([**reference**](http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/)), this is narrower problem that can be solve in O(1) complexity because of simplified rule.

## The decision rule
We look at the remainder of the division for smaller unit (a=4) and try to remove some of that smaller number in the sum, try to replace by the larger number or the multiple of larger number.

rem = n%4 = {0, 1, 2, 3}
* if rem == 0, yes.
* if rem == 1, this also implies a `multiple remainder` of 21 (rem + 5*a) and also a multiple of b=7
* if rem == 2, this also implies a `multiple remainder` of 14 (rem + 3*a) and also a multiple of b=7
* if rem == 3, this also implies a `multiple remainder` of  7 (rem + 1*a) and also a multiple of b=7

For example n = 11,
11%4 = 3
and 11>7
so this number can be represented as ax+by.

## In conclusion
Since the set of number that doesn't satisfy the `lucky ` property in this problem is small. We can list an exhaustive list of those number.
For [4, 7], the list of number that can't be represented in their sum is: `[1, 2, 3, 5, 6, 9, 10, 13, 17]`.

## Sister problem
For [3, 7], the exclusion list is [1, 2, 4, 5, 8, 11]. All positive numbers outside this list can be represented as a sum of multiple of 3 and 7.
rem = n%4 = {0, 1, 2}
* if rem == 0, yes.
* if rem == 1, this also implies a `multiple remainder` of 7 (rem + 2*a) and also a multiple of b=7
* if rem == 2, this also implies a `multiple remainder` of 14 (rem + 4*a) and also a multiple of b=7
