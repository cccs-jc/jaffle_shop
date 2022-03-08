
-- post hook can be moved into dbt_project.yml so that it applies to all models

{{ config(
    materialized='incremental',
    incremental_strategy='append',
    post_hook=[
        "DELETE FROM {{this}} WHERE event_datetime < TIMESTAMP '{{var('start_date')}}'",
        "CALL {{var('catalog')}}.system.remove_orphan_files(table => '{{this}}', dry_run => true)",
        "CALL {{var('catalog')}}.system.expire_snapshots(table => '{{this}}', older_than => TIMESTAMP '{{var('start_date')}}', retain_last => 5)",
    ]
) }}





select
    now() as event_datetime,
    named_struct('f1', 1, 'f2', 'allo', 'farray', array(1,2,3)) as complex, 
    * 
from 
    {{ ref('stg_orders') }}
