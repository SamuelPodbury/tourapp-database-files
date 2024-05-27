DELIMITER //
CREATE TRIGGER tourReviewTrigger 
AFTER INSERT 
ON TourReview FOR EACH ROW
BEGIN
    DECLARE avgRatings DOUBLE;

    SELECT AVG(rating)
    INTO avgRatings
    FROM TourReview
    WHERE TourReview.tourID = NEW.tourID;

    UPDATE Tour
    SET rating = avgRatings
    WHERE Tour.tourID = NEW.tourID;
END;

//

CREATE TRIGGER userReviewTrigger 
AFTER INSERT 
ON UserReview FOR EACH ROW
BEGIN
    DECLARE avgRatings DOUBLE;

    SELECT AVG(rating)
    INTO avgRatings
    FROM UserReview
    WHERE UserReview.subjectID = NEW.subjectID;

    UPDATE User
    SET rating = avgRatings
    WHERE User.userID = NEW.subjectID;
END;

//

DELIMITER ;