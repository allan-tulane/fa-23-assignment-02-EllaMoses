# CMPS 2200 Assignment 2

**Name:** Ella Moses

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$  

    The cost of the root is 1. The cost of level 1 is $2*1=2$. The cost of level 2 is $4*1=4$. The cost is geometrically increasing by a factor of 2 so the tree is leaf dominated. This means that $W(n) = O(n^{log_3(2)})$

  * $W(n)=5W(n/4)+n$

     The cost of the root is n. The cost of level 1 is $5*(n/4)=(5/4)n$. The cost of level 2 is $25*(n/16)=(25/16)n$. The cost is geometrically increasing by a factor of $(5/4)$ so the tree is is leaf dominated. This means that $W(n) = O(n^{log_4(5)})$


  * $W(n)=7W(n/7)+n$

    The cost of the root is n. The cost of level 1 is $7*(n/7)=n$. The cost of level 2 is $49*(n/49)= n$. The cost is constant so the tree is balanced. This means that $W(n)=O(nlogn)$. 

  * $W(n)=9W(n/3)+n^2$

    The cost of the root is $n^2$. The cost of level 1 is $9*(n/3)^2=n^2$. The cost of level 2 is $81*(n/9)^2= n^2$. The cost is constant so the tree is balanced. This means that $W(n)=O(n^2logn)$. 

  * $W(n)=8W(n/2)+n^3$

    The cost of the root is $n^3$. The cost of level 1 is $8*(n/2)^3=n^3$. The cost of level 2 is $64*(n/4)^3= n^3$. The cost is constant so the tree is balanced. This means that $W(n)=O(n^3logn)$.

  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  
.  
.  
.  
  * $W(n)=W(n-1)+2$

    The cost of the root is 2. The cost of level 1 is 2. The cost of level 2 is 2. The cost is constant so the tree is balanced. There are n levels so $W(n)=O(n)$.

  * $W(n)= W(n-1)+n^c$, with $c\geq 1$

    The cost of the root is $n^c$. The cost of the level 1 is $(n -1) ^c$. The cost of level 2 is $(n -2) ^c$. 

  * $W(n)=W(\sqrt{n})+1$

    The cost of the root is 1. The cost of the level 1 is 1. The cost of level 2 is 1. The cost is constant so the tree is balanced. There are 

2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

    Algorithm A can be written as $W(n)=5W(n/2)+n$. The cost of the root is n. The cost of  level 1 is $5*(n/2)=(5/2)n$. The cost of level 2 is $25*(n/4)=(25/4)n$. The cost is geometrically increasing by a factor of $(5/2)$ so the tree is is leaf dominated. This means that $W(n) = O(n^{log_2(5)})$ 

    Algorithm B can be written as $W(n)=2W(n-1)+1$. The cost of the root is 1. The cost of  level 1 is 2. The cost of level 2 is 4. The cost is geometrically increasing by a factor of 2 so the tree is is leaf dominated.

    Algorithm C can be written as $W(n)=9W(n/3)+n^2$. The cost of the root is $n^2$. The cost of level 1 is $9*(n/3)^2=n^2$. The cost of level 2 is $81*(n/9)^2= n^2$. The cost is constant so the tree is balanced. This means that $W(n)=O(n^2logn)$. 

  


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


