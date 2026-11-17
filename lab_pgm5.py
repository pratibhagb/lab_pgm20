import sys
def simInt(principal,interest,time):
    return(principal* interest*time)/100
if __name__ == "__main__":
    p=float(sys.argv[1])
    i=float(sys.argv[2])
    t=float(sys.argv[3])

    print("Simple interest:",simInt(p,i,t))