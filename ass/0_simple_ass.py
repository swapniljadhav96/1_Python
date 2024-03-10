# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:37:28 2024

@author: suraj
"""
#age Predication calculation

print("What is your todays age")
years_today=input("years :")
months_today=input(" months :")
days_today=input(" days :")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"your total age today in days   {total_days_today}")
print("Let us assume you are expected to live 90 years")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"Your remaining life in days   {remaining_days_to_live}")