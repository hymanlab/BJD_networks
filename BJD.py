import numpy as np
import input as ip

_node = 0
_data = 1

_upper = 0
_lower = 1

def add_nodes(B, degvec, letter, bipartite):
    """Add nodes with a letter prefix, and bipartite data to the graph B"""
    mcount = 0
    d = 1
    for deg in np.nditer(degvec):
        for i in xrange(1,deg+1):
            mcount = mcount + 1
            node = letter+'{}'.format(mcount)
            B.add_node(node, bipartite=bipartite, deg=d)
        d = d + 1

def add_upper_nodes(B, degvec):
    add_nodes(B, degvec, 'u', _upper)
def add_lower_nodes(B, degvec):
    add_nodes(B, degvec, 'l', _lower)

def is_upper(datanode):
    return datanode[_data]['bipartite'] == 0
def is_lower(datanode):
    return not is_upper(datanode)

G=ip.G
 
m_list= [n[0] for n in G.nodes(data=True) if is_lower(n)]#list of men

f_list= [n[0] for n in G.nodes(data=True) if is_upper(n)]#list of women


km=max([G.degree(i) for i in m_list])
kw=max([G.degree(i) for i in f_list])

N=[[]]
dN=[[]]
dd_list=np.zeros(shape=(km,kw))
for i in range(0,km):
    degi=[]
    for j in m_list:
        if G.degree(j)==i+1:
            degi.append(j)
    Nj=[]
    dNj=[]
    for j in degi:
        Nj.extend(G.neighbors(j))
                
    for n in Nj:
        dNj.append(G.degree(n))
                    
    N.append(Nj) 
    dN.append(dNj)
            
    for jj in range(0,kw):
        dd_list[i][jj]=(dN[i+1]).count(jj+1)

         
                         
Bjd=dd_list.astype(int)   
BJD=Bjd.transpose()

return BJD