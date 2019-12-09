#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on day 12/02/2019
Course: CS 2302 - Data Structures
Author: Brian Perez
Assignment: Lab #6
Instructor: Diego Aguirre 
D.O.L.M.: 12/05/19 
"""

def editDistDP(str1, str2, m, n): 

    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 

            if i == 0: 
                dp[i][j] = j   
                
           
            elif j == 0: 
                dp[i][j] = i    
  
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 

            else: 
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 
  
# Driver program 
str1 = "Josh"
str2 = "Brian"
  
print(editDistDP(str1, str2, len(str1), len(str2))) 