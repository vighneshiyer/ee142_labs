
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def parallel_to_series(Rp, Cp, f):
    Xp = -1/(2*np.pi*f * Cp)
    Q = Rp/Xp
    Rs = Rp/(1+Q**2)
    Xs = Xp/(1+Q**(-2))
    return Rs, Xs


# In[3]:


parallel_to_series(1000, 75e-15, 5e9)


# In[4]:


def L_match(R_hi, R_lo, f):
    m = R_hi/R_lo
    Q = np.sqrt(m - 1)
    X_p = R_hi/Q
    C_p = 1/(X_p * 2*np.pi*f)
    X_s = -X_p/(1+Q**(-2))
    L_s = X_s/(2*np.pi*f)
    return X_p, X_s, C_p, L_s


# In[5]:


L_match(1000, 20.615, 5e9)


# In[6]:


def X_to_L(X, f):
    return X/(2*np.pi*f)

def X_to_C(X, f):
    return 1/(x*2*np.pi*f)

def C_to_X(C, f):
    return 1/(C*2*np.pi*f)

def L_to_X(L, f):
    return L*2*np.pi*f


# In[7]:


print(C_to_X(75e-15, 5e9))
print(L_to_X(13.51e-9, 5e9))


# In[8]:


L_match(1000, 143.579246, 5e9)

