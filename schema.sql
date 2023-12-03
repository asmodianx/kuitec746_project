SQL Created on PostgreSQL v14 using PgAdmin4
CREATE SCHEMA IF NOT EXISTS kershner
CREATE TABLE IF NOT EXISTS kershner."API"
(
"APIGUID" uuid NOT NULL DEFAULT gen_random_uuid(),
"API" character varying COLLATE pg_catalog."default" NOT NULL,
"OwnerEmailAddress" character varying COLLATE pg_catalog."default" NOT NULL,
"DateExpires" timestamp without time zone NOT NULL,
"PermissionCreate" boolean NOT NULL DEFAULT false,
"PermissionGlobalAdmin" boolean NOT NULL DEFAULT false,
"IsDisabled" boolean NOT NULL DEFAULT false,
"IsDeleted" boolean NOT NULL DEFAULT false,
CONSTRAINT "API_pkey" PRIMARY KEY ("APIGUID")
);
COMMENT ON TABLE kershner."API" IS 'Contains api keys and meta data';
CREATE TABLE IF NOT EXISTS kershner."DataOutputFormat"
(
"OutputFormatGuid" uuid NOT NULL DEFAULT gen_random_uuid(),
"Name" character varying COLLATE pg_catalog."default" NOT NULL,
"Description" character varying COLLATE pg_catalog."default" NOT NULL,
"FunctionName" character varying COLLATE pg_catalog."default" NOT NULL,
"FileExtension" character varying COLLATE pg_catalog."default" NOT NULL,
"FileMIMEType" character varying COLLATE pg_catalog."default" NOT NULL,
CONSTRAINT "DataOutputFormat_pkey" PRIMARY KEY ("OutputFormatGuid")
);
COMMENT ON TABLE kershner."DataOutputFormat" IS 'Format is an output format and/or
transformation supported by the application. Depending on the output format it may
generate multiple cache documents for a single CacheMetadata entry for key value
searches. ';
CREATE TABLE IF NOT EXISTS kershner."FileMetadata"
(
"APIGUID" uuid NOT NULL,
"FileMetaDataGUID" uuid NOT NULL DEFAULT gen_random_uuid(),
"Name" character varying COLLATE pg_catalog."default" NOT NULL,
"Description" character varying COLLATE pg_catalog."default" NOT NULL,
"DateUploaded" timestamp without time zone NOT NULL,
"DateModified" timestamp without time zone NOT NULL,
"Revision" integer NOT NULL DEFAULT 0,
"IsCurrent" boolean NOT NULL DEFAULT true,
"IsDeleted" boolean NOT NULL DEFAULT false,
"FileGuid" uuid NOT NULL,
"InputFormatGuid" uuid NOT NULL,
"FileHash" character varying COLLATE pg_catalog."default" NOT NULL,
"FileCacheExpiration" integer NOT NULL DEFAULT 1200,
CONSTRAINT "FileMetadata_pkey" PRIMARY KEY ("FileMetaDataGUID"),
CONSTRAINT "APIGUID" FOREIGN KEY ("APIGUID")
REFERENCES kershner."API" ("APIGUID") MATCH SIMPLE
ON UPDATE NO ACTION
ON DELETE NO ACTION
);
COMMENT ON TABLE kershner."FileMetadata" IS 'Contains revision details on files';
CREATE TABLE IF NOT EXISTS kershner."Cache"
(
"CacheGUID" uuid NOT NULL DEFAULT gen_random_uuid(),
"CacheKey" character varying COLLATE pg_catalog."default" NOT NULL,
"CacheValue" character varying COLLATE pg_catalog."default" NOT NULL,
"IsDeleted" boolean NOT NULL DEFAULT false,
CONSTRAINT "Cache_pkey" PRIMARY KEY ("CacheGUID")
);
COMMENT ON TABLE kershner."Cache" IS 'Converted lookup files in KV, CSV, TEXT LIST
or JSON format. ';
CREATE TABLE IF NOT EXISTS kershner."CacheMetadata"
(
"CacheMetadataGUID" uuid NOT NULL DEFAULT gen_random_uuid(),
"CacheGUID" uuid NOT NULL,
"FileMetadataGUID" uuid NOT NULL,
"OutputFormatGUID" uuid NOT NULL,
"ExpirationTimestamp" timestamp without time zone NOT NULL,
CONSTRAINT "CacheMetadata_pkey" PRIMARY KEY ("CacheMetadataGUID"),
CONSTRAINT "CacheGUID" FOREIGN KEY ("CacheGUID")
REFERENCES kershner."Cache" ("CacheGUID") MATCH SIMPLE
ON UPDATE NO ACTION
ON DELETE NO ACTION,
CONSTRAINT "FileMetadataGUID" FOREIGN KEY ("FileMetadataGUID")
REFERENCES kershner."FileMetadata" ("FileMetaDataGUID") MATCH SIMPLE
ON UPDATE NO ACTION
ON DELETE NO ACTION,
CONSTRAINT "OutputFormatGUID" FOREIGN KEY ("OutputFormatGUID")
REFERENCES kershner."DataOutputFormat" ("OutputFormatGuid") MATCH SIMPLE
ON UPDATE NO ACTION
ON DELETE NO ACTION
);
COMMENT ON TABLE kershner."CacheMetadata" IS 'Describes the Cache output object';
CREATE TABLE IF NOT EXISTS kershner."InputFile"
(
"fileGuid" uuid NOT NULL DEFAULT gen_random_uuid(),
"fileContents" text COLLATE pg_catalog."default",
CONSTRAINT "InputFile_pkey" PRIMARY KEY ("fileGuid")
);
COMMENT ON TABLE kershner."InputFile" IS 'Contains the original lookup file';
CREATE TABLE IF NOT EXISTS kershner."InputFileFormat"
(
"InputFormatGuid" uuid NOT NULL DEFAULT gen_random_uuid(),
"Name" character varying COLLATE pg_catalog."default" NOT NULL,
"Description" character varying COLLATE pg_catalog."default" NOT NULL,
"FileExtension" character varying COLLATE pg_catalog."default" NOT NULL,
"FileMIMEType" character varying COLLATE pg_catalog."default" NOT NULL,
CONSTRAINT "InputFileFormat_pkey" PRIMARY KEY ("InputFormatGuid")
);
COMMENT ON TABLE kershner."InputFileFormat" IS 'Format is an input file format
supported by the application.';
CREATE TABLE IF NOT EXISTS kershner."InputFileFormat"
(
"InputFormatGuid" uuid NOT NULL DEFAULT gen_random_uuid(),
"Name" character varying COLLATE pg_catalog."default" NOT NULL,
"Description" character varying COLLATE pg_catalog."default" NOT NULL,
"FileExtension" character varying COLLATE pg_catalog."default" NOT NULL,
"FileMIMEType" character varying COLLATE pg_catalog."default" NOT NULL,
CONSTRAINT "InputFileFormat_pkey" PRIMARY KEY ("InputFormatGuid")
);
COMMENT ON TABLE kershner."InputFileFormat" IS 'Format is an input file format
supported by the application.';
CREATE TABLE IF NOT EXISTS kershner."Search"
(
"SearchGUID" uuid NOT NULL DEFAULT gen_random_uuid(),
"Name" character varying COLLATE pg_catalog."default" NOT NULL,
"Description" character varying COLLATE pg_catalog."default" NOT NULL,
CONSTRAINT "Search_pkey" PRIMARY KEY ("SearchGUID")
);
COMMENT ON TABLE kershner."Search" IS 'List of search functions and transformations
supported used for error and help prompts.';

/*
api insert
INSERT INTO kershner."API"(
	"APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted")
	VALUES (gen_random_uuid(), 'TESTKEYTESTKEYTESTKEYTESTKEY', 'joel.kershner@gmail.com', '2525-12-24', true, true, false, false);

INSERT INTO kershner."InputFileFormat"(
	"InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType")
	VALUES (gen_random_uuid(), '.json', 'json data file', '.json', 'application/json');
	
INSERT INTO kershner."InputFile"(
	"fileGuid", "fileContents")
	VALUES (gen_random_uuid(), '{"result":{"key": "val","key1": "val1"}}');

INSERT INTO kershner."FileMetadata"("APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration")
SELECT 
	'b7c4030e-942a-43c8-9274-64af9549877f' as "APIGUID",
	gen_random_uuid() as "FileMetaDataGUID",
	'example.json' as "Name",
	'example json data' as "Description",
	CURRENT_DATE as "DateUploaded",
	CURRENT_DATE as "DateModified",
	'1' as "Revision",
	true as "IsCurrent",
	false as "IsDeleted",
	"fileGuid" as "fileGuid",
	'ebbe18b9-a50f-4448-8fc2-1d37c5a05b07' as "InputFormatGuid",
	md5("fileContents")::text as fileHash,
	'900' as "FileCacheExpiration" 
FROM kershner."InputFile" WHERE "fileGuid" = '4a648b2f-a1ae-4fd4-aa5a-e1d135ed62bc';
insert into kershner."DataOutputFormat" values(gen_random_uuid(),'json','JSON formated output','json.dumps','.json','application/json');

INSERT INTO kershner."CacheMetadata"("CacheMetadataGUID", "CacheGUID", "FileMetadataGUID", "OutputFormatGUID", "ExpirationTimestamp")
	( select 
		gen_random_uuid() as CacheMetadataGUID,
		? as CacheGUID, 
		'4a648b2f-a1ae-4fd4-aa5a-e1d135ed62bc' as FileMetadataGUID, 
		'730ae285-e702-49cd-be3c-66e2a8b2915d' as OutputFormatGUID,
		timestamp + (FileCacheExpiration seconds) as ExpirationTimestamp 
	  from kershner.FileMetadata where FileMetaDataGUID='4a648b2f-a1ae-4fd4-aa5a-e1d135ed62bc'
	  );

select 
A."API",A."OwnerEmailAddress",
B."Name",B."Description",B."DateModified",B."DateUploaded",B."Revision",B."Name",B."IsCurrent",
D."FileMIMEType",D."FileExtension",
C."fileContents"
from 
"kershner"."API" A,
"kershner"."FileMetadata" B,
"kershner"."InputFile" C,
"kershner"."InputFileFormat" D
WHERE 
A."APIGUID" = 'b7c4030e-942a-43c8-9274-64af9549877f' AND
A."APIGUID" = B."APIGUID" AND
B."FileGuid" = C."fileGuid" AND
B."InputFormatGuid" = D."InputFormatGuid" AND
A."IsDeleted" = false AND 
A."IsDisabled" = false AND 
A."DateExpires"::date > current_date AND
B."IsCurrent" = true AND
B."IsDeleted" = false;

select 
A."API",A."OwnerEmailAddress",
B."FileMetaDataGUID",B."Name",B."Description",B."DateModified",B."DateUploaded",B."Revision",B."Name",B."IsCurrent",
D."FileMIMEType",D."FileExtension",
C."fileContents"
from 
"kershner"."API" A,
"kershner"."FileMetadata" B,
"kershner"."InputFile" C,
"kershner"."InputFileFormat" D
WHERE 
A."APIGUID" = %s AND
B."FileMetaDataGUID" = %s
A."APIGUID" = B."APIGUID" AND
B."FileGuid" = C."fileGuid" AND
B."InputFormatGuid" = D."InputFormatGuid" AND
A."IsDeleted" = false AND 
A."IsDisabled" = false AND 
A."DateExpires"::date > current_date AND
B."IsCurrent" = true AND
B."IsDeleted" = false;

*/


