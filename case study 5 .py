class person:

    def __init__(self,fn,ln,email,dob):
        self.fn=fn
        self.ln=ln
        self.email=email
        self.dob=dob
    def dis(self):
        print(self.fn)
        print(self.ln)
        print(self.email)
        print(self.dob)
   



a=person('prasa','sai','sai@gmail.com',7_11_1996)
a.dis()
