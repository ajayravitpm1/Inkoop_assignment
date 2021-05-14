import pandas as pd
data=pd.read_csv("C:/Users/user/hotels.csv")
del data['Sr. No.']

State=input("Enter state")
cost_or_rating=input("Enter cost or rating")
operation=input("Enter highest or cheapest or average")

# for Tamilnadu
if State=="Tamilnadu":
    
   if cost_or_rating=="cost":
       
      if operation=="highest": 
          d=data[data.State=="Tamilnadu"]
          m1=max(data["Cost"])
          hotel_code=d[data.Cost==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with highest price in %s is %s with price %d"%(State,l,m1))
        
      if operation=="cheapest":
          d=data[data.State=="Tamilnadu"]
          m1=min(data["Cost"])
          hotel_code=d[data.Cost==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with cheapest price in %s is %s with price %d"%(State,l,m1))
        
      if operation=="average":
          d=data[data.State=="Tamilnadu"]
          l=list(data["Cost"])
          avg=sum(l)/len(l)
          print("Average cost of Hotel in %s is %f"%(State,avg))
        
   if cost_or_rating=="rating":
       
      if operation=="highest": 
          d=data[data.State=="Tamilnadu"]
          m1=max(data["Ratings"])
          hotel_code=d[data.Ratings==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with highest rating in %s is %s with rating %d"%(State,l,m1))
    
      if operation=="cheapest":
          d=data[data.State=="Tamilnadu"]
          m1=min(data["Ratings"])
          hotel_code=d[data.Ratings==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with cheapest rating in %s is %s with rating %d"%(State,l,m1))
        
      if operation=="average":
          d=data[data.State=="Tamilnadu"]
          l=list(data["Ratings"])
          avg=sum(l)/len(l)
          print("Average rating of Hotel in %s is %f"%(State,avg))
    
# for Karnataka    
if State=="Karnataka":
    
   if cost_or_rating=="cost":
       
      if operation=="highest": 
          d=data[data.State=="Karnataka"]
          m1=max(data["Cost"])
          hotel_code=d[data.Cost==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with highest price in %s is %s with price %d"%(State,l,m1))
        
      if operation=="cheapest":
          d=data[data.State=="Karnataka"]
          m1=min(data["Cost"])
          hotel_code=d[data.Cost==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with cheapest price in %s is %s with price %d"%(State,l,m1))
        
      if operation=="average":
          d=data[data.State=="Karnataka"]
          l=list(data["Cost"])
          avg=sum(l)/len(l)
          print("Average cost of Hotel in %s is %f"%(State,avg))
        
   if cost_or_rating=="rating":
       
      if operation=="highest": 
          d=data[data.State=="Karnataka"]
          m1=max(data["Ratings"])
          hotel_code=d[data.Ratings==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with highest rating in %s is %s with rating %d"%(State,l,m1))
        
      if operation=="cheapest":
          d=data[data.State=="Karnataka"]
          m1=min(data["Ratings"])
          hotel_code=d[data.Ratings==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with cheapest rating in %s is %s with rating %d"%(State,l,m1))
        
      if operation=="average":
          d=data[data.State=="Karnataka"]
          l=list(data["Ratings"])
          avg=sum(l)/len(l)
          print("Average rating of Hotel in %s is %f"%(State,avg))
        
# for Maharashtra
if State=="Maharashtra":
    
   if cost_or_rating=="cost":
       
      if operation=="highest": 
          d=data[data.State=="Maharashtra"]
          m1=max(data["Cost"])
          hotel_code=d[data.Cost==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with highest price in %s is %s with price %d"%(State,l,m1))
        
      if operation=="cheapest":
          d=data[data.State=="Maharashtra"]
          m1=min(data["Cost"])
          hotel_code=d[data.Cost==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with cheapest price in %s is %s with price %d"%(State,l,m1))
        
      if operation=="average":
          d=data[data.State=="Maharashtra"]
          l=list(data["Cost"])
          avg=sum(l)/len(l)
          print("Average cost of Hotel in %s is %f"%(State,avg))
        
   if cost_or_rating=="rating":
       
      if operation=="highest": 
          d=data[data.State=="Maharashtra"]
          m1=max(data["Ratings"])
          hotel_code=d[data.Ratings==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with highest rating in %s is %s with rating %d"%(State,l,m1))
        
      if operation=="cheapest":
          d=data[data.State=="Maharashtra"]
          m1=min(data["Ratings"])
          hotel_code=d[data.Ratings==m1]
          l=list(hotel_code["Hotel Code"])
          print("Hotel with cheapest rating in %s is %s with rating %d"%(State,l,m1))
        
      if operation=="average":
          d=data[data.State=="Maharashtra"]
          l=list(data["Ratings"])
          avg=sum(l)/len(l)
          print("Average rating of Hotel in %s is %f"%(State,avg))
        
    















