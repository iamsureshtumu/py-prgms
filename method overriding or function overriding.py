# Mrthod overriding or Function Overriding


# here we can see that father gave property and said to marry a girl 'subbalaxmi'

class p:
    def property(self):
        print('cash+gold+property+power')

    def marry(self):
        print('subbalaxmi')

class c(p):
    pass

c=c()
c.property()
c.marry()

# here in this child refused to marry 'subbalaxmi' and he overrided the method
# with other girl name called 'katrina'

class p:
    def property(self):
        print('cash+gold+property+power')

    def marry(self):
        print('subbalaxmi')

class c(p):
    def marry(self):
        print('katrina')

c=c()
c.property()
c.marry()

# he have another chance too get both 'subbi' and 'kathi' by using << super().marry() >>
class p:
    def property(self):
        print('cash+gold+property+power')

    def marry(self):
        print('subbalaxmi')

class c(p):
    def marry(self):
        super().marry() # he can handle both
        print('katrina')

c=c()
c.property()
c.marry()

