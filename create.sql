-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-12-13 19:30:40.469

-- tables
-- Table: Ads
CREATE TABLE Ads (
    ad_id serial  NOT NULL,
    company_name text  NOT NULL,
    message text  NOT NULL,
    views int  NOT NULL,
    CONSTRAINT Ads_pk PRIMARY KEY (ad_id)
);

-- Table: Audio_Content
CREATE TABLE Audio_Content (
    content_id serial  NOT NULL,
    artist_name text  NOT NULL,
    name text  NOT NULL,
    date_published date  NOT NULL,
    album text  NOT NULL,
    CONSTRAINT Audio_Content_pk PRIMARY KEY (content_id)
);

-- Table: Belongs_To
CREATE TABLE Belongs_To (
    content_id serial  NOT NULL,
    category_id serial  NOT NULL,
    CONSTRAINT Belongs_To_pk PRIMARY KEY (content_id,category_id)
);

-- Table: Category
CREATE TABLE Category (
    category_id serial  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Category_pk PRIMARY KEY (category_id)
);

-- Table: Content_Creator
CREATE TABLE Content_Creator (
    creator_id serial  NOT NULL,
    name text  NOT NULL,
    bio text  NOT NULL,
    num_monthly_listeners int  NOT NULL,
    num_followers int  NOT NULL,
    CONSTRAINT Content_Creator_pk PRIMARY KEY (creator_id)
);

-- Table: Follows
CREATE TABLE Follows (
    user_id serial  NOT NULL,
    creator_id serial  NOT NULL,
    rating int  NOT NULL,
    CONSTRAINT rating_check CHECK (rating >= 1 AND rating <= 5) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT Follows_pk PRIMARY KEY (user_id,creator_id)
);

-- Table: Makes
CREATE TABLE Makes (
    creator_id serial  NOT NULL,
    content_id serial  NOT NULL,
    CONSTRAINT Makes_pk PRIMARY KEY (creator_id,content_id)
);

-- Table: Messages
CREATE TABLE Messages (
    message_id serial  NOT NULL,
    sent_to serial  NOT NULL,
    creator_id serial  NOT NULL,
    message text  NOT NULL,
    CONSTRAINT Messages_pk PRIMARY KEY (message_id)
);

-- Table: User
CREATE TABLE "User" (
    user_id serial  NOT NULL,
    name text  NOT NULL,
    followers int  NOT NULL,
    following int  NOT NULL,
    session text  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Belongs_To_Audio_Content (table: Belongs_To)
ALTER TABLE Belongs_To ADD CONSTRAINT Belongs_To_Audio_Content
    FOREIGN KEY (content_id)
    REFERENCES Audio_Content (content_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Belongs_To_Category (table: Belongs_To)
ALTER TABLE Belongs_To ADD CONSTRAINT Belongs_To_Category
    FOREIGN KEY (category_id)
    REFERENCES Category (category_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Content_Creator_Follows (table: Follows)
ALTER TABLE Follows ADD CONSTRAINT Content_Creator_Follows
    FOREIGN KEY (creator_id)
    REFERENCES Content_Creator (creator_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Follows_User (table: Follows)
ALTER TABLE Follows ADD CONSTRAINT Follows_User
    FOREIGN KEY (user_id)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Makes_Audio_Content (table: Makes)
ALTER TABLE Makes ADD CONSTRAINT Makes_Audio_Content
    FOREIGN KEY (content_id)
    REFERENCES Audio_Content (content_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Makes_Content_Creator (table: Makes)
ALTER TABLE Makes ADD CONSTRAINT Makes_Content_Creator
    FOREIGN KEY (creator_id)
    REFERENCES Content_Creator (creator_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_Content_Creator (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_Content_Creator
    FOREIGN KEY (creator_id)
    REFERENCES Content_Creator (creator_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_User (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_User
    FOREIGN KEY (sent_to)
    REFERENCES "User" (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

