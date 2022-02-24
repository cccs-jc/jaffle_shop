select 
    named_struct('f1', 1, 'f2', 'allo', 'farray', array(1,2,3)) as complex, 
    * 
from 
    {{ ref('stg_orders') }}
