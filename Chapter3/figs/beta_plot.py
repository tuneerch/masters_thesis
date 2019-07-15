import matplotlib.pyplot as plt
import numpy as np

[r,a,b,alpha,beta] = np.loadtxt('B_profiles.dat')

alpha, beta = 1e5*alpha, 1e5*beta

#plt.figure(figsize=(,2))
plt.semilogy(r,alpha,'k-', label = '$\\alpha(r)$')
plt.semilogy(r,beta*b,'k--', label = '$b(r)*\\beta(r)$')
plt.grid(True)
plt.xlabel('$r/R_{\odot}$')
plt.ylabel('$\mathbf{B}$ magnitude ($G$)')
plt.legend()
plt.savefig('/home/tuneer/Desktop/helio_project/thesis/Chapter3/figs/alpha_beta.pdf')
plt.show()


plt.plot(r,b,'k-', label = 'b(r)')
plt.plot(r,a,'k--', label = '$b(r)-r\dot{b}(r)$')
plt.grid(True)
plt.xlabel('$r/R_{\odot}$')
plt.ylabel('Dipolar field functions')
plt.legend()
plt.savefig('/home/tuneer/Desktop/helio_project/thesis/Chapter3/figs/b.pdf')
plt.show()
