/*SQL Created on PostgreSQL v14 using PgAdmin4 */
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
