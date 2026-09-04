  # CMPS 6610 Problem Set 01
## Answers

**Kailee Segarra**


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**
  - 1a 
      **Yes**
      Since $2^{n+1} = 2 \cdot 2^n$, the two functions only differ by a constant factor of 2. Constant factors do not change the asymptotic growth rate, so $2^{n+1} \in O(2^n)$.

  - 1b    
      **No**
      We can compare the two functions using

        $$\frac{2^{2^n}}{2^n} = 2^{2^n-n}.$$

      This value continues to increase as $n$ grows, so $2^{2^n}$ grows much faster than $2^n$. Therefore, $2^{2^n} \notin O(2^n)$.

  - 1c
      **No**
      $n^{1.01}$ is a polynomial function, while $\log^2 n$ is a logarithmic function. A positive power of $n$ eventually grows faster than any fixed power of $\log n$. Therefore, $n^{1.01} \notin O(\log^2 n)$.

  - 1d
      **Yes**
      Since $n^{1.01}$ grows faster than $\log^2 n$, it will eventually be at least as large as a constant multiple of $\log^2 n$. Therefore, $n^{1.01} \in \Omega(\log^2 n)$.

  - 1e
      **No**
      Since $\sqrt{n} = n^{1/2}$, it is a polynomial function. Polynomial functions with a positive exponent eventually grow faster than fixed powers of logarithmic functions. Therefore, $\sqrt{n} \notin O(\log^3 n)$.

  - 1f
      **Yes**
      Because $\sqrt{n}$ grows faster than $\log^3 n$, it will eventually be at least as large as a constant multiple of $\log^3 n$. Therefore, $\sqrt{n} \in \Omega(\log^3 n)$.

  - 1g
      Suppose there is a function $f(n)$ that belongs to both $o(g(n))$ and $\omega(g(n))$.

      Since $f(n) \in o(g(n))$, the definition must hold for every positive constant $c$. Choose $c = \frac{1}{2}$. Then, for sufficiently large $n$,

          $$f(n) \leq \frac{1}{2}g(n).$$

      Since $f(n) \in \omega(g(n))$, choose $c = 2$. Then, for sufficiently large $n$,

        $$f(n) \geq 2g(n).$$

      For sufficiently large $n$, these two inequalities would have to be true at the same time, which is impossible. Therefore, no function can belong to both sets, so

        $$o(g(n)) \cap \omega(g(n)) = \emptyset.$$


2. **SPARC to Python**

  - 2b
      The function foo computes the greatest common divisor (GCD) of two integers. It repeatedly uses the remainder of the larger number divided by the smaller number until one of the values becomes zero. The remaining value is the GCD.
  - 2c
      The work of foo is $O(\log n)$ because each recursive call reduces the size of the problem, and Euclid's algorithm takes a logarithmic number of recursive calls in the worst case. The span is also $O(\log n)$ because each recursive call depends on the result of the previous call, so the calls cannot be performed in parallel.

3. **Parallelism and recursion**

  - 3b
      The iterative implementation has $O(n)$ work because it examines each element in the list once. Its span is also $O(n)$ because the loop runs sequentially and each step depends on the previous state of the counters.

  - 3d
      The recursive implementation has $O(n)$ work. The list is divided into two halves, and each element is eventually processed once, with constant work used to combine the results from each half. Because the left and right recursive calls are executed sequentially in this version, the span is also $O(n)$.

  - 3e
      If the two recursive calls are executed in parallel, the total work remains $O(n)$ because the same amount of computation is still performed. However, the span becomes $O(\log n)$ because only one branch of the recursion contributes to the critical path at each level of the divide-and-conquer process.
      
4. **GCD**
