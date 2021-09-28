import streamlit as st
import sklearn
import pickle
st.title("Grade prediction")
model={
	0:pickle.load(open('ml2.pkl','rb')),
	1:pickle.load(open('ml3.pkl','rb')),
	2:pickle.load(open('ml4.pkl','rb')),
	3:pickle.load(open('ml5.pkl','rb')),
    4:pickle.load(open('ml6.pkl','rb')),
    5:pickle.load(open('ml7.pkl','rb')),
    6:pickle.load(open('ml8.pkl','rb'))
}

b=[]
o=0
while True:
	c=st.number_input(f"enter your sem {o+1} grade",0.0,9.0)
	b.append(c)
	o+=1
	if b[-1]==0.00 or o==7:
		break
if b[-1]==0:
	b=b[:-1]
if o-1>0:
	st.write(len(b)+1)
	loaded_model=model[len(b)-1]
	p=loaded_model.predict([b])
	st.write(p[0])
