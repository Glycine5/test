import streamlit as st
import plotly.express as px
st.title('なかモン先制率計算機')
#st.title('aa')
agil_1=st.number_input('すばやさA', 0, 2000, 0)
agil_2=st.number_input('すばやさB', 0, 2000, 0)

def sensei(agil_1,agil_2):
    import math
    A1=math.floor(int(agil_1)*0.87)
    A2=math.floor(int(agil_1)*0.88)
    A3=math.floor(int(agil_1)*0.89)
    A4=math.floor(int(agil_1)*0.90)
    A5=math.floor(int(agil_1)*0.91)
    A6=math.floor(int(agil_1)*0.92)
    A7=math.floor(int(agil_1)*0.93)
    A8=math.floor(int(agil_1)*0.94)
    A9=math.floor(int(agil_1)*0.95)
    A10=math.floor(int(agil_1)*0.96)
    A11=math.floor(int(agil_1)*0.97)
    A12=math.floor(int(agil_1)*0.98)
    A13=math.floor(int(agil_1)*0.99)
    A14=math.floor(int(agil_1)*1)
    B1=math.floor(int(agil_2)*0.87)
    B2=math.floor(int(agil_2)*0.88)
    B3=math.floor(int(agil_2)*0.89)
    B4=math.floor(int(agil_2)*0.90)
    B5=math.floor(int(agil_2)*0.91)
    B6=math.floor(int(agil_2)*0.92)
    B7=math.floor(int(agil_2)*0.93)
    B8=math.floor(int(agil_2)*0.94)
    B9=math.floor(int(agil_2)*0.95)
    B10=math.floor(int(agil_2)*0.96)
    B11=math.floor(int(agil_2)*0.97)
    B12=math.floor(int(agil_2)*0.98)
    B13=math.floor(int(agil_2)*0.99)
    B14=math.floor(int(agil_2)*1)

    A_arr = [A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14]
    B_arr = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14]
    n = (sum(x<=A1 for x in B_arr) + sum(x<=A2 for x in B_arr) + sum(x<=A3 for x in B_arr) + sum(x<=A4 for x in B_arr) + sum(x<=A5 for x in B_arr) + sum(x<=A6 for x in B_arr) + sum(x<=A7 for x in B_arr) + sum(x<=A8 for x in B_arr) + sum(x<=A9 for x in B_arr) + sum(x<=A10 for x in B_arr) + sum(x<=A11 for x in B_arr) + sum(x<=A12 for x in B_arr) + sum(x<=A13 for x in B_arr) + sum(x<=A14 for x in B_arr))/(14*14)
   # if agil_1==0 or agil_2==0:
   #     n=0
   # else:
   #     pass
    return n

answer = sensei(agil_1,agil_2)



st.write('Aの先制率は',str(answer))
st.write('Bの先制率は',str(1-answer))


