INSERT INTO User(emailAddress, password, userType, fname, lname, contact, profilePicture, profileDescription, accountBalance) VALUES ('admin@admin.com', 'tour', 'admin', 'admin', 'user', '1111 111 111', NULL, "Admin of the System", 0);

/*Tourist User*/
INSERT INTO User(emailAddress, password, userType, fname, lname, contact, profilePicture, profileDescription, accountBalance) VALUES ('JohnSmith@gmail.com', 'tour', 'tourist', 'John', 'Smith', '0543 150 980', NULL, 'Placeholder Description', 100);
INSERT INTO CardDetails VALUES (2, 'John Smith', 7469747641314607, '11/20');

/*Guide User*/
INSERT INTO User(emailAddress, password, userType, fname, lname, contact, profilePicture, profileDescription, accountBalance) VALUES ('JaneSmith@gmail.com', 'tour', 'guide', 'Jane', 'Smith', '0543 150 979', NULL, 'Placeholder Description', 100);
INSERT INTO BankDetails VALUES (3, 'Jane Smith', 'Greater Bank', 257065, 7917135486);
INSERT INTO CardDetails VALUES (3, 'Jane Smith', 8726772600822664, '7/20');

INSERT INTO User(emailAddress, password, userType, fname, lname, contact, profilePicture, profileDescription, accountBalance) VALUES ('bob@gmail.com', 'tour', 'guide', 'Bob', 'Smith', '0400 000 000', NULL, 'Placeholder Description', 100);



/*Tour 1 for Guide 1*/
INSERT INTO Tour(guideID, name, status, maxCapacity, price, intensity, category, description, location, rating, negotiable, repeatFreq, startDate, startTime) VALUES (3, 'Mock Tour 1', TRUE, 2, 31, 'Low', 'Food', 'Placeholder description', 'Sydney',  NULL, FALSE, 'Weekly', '2020-07-30', '13:30:00');
INSERT INTO TourInstance(tourID, tourDate, capacity) VALUES (1, '2020-07-30', 1);
INSERT INTO TourInstance(tourID, tourDate, capacity) VALUES (1, '2020-08-06', 1);
INSERT INTO ItineraryItem(time, tourID, title) VALUES ('13:30:00', '1', 'Itinerary Title 1');

/*Tour 2 for Guide 1*/
INSERT INTO Tour(guideID, name, status, maxCapacity, price, intensity, category, description, location, rating, negotiable, repeatFreq, startDate, startTime) VALUES (3, 'Mock Tour 2', TRUE, 8, 47, 'High', 'Cultural', 'Placeholder description', 'Adelaide', NULL, TRUE, 'Monthly', '2020-06-13', '13:30:00');
INSERT INTO TourInstance(tourID, tourDate, capacity) VALUES (2, '2020-06-13', 3);
INSERT INTO ItineraryItem(time, tourID, title) VALUES ('13:30:00', '2', 'Itinerary Title 1');

/*Booking for Tour 1*/
INSERT INTO Booking(numberOfTourists, price, touristID, tourInstanceID, tourDate, tourID, notes) VALUES (1, 31, 2, 1, '2020-05-20', 1, "Vegetarian food only");
INSERT INTO Booking(numberOfTourists, price, touristID, tourInstanceID, tourDate, tourID) VALUES (1, 31, 4, 2, '2020-05-20', 1);

/*Booking for Tour 2*/

INSERT INTO Booking(numberOfTourists, price, touristID, tourInstanceID, tourDate, tourID) VALUES (4, 33, 2, 3, '2020-08-20', 2);
INSERT INTO Booking(numberOfTourists, price, touristID, tourInstanceID, tourDate, tourID) VALUES (1, 50, 4, 3, '2020-08-20', 2);

/*Transaction for Tourist*/
INSERT INTO Transaction(date, amount, type, touristID) VALUES ('2020-06-30', 100, 'Credit Purchase', 2);

/*Transaction for Guide*/
INSERT INTO Transaction(date, amount, type, guideID) VALUES ('2020-06-21', 100, 'Guide Payment', 3);

/*Message from Tourist to Guide*/
INSERT INTO Message(subject, body, sentDate, sentTime, senderID, recieverID) VALUES ('Information about Tour', 'Hi, I would just like to learn more about your tour.', '2020-07-15', '13:28:40', 2, 3);

/*Message from Guide to Tourist*/
INSERT INTO Message(subject, body, sentDate, sentTime, senderID, recieverID) VALUES ('Re:Information about Tour', 'What would you like to know.', '2020-07-15', '13:35:23', 3, 2);

/*Dispute from Tourist*/
INSERT INTO Dispute(description, status, userSubmitID) VALUES ('I had a problem with a tour I went on :(', TRUE, 2);

/*Dispute(2) from Guide*/
INSERT INTO Dispute(description, status, userSubmitID) VALUES ('My last payment did not go through', FALSE, 3);

/*Message from Admin to Guide for Dispute(2)*/
INSERT INTO Message(subject, body, sentDate, sentTime, senderID, recieverID, disputeID) VALUES ('Payment Resolved', 'The issue with your payment has been resovled.', '2020-06-21', '10:32:54', 1, 3, 2);

/*TourReview for Tour 1*/
INSERT INTO TourReview(rating, reviewText, reviewerID, tourID) VALUES (4, "Good Tour s(-_-)b", 2, 1);

/*UserReview for Guide*/
INSERT INTO UserReview(rating, reviewText, reviewerID, subjectID) VALUES (5, "Very friendly", 2, 3);
