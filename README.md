# inmar_api

# REST API for representing Meta-Data with end points (only GET endpoints created as of now)

/api/v1/location, -> fetch all sku data 
/api/v1/location/{location_id}/department -> fetch based on location_id parameter
/api/v1/location/{location_id}/department/{department_id}/category -> fetch based on location_id, department_id parameters
/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory -> fetch based on location_id, department_id,category_id parameters
/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id} -> fetch based on location_id,       
                                                                                                      department_id,category_id and subcategory_id parameters
