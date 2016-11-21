import re

#Functions in the super class Expr are there to avoid reimplementing them and so that
#every subclass inherits its implementations

def Equiv(p,q) :
    return Or(And(p,q),And(Not(p),Not(q)))

class Expr:
    def __init__(this,e):  #avoiding code repetition with the Not and Var class initialisations
        this.e=e
    
    def eval(this,d):
        temp_str=list(str(this))   #convert string of this object into list for iterating
        for key in d:
            for i in range(0,len(temp_str)):   #iterate over each character in the list
                if(key==temp_str[i]):       #if character equals the variable assigned to this expr then
                    temp_str[i]=str(d[key])     #set the character here to a string representaion of the boolean
        final_str = "".join(str(x) for x in temp_str)  #join each list item in temp_str together with no spaces
        return eval(final_str)

    def isTauto(this):
        is_tauto = True
        regList = re.sub("([/)/(])|(and)|(or)|(not)","",str(this)).split()  #removes everything but the variables
        theset = set(regList)                                  #turns variable list into unique set
        d = {}                                      #new dictionary object
        for i in theset:                            #presets all of the variables and associates them with true booleans
            d[i]=True
               
        for key in d:
            if(d[key]==False):          #toggles current variable association True/False
                d[key]=True
            if(this.eval(d) is False):
                is_tauto=False

            def iterate_all():              #encapsulation to avoid repeated code
                for key2 in d:
                    if(key!=key2):
                        if(d[key2]==False):         #tests every other variable combination
                            d[key2]=True
                            if(this.eval(d) is False):
                                is_tauto=False
                        if(d[key2]==True):
                            d[key2]=False
                            if(this.eval(d) is False):
                                is_tauto=False
            iterate_all()                           #iterate before setting the key in question to a different boolean
                
            if(d[key]==True):
                d[key]=False    
            if(this.eval(d) is False):
                is_tauto=False
                    
            iterate_all()                   #iterate after setting key to False (make sure that all true and false combinations have been made)

        return is_tauto

    
               
class initxy (Expr):    #avoiding repeated init code by inheriting Expr class and making the And and Or objects its subclass        
    def __init__(this,x,y):
        this.x=x
        this.y=y

class Not (Expr):
    def __str__(this):
        if(("and" in str(this.e)) or ("or" in str(this.e))):
            return "not ("+str(this.e)+")"      #parenthesise if the string in question has any lower precendence booleans
        else:
            return 'not '+str(this.e)

class And (initxy):
    def __str__(this):
        if("or" in str(this.x) and "or" in str(this.y)):            #checks for "or" if it exists parenthesise it due to its lower precedence
            return "("+str(this.x)+") and ("+str(this.y)+")"
        elif("or" in str(this.x)):
            return "("+str(this.x)+") and "+str(this.y)
        elif("or" in str(this.y)):
            return str(this.x)+" and ("+str(this.y)+")"
        elif("and" in str(this.x)):
            return "("+str(this.x)+") and "+str(this.y)
        else:
            return str(this.x)+" and "+str(this.y)

class Or (initxy):
    def __str__(this):
        return str(this.x)+" or "+str(this.y)       #lowest precedence goes unchanged

class Var (Expr):
    def __str__(this) :
        return str(this.e)
