"""

Run the general solver routine solveit(...), which is designed to
handle an arbitrary matrix.

"""

from scipy import rand
from numpy import arange, array           
from pyamg import solveit                 
from pyamg.gallery import poisson         
from pyamg.util.linalg import norm        

if __name__ == '__main__':

    ##
    # Run solveit(...) with the verbose option
    n = 100
    A = poisson((n,n),format='csr')         
    b = array(arange(A.shape[0]), dtype=float)
    print ""
    x = solveit(A,b,verb=True)
    
    ##
    # Return the solver generated by solveit(...) so that it can be used again
    print ""
    (x,ml) = solveit(A,b,verb=True,return_solver=True,tol=1e-8)               
    # run for a new right-hand-side
    b2 = rand(b.shape[0],)
    print ""
    x2 = solveit(A,b2,verb=True,solver=ml,tol=1e-8)
    print ""
