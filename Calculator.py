import streamlit as st

st.title('Mud Weight to PSI Calculator')






def ppg_to_psi():
    st.session_state.psi = st.session_state.ppg * st.session_state.depth * .052



def psi_to_ppg():
    st.session_state.ppg = st.session_state.psi / st.session_state.depth / .052


def depth():
    st.session_state.depth 
    

def clear():
    st.session_state.depth, st.session_state.psi, st.session_state.ppg = 0,0,0
    
    
col1, buff, col2 = st.columns([2,1,2])
with col1:
    Depth = st.number_input('Depth (ft)' , key = 'depth')
    
    
with st.container():   
    col1, buff, col2 = st.columns([2,1,2])
    with col1:
        Mud = st.number_input('Mud Weight (PPG)' , key = 'ppg',
                             on_change = ppg_to_psi)



    with col2:
        Pressure = st.number_input('Formation Pressure (PSI):' , key = 'psi',
                                  on_change = psi_to_ppg)    
        
st.button('Clear Inputs', on_click = clear)        