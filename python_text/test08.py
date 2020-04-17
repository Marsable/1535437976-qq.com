#coding="gbk"
import pickle

with open(r"G:\data.dat","wb") as f:
    a1 = "茅尧舜"
    a2 = 123
    a3 = [10,20,30]

    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

with open(r"G:\data.dat","rb") as f:
    a1 = pickle.load(f)
    a2 = pickle.load(f)
    a3 = pickle.load(f)
    print(a1)
    print(a2)
    print(a3)