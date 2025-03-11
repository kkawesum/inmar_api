# inmar_api

# REST API for representing Meta-Data with end points (only GET endpoints created as of now)

/api/v1/location, -> fetch all sku data 
/api/v1/location/{location_id}/department -> fetch based on location_id parameter
/api/v1/location/{location_id}/department/{department_id}/category -> fetch based on location_id, department_id parameters
/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory -> fetch based on location_id, department_id,category_id parameters
/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id} -> fetch based on location_id,       
                                                                                                      department_id,category_id and subcategory_id parameters

I am using the shipped SQLITE3 database alongwith the ORM for reading the stored data.

* For adding Post, Put, Patch, Delete methods we just have to extend the APIView classes to use these methods.

Example: def post(self,request,*args):
            ...

* All the sample data has not been uploaded to the database,this is just a MVP.
  
