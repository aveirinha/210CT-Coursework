DERIVATE_POLINOMIALS(pol, deg)
   FOR i <- 1 TO deg                        //because de last element is not revant
      pol_deriv[i] <- pol[i] * i
   RETURN pol_deriv


DERIVATE_POLINOMIALS(p1, deg1)

DERIVATE_POLINOMIALS(p2, deg2)



ex1d


a) O(n)

b) O(n^2)

c) O(n)
