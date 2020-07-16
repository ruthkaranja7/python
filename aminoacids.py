global aa
aa=[]
class aminoAcids:
        
    def AAIndices(self,f,aa): #lists all of the apparent indexes of the specified amino acid
        print 'The index(or indices) of',aa, 'are:'
        for i in open(f):
            j=i.split() #returns substrings
            if j[0]=='ATOM'and j[3]==aa:
                index = j[5]
                print index,
                                  
    def aaOfIndex(self,f,index): #gives the amino acid having the specified index
        print 'The amino acid having index',index, 'is:'
        for i in open(f):
            j=i.split() #returns substrings
            if j[0]=='ATOM' and j[5]==str(index):
                a=j[3]
                print a
                if j[3]==a:
                    break #just stops rewriting of the same amino acid
                                                   
    def listOfAtoms(self,f,aa):
        print 'The amino acid',aa,'has the following atoms:'
        for i in open(f):
            j=i.split()
            if j[0]=='ATOM' and j[3]==aa:
                print j[11],

    def NoOfAtoms(self,f,aa):
        count=0
        for i in open(f):
            j=i.split()
            if j[0]=='ATOM' and j[3]==aa:
                count=count+1
        print aa, 'has a total of', count,'atoms in this protein.'
        
    def AANames(self,f): #gives the amino acids names found in this protein
        aminoacid=[]
        aaUnique=[]
        for i in open(f):
            j=i.split() #returns substrings 
            if j[0]=='SEQRES':           
                aminoacid.append(j[4:]) # it will only append aminoacids
    
        global aa
        i=0
        while i<len(aminoacid): # until we reach the length of our list we will continue to add to have full length of aminoacid sequence
            aa+= aminoacid[i]
            i+=1                      
        for i in aa:
            if i not in aaUnique:
                aaUnique.append(i)
        print ' '.join(aaUnique)

trial1=aminoAcids()
#trial1.AAIndices('UBQ.pdb','LEU')
#trial1.listOfAtoms('UBQ.pdb','LEU')
#trial1.NoOfAtoms('UBQ.pdb','LEU')
#trial1.aaOfIndex('UBQ.pdb',15)
trial1.AANames('UBQ.pdb')