class student():
    n1=int(input('ent marks'))
    rollno=213
    name='dsnv'
    marksineng=n1
    marksinmaths=90
    marksinscience=90
    outof=300
    total=marksineng+marksinmaths+marksinscience
    percentage=(total/outof)*100
    @staticmethod
    def hi():
        print('studenttotal:',student.total)
        print('studentpercentage',student.percentage)        

student.hi()
                
                
               
        
        
    
