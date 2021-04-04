# Seed Commons

Seed builder include several methods (utils, helpers) to ease the development of the project

## Utils

-   `seed.util.request_util.has_fields_or_400`
    >    Returns 400 exception if a field is missing in request
    
-   `seed.util.query_util.sql_alike_q`
    >   Return a Q Object base on an SQL alike query<br/>
        Example \"(key_1=1 AND key_2=2) OR (key_3=3)\" returns Q(OR(AND(key_1=1, key_2=2), key_3=3)
    
-   `seed.util.query_util.multi_q`
    >   Return a Q Object base on a multilevel query <br/>
        Example [{key_1: 1, key_2: 2}, {key_3: 3}] returns Q(OR(AND(key_1=1, key_2=2), key_3=3)
    
-   `seed.util.model_util.inherit_perms`
    >   Create a new permission collection in a specific attribute with parent_model perms<br/>
        Example (Account, master_account) -> returns ["master_account__owner_id¨]
    
-   `seed.helpers.save_file.save_file`
    >   Saves a local file in media/static folder and in file model (database) based on server settings