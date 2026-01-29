
contacts = [{"Name":"Sagar","Age":17,"Mobile":4357943579},{"Name":"Shikhar","Age":20,"Mobile":893274937},{"Name":"Harpreet","Age":19,"Mobile":237498237}]

# what user want to do
print()
print("------What you want to do [add new detail, see all details, edit detail, remove  detail]-----")

task = input("Enter task: ")


#  add new contact detail
if task == "add new detail":
  x = int(input("How many entries you want to enter: "))
  
  for i in range(1,x+1):
  
              
    print("-----Enter your details-----")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    mobile = int(input("Enter your phone number: "))


    contacts.append({"Name":name,"Age":age,"Mobile":mobile})
    print("Details added successfully!")

    # see all contacts details
    
  print("-----All Contacts-----")
  for i in contacts:
   print(f"Name: {i ['Name']}, Age: {i['Age']}, Mobile: {i['Mobile']}")

# see all contacts details
elif task == "see all details":
    print("-----All Contacts-----")
    for i in contacts:
      print(f"Name: {i ['Name']}, Age: {i['Age']}, Mobile: {i['Mobile']}")

 # remove a contact
elif task == "remove detail":
     rem = input("Enter the name you want to delete: ")
     for i in contacts:
        if i["Name"]==rem:
           contacts.remove(i)
           print("Contact removed successfully!")
        else:
           print("Contact not found!")


elif task == "edit detail":
  edit = input("Enter the name which you want to update: ")
  for i in contacts:
    if i["Name"] == edit :
      print("What you want to update")
      print("1. Name")
      print("2. Age")
      print("3. Mobile")
      choice = int(input("Enter your choice (1-3): "))

      if choice ==1:
         new_name = input("Enter new name: ")
         i["Name"]=new_name

      elif choice == 2:
         new_age = int(input("Enter new age: "))
         i["Age"]=new_age

      elif choice == 3:
         new_mobile = int(input("Enter new mobile number: "))
         i["Mobile"] = new_mobile

      else:
         print("Invaid Choice!")
  print("Details Updated Successfully!")
  print("-----All Contacts-----")
  for i in contacts:
      print(f"Name: {i ['Name']}, Age: {i['Age']}, Mobile: {i['Mobile']}")

else:
   print("Invalid Task Entered!")


   


  