--show_all.sql file
\c project;

\echo 'This table represents ads on Spotify and the companies that they come from.'
SELECT * FROM Ads;

\echo 'This table represents people who create audio content on Spotify'
SELECT * FROM Content_Creator;

\echo 'This table represents users who listen to content on Spotify.'
SELECT * FROM "User";

\echo 'This table represents a relation between users and content creators: users can follow content creators and give them ratings'
SELECT * FROM Follows;

\echo 'This table represents some songs on Spotify'
SELECT * FROM Audio_Content;

\echo 'This table represents different genres that audio content can be categorized into'
SELECT * FROM Category;

\echo 'This table represents a relation between audio content and category that shows which songs belong to which genres'
SELECT * FROM Belongs_to;

\echo 'This table represents messages content creators can send to listeners'
SELECT * FROM Messages;

\echo 'This table represents content creators who create certain audio content'
SELECT * FROM Makes;