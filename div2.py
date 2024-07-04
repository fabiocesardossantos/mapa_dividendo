
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import matplotlib.pyplot as plt


def Dividendos():
    st.title('10 Maiores Pagodores de Dividendos')
    st.markdown('-----')
    st.subheader('Essas são as 10 Empresas com maior Dividend Yield nos ultimos 14 anos')


    div =[  
        ['CMIN3','12.72%'],
       ['BRAP4','11.20%' ],
       ['TAEE11','8.63%'],
       [ 'CMIG4','8.54%'],
       [ 'PETR4','8.36%'],
       [ 'PETR3','7.53%' ],
       [  'VIVT3','7.47%'],
       [ 'BBSE3','6.88%'],
       [ 'ELET6','6.67%'],
        [ 'BBAS3','6.34%']
          ]
    div1 = pd.DataFrame(div)
    
    
    div1 = div1.rename(columns={0:'Empresas',1:'Dividendos'})
    div2 =  div1.reindex(index=div1.index[::-1])
    col1, col2 =st.columns([1,2])

    with col1:
        st.subheader('Dividendos')
        st.write(div2)
    with col2:
        st.subheader('demostrativos dos Dividendos')   
        fig, ax = plt.subplots()
        ax.bar(div2['Empresas'], div2['Dividendos'])
        ax.set_xlabel('Empresas')
        ax.set_ylabel('Dividendos')
        st.pyplot(fig)

def Previsão():
    #st.title('Previsão para os proximos DIVIDENDOS')
    #st.subheader('Previsão para os proximos pagementos de dividendos para as 10 maiores empresas pagodores de dividendo ')
    
    previsao = {
        'CMIN3':['10,32%'], #c
        'BRAP4':['14.25%'],#c
        'TAEE11':['8.63%'],
        'CMIG4':['8.54%'],
        'PETR4':['8.36%'],
        'PETR3':['7.53%' ],
        'VIVT3'	:['7.47%'],
        'BBSE3'	:['6.88%'],
        'ELET6'	:['6.67%'],
        'BBAS3':['5.44%']#c
    }

    



def main():
    st.title('Mapa de Dividenos')
    st.markdown('-----')
    st.sidebar.image('mapadividendo.png',caption='Mapa Dividendo', width=180)
    indices = ['Dividendos']
    escolha = st.sidebar.radio('Escolha', indices)
    
    if escolha == 'Dividendos':
        Dividendos()

    #if escolha == 'Previsão':
        #Previsão()
    
   
main()    
