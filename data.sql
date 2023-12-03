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
