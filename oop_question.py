# -*- coding: utf-8 -*-
"""oop question.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AfaTTZB-Uv54CLwle_p2qNLXXPKAMiXC
"""

from datetime import datetime
class MentalHealthEntry:
  def __init__(self, daily_mood,activities,hours_of_sleep,date):
    self.daily_mood=daily_mood
    self.activities=activities
    self.hours_of_sleep=hours_of_sleep
    self.date=date


  def __str__(self):
    return f"Daily Mood: {self.daily_mood}, | Activities: {self.activities}, | Hours of Sleep: {self.hours_of_sleep},|  Date: {self.date}"

class MentalHealthTracker:
  def __init__(self):
    self.entries=[]

  def add_entry(self,entry):
    self.entries.append(entry)

  def view_entries(self):
    if not self.entries:
      print("No entries found.")
    else:
      for entry in self.entries:
        print(entry)

  def mood_stats(self,daily_mood):
    print(f"mood of {daily_mood} are:")
    found=False
    for i in self.entries:
      if i.daily_mood==daily_mood:
        print(i)
        found=True
    if not found:
      print("No such mood found.")

  def avg_sleep(self):
    tot=0
    for i in self.entries:
      tot+=i.hours_of_sleep
    return tot/len(self.entries)

  def activity_stats(self,activities):
    if not self.entries:
      print("No entries found.")
    else:
      w=0
      e=0
      r=0
      for i in self.entries:
        if i.activities == "exercise":
          e+=1
        elif i.activities == "working":
          r+=1
        elif i.activities == "sleeping":
          w+=1
      print(f"high:{e} | medium: {r} | low: {w}")

a=datetime.today()
patient=MentalHealthTracker()
patient.add_entry(MentalHealthEntry("Happy","exercise",5,a))
patient.add_entry(MentalHealthEntry("Sad","exercise",7,a))
patient.add_entry(MentalHealthEntry("Happy","exercise",5,a))

patient.view_entries()

patient.mood_stats("Happy")
patient.avg_sleep()
patient.activity_stats("exercise")

class Licence:
  def __init__(self,Product_Name,Licence_Key,Licence_Status,Expiry_Date):
    self.Product_Name=Product_Name
    self.Licence_Key=Licence_Key
    self.Licence_Status=Licence_Status
    self.Expiry_Date=Expiry_Date

  def __str__(self):
    return f"Product Name: {self.Product_Name}, | Licence Key: {self.Licence_Key}, | Licence Status: {self.Licence_Status},|  Expiry Date: {self.Expiry_Date}"

class LicenceManager:
  def __init__(self):
    self.licences=[]

  def add_new_licence(self,licence):
    self.licences.append(licence)

  def view_licence(self):
    for i in self.licences:
      if not self.licences:
        print("No licences found.")
      else:
        print(i)
  def view_status(self,status):
    print(f"Licence of {status}:")
    for i in self.licences:
      if i.Licence_Status==status:
        print(i)
      else:
        print("No such status found.")

  def count_product(self,product_name):
    count=0
    for i in self.licences:
      if i.Product_Name==product_name:
        count+=1
    return count

  def count_overall(self):
    a=0
    b=0
    c=0
    for i in self.licences:
      if i.Licence_Status=="Active":
        a+=1
      elif i.Licence_Status=="Inactive":
        b+=1
      elif i.Licence_Status=="Expired":
        c+=1
    print(f"Active: {a} | Inactive: {b} | Expired: {c}")

  def check_key_expiry(self,key):
    found=False
    for i in self.licences:
      if i.Licence_Key==key:
        if i.Expiry_Date < datetime.today():
          print("Licence Expired.")
        else:
          print("Licence Valid.")
        found=True
    if not found:
      print("No such key found.")


  def expiry_check(self):
    e=datetime.today()
    for i in self.licences:
      if i.Expiry_Date < e:
        print(i)