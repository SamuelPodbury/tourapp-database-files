import random
from datetime import date, timedelta
from faker import Faker

class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

class Tourist:
    def __init__(self, userID, userType, accountBalance):
        self.userID = userID
        self.userType = userType
        self.accountBalance = accountBalance
        self.bookings = []
        self.reviewers = []

class Guide:
    def __init__(self, userID):
        self.userID = userID
        self.tours = []

class Tour:
    def __init__(self, tourID, status, startDate, repeatFreq, guideID, maxCapacity, price):
        self.tourID = tourID
        self.status = status
        self.startDate = startDate
        self.repeatFreq = repeatFreq
        self.guideID = guideID
        self.maxCapacity = maxCapacity
        self.price = price
        self.tourInstances = []
        self.reviewers = []
        self.rating = None

class TourInstance:
    def __init__(self, tourDate, capacity, tourInstanceID):
        self.tourDate = tourDate
        self.capacity = capacity
        self.tourInstanceID = tourInstanceID

class Booking:
    def __init__(self, bookingID , touristID, tourInstanceID, tourDate, tour):
        self.bookingID = bookingID
        self.touristID = touristID
        self.tourInstanceID = tourInstanceID
        self.tourDate = tourDate
        self.tour = tour

class Transaction:
    def __init__(self, amount):
        self.amount = amount

class Message:
    def __init__(self, reciverID, disputeID):
        self.reciverID = reciverID
        self.disputeID = disputeID

tourist_list = []
guide_list = []
tour_list = []

random.seed()
fake = Faker("en_AU")
bank_options = ["Commonwealth Bank", "IMB Bank", "Greater Bank", "Bank of Queensland", "ANZ", "Macquarie Bank"]
email_options = ["gmail.com", "outlook.com", "mail.com", "yahoo.com"]
email_list = []
contact_list = []

tour_intensity_options = ["Low", "Medium", "High"]
tour_category_options = ["Family", "Adventure", "Cultural", "Food", "Music"]
tour_location_options = ["Sydney", "Melbourne", "Brisbane", "Canberra", "Adelaide", "Perth", "Darwin", "Hobart", "Wollongong"]
tour_repeat_freq_options = ["Once off", "Daily", "Weekly", "Monthy"]
tour_counter = 2
tour_instance_counter = 3
booking_counter = 4
dispute_counter = 2

tour_review_text_options = ["Very bad tour :(", "Was not very happy with the tour", "I had some fun, but it could be better", "Very enjoyable tour :)", "Best tour I have ever been on. Highly recommended"]

guide_review_text_options = ["This guide is clueless :(", "This guide gets a bit lost sometimes", "Pretty good guide, but needs to communicate more", "Good guide, I would be happy to go on more of their tours", "Best guide, really recommend their tours"]
tourist_review_text_options = ["Very rude tourist, did not pay any attention to instructions", "Was very late because they slept in, wasted heaps of time", "Fairly good tourist, sometimes lost interest", "Good tourist, polite and was helpful to the other tourists", "Fantastic tourist, helped other tourists and was very interested in all the activities."]

def userGenerate(userID, user_type):

    #Generate fname and lname
    fname = fake.first_name()
    lname = fake.last_name()
    password = "tour"

    #Generate Email from fname and lname
    email = None
    while email in email_list or email is None:
        email = fname + lname + "@" + email_options[random.randrange(4)]
        if email in email_list:
            email = fname + lname + "@" + email_options[random.randrange(4)] + str(random.randrange(999))
    email_list.append(email)

    #Generate contact phone number
    contact = None
    while contact in contact_list or contact is None:
        contact = "05" + str(random.randrange(100)).zfill(2) + " " + str(random.randrange(1000)).zfill(3) + " " + str(random.randrange(1000)).zfill(3)
    contact_list.append(contact)

    #Generate a description
    profileDescription = "Placeholder Description"

    #Generate account balance, change when transactions are generated.
    accountBalance = str(random.randrange(50,100))

    #Write to file
    data_file = open("dataFile.sql", "a")
    data_file.write("\nINSERT INTO User(emailAddress, password, userType, fname, lname, contact, profilePicture, profileDescription, accountBalance) VALUES ('" + email + "', '" + password + "', '" + user_type + "', '" + fname + "', '" + lname + "', '" + contact + "', NULL, '" + profileDescription + "', " + accountBalance + ");\n")

    #If the user is a guide, generate bankDetails
    if user_type == "guide":
        generateBankDetails(userID, fname, lname, data_file)
        #Add new guide to guide_list
        guide = Guide(userID)
        #Generate Tours
        for _ in range(random.randrange(2,6)):
            tourGenerate(guide, data_file)
        guide_list.append(guide)

    #Creating CardDetails for some of the users
    if random.randrange(3) == 2:
        generateCardDetails(userID, fname, lname, data_file)

    data_file.close()

    tourist_list.append(Tourist(userID, user_type, accountBalance))
    
def generateBankDetails(userID, fname, lname, data_file):
    account_holder_name = fname + " " + lname
    bank_name = bank_options[random.randrange(6)]
    BSB = random.randrange(100000, 999999)
    account_number = random.randrange(1000000000, 9999999999)
    data_file.write("INSERT INTO BankDetails VALUES (" + str(userID) + ", '" + account_holder_name + "', '" + bank_name + "', " + str(BSB) + ", " + str(account_number) + ");\n")

def generateCardDetails(userID, fname, lname, data_file):
    card_holder_name = fname + " " + lname
    card_number = random.randrange( 1000000000000000, 9999999999999999)
    expiration_date = str(random.randrange(1,12)) + "/" + str(random.randrange(20,22))
    data_file.write("INSERT INTO CardDetails VALUES (" + str(userID) + ", '" + card_holder_name + "', " + str(card_number) + ", '" + expiration_date + "');\n")

def tourGenerate(guide, data_file):
    global tour_counter

    tour_counter += 1

    #generate tour name
    name = "Mock Tour " + str(tour_counter)

    #generate status
    status = "FALSE" if random.randrange(3) == 2 else "TRUE"

    #generate capacity
    maxCapacity = random.randrange(1,11)

    #generate price
    price = str(random.randrange(5, 21))

    #generate intensity
    intensity = tour_intensity_options[random.randrange(3)]
    
    #generate category
    category = tour_category_options[random.randrange(5)]

    #generate description
    description = "Placeholder description"

    #generate location
    location = tour_location_options[random.randrange(9)]

    #generate negotiable
    negotiable = "FALSE" if random.randrange(3) == 2 else "TRUE"

    #generate repeatFreq
    repeatFreq = tour_repeat_freq_options[random.randrange(3)]

    #generate startTime
    startTime = Time(random.randrange(6,19), 0)

    #generate startDate
    startDate = fake.date_between_dates(date(2020,3,1), date(2020,6,1))

    #Add tour to tour_list
    tour = Tour(tour_counter, status, startDate, repeatFreq, guide.userID, maxCapacity, price)
    tour_list.append(tour)

    data_file.write("INSERT INTO Tour(guideID, name, status, maxCapacity, price, intensity, category, description, location, negotiable, repeatFreq, startDate, startTime) VALUES (" + str(guide.userID) + ", '" + name + "', " + status + ", " + str(maxCapacity) + ", " + price + ", '" + intensity + "', '" + category + "', '" + description + "', '" + location + "', " + negotiable + ", '" + repeatFreq + "', '" + str(startDate) + "', '" + str(startTime.hour).zfill(2) + ":" + str(startTime.minute).zfill(2) + "');\n")

    #Add tour to guide's list of tours
    guide.tours.append(guide)

    itinerary_count = 1
    for _ in range(random.randrange(1,4)):
        generateItineraryItem(tour_counter, startTime, data_file, itinerary_count)
        itinerary_count += 1
        startTime.minute += 20 #Every Item has 20min between them

def generateItineraryItem(tourID, startTime, data_file, itinerary_count):

    title = "Itinerary Title " + str(itinerary_count)

    data_file.write("INSERT INTO ItineraryItem(time, tourID, title) VALUES ('" + str(startTime.hour).zfill(2) + ":" + str(startTime.minute).zfill(2) + "', '" + str(tourID) + "', '" + title + "');\n")

def generateTourInstance(tour, tour_date, numberOfTourists, data_file):
    global tour_instance_counter
    tour_instance_counter += 1
    #Retrive tourID
    tourID = tour.tourID
    #Retrive capacity
    capacity =  tour.maxCapacity - numberOfTourists
    #Create insert statement
    data_file.write("INSERT INTO TourInstance(tourID, tourDate, capacity) VALUES (" + str(tourID) + ", '" + str(tour_date) + "', " + str(capacity) + ");\n")

    #Add TourInstance to Tour object
    tour.tourInstances.append(TourInstance(tour_date, capacity, tour_instance_counter))
    return tour_instance_counter

def generateTransaction(user):
    data_file = open("dataFile.sql", "a")
    if user.userType == "guide":
        for _ in range(random.randrange(3)):
            #generate a date the transaction was made
            transaction_date = fake.date_between_dates(date(2020,1,1), date.today())
            #generate amount of money paid to guide
            amount = random.randrange(500)
            #transaction is for a guide payment
            type = "withdraw"
            #guideID
            guideID = user.userID

            #write to file
            data_file.write("INSERT INTO Transaction(date, amount, type, guideID) VALUES ('" + str(transaction_date) + "', " + str(amount) + ", '" + type + "', " + str(guideID) + ");\n")

    #generate a date the transaction was made
    transaction_date = fake.date_between_dates(date(2020,1,1), date.today())
    #generate the amount of credit that was purchased
    amount = user.accountBalance
    #transaction is for a credit purchase
    type = "credit purchase"
    #touristID
    touristID = user.userID

    #write to file
    data_file.write("INSERT INTO Transaction(date, amount, type, touristID) VALUES ('" + str(transaction_date) + "', " + str(amount) + ", '" + type + "', " + str(touristID) + ");\n")

def generateBooking(user):
    global booking_counter
    data_file = open("dataFile.sql", "a")
    tourInstanceID = 0
    #Select tour
    tour = tour_list[random.randrange(0, len(tour_list))]
    
    #Check if the tour is active, if not it cannot be booked
    if tour.status == "FALSE":
        return

    #Check if the user has already made a booking for this tour
    for booking in user.bookings:
        if booking.tour == tour:
            return

    #numberOfTourists determined by tourInstance availability
    numberOfTourists = 0
    #retrieve tour price
    price = tour.price
    #retrieve touristID
    touristID = user.userID
    #generate date based on tour startDate and repeatFreq
    repeat_freq_days = 0 
    if tour.repeatFreq == "Daily":
        repeat_freq_days = 1
    elif tour.repeatFreq == "Weekly":
        repeat_freq_days = 7
    elif tour.repeatFreq == "Monthly":
        repeat_freq_days = 30
    tour_date_delta = timedelta(days=random.randrange(3)*repeat_freq_days)
    tour_instance_date = tour.startDate + tour_date_delta

    #If a TourInstance on the date doesn't exist, one is generated
    tour_instance_exists = False
    for tour_instance in tour.tourInstances:
        if tour_instance.tourDate == tour_instance_date:
            tour_instance_exists = True
            #Reduce capacity of tourInstance
            if tour_instance.capacity == 0:
                return
            numberOfTourists =  random.randrange(1, max(tour_instance.capacity,2))
            tour_instance.capacity -= numberOfTourists
            data_file.write("UPDATE TourInstance SET capacity = " + str(tour_instance.capacity) + " WHERE tourInstanceID = " + str(tour_instance.tourInstanceID) + ";\n")
            tourInstanceID = tour_instance.tourInstanceID
            break
    
    #No TourInstance was found
    if tour_instance_exists is False:
        #Generate numberOfTourists
        numberOfTourists = random.randrange(1, max(tour.maxCapacity,2))
        #Generate a new TourInstance
        tourInstanceID = generateTourInstance(tour, tour_instance_date, numberOfTourists, data_file)

    price = int(price) * numberOfTourists
    adminCut = float(price) / 10
    guideCut = float(price) - adminCut
    cancelled = "FALSE" if random.randrange(1,6) != 5 else "TRUE"

    booking_counter += 1
    data_file.write("INSERT INTO Booking(numberOfTourists, price, touristID, tourInstanceID, tourdate, tourID, cancelled) VALUES (" + str(numberOfTourists) + ", " + str(price) +", " + str(touristID) + ", " + str(tourInstanceID) + ", '" + str(tour_instance_date) + "', " + str(tour.tourID) + ", " + str(cancelled) + " );\n")
    user.bookings.append(Booking(booking_counter, user.userID, tourInstanceID, tour_instance_date, tour))
    
    #Transfer admin payment
    data_file.write("UPDATE User SET accountBalance = accountBalance + " + str(adminCut) + " WHERE userID = 1;\n")

    #Check if booking was cancelled
    if cancelled == "FALSE":
        data_file.write("UPDATE User SET accountBalance = accountBalance + " + str(guideCut) + " WHERE userID = " + str(tour.guideID) + ";\n")
        

def generateDispute(user):
    data_file = open("dataFile.sql", "a")
    global dispute_counter
    dispute_counter += 1

    #generate dispute description
    description = "Placeholder Description"

    #generate dispute status
    status = "FALSE" if random.randrange(2) == 1 else "TRUE"

    #retrieve userID
    userSubmitID = user.userID

    #select booking and retrieve bookingID
    booking = user.bookings[random.randrange(len(user.bookings))]
    bookingID = booking.bookingID

    #write dispute to file
    data_file.write("INSERT INTO Dispute(description, status, userSubmitID, bookingID) VALUES ('" + description + "', " + status + ", " + str(userSubmitID) + ", " + str(bookingID) + ");\n")

    #send notification message to the admin after every dispute
    subject = "New Dispute"
    body = "A new dispute has been lodged on booking " + str(bookingID)
    dispute_date = fake.date_between_dates(date(2020,1,1), booking.tourDate)
    dispute_time = Time(random.randrange(9,17), random.randrange(1,60))
    senderID = user.userID
    reciverID = 1
    data_file.write("INSERT INTO Message(subject, body, sentDate, sentTime, senderID, recieverID, disputeID) VALUES ('" + subject + "', '" + body + "', '" + str(dispute_date) + "', '" + str(dispute_time.hour) + ":" + str(dispute_time.minute) + "', " + str(senderID) + ", " + str(reciverID) + ", " + str(dispute_counter) + ");\n")

    #generate messages for dispute
    if status == "FALSE":
        generateDisputeMessage(user, booking, dispute_date, dispute_counter, data_file)

def generateDisputeMessage(user, booking, dispute_date, disputeID, data_file):
    
    #generate subject
    subject = "Dispute resolved"

    #generate body
    body = "This dispute has been resolved"

    #generate sendDate, must be before a booked tour date
    sentDate = fake.date_between_dates(dispute_date, booking.tourDate)

    #generate sendTime
    sentTime = Time(random.randrange(9,17), random.randrange(1,60))

    #senderID is admin id, so 1
    senderID = 1

    #retrieve recieverID from user
    reciverID = user.userID

    data_file.write("INSERT INTO Message(subject, body, sentDate, sentTime, senderID, recieverID, disputeID) VALUES ('" + subject + "', '" + body + "', '" + str(sentDate) + "', '" + str(sentTime.hour) + ":" + str(sentTime.minute) + "', " + str(senderID) + ", " + str(reciverID) + ", " + str(disputeID) + ");\n")

def generateMessage(subject, senderID, reciverID, date):
    data_file = open("dataFile.sql", "a")
    #generate body
    body = ""
    if subject == "Tour Inquiry":
        body = "I would like to know a bit more about this tour."
    else:
        body = "Sure, what would you like to know?"

    #generate sentDate
    sentDate = fake.date_between_dates(date, date.today())

    #generate sentTime
    sentTime = Time(random.randrange(9,20), random.randrange(1,60))

    #write to file
    data_file.write("INSERT INTO Message(subject, body, sentDate, sentTime, senderID, recieverID) VALUES ('" + subject + "', '" + body + "', '" + str(sentDate) + "', '" + str(sentTime.hour) + ":" + str(sentTime.minute) + "', " + str(senderID) + ", " + str(reciverID) + ");\n")
    
    #return sentDate so the reponse can be sent after the first message
    return sentDate

def generateTourReview(tour):
    data_file = open("dataFile.sql", "a")

    #retrieve user reviewer
    reviewer = None
    while reviewer in tour.reviewers or reviewer is None:
        reviewer = tourist_list[random.randrange(len(tourist_list))]

    #generate rating
    if tour.rating is None:
        tour.rating = random.randrange(1,6)
    else:
        tour.rating = random.randrange(max(tour.rating-1, 1),6)

    #generate review text based on rating
    reviewText = tour_review_text_options[tour.rating-1]

    data_file.write("INSERT INTO TourReview(rating, reviewText, reviewerID, tourID) VALUES (" + str(tour.rating) + ", '" + reviewText + "', " + str(reviewer.userID) + ", " + str(tour.tourID) + ");\n")

    tour.reviewers.append(reviewer)

def generateUserReview(user):
    data_file = open("dataFile.sql", "a")

    #retrieve user reviewer
    reviewer = None
    while reviewer in user.reviewers or reviewer is None:
        reviewer = tourist_list[random.randrange(len(tourist_list))]
    
    #generate rating
    rating = random.randrange(1,6)

    #generate review text based on rating
    if user.userType == "guide":
        #text for guides
        reviewText = guide_review_text_options[rating-1]
    else:
        #tourist can't review tourist
        if reviewer.userType == "tourist":
            return
        #text for tourist
        reviewText = tourist_review_text_options[rating-1]

    data_file.write("INSERT INTO UserReview(rating, reviewText, reviewerID, subjectID) VALUES (" + str(rating) + ", '" + reviewText + "', " + str(reviewer.userID) + ", " + str(user.userID) + ");\n")

    user.reviewers.append(reviewer)
    

def clearFile():
    #Open the file in write mode to overwrite the previous data
    data_file =  open("dataFile.sql", "w")
    #Clear existing data
    data_file.write("")
    data_file.close()

#Run
clearFile()
#Generate Guides, Tours and ItineraryItems
for i in range(4,75):
	userGenerate(i, "guide")

#Generate Tourists
for i in range(75,300):
    userGenerate(i, "tourist")

#Generate Transactions
for user in tourist_list:
    generateTransaction(user)

#Generate Bookings and TourInstances
for user in tourist_list:
    for _ in range(random.randrange(5, 10)):
        generateBooking(user) #generate booking and TourInstance if there isn't one

#Generate Disputes and Dispute Messages
for user in tourist_list:
    if len(user.bookings) == 0: #If the user has no bookings not dispute are made
        continue
    generateDispute(user) #generate a dispute and messages

#Generate Messages
for tourist in tourist_list:
    tour = tour_list[random.randrange(len(tour_list))]
    sentDate = generateMessage("Tour Inquiry", tourist.userID, tour.guideID, date(2020, 1, 1)) #initial message from tourist to guide
    generateMessage("Re:Tour Inquiry", tour.guideID, tourist.userID, sentDate) #guides reponse to the tourist message

#Generate Tour Reviews
for tour in tour_list:
    for _ in range(random.randrange(5,11)):
        generateTourReview(tour)

#Generate User Reviews
for user in tourist_list:
    for _ in range(random.randrange(5,11)):
        generateUserReview(user)
