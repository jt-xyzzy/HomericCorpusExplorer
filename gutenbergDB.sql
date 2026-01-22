
DROP TABLE IF EXISTS "persons";
CREATE TABLE "persons" (
    "pers_id"    INTEGER NOT NULL unique,
    "pers_name"    TEXT NOT NULL,
    "text_fk",
    PRIMARY KEY("pers_id" AUTOINCREMENT),
    FOREIGN KEY("text_fk") REFERENCES "texts"("text_id")
);
DROP TABLE IF EXISTS "texts";
CREATE TABLE "texts" (
    "text_id"    TEXT NOT NULL UNIQUE,
    "pub_date"    INTEGER NOT NULL,
    "title"    TEXT NOT NULL,
    "source"    TEXT NOT NULL,
    PRIMARY KEY("text_id")
);

INSERT INTO "texts" ("text_id","pub_date","title","source") VALUES ('hom0',1791,'The Odyssey of Homer','https://www.gutenberg.org/ebooks/24269'),
 ('hom4',1900,'The Odyssey, Rendered into English prose for the use of those who cannot read the original','https://www.gutenberg.org/ebooks/1727'),
 ('hom1',1712,'The Odyssey by Homer','https://www.gutenberg.org/ebooks/3160'),
 ('hom3',1879,'The Odyssey of Homer','https://www.gutenberg.org/ebooks/1728'),
 ('hom2',1611,'The Odysseys of Homer, together with the shorter poems','https://www.gutenberg.org/ebooks/48895');

 INSERT INTO "persons" ("pers_id","pers_name","text_fk") VALUES (1,'William Cowper','hom0'),
 (2,'Samuel Butler','hom4'),
 (3,'Alexander Pope','hom1'),
 (4,'Samuel Henry Butcher','hom3'),
 (5,'Andrew Lang','hom3'),
 (6,'George Chapman','hom2');
