CREATE TABLE "users" (
  "id" serial PRIMARY KEY,
  "username" VARCHAR ( 255 ) UNIQUE NOT NULL,
  "email" VARCHAR ( 255 ) UNIQUE NOT NULL,
  "hashed_password" VARCHAR ( 255 ) NOT NULL
);
