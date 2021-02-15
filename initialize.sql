\connect postgres

drop database if exists project;
create database project;

\connect project;

\i create.sql

\copy Ads(company_name, message, views)                                 FROM 'Ads.csv'                  csv header
\copy Content_Creator(name, bio, num_monthly_listeners, num_followers)  FROM 'Content Creator.csv'      csv header
\copy "User"(name, followers, following, session)                       FROM 'User.csv'                 csv header
\copy Follows(user_id, creator_id, rating)                              FROM 'Follows.csv'              csv header
\copy Audio_Content(artist_name, name, date_published, album)           FROM 'Audio Content.csv'        csv header
\copy Category(name)                                                    FROM 'Category.csv'             csv header
\copy Belongs_To(content_id, category_id)                               FROM 'Belongs To.csv'           csv header
\copy Messages(sent_to, creator_id, message)                            FROM 'Messages.csv'             csv header
\copy Makes(creator_id, content_id)                                     FROM 'Makes.csv'                csv header