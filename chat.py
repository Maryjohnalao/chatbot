#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:42:35 2023

@author: anualao
"""

import streamlit as st
from chat_model import greeting, response, sent_tokens

def main():
    
    st.title('Jaakoes ChatBot')
    st.write('Hey there! what do you want me to do for you?')
    user_response = st.text_input('You: ')
   
    user_response = user_response.lower()
    flag = True
    while(flag):
     if(user_response!='bye'):
         if(user_response=='thanks' or user_response=='thank you' ):
             flag=False   
             st.write("ROBO: You are welcome..")
         else:
             if(greeting(user_response)!=None):
                 st.write(f"ROBO: {greeting(user_response)}")
             else:
                 st.write("ROBO: ")
                 st.write(response(user_response))
                 sent_tokens.remove(user_response)
     else:
         flag=False
         st.write("ROBO: Bye! take care..") 
   
  
   
if __name__ == '__main__':
    main()