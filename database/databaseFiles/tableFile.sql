CREATE TABLE User(
    userID  			INT             NOT NULL AUTO_INCREMENT,
    emailAddress    	VARCHAR(50)     NOT NULL,
    password    		VARCHAR(50)     NOT NULL,
    userType    		VARCHAR(10)     NOT NULL,
    fname   			VARCHAR(50)     NOT NULL,
    lname   			VARCHAR(50)     NOT NULL,
    contact	    		VARCHAR(50)     NOT NULL,
    profilePicture  	VARCHAR(200)		    ,
    profileDescription  VARCHAR(200)		    ,
    accountBalance  	DECIMAL(6,2)		   	,
    rating              DECIMAL(2,1)            ,
    CONSTRAINT user_pkey 	PRIMARY KEY(userID),
    CONSTRAINT user_ckey1 	UNIQUE(emailAddress),
    CONSTRAINT user_ckey2 	UNIQUE(contact)
);

CREATE TABLE BankDetails(
    userID  			INT             NOT NULL,
    accountHolderName   VARCHAR(50)     NOT NULL,
    bankName            VARCHAR(80)     NOT NULL,
    BSB                 DECIMAL(6)      NOT NULL,
    accountNumber       DECIMAL(10)     NOT NULL,
    CONSTRAINT bank_details_pkey 	PRIMARY KEY(userID),
    CONSTRAINT bank_details_fkey    FOREIGN KEY(userID) REFERENCES User(userID),
    CONSTRAINT bank_details_ckey 	UNIQUE(accountNumber)
);

CREATE TABLE CardDetails(
    userID  			INT             NOT NULL,
    cardHolderName      VARCHAR(50)     NOT NULL,
    cardNumber          DECIMAL(16)     NOT NULL,
    expirationDate     VARCHAR(5)      NOT NULL,
    CONSTRAINT card_details_pkey 	PRIMARY KEY(userID),
    CONSTRAINT card_details_fkey    FOREIGN KEY(userID) REFERENCES User(userID)
);

CREATE TABLE Tour(
    tourID          INT             NOT NULL AUTO_INCREMENT,
    guideID         INT             NOT NULL,
    name            VARCHAR(50)     NOT NULL,
    status          BOOLEAN         NOT NULL,
    maxCapacity     INT             NOT NULL,
    price           DECIMAL(6,2)    NOT NULL,
    intensity       VARCHAR(10)     NOT NULL,
    category        VARCHAR(30)     NOT NULL,
    description     VARCHAR(250)    NOT NULL,
    location        VARCHAR(50)     NOT NULL,
    rating          DECIMAL(2,1)            ,
    negotiable      BOOLEAN         NOT NULL,
    repeatFreq      VARCHAR(20)             ,
    startDate       DATE            NOT NULL,
    startTime       VARCHAR(15)            NOT NULL,
    CONSTRAINT tour_pkey 	PRIMARY KEY(tourID),
    CONSTRAINT tour_ckey    UNIQUE(guideID, name),
    CONSTRAINT tour_fkey    FOREIGN KEY(guideID) REFERENCES User(userID)
);

CREATE TABLE TourInstance(
    tourInstanceID  INT             NOT NULL AUTO_INCREMENT,
    tourID          INT             NOT NULL,
    tourDate        DATE            NOT NULL,
    capacity        INT             NOT NULL,
    CONSTRAINT tourInstance_pkey PRIMARY KEY(tourInstanceID),
    CONSTRAINT tourInstance_fkey FOREIGN KEY(tourID) REFERENCES Tour(tourID)
);

CREATE TABLE ItineraryItem(
    time            TIME            NOT NULL,
    tourID          INT             NOT NULL,
    title           VARCHAR(100)    NOT NULL,
    CONSTRAINT itinerary_item_pkey PRIMARY KEY(time, tourID),
    CONSTRAINT intensity_item_fkey FOREIGN KEY(tourID) REFERENCES Tour(tourID)
);

CREATE TABLE Booking(
    bookingID           INT             NOT NULL AUTO_INCREMENT,
    numberOfTourists    INT             NOT NULL,
    price               DECIMAL(6,2)    NOT NULL,
    touristID           INT             NOT NULL,
    tourInstanceID      INT             NOT NULL,
    tourdate			VARCHAR(20)		NOT NULL,
    tourID				INT				NOT NULL,
    notes               VARCHAR(250)            ,
    cancelled           BOOLEAN         NOT NULL DEFAULT FALSE,
    CONSTRAINT booking_pkey PRIMARY KEY(bookingID),
    CONSTRAINT booking_fkey1 FOREIGN KEY(touristID) REFERENCES User(userID),
    CONSTRAINT booking_fkey2 FOREIGN KEY(tourInstanceID) REFERENCES TourInstance(tourInstanceID),
    CONSTRAINT booking_fkey3 FOREIGN KEY(tourID) REFERENCES Tour(tourID)
);

CREATE TABLE Transaction(
    transactionID   INT             NOT NULL AUTO_INCREMENT,
    date            DATE            NOT NULL,
    amount          DECIMAL(6,2)    NOT NULL, 
    type            VARCHAR(20)     NOT NULL,
    touristID       INT                     ,
    guideID         INT                     ,
    CONSTRAINT transaction_pkey PRIMARY KEY(transactionID),
    CONSTRAINT transaction_fkey1 FOREIGN KEY(touristID) REFERENCES User(userID),
    CONSTRAINT transaction_fkey2 FOREIGN KEY(guideID) REFERENCES User(userID)
);

CREATE TABLE TourReview(
    reviewID        INT             NOT NULL AUTO_INCREMENT,
    rating          INT             NOT NULL,
    reviewText      VARCHAR(250)    NOT NULL,
    reviewerID      INT             NOT NULL,
    tourID          INT             NOT NULL,
    CONSTRAINT tour_review_pkey PRIMARY KEY(reviewID),
    CONSTRAINT tour_review_fkey1 FOREIGN KEY(reviewerID) REFERENCES User(userID),
    CONSTRAINT tour_review_fkey2 FOREIGN KEY(tourID) REFERENCES Tour(tourID)
);

CREATE TABLE UserReview(
    reviewID        INT             NOT NULL AUTO_INCREMENT,
    rating          INT             NOT NULL,
    reviewText      VARCHAR(250)    NOT NULL,
    reviewerID      INT             NOT NULL,
    subjectID       INT             NOT NULL,
    CONSTRAINT user_review_pkey  PRIMARY KEY(reviewID),
    CONSTRAINT user_review_fkey1 FOREIGN KEY(reviewerID) REFERENCES User(userID),
    CONSTRAINT user_review_fkey2 FOREIGN KEY(subjectID) REFERENCES User(userID)
);

CREATE TABLE Dispute(
    disputeID       INT             NOT NULL AUTO_INCREMENT,
    description     VARCHAR(500)    NOT NULL,
    status          BOOLEAN         NOT NULL,
    userSubmitID    INT             NOT NULL,
    bookingID       INT                     ,
    CONSTRAINT dispute_pkey     PRIMARY KEY(disputeID),
    CONSTRAINT dispute_fkey1    FOREIGN KEY(userSubmitID) REFERENCES User(userID),
    CONSTRAINT dispute_fkey2    FOREIGN KEY(bookingID) REFERENCES Booking(bookingID)
);

CREATE TABLE Message(
    messageID       INT             NOT NULL AUTO_INCREMENT,
    subject         VARCHAR(100)    NOT NULL,
    body            VARCHAR(500)    NOT NULL,
    sentDate        DATE            NOT NULL,
    sentTime        TIME            NOT NULL,
    senderID        INT             NOT NULL,
    recieverID      INT             NOT NULL,
    disputeID       INT                     ,
    CONSTRAINT message_pkey PRIMARY KEY(messageID),
    CONSTRAINT message_fkey1 FOREIGN KEY(senderID) REFERENCES User(userID),
    CONSTRAINT message_fkey2 FOREIGN KEY(recieverID) REFERENCES User(userID),
    CONSTRAINT message_fkey3 FOREIGN KEY(disputeID) REFERENCES Dispute(disputeID)
);
