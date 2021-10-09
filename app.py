import streamlit as st
import sklearn
import pickle

import base64

LOGO_IMAGE = "st.png"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:100 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
		position: relative;
         top: -200px;
        left: -606px;
    }
	
    .logo-img {
		  
           position: relative;
           top: -161px;
           left: -606px;
		   width: 25%;
           height: 20%;
		   opacity: 2;
    } 
    
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
<body class="y">
	<h2 class="con"></h2>
<p class="cont"></p>
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Cicadas</p>
    </div>
	</body>
    """,
    unsafe_allow_html=True
)  

st.title("Grade prediction")
if(st.button("Info")):
    st.info("This model only takes numbers as an input (both integer & float).")
model={
	0:pickle.load(open('ml2.pkl','rb')),
	1:pickle.load(open('ml3.pkl','rb')),
	2:pickle.load(open('ml4.pkl','rb')),
	3:pickle.load(open('ml5.pkl','rb')),
    # 4:pickle.load(open('ml6.pkl','rb')),
    # 5:pickle.load(open('ml7.pkl','rb')),
    # 6:pickle.load(open('ml8.pkl','rb'))
}

b=[]
o=0
while True:
	c=st.number_input(f"Enter your {o+1} Semester Grade",0.0,10.0)
	b.append(c)
	o+=1
	if b[-1]==0.00 or o==4:
		break
if b[-1]==0:
	b=b[:-1]
if o-1>0:
	#st.write("Predicted Result of your "+str(len(b)+1)+" Semester is" )
	loaded_model=model[len(b)-1]
	p=loaded_model.predict([b])
try:
    if p[0]>=10:st.success("Predicted Result of your "+str(len(b)+1)+" Semester is "+str(10))
    else:st.success("Predicted Result of your "+str(len(b)+1)+" Semester is "+str(p[0]))
except:
    pass