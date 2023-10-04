Users = []
Houses = []
House_Requests = []

class User:
    id = 0
    def __init__(self, name, email, phn_nbr, password):
        User.id += 1
        self.name = name
        self.email = email
        self.phn_nbr = phn_nbr
        self.password = password


class House:
    id = 0
    def __init__(self, owner_id, name, permissible_gender, rent, total_space, avail_space, address, status):
        House.id += 1
        self.owner_id = owner_id
        self.name = name
        self.permissible_gender = permissible_gender
        self.rent = rent
        self.total_space = total_space
        self.avail_space = avail_space
        self.address = address
        self.status = status

user1 = Users.append(User("Ram", "ram@gmail.com", 6754328909, "ram@123"))
user2 = Users.append(User("Raj", "raj@gmail.com", 7845632890, "raj@123"))
user3 = Users.append(User("Rahul", "rahul@gmail.com", 6754328909, "rahul@123"))
user4 = Users.append(User("Rayon", "rayon@gmail.com", 6754328909, "rayon@123"))
user5 = Users.append(User("Rathesh", "rathesh@gmail.com", 6754328909, "rathesh@123"))
# print(Users[0].name)


while True:
    print("----------Welcome------------")
    name = input("Enter user name :")
    password = input("Enter Password :")

    if name == "admin" and password == "admin@123":
        pass
        # add or remove pending house requests 

    for user in Users:
        if user.name == name and user.password == password:
            print("Successfully Logged in!")
            print("1. Add House\n2. View my Houses\n3. Request House\n4. Received Requests")
            choice = int(input("Enter your choice :"))
            if choice == 1:
                print("--------------Add House----------------")
                owner_id = user.id
                name = input("Enter House name: ") 
                permissible_gender = input("Enter permissible_gender(male/female): ") 
                rent = int(input("Enter Rent amount: "))
                total_space = int(input("Enter total space: ")) 
                avail_space = int(input("Enter available space: "))
                address = input("Enter address: ") 
                status = "pending"
                Houses.append(House(owner_id, name, permissible_gender, rent, total_space, avail_space, address, status))
                print("House added successfully...")
            
            if choice == 2:
                print("--------------View My Houses----------------")
                for house in Houses:
                    if house.owner_id == user.id:
                        print(f"House name: {house.name} | Permissible gender: {house.permissible_gender} | Rent: {house.rent} | Total space: {house.total_space} | Available space: {house.avail_space} | Address: {house.address} | Status: {house.status}")

            if choice == 3:
                print("--------------Request House----------------")
                permissible_gender = input("Enter permissible_gender: ") 
                rent = int(input("Enter Rent amount: ")) 
                needed_space = int(input("Enter needed space: "))
                location = input("Enter location: ") 
                for house in Houses:
                    if house.permissible_gender.lower() == permissible_gender.lower() and house.rent <= rent and house.avail_space >= needed_space and location.lower() in house.location.lower() and house.status == "accepted":
                        for user1 in Users:
                            if house.owner_id == user1.id:
                                print(f"House id: {house.id} House name: {house.name} | Permissible gender: {house.permissible_gender} | Rent: {house.rent} | Total space: {house.total_space} | Available space: {house.avail_space} | Address: {house.address} | House owner Name: {user1.name} | House owner phone number: {user1.phn_nbr}")

                        house_id = int(input(("Enter the id of house you want")))
                        House_Requests.append({"house_id" : house.house_id, "owner_id" : house.owner_id, "needed_space" : needed_space})
                        print("Request sent to the house owner...")

            if choice == 4:
                for req in House_Requests:
                    if user.id == req.owner_id:
                        for h in Houses:
                            if 
                        






